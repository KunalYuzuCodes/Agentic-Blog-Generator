import argparse
import os
import shutil
import logging
from typing import List, Dict, Any, Optional
import networkx as nx
import json
from datetime import datetime

from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from langchain.vectorstores.chroma import Chroma

from get_embedding_function import get_embedding_function

logger = logging.getLogger("AgentDatabase")

CHROMA_PATH = "chroma"
TEXT_DATA_PATH = "text_data"
KNOWLEDGE_GRAPH_PATH = "knowledge_graph.json"

class KnowledgeManager:
    def __init__(self):
        self.embedding_function = get_embedding_function()
        self.graph = self._load_knowledge_graph()
        
    def _load_knowledge_graph(self):
        """Load or create knowledge graph"""
        if os.path.exists(KNOWLEDGE_GRAPH_PATH):
            try:
                with open(KNOWLEDGE_GRAPH_PATH, 'r') as f:
                    graph_data = json.load(f)
                G = nx.node_link_graph(graph_data)
                logger.info(f"Loaded knowledge graph with {len(G.nodes)} nodes and {len(G.edges)} edges")
                return G
            except Exception as e:
                logger.error(f"Error loading knowledge graph: {str(e)}")
        
        # Create new graph
        G = nx.DiGraph()
        logger.info("Created new knowledge graph")
        return G
        
    def _save_knowledge_graph(self):
        """Save knowledge graph to disk"""
        graph_data = nx.node_link_data(self.graph)
        with open(KNOWLEDGE_GRAPH_PATH, 'w') as f:
            json.dump(graph_data, f)
        logger.info(f"Saved knowledge graph with {len(self.graph.nodes)} nodes and {len(self.graph.edges)} edges")
    
    def update_knowledge_graph(self, chunks: List[Document]):
        """Update knowledge graph with new document chunks"""
        # Add nodes for documents
        for chunk in chunks:
            doc_id = chunk.metadata.get("id")
            source = chunk.metadata.get("source", "")
            
            # Add document node if it doesn't exist
            if not self.graph.has_node(doc_id):
                self.graph.add_node(doc_id, 
                                   type="document",
                                   content=chunk.page_content[:100] + "...",
                                   source=source,
                                   last_updated=datetime.now().isoformat())
            
            # Extract entities and concepts (simplified)
            # In a real system, use NER and concept extraction
            keywords = self._extract_keywords(chunk.page_content)
            
            # Add connections between document and concepts
            for keyword in keywords:
                if not self.graph.has_node(keyword):
                    self.graph.add_node(keyword, type="concept")
                
                # Connect document to concept
                self.graph.add_edge(doc_id, keyword, type="contains")
        
        self._save_knowledge_graph()
    
    def _extract_keywords(self, text: str, max_keywords: int = 5) -> List[str]:
        """Simple keyword extraction (placeholder for more sophisticated NLP)"""
        # This is a very simplified version - in a real system use proper NLP
        common_words = {"the", "and", "a", "to", "of", "in", "is", "that", "it", "for"}
        words = text.lower().split()
        word_freq = {}
        
        for word in words:
            word = ''.join(c for c in word if c.isalnum())
            if len(word) > 4 and word not in common_words:
                word_freq[word] = word_freq.get(word, 0) + 1
                
        # Get top keywords
        keywords = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        return [k for k, v in keywords[:max_keywords]]
    
    def load_documents(self):
        """Load documents from text directory"""
        document_loader = DirectoryLoader(
            TEXT_DATA_PATH, 
            loader_cls=lambda path: TextLoader(path, encoding="utf-8")
        )
        return document_loader.load()

    def split_documents(self, documents: List[Document]):
        """Split documents into chunks"""
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=80,
            length_function=len,
            is_separator_regex=False,
        )
        return text_splitter.split_documents(documents)

    def calculate_chunk_ids(self, chunks):
        """Calculate unique IDs for document chunks"""
        last_source = None
        current_chunk_index = 0

        for chunk in chunks:
            source = chunk.metadata.get("source")
            current_chunk_index += 1 if source == last_source else 0

            # Calculate the chunk ID.
            chunk_id = f"{source}:{current_chunk_index}"
            last_source = source

            # Add it to the metadata.
            chunk.metadata["id"] = chunk_id

        return chunks

    def update_database(self, reset: bool = False) -> Dict[str, Any]:
        """Update the vector database with new documents"""
        results = {
            "new_documents": 0,
            "total_documents": 0,
            "knowledge_graph_nodes": 0,
            "knowledge_graph_edges": 0
        }
        
        # Clear database if requested
        if reset and os.path.exists(CHROMA_PATH):
            shutil.rmtree(CHROMA_PATH)
            logger.info("Cleared existing database")
        
        # Load and process documents
        documents = self.load_documents()
        chunks = self.split_documents(documents)
        chunks_with_ids = self.calculate_chunk_ids(chunks)
        
        # Load or create the database
        db = Chroma(
            persist_directory=CHROMA_PATH, 
            embedding_function=self.embedding_function
        )
        
        # Check for existing documents
        existing_items = db.get(include=[])
        existing_ids = set(existing_items["ids"])
        results["total_documents"] = len(existing_ids)
        
        # Add new documents
        new_chunks = []
        for chunk in chunks_with_ids:
            if chunk.metadata["id"] not in existing_ids:
                new_chunks.append(chunk)
        
        if new_chunks:
            logger.info(f"Adding {len(new_chunks)} new documents to database")
            new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
            db.add_documents(new_chunks, ids=new_chunk_ids)
            db.persist()
            results["new_documents"] = len(new_chunks)
            results["total_documents"] += len(new_chunks)
            
            # Update knowledge graph with new documents
            self.update_knowledge_graph(new_chunks)
        else:
            logger.info("No new documents to add")
        
        # Update results with knowledge graph stats
        results["knowledge_graph_nodes"] = len(self.graph.nodes)
        results["knowledge_graph_edges"] = len(self.graph.edges)
        
        return results

    def query_similar(self, query_text: str, k: int = 5) -> List[tuple]:
        """Query the database for similar documents"""
        db = Chroma(
            persist_directory=CHROMA_PATH, 
            embedding_function=self.embedding_function
        )
        return db.similarity_search_with_score(query_text, k=k)
    
    def get_related_concepts(self, document_id: str, max_depth: int = 2) -> Dict[str, Any]:
        """Get related concepts from knowledge graph"""
        if not self.graph.has_node(document_id):
            return {"error": f"Document {document_id} not found in knowledge graph"}
            
        # Get subgraph of related nodes up to max_depth
        nodes_to_explore = {document_id}
        explored = set()
        related = {document_id: {"depth": 0, "type": self.graph.nodes[document_id].get("type")}}
        
        for depth in range(1, max_depth + 1):
            next_nodes = set()
            for node in nodes_to_explore:
                explored.add(node)
                # Get neighbors in both directions
                neighbors = set(self.graph.successors(node)) | set(self.graph.predecessors(node))
                for neighbor in neighbors:
                    if neighbor not in explored and neighbor not in related:
                        related[neighbor] = {
                            "depth": depth,
                            "type": self.graph.nodes[neighbor].get("type")
                        }
                        next_nodes.add(neighbor)
            nodes_to_explore = next_nodes
            if not nodes_to_explore:
                break
                
        return {
            "central_node": document_id,
            "related_nodes": related,
            "total_related": len(related) - 1  # Exclude the central node
        }

# Tool function for the agent
def update_database(reset: bool = False):
    manager = KnowledgeManager()
    results = manager.update_database(reset)
    
    # Update agent memory
    from agent_core import agent
    agent.memory.add_knowledge_update(
        source="database",
        status=f"updated with {results['new_documents']} new documents"
    )
    agent.memory.save()
    
    return results
