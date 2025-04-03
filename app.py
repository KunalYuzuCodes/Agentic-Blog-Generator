import streamlit as st
import asyncio
import time
import json
from datetime import datetime

from agent_core import agent, AgentState
from agentic_query import query_database
from agentic_crawler import crawl_sitemap
from agentic_converter import convert_to_text
from agentic_database import update_database

# Register tools with the agent
agent.register_tool("crawl_sitemap", crawl_sitemap, "Crawl websites from sitemaps")
agent.register_tool("convert_to_text", convert_to_text, "Convert HTML/MD to text")
agent.register_tool("update_database", update_database, "Update vector database")
agent.register_tool("query_database", query_database, "Query the knowledge base")

st.set_page_config(page_title="Agentic AI Blog Generator", layout="wide")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "feedback_given" not in st.session_state:
    st.session_state.feedback_given = set()

# Sidebar with agent controls
st.sidebar.title("🤖 Agent Controls")

# Agent status
agent_status = st.sidebar.empty()

# Knowledge base management
st.sidebar.subheader("Knowledge Management")
col1, col2 = st.sidebar.columns(2)

with col1:
    if st.button("Update Knowledge"):
        with st.spinner("Updating knowledge base..."):
            asyncio.run(agent.set_goal("update_knowledge"))
            asyncio.run(agent.execute_plan())
            st.success("Knowledge base updated!")

with col2:
    if st.button("Reset Database"):
        if st.sidebar.checkbox("Confirm reset"):
            with st.spinner("Resetting database..."):
                asyncio.run(update_database(reset=True))
                st.success("Database reset complete!")

# Agent memory and metrics
st.sidebar.subheader("Agent Memory")
if st.sidebar.checkbox("Show Agent Memory"):
    memory_data = json.loads(agent.memory.json())
    st.sidebar.json(memory_data)

# Main content area
st.title("📝 Agentic AI Blog Generator")
st.markdown(
    """
    Enter a topic, and our AI agent will generate a **detailed, engaging, and structured** Medium blog post.
    The agent continuously learns and improves its knowledge base.
    """
)

# Display chat history
for i, message in enumerate(st.session_state.chat_history):
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])
        
        # Show feedback buttons if not already given
        if i not in st.session_state.feedback_given:
            col1, col2, col3 = st.columns([1, 1, 3])
            with col1:
                if st.button("👍 Helpful", key=f"helpful_{i}"):
                    # Update satisfaction score in memory
                    if i < len(agent.memory.interactions):
                        agent.memory.interactions[i]["satisfaction_score"] = 1.0
                        agent.memory.save()
                    st.session_state.feedback_given.add(i)
                    st.rerun()
            with col2:
                if st.button("👎 Not Helpful", key=f"not_helpful_{i}"):
                    # Update satisfaction score in memory
                    if i < len(agent.memory.interactions):
                        agent.memory.interactions[i]["satisfaction_score"] = 0.0
                        agent.memory.save()
                    st.session_state.feedback_given.add(i)
                    st.rerun()

# User input
query = st.chat_input("Enter your blog topic:")

if query:
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": query})
    st.chat_message("user").write(query)
    
    # Update agent status
    agent_status.info(f"Status: {AgentState.EXECUTING.value}")
    
    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Generating blog post..."):
            response = asyncio.run(agent.handle_query(query))
            st.write(response)
            
            # Add assistant message to chat history
            st.session_state.chat_history.append({"role": "assistant", "content": response})
    
    # Update agent status
    agent_status.info(f"Status: {AgentState.IDLE.value}")
