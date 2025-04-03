import asyncio
import logging
from agent_core import agent
from agentic_crawler import crawl_sitemap
from agentic_converter import convert_to_text
from agentic_database import update_database
from agentic_query import query_database

# Configure logging
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                   handlers=[logging.FileHandler("agent_init.log"), logging.StreamHandler()])
logger = logging.getLogger("AgentInit")

async def initialize():
    """Initialize the agent with tools and initial knowledge"""
    logger.info("Initializing agent...")
    
    # Register tools
    agent.register_tool("crawl_sitemap", crawl_sitemap, "Crawl websites from sitemaps")
    agent.register_tool("convert_to_text", convert_to_text, "Convert HTML/MD to text")
    agent.register_tool("update_database", update_database, "Update vector database")
    agent.register_tool("query_database", query_database, "Query the knowledge base")
    
    # Set initial goal to update knowledge
    await agent.set_goal("update_knowledge")
    
    # Execute the plan
    success = await agent.execute_plan()
    
    if success:
        logger.info("Agent initialization complete!")
    else:
        logger.error("Agent initialization failed!")
    
    return success

if __name__ == "__main__":
    asyncio.run(initialize())
