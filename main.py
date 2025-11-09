"""
EduMentor - O/L Multi-Subject Tutor Expert System
--------------------------------------------------
AGENT ARCHITECTURE: Expert Agent using Expert Systems as Tools
"""

import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from agents.expert_agent import ExpertAgent

# Page configuration
st.set_page_config(
    page_title="EduMentor - AI Tutor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

#z Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: bold;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #555;
        text-align: center;
        margin-bottom: 2rem;
    }
    .expert-rule-box {
        background-color: #f0f8ff;
        padding: 1rem;
        border-left: 4px solid #1E88E5;
        border-radius: 4px;
        margin: 1rem 0;
    }
    .refined-response-box {
        background-color: #fff8e1;
        padding: 1rem;
        border-left: 4px solid #FFA726;
        border-radius: 4px;
        margin: 1rem 0;
    }
    .clarification-box {
        background-color: #fff3e0;
        padding: 1rem;
        border-left: 4px solid #FF9800;
        border-radius: 4px;
        margin: 1rem 0;
    }
    .diagnosis-box {
        background-color: #e8f5e9;
        padding: 1.5rem;
        border-left: 4px solid #4CAF50;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .stButton>button {
        width: 100%;
        background-color: #1E88E5;
        color: white;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def initialize_system():
    """Initialize the Expert Agent (cached for performance)."""
    return ExpertAgent()


def get_agent():
    """Get or create Expert Agent for this session."""
    if 'agent' not in st.session_state:
        st.session_state.agent = ExpertAgent()
    return st.session_state.agent


def display_response(result: dict):
    """Display the system's response based on type."""
    
    # Check if this is a clarification request
    if result.get('needs_clarification'):
        st.markdown('<div class="clarification-box">', unsafe_allow_html=True)
        st.markdown("### 🤔 Let me understand better...")
        st.markdown(result['response'])
        st.markdown('</div>', unsafe_allow_html=True)
        return
    
    # Display tool used
    tool_used = result.get('tool_used', 'Unknown')
    st.info(f"**🔧 Tool Used:** {tool_used.replace('_', ' ').title()}")
    
    # Display the enhanced response
    st.markdown("### � Answer")
    st.markdown(result['response'])
    
    # Show expert system details in expander
    if result.get('raw_expert_response'):
        with st.expander("🔍 Expert System Details", expanded=False):
            expert_data = result['raw_expert_response']
            
            if isinstance(expert_data, dict):
                if expert_data.get('concept'):
                    st.markdown(f"**Concept:** {expert_data['concept']}")
                if expert_data.get('topic'):
                    st.markdown(f"**Topic:** {expert_data['topic']}")
                if expert_data.get('explanation'):
                    st.markdown("**Expert Explanation:**")
                    st.markdown(expert_data['explanation'])
                if expert_data.get('examples'):
                    st.markdown("**Examples:**")
                    for ex in expert_data['examples']:
                        st.markdown(f"- {ex}")
    
    # Show analysis details
    if result.get('analysis'):
        with st.expander("🧠 Agent Analysis", expanded=False):
            analysis = result['analysis']
            # Handle both old (query_topic) and new (topics) format
            topics = result.get('query_topics', [analysis.get('query_topic')]) if analysis.get('query_topic') else result.get('query_topics', [])
            if topics and topics != [None]:
                st.markdown(f"**Query Topic(s):** {', '.join(topics)}")
            st.markdown(f"**Reasoning:** {analysis.get('reasoning', 'N/A')}")


def main():
    """Main application."""
    
    # Initialize session state for agent if not exists
    if 'agent' not in st.session_state:
        st.session_state.agent = ExpertAgent()
    
    agent = st.session_state.agent
    
    # Initialize messages if not exists
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Header
    st.markdown('<p class="main-header">🎓 EduMentor</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Agent-Powered O/L Tutor using Expert Systems as Tools</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("## ℹ️ System Architecture")
        st.markdown("""
        **Agent-Tool Pattern:**
        
        1. 🤖 **Expert Agent** (Coordinator)
           - Powered by Gemini LLM
           - Analyzes student queries
           - Selects appropriate tool
           - Enhances responses
        
        2. 🔧 **Expert System Tools**
           - Biology Expert (@Rule-based)
           - Physics Expert (@Rule-based)
           - Chemistry Expert (@Rule-based)
           - Study Guide Expert (Diagnostic)
        
        3. ⚙️ **Process Flow**
           - Query Analysis → Tool Selection → Expert Execution → Response Enhancement
        
        **Benefits:**
        - Clear separation of concerns
        - Expert systems as reusable tools
        - LLM provides intelligence layer
        - Traditional rules provide accuracy
        """)
        
        st.markdown("---")
        
        # Stats
        if st.button("📊 View Conversation Stats"):
            st.info(f"**Conversations:** {len(agent.conversation_history)}")
            st.info(f"**Available Tools:** {', '.join(agent.tools.keys())}")
        
        if st.button("🗑️ Clear History"):
            agent.reset()
            st.session_state.messages = []
            st.success("Conversation cleared!")
            st.rerun()
        
        st.markdown("---")
        st.markdown("### 📚 Available Subjects")
        st.markdown("""
        - ✅ Biology (Information)
        - ✅ Physics (Information)
        - ✅ Chemistry (Information)
        - ✅ Study Guide (Diagnostic)
        - ⏳ Mathematics (coming soon)
        - ⏳ History (coming soon)
        
        **Two Expert Types:**
        - 🔵 **Information**: Direct Q&A
        - 🟢 **Diagnostic**: Progressive questioning
        """)
    
    # Main content area
    st.markdown("---")
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            if message["role"] == "assistant":
                display_response(message["content"])
            else:
                st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me anything about O/L subjects..."):
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Process query
        with st.chat_message("assistant"):
            with st.spinner("🤔 Thinking..."):
                result = agent.process_query(prompt)
                display_response(result)
                st.session_state.messages.append({"role": "assistant", "content": result})
    
    # Examples to try
    st.markdown("---")
    st.markdown("### 💭 Example Questions")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("What is photosynthesis?"):
            st.session_state.messages.append({"role": "user", "content": "What is photosynthesis?"})
            st.rerun()
    
    with col2:
        if st.button("Explain forces"):
            st.session_state.messages.append({"role": "user", "content": "Explain forces"})
            st.rerun()
    
    with col3:
        if st.button("How does respiration work?"):
            st.session_state.messages.append({"role": "user", "content": "How does respiration work?"})
            st.rerun()
    
    with col4:
        if st.button("I'm struggling with studies"):
            st.session_state.messages.append({"role": "user", "content": "I'm struggling with my studies"})
            st.rerun()


if __name__ == "__main__":
    main()
