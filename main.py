"""
EduMentor - O/L Multi-Subject Tutor Expert System
--------------------------------------------------
Phase 2+3: Multi-Agent System + LLM Integration
Streamlit-based user interface with natural language enhancement.
"""

import streamlit as st
import os
from datetime import datetime

# Import MAS components
from agents.coordinator_agent import CoordinatorAgent

# Import LLM components
from llm.gemini_interface import GeminiInterface, HybridSystem

# Import utilities
from utils.language_detector import detect_language
from utils.response_formatter import create_display

# Import configuration
import config


# Page configuration
st.set_page_config(
    page_title=config.PAGE_TITLE,
    page_icon=config.PAGE_ICON,
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
    }
    .sub-header {
        font-size: 1.2rem;
        color: #555;
        text-align: center;
        margin-bottom: 2rem;
    }
    .agent-badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: bold;
        margin: 0.3rem;
        font-size: 0.9rem;
    }
    .response-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1E88E5;
        margin: 1rem 0;
    }
    .enhanced-badge {
        background-color: #FFD700;
        color: #333;
        padding: 0.2rem 0.6rem;
        border-radius: 10px;
        font-size: 0.8rem;
        font-weight: bold;
    }
    .expert-badge {
        background-color: #4CAF50;
        color: white;
        padding: 0.2rem 0.6rem;
        border-radius: 10px;
        font-size: 0.8rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)


def initialize_session_state():
    """Initialize session state variables."""
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []
    
    if 'question_count' not in st.session_state:
        st.session_state.question_count = 0
    
    if 'coordinator' not in st.session_state:
        # Initialize MAS Coordinator
        st.session_state.coordinator = CoordinatorAgent()
    
    if 'llm_interface' not in st.session_state:
        # Initialize LLM Interface
        api_key = os.getenv('GEMINI_API_KEY')
        st.session_state.llm_interface = GeminiInterface(api_key)
    
    if 'hybrid_system' not in st.session_state:
        # Initialize Hybrid System (MAS + LLM)
        st.session_state.hybrid_system = HybridSystem(
            st.session_state.coordinator,
            st.session_state.llm_interface
        )


def display_header():
    """Display main header."""
    st.markdown('<div class="main-header">🎓 EduMentor</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="sub-header">AI-Powered Multi-Subject O/L Tutor - {config.PHASE}</div>',
        unsafe_allow_html=True
    )
    
    st.markdown(f"""
    Welcome to **EduMentor v{config.SYSTEM_VERSION}**! 
    
    I'm powered by:
    - 🤖 **Multi-Agent System** with 6 specialized agents
    - 🌟 **Gemini AI** for natural language explanations
    - 🌍 **Multilingual Support** (English, Sinhala, Tamil)
    
    Ask me anything about **Physics, Biology, Chemistry, Mathematics, History**, or **Study Tips**!
    """)


def display_sidebar():
    """Display sidebar with settings and info."""
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # Language selection
        st.subheader("🌍 Language")
        language = st.selectbox(
            "Response Language",
            options=list(config.SUPPORTED_LANGUAGES),
            format_func=lambda x: config.LANGUAGE_NAMES.get(x, x),
            index=0
        )
        
        # LLM toggle
        st.subheader("🌟 Enhancement")
        use_llm = st.checkbox(
            "Use AI Enhancement",
            value=config.LLM_ENABLED and st.session_state.llm_interface.is_enabled(),
            help="Enhance responses with Gemini AI for natural language"
        )
        
        # Subject filter
        st.subheader("📚 Subjects")
        st.markdown("**Available Agents:**")
        for subject, info in config.SUBJECTS.items():
            if info['enabled']:
                st.markdown(f"{info['icon']} {subject}")
        
        st.divider()
        
        # System info
        st.subheader("ℹ️ System Info")
        system_info = st.session_state.hybrid_system.get_system_info()
        st.write(f"**Agents:** {system_info['agents_available']}")
        st.write(f"**MAS:** {'✓ Enabled' if system_info['mas_enabled'] else '✗ Disabled'}")
        st.write(f"**LLM:** {'✓ Enabled' if system_info['llm_enabled'] else '✗ Disabled'}")
        
        # Statistics
        if config.ENABLE_AGENT_STATISTICS:
            st.divider()
            st.subheader("📊 Agent Statistics")
            stats = st.session_state.coordinator.get_agent_statistics()
            for agent_name, count in stats.items():
                st.write(f"**{agent_name}:** {count} questions")
        
        # Clear history
        st.divider()
        if st.button("🗑️ Clear History"):
            st.session_state.conversation_history = []
            st.session_state.question_count = 0
            st.rerun()
        
        return language, use_llm


def display_question_input():
    """Display question input area."""
    st.subheader("💬 Ask Your Question")
    
    col1, col2 = st.columns([4, 1])
    
    with col1:
        question = st.text_area(
            "Type your question here:",
            placeholder="Example: What is photosynthesis?",
            height=100,
            label_visibility="collapsed"
        )
    
    with col2:
        st.write("")  # Spacing
        st.write("")  # Spacing
        submit = st.button("🚀 Ask", type="primary", use_container_width=True)
    
    return question, submit


def process_and_display_response(question, language, use_llm):
    """Process question and display response."""
    
    if not question or question.strip() == "":
        st.warning("⚠️ Please enter a question!")
        return
    
    # Show processing
    with st.spinner("🤔 Thinking..."):
        # Auto-detect language if enabled
        if config.AUTO_DETECT_LANGUAGE:
            detected_lang = detect_language(question)
            st.info(f"🌍 Detected language: {config.LANGUAGE_NAMES.get(detected_lang, detected_lang)}")
            if detected_lang != 'en' and language == 'en':
                language = detected_lang
        
        # Process through hybrid system
        try:
            response = st.session_state.hybrid_system.process_question(
                question,
                language=language,
                use_llm=use_llm
            )
            
            # Format response for display
            display_data = create_display(response)
            
            # Store in history
            st.session_state.conversation_history.append({
                'timestamp': datetime.now(),
                'question': question,
                'response': display_data,
                'language': language
            })
            st.session_state.question_count += 1
            
            # Display response
            display_response(display_data)
            
        except Exception as e:
            st.error(f"❌ Error processing question: {str(e)}")
            if config.DEBUG_MODE:
                st.exception(e)


def display_response(display_data):
    """Display formatted response."""
    
    st.markdown('<div class="response-box">', unsafe_allow_html=True)
    
    # Status and metadata
    col1, col2, col3 = st.columns([2, 2, 2])
    with col1:
        st.markdown(f"**Status:** {display_data['status']}")
    with col2:
        st.markdown(f"**Agent:** {display_data['agent']}")
    with col3:
        if display_data.get('enhancement') == '🌟 LLM Enhanced':
            st.markdown('<span class="enhanced-badge">🌟 AI Enhanced</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span class="expert-badge">📖 Expert System</span>', unsafe_allow_html=True)
    
    st.divider()
    
    # Topic and concept
    st.markdown(f"### {display_data['topic']}")
    st.markdown(f"**Concept:** {display_data['concept']}")
    
    st.divider()
    
    # Main explanation
    st.markdown("### 📝 Explanation")
    st.markdown(display_data['explanation'])
    
    # Examples if available
    if 'examples' in display_data:
        st.divider()
        st.markdown("### 📚 Examples")
        st.markdown(display_data['examples'])
    
    st.markdown('</div>', unsafe_allow_html=True)


def display_conversation_history():
    """Display conversation history."""
    if st.session_state.conversation_history:
        st.divider()
        st.subheader("📜 Conversation History")
        
        for i, entry in enumerate(reversed(st.session_state.conversation_history[-5:])):
            with st.expander(f"Q{st.session_state.question_count - i}: {entry['question'][:50]}..."):
                st.write(f"**Time:** {entry['timestamp'].strftime('%H:%M:%S')}")
                st.write(f"**Language:** {entry['language'].upper()}")
                st.write(f"**Topic:** {entry['response']['topic']}")
                st.write(f"**Agent:** {entry['response']['agent']}")
                st.markdown("**Answer:**")
                st.markdown(entry['response']['explanation'][:200] + "...")


def display_quick_examples():
    """Display quick example questions."""
    st.divider()
    st.subheader("💡 Quick Examples")
    
    examples = {
        "Physics": "What is Newton's law of motion?",
        "Biology": "Explain photosynthesis",
        "Chemistry": "What are acids and bases?",
        "Mathematics": "How do I solve algebraic equations?",
        "History": "Tell me about Sri Lankan independence",
        "Study Tips": "How can I improve my memory?"
    }
    
    cols = st.columns(3)
    for i, (subject, example) in enumerate(examples.items()):
        with cols[i % 3]:
            if st.button(f"{config.SUBJECTS[subject]['icon']} {example}", key=f"example_{i}"):
                st.session_state.example_question = example
                st.rerun()


def main():
    """Main application logic."""
    
    # Initialize
    initialize_session_state()
    
    # Display UI components
    display_header()
    language, use_llm = display_sidebar()
    
    # Check for example question
    if hasattr(st.session_state, 'example_question'):
        question = st.session_state.example_question
        del st.session_state.example_question
        process_and_display_response(question, language, use_llm)
        st.rerun()
    
    # Question input
    question, submit = display_question_input()
    
    # Process question
    if submit:
        process_and_display_response(question, language, use_llm)
    
    # Display history
    display_conversation_history()
    
    # Display examples
    display_quick_examples()
    
    # Footer
    st.divider()
    st.markdown(f"""
    <div style='text-align: center; color: #888; padding: 2rem;'>
        <p><strong>{config.SYSTEM_NAME} v{config.SYSTEM_VERSION}</strong></p>
        <p>{config.PHASE}</p>
        <p>Powered by Experta + Gemini AI | Multi-Agent System with 6 Specialized Agents</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
