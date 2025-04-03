import os
import asyncio
import logging
from datetime import datetime
from typing import List, Dict, Any, Optional
from enum import Enum
from pydantic import BaseModel

# Configure logging
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                   handlers=[logging.FileHandler("agent.log"), logging.StreamHandler()])
logger = logging.getLogger("AgentCore")

class AgentState(Enum):
    IDLE = "idle"
    PLANNING = "planning"
    EXECUTING = "executing"
    REFLECTING = "reflecting"
    ERROR = "error"

class AgentMemory(BaseModel):
    """Long-term memory for the agent to store experiences and learnings"""
    interactions: List[Dict[str, Any]] = []
    knowledge_updates: List[Dict[str, str]] = []
    performance_metrics: Dict[str, float] = {}
    last_crawl_time: Optional[datetime] = None
    
    def add_interaction(self, query: str, response: str, sources: List[str], 
                       satisfaction_score: Optional[float] = None):
        """Record an interaction with a user"""
        self.interactions.append({
            "timestamp": datetime.now().isoformat(),
            "query": query,
            "response": response,
            "sources": sources,
            "satisfaction_score": satisfaction_score
        })
        
    def add_knowledge_update(self, source: str, status: str):
        """Record a knowledge base update"""
        self.knowledge_updates.append({
            "timestamp": datetime.now().isoformat(),
            "source": source,
            "status": status
        })
        
    def update_metric(self, metric_name: str, value: float):
        """Update a performance metric"""
        self.performance_metrics[metric_name] = value
        
    def save(self, path: str = "agent_memory.json"):
        """Save memory to disk"""
        import json
        with open(path, "w") as f:
            f.write(self.json())
            
    @classmethod
    def load(cls, path: str = "agent_memory.json"):
        """Load memory from disk"""
        import json
        if os.path.exists(path):
            with open(path, "r") as f:
                return cls.parse_raw(f.read())
        return cls()

class AgentCore:
    """Core agent controller that orchestrates the agent's activities"""
    
    def __init__(self):
        self.state = AgentState.IDLE
        self.memory = AgentMemory.load()
        self.goals = []
        self.current_plan = []
        self.available_tools = {}
        
    def register_tool(self, name: str, func: callable, description: str):
        """Register a tool that the agent can use"""
        self.available_tools[name] = {
            "function": func,
            "description": description
        }
        logger.info(f"Registered tool: {name}")
        
    async def set_goal(self, goal: str):
        """Set a new goal for the agent"""
        self.goals.append(goal)
        logger.info(f"New goal set: {goal}")
        await self.create_plan()
        
    async def create_plan(self):
        """Create a plan to achieve the current goals"""
        self.state = AgentState.PLANNING
        logger.info("Creating plan to achieve goals")
        
        # Simple planning for now - will be expanded with LLM-based planning
        if "update_knowledge" in self.goals:
            self.current_plan = [
                {"tool": "crawl_sitemap", "params": {}},
                {"tool": "convert_to_text", "params": {}},
                {"tool": "update_database", "params": {"reset": False}}
            ]
        
        self.state = AgentState.IDLE
        return self.current_plan
        
    async def execute_plan(self):
        """Execute the current plan"""
        self.state = AgentState.EXECUTING
        
        for step in self.current_plan:
            tool_name = step["tool"]
            params = step["params"]
            
            if tool_name in self.available_tools:
                logger.info(f"Executing tool: {tool_name}")
                try:
                    tool = self.available_tools[tool_name]["function"]
                    if asyncio.iscoroutinefunction(tool):
                        result = await tool(**params)
                    else:
                        result = tool(**params)
                    logger.info(f"Tool {tool_name} executed successfully")
                except Exception as e:
                    logger.error(f"Error executing tool {tool_name}: {str(e)}")
                    self.state = AgentState.ERROR
                    return False
            else:
                logger.error(f"Unknown tool: {tool_name}")
                self.state = AgentState.ERROR
                return False
                
        self.state = AgentState.IDLE
        return True
        
    async def reflect(self):
        """Reflect on recent actions and update strategy"""
        self.state = AgentState.REFLECTING
        
        # Analyze recent performance
        if len(self.memory.interactions) > 0:
            # Calculate response quality metrics
            satisfaction_scores = [i.get("satisfaction_score", 0) for i in self.memory.interactions 
                                 if i.get("satisfaction_score") is not None]
            if satisfaction_scores:
                avg_satisfaction = sum(satisfaction_scores) / len(satisfaction_scores)
                self.memory.update_metric("avg_satisfaction", avg_satisfaction)
                
            # Determine if knowledge needs updating
            if not self.memory.last_crawl_time:
                logger.info("Knowledge base needs updating")
                await self.set_goal("update_knowledge")
            
            else: 
                if isinstance(self.memory.last_crawl_time, str):
                    last_crawl_dt = datetime.fromisoformat(self.memory.last_crawl_time)
                else:
                    last_crawl_dt = self.memory.last_crawl_time

                days_since_update = (datetime.now() - last_crawl_dt).days
                if days_since_update > 7:
                    logger.innfo(f"Knowledge base needs updating (last updated {days_since_update} days ago)")
                    await self.set_goal("update Knowledge")
                
        self.state = AgentState.IDLE
        
    async def handle_query(self, query: str):
        """Process a user query"""
        # First reflect on past performance and state
        await self.reflect()
        
        # Use the query tool
        if "query_database" in self.available_tools:
            tool = self.available_tools["query_database"]["function"]
            response = await tool(query)
            
            # Record the interaction
            self.memory.add_interaction(query, response, [], None)
            self.memory.save()
            
            return response
        else:
            logger.error("Query tool not available")
            return "I'm unable to process your query at the moment."

agent = AgentCore()