import asyncio
import os
import requests
from xml.etree import ElementTree
import time
from typing import List, Dict, Any, Optional
from datetime import datetime
import logging
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

logger = logging.getLogger("AgentCrawler")

class AgentCrawler:
    def __init__(self):
        self.browser_config = BrowserConfig(
            headless=True,
            verbose=False,
            extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
        )
        self.crawl_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)
        self.known_sitemaps = {
            "pydantic_ai": "https://ai.pydantic.dev/sitemap.xml",
            # Add more sitemaps as the agent discovers them
        }
        
    def save_markdown(self, url: str, content: str) -> str:
        """Saves the crawled content as a Markdown file in the 'data' folder."""
        os.makedirs("data", exist_ok=True)
        filename = url.rstrip("/").split("/")[-1] or "index"
        filepath = os.path.join("data", f"{filename}.md")
        
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)
        logger.info(f"Saved: {filepath}")
        return filepath

    async def crawl_parallel(self, urls: List[str], max_concurrent: int = 3) -> Dict[str, Any]:
        """Crawl multiple URLs in parallel and return statistics"""
        logger.info(f"Crawling {len(urls)} URLs in parallel (max {max_concurrent} concurrent)")
        
        crawler = AsyncWebCrawler(config=self.browser_config)
        await crawler.start()

        results = {
            "success_count": 0,
            "fail_count": 0,
            "start_time": time.time(),
            "urls_processed": [],
            "errors": []
        }

        try:
            for i in range(0, len(urls), max_concurrent):
                batch = urls[i : i + max_concurrent]
                tasks = []
                
                for j, url in enumerate(batch):
                    session_id = f"parallel_session_{i + j}"
                    task = crawler.arun(url=url, config=self.crawl_config, session_id=session_id)
                    tasks.append(task)

                batch_results = await asyncio.gather(*tasks, return_exceptions=True)
                
                for url, result in zip(batch, batch_results):
                    if isinstance(result, Exception):
                        logger.error(f"Error crawling {url}: {result}")
                        results["fail_count"] += 1
                        results["errors"].append({"url": url, "error": str(result)})
                    elif result.success:
                        logger.info(f"Successfully crawled {url}")
                        self.save_markdown(url, result.html)
                        results["success_count"] += 1
                        results["urls_processed"].append(url)
                    else:
                        logger.warning(f"Unsuccessful crawl of {url}")
                        results["fail_count"] += 1
                        results["errors"].append({"url": url, "error": "Unsuccessful crawl"})

        finally:
            results["end_time"] = time.time()
            results["total_time"] = results["end_time"] - results["start_time"]
            await crawler.close()
            
        return results

    def discover_sitemaps(self, base_url: str) -> List[str]:
        """Attempt to discover sitemaps for a given domain"""
        potential_paths = [
            "/sitemap.xml",
            "/sitemap_index.xml",
            "/sitemap/sitemap.xml",
            "/wp-sitemap.xml"
        ]
        
        discovered = []
        for path in potential_paths:
            try:
                url = base_url.rstrip('/') + path
                response = requests.get(url, timeout=10)
                if response.status_code == 200 and '<urlset' in response.text:
                    discovered.append(url)
                    logger.info(f"Discovered sitemap: {url}")
            except Exception as e:
                logger.debug(f"Failed to check {path}: {str(e)}")
                
        return discovered

    def get_urls_from_sitemap(self, sitemap_url: str) -> List[str]:
        """Fetches all URLs from a sitemap."""
        try:
            response = requests.get(sitemap_url)
            response.raise_for_status()
            root = ElementTree.fromstring(response.content)
            namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            urls = [loc.text for loc in root.findall('.//ns:loc', namespace)]
            return urls
        except Exception as e:
            logger.error(f"Error fetching sitemap {sitemap_url}: {e}")
            return []

    async def crawl_site(self, site_key: str = "pydantic_ai", discover: bool = False) -> Dict[str, Any]:
        """Crawl a specific site by key or discover new sitemaps"""
        if site_key in self.known_sitemaps:
            sitemap_url = self.known_sitemaps[site_key]
            urls = self.get_urls_from_sitemap(sitemap_url)
            if urls:
                logger.info(f"Found {len(urls)} URLs to crawl from {site_key}")
                results = await self.crawl_parallel(urls, max_concurrent=25)
                results["site_key"] = site_key
                results["sitemap_url"] = sitemap_url
                return results
            else:
                return {"error": f"No URLs found in sitemap for {site_key}"}
        elif discover:
            # Try to discover sitemaps for the provided URL
            discovered = self.discover_sitemaps(site_key)  # Treating site_key as URL
            if discovered:
                # Add to known sitemaps
                domain = site_key.split("//")[-1].split("/")[0]
                self.known_sitemaps[domain] = discovered[0]
                
                urls = self.get_urls_from_sitemap(discovered[0])
                if urls:
                    logger.info(f"Found {len(urls)} URLs to crawl from discovered sitemap")
                    results = await self.crawl_parallel(urls, max_concurrent=25)
                    results["site_key"] = domain
                    results["sitemap_url"] = discovered[0]
                    return results
            return {"error": "Could not discover sitemap"}
        else:
            return {"error": f"Unknown site key: {site_key}"}

# Tool function for the agent
async def crawl_sitemap(site_key: str = "pydantic_ai", discover: bool = False):
    crawler = AgentCrawler()
    results = await crawler.crawl_site(site_key, discover)
    
    # Update agent memory with crawl time
    from agent_core import agent
    agent.memory.last_crawl_time = datetime.now().isoformat()
    agent.memory.save()
    
    return results
