import os
import glob
import html2text
import logging
from typing import Dict, List, Any
import re
from datetime import datetime

logger = logging.getLogger("AgentConverter")

class ContentConverter:
    def __init__(self):
        self.converter = html2text.HTML2Text()
        self.converter.ignore_links = False  # We'll extract links for knowledge graph
        
    def extract_metadata(self, html_content: str, file_path: str) -> Dict[str, Any]:
        """Extract metadata from HTML content"""
        metadata = {
            "source_file": file_path,
            "extraction_date": datetime.now().isoformat(),
            "word_count": len(html_content.split()),
        }
        
        # Extract title
        title_match = re.search(r"<title>(.*?)</title>", html_content, re.IGNORECASE)
        if title_match:
            metadata["title"] = title_match.group(1)
            
        # Extract description
        desc_match = re.search(r'<meta\s+name="description"\s+content="(.*?)"', html_content, re.IGNORECASE)
        if desc_match:
            metadata["description"] = desc_match.group(1)
            
        # Extract links for knowledge graph
        links = re.findall(r'href="(https?://[^"]+)"', html_content)
        metadata["links"] = list(set(links))
        
        return metadata

    def convert_html_to_text(self, input_folder: str, output_folder: str) -> Dict[str, Any]:
        """Convert HTML/MD files to text with enhanced metadata"""
        os.makedirs(output_folder, exist_ok=True)
        
        md_files = glob.glob(os.path.join(input_folder, "*.md"))
        results = {
            "files_processed": 0,
            "metadata_extracted": [],
            "errors": []
        }
        
        for md_file in md_files:
            try:
                with open(md_file, "r", encoding="utf-8") as file:
                    html_content = file.read()
                
                # Extract metadata before conversion
                metadata = self.extract_metadata(html_content, md_file)
                
                # Convert HTML to plain text
                plain_text = self.converter.handle(html_content)
                
                # Get filename without extension
                filename = os.path.splitext(os.path.basename(md_file))[0] + ".txt"
                output_path = os.path.join(output_folder, filename)
                
                # Save to new text file
                with open(output_path, "w", encoding="utf-8") as text_file:
                    text_file.write(plain_text)
                
                logger.info(f"Converted: {md_file} -> {output_path}")
                results["files_processed"] += 1
                results["metadata_extracted"].append(metadata)
                
            except Exception as e:
                logger.error(f"Error converting {md_file}: {str(e)}")
                results["errors"].append({"file": md_file, "error": str(e)})
        
        return results

# Tool function for the agent
def convert_to_text(input_folder: str = "data", output_folder: str = "text_data"):
    converter = ContentConverter()
    results = converter.convert_html_to_text(input_folder, output_folder)
    
    # Update agent memory
    from agent_core import agent
    for metadata in results["metadata_extracted"]:
        agent.memory.add_knowledge_update(
            source=metadata.get("source_file", "unknown"),
            status="converted"
        )
    agent.memory.save()
    
    return results
