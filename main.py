"""
EduMentor - O/L Multi-Subject Tutor Expert System
--------------------------------------------------
NEW ARCHITECTURE: Intent Classifier + Traditional @Rule Expert Systems + Response Refinement
"""

import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from core.orchestrator import SystemOrchestrator

# Page configuration
st.set_page_config(
    page_title="EduMentor - AI Tutor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
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
    """Initialize the orchestrator (cached for performance)."""
    return SystemOrchestrator()


def get_orchestrator():
    """Get or create orchestrator for this session."""
    if 'orchestrator' not in st.session_state:
        st.session_state.orchestrator = SystemOrchestrator()
    return st.session_state.orchestrator


def display_response(result: dict):
    """Display the system's response based on type."""
    
    response_type = result.get('response_type', 'answer')
    
    if response_type == 'clarification_request':
        st.markdown('<div class="clarification-box">', unsafe_allow_html=True)
        st.markdown("### 🤔 Clarification Needed")
        st.markdown(result['content'])
        st.markdown('</div>', unsafe_allow_html=True)
    
    elif response_type == 'diagnosis':
        # Diagnostic expert response (Study Guide)
        st.markdown('<div class="diagnosis-box">', unsafe_allow_html=True)
        
        # Diagnosis header
        diagnosis_data = result.get('expert_rule', result)
        concept = diagnosis_data.get('concept', 'Diagnosis')
        confidence = diagnosis_data.get('confidence', 'High')
        
        # Display confidence badge
        if 'Medium' in confidence or 'Low' in confidence:
            st.warning(f"**{concept}** (Confidence: {confidence})")
        else:
            st.success(f"**{concept}**")
        
        # Main diagnosis
        if diagnosis_data.get('diagnosis'):
            st.markdown("### 📋 Problem Identified")
            st.markdown(diagnosis_data['diagnosis'])
        
        # Explanation
        if diagnosis_data.get('explanation'):
            st.markdown("### 📖 Why This Happens")
            st.markdown(diagnosis_data['explanation'])
        
        # Recommendations (most important!)
        if diagnosis_data.get('recommendation'):
            with st.expander("💡 **Personalized Action Plan** (Click to expand)", expanded=True):
                st.markdown(diagnosis_data['recommendation'])
        
        # Reasoning chain (explainability)
        if diagnosis_data.get('reasoning_chain'):
            with st.expander("🔍 How I Reached This Conclusion", expanded=False):
                st.markdown("**Reasoning Steps:**")
                for i, step in enumerate(diagnosis_data['reasoning_chain'], 1):
                    st.markdown(f"{i}. {step}")
        
        # Examples
        if diagnosis_data.get('examples'):
            with st.expander("📝 Practice Suggestions", expanded=False):
                for example in diagnosis_data['examples']:
                    st.markdown(f"- {example}")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
    elif response_type == 'answer':
        # Display topic and concept
        col1, col2 = st.columns([1, 3])
        with col1:
            st.info(f"**Subject:** {result.get('subject', 'N/A')}")
        with col2:
            st.success(f"**Concept:** {result.get('concept', 'N/A')}")
        
        # Expert System Rule (Original)
        with st.expander("📖 Expert System Rule (Click to expand)", expanded=False):
            st.markdown('<div class="expert-rule-box">', unsafe_allow_html=True)
            st.markdown(result.get('expert_rule', 'N/A'))
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Refined Response (LLM-enhanced)
        st.markdown("### 🌟 AI-Enhanced Explanation")
        st.markdown('<div class="refined-response-box">', unsafe_allow_html=True)
        st.markdown(result['content'])
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Examples
        if result.get('examples'):
            st.markdown("### 💡 Examples")
            for example in result['examples']:
                st.markdown(f"- {example}")
    
    elif response_type == 'error':
        st.error(result['content'])


def main():
    """Main application."""
    
    # Initialize session state for orchestrator if not exists
    if 'orchestrator' not in st.session_state:
        st.session_state.orchestrator = SystemOrchestrator()
    
    orchestrator = st.session_state.orchestrator
    
    # Initialize messages if not exists
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Header
    st.markdown('<p class="main-header">🎓 EduMentor</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Your Intelligent O/L Tutor with Traditional Expert Systems</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("## ℹ️ System Architecture")
        st.markdown("""
        **New Design:**
        1. 🎯 **Intent Classifier** (LLM)
           - Understands your question
           - Routes to correct subject
        
        2. 🎓 **Expert Systems** (@Rule-based)
           - Biology, Physics, Chemistry, Math, History
           - Traditional Experta inference engine
           - Pattern matching with @Rule decorators
        
        3. 🌟 **Response Refiner** (LLM)
           - Makes expert output friendly
           - NO new facts added
           - Pure language enhancement
        
        4. 🧠 **Conversation Memory**
           - Remembers context
           - Helps with clarifications
        """)
        
        st.markdown("---")
        
        # Stats
        if st.button("📊 View Conversation Stats"):
            stats = orchestrator.get_conversation_stats()
            st.json(stats)
        
        if st.button("🗑️ Clear History"):
            orchestrator.clear_conversation()
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
                result = orchestrator.process_query(prompt)
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
