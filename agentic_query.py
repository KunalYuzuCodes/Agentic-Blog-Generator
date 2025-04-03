import logging
from typing import Dict, Any, List, Optional
import asyncio
from datetime import datetime

from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from pydantic_ai import Agent, RunContext

from get_embedding_function import get_embedding_function
from agentic_database import KnowledgeManager

logger = logging.getLogger("AgentQuery")

# Enhanced prompt template with self-reflection
PROMPT_TEMPLATE = """
## Context

You are an AI assistant that generates detailed and engaging Medium blog articles on given topics. The blog should be informative, structured, and well-researched, incorporating context from retrieved documents.

## Goal

Generate a comprehensive and reader-friendly Medium blog post based on the given topic and supporting contextual information.

## Structure

- **[Catchy but Controversial Title That Hooks the Reader]**
- **Introduction:**
  - Start with a compelling hook (question, fact, or anecdote).
  - Introduce the topic in details and its significance.
  - Clearly outline what the reader will gain from the article.
- **Main Sections:**
  - Use clear, engaging headings.
  - Explain concepts in a detailed but an easy-to-understand manner.
  - Include examples, statistics, code snippets, or anecdotes.
  - Provide actionable insights.
  - Use bullet points when necessary.
- **Conclusion:**
  - Summarize key takeaways.
  - End with a thought-provoking statement or a call to action.
  - Encourage readers to comment or share their thoughts.

## Instructions

- Ensure clarity and readability with a conversational tone.
- Use formatting elements such as **bold**, *italics*, and block quotes for emphasis.
- Generate content with a word count of approximately 700-800 words per section.
- Integrate code snippets where relevant.

## Self-Reflection

Before finalizing your response, consider:
1. Have I fully addressed the user's query?
2. Is my response well-structured and easy to follow?
3. Have I incorporated the most relevant information from the context?
4. Are there any gaps in my explanation that should be addressed?

---

### Contextual Information:

{context}

### Topic:

{question}
"""

class QueryEngine:
    def __init__(self):
        self.knowledge_manager = KnowledgeManager()
        self.models = {
            "default": "deepseek-r1:14b",
            "fast": "llama3.1:8b",
            "creative": "deepseek-r1:14b"
        }
        self.current_model = "default"
        
    def select_model(self, query: str) -> str:
        """Select appropriate model based on query characteristics"""
        query_lower = query.lower()
        
        # Simple heuristic model selection
        if len(query) < 50:
            return self.models["fast"]
        elif any(word in query_lower for word in ["creative", "story", "imagine"]):
            return self.models["creative"]
        else:
            return self.models["default"]
    
    async def generate_response(self, query: str, model_override: Optional[str] = None) -> Dict[str, Any]:
        """Generate response using RAG"""
        start_time = datetime.now()
        
        # Get similar documents
        results = self.knowledge_manager.query_similar(query, k=5)
        context_text = "\n\n---\n\n".join([doc.page_content for doc, _ in results])
        
        # Prepare prompt
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(context=context_text, question=query)
        
        # Select model
        model_name = model_override or self.select_model(query)
        model = Ollama(model=model_name)
        
        # Generate response
        response_text = model.invoke(prompt)
        
        # Get sources and related concepts
        sources = [doc.metadata.get("id", None) for doc, _ in results]
        related_concepts = {}
        
        if sources:
            # Get related concepts from knowledge graph for first source
            related_concepts = self.knowledge_manager.get_related_concepts(sources[0])
        
        end_time = datetime.now()
        processing_time = (end_time - start_time).total_seconds()
        
        return {
            "response": response_text,
            "sources": sources,
            "model_used": model_name,
            "processing_time": processing_time,
            "related_concepts": related_concepts
        }

# Tool function for the agent
async def query_database(query: str, model_override: Optional[str] = None) -> str:
    engine = QueryEngine()
    result = await engine.generate_response(query, model_override)
    
    # Update agent memory
    from agent_core import agent
    agent.memory.add_interaction(
        query=query,
        response=result["response"],
        sources=result["sources"],
        satisfaction_score=None  # Will be updated later with feedback
    )
    agent.memory.save()
    
    return result["response"]