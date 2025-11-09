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
    
    # Check if this is a study guide diagnosis (complete)
    if result.get('tool_used') == 'study_guide_expert' and isinstance(result.get('response'), dict):
        diagnosis = result['response']
        st.markdown('<div class="diagnosis-box">', unsafe_allow_html=True)
        st.markdown(f"### 🎯 {diagnosis.get('concept', 'Diagnosis')}")
        st.markdown(f"**📋 Diagnosis:** {diagnosis.get('diagnosis', 'N/A')}")
        
        if diagnosis.get('explanation'):
            with st.expander("📖 Why This Happens", expanded=True):
                st.markdown(diagnosis['explanation'])
        
        if diagnosis.get('recommendation'):
            with st.expander("💡 Recommended Action Plan", expanded=True):
                st.markdown(diagnosis['recommendation'])
        
        if diagnosis.get('examples'):
            with st.expander("✅ Quick Tips", expanded=False):
                for ex in diagnosis['examples']:
                    st.markdown(f"- {ex}")
        
        st.markdown('</div>', unsafe_allow_html=True)
        return
    
    # Display tool used and confidence metrics
    tool_used = result.get('tool_used', 'Unknown')
    confidence_data = result.get('confidence_metrics')
    
    # Create header with tool and confidence
    col1, col2 = st.columns([2, 1])
    with col1:
        st.info(f"**🔧 Tool Used:** {tool_used.replace('_', ' ').title()}")
    with col2:
        if confidence_data:
            cf = confidence_data.get('aggregate_certainty', 0)
            level = confidence_data.get('confidence_level', 'UNKNOWN')
            
            # Color code based on confidence level
            if level == 'HIGH':
                color = '#4CAF50'  # Green
                emoji = '🟢'
            elif level == 'MEDIUM':
                color = '#FF9800'  # Orange
                emoji = '🟡'
            elif level == 'LOW':
                color = '#F44336'  # Red
                emoji = '🔴'
            else:
                color = '#9E9E9E'  # Gray
                emoji = '⚪'
            
            st.markdown(f"""
            <div style="background-color: {color}20; padding: 10px; border-radius: 5px; border-left: 4px solid {color};">
                <div style="font-size: 12px; color: #666;">Confidence</div>
                <div style="font-size: 20px; font-weight: bold; color: {color};">
                    {emoji} {cf:.1%} <span style="font-size: 14px;">({level})</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Display the enhanced response
    st.markdown("### 💡 Answer")
    st.markdown(result['response'])
    
    # Show confidence details in expander
    if confidence_data and confidence_data.get('num_rules_fired', 0) > 0:
        with st.expander("📊 Confidence Metrics", expanded=False):
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Aggregate Certainty", f"{confidence_data.get('aggregate_certainty', 0):.3f}")
                st.metric("Average Certainty", f"{confidence_data.get('average_certainty', 0):.3f}")
                st.metric("Rules Fired", confidence_data.get('num_rules_fired', 0))
            
            with col2:
                st.metric("Max Certainty", f"{confidence_data.get('max_certainty', 0):.3f}")
                st.metric("Min Certainty", f"{confidence_data.get('min_certainty', 0):.3f}")
                st.metric("Confidence Level", confidence_data.get('confidence_level', 'N/A'))
            
            # Show distribution if available
            if confidence_data.get('certainty_distribution'):
                st.markdown("**Certainty Distribution:**")
                dist = confidence_data['certainty_distribution']
                cols = st.columns(4)
                for i, (level, count) in enumerate(dist.items()):
                    if count > 0:
                        with cols[i]:
                            st.metric(level, count)
    
    # Show expert system details in expander
    if result.get('raw_expert_response'):
        with st.expander("🔍 Expert System Details", expanded=False):
            expert_data = result['raw_expert_response']
            
            if isinstance(expert_data, dict):
                if expert_data.get('concept'):
                    st.markdown(f"**Concept:** {expert_data['concept']}")
                if expert_data.get('topic'):
                    st.markdown(f"**Topic:** {expert_data['topic']}")
                if expert_data.get('certainty_factor'):
                    st.markdown(f"**Certainty Factor:** {expert_data['certainty_factor']:.3f}")
                if expert_data.get('explanation'):
                    st.markdown("**Expert Explanation:**")
                    st.markdown(expert_data['explanation'])
                if expert_data.get('examples'):
                    st.markdown("**Examples:**")
                    for ex in expert_data['examples']:
                        st.markdown(f"- {ex}")
            elif isinstance(expert_data, list):
                # Display multiple responses in a flat structure (no nested expanders)
                st.markdown(f"**{len(expert_data)} rules matched:**")
                for i, data in enumerate(expert_data, 1):
                    st.markdown("---")
                    st.markdown(f"### Response {i}: {data.get('concept', 'N/A')}")
                    if data.get('certainty_factor'):
                        cf = data['certainty_factor']
                        level = data.get('confidence_level', 'N/A')
                        # Color code the CF
                        if level == 'HIGH':
                            color = '#4CAF50'
                        elif level == 'MEDIUM':
                            color = '#FF9800'
                        else:
                            color = '#F44336'
                        st.markdown(f"**Certainty Factor:** <span style='color: {color}; font-weight: bold;'>{cf:.3f} ({level})</span>", unsafe_allow_html=True)
                    if data.get('explanation'):
                        st.markdown("**Explanation:**")
                        st.markdown(data['explanation'][:300] + "..." if len(data['explanation']) > 300 else data['explanation'])
                    if data.get('examples') and len(data['examples']) > 0:
                        st.markdown("**Examples:**")
                        for ex in data['examples'][:3]:  # Show first 3 examples
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
    
    # Track if we're in clarification mode
    if 'awaiting_clarification' not in st.session_state:
        st.session_state.awaiting_clarification = False
    if 'clarification_tool' not in st.session_state:
        st.session_state.clarification_tool = None
    
    # Initialize study guide messages separately
    if 'study_guide_messages' not in st.session_state:
        st.session_state.study_guide_messages = []
    
    # Header
    st.markdown('<p class="main-header">🎓 EduMentor</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Agent-Powered O/L Tutor using Expert Systems as Tools</p>', unsafe_allow_html=True)
    
    # Create tabs
    tab1, tab2 = st.tabs(["📚 Subject Tutor", "🧠 Study Guide & Wellness"])
    
    with tab1:
        subject_tutor_tab(agent)
    
    with tab2:
        study_guide_tab()

def subject_tutor_tab(agent):
    """Subject-specific tutoring tab (Biology, Physics, Chemistry)."""
    
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
        - ✅ Study Guide (Separate Tab →)
        - ⏳ Mathematics (coming soon)
        - ⏳ History (coming soon)
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
        
        # Debug: Show current state
        print(f"\n🔍 DEBUG: Processing '{prompt}'")
        print(f"   Awaiting clarification: {st.session_state.awaiting_clarification}")
        print(f"   Clarification tool: {st.session_state.clarification_tool}")
        
        # Process query
        with st.chat_message("assistant"):
            with st.spinner("🤔 Thinking..."):
                # Check if we're responding to a clarification question
                if st.session_state.awaiting_clarification:
                    print(f"   → Handling as clarification response")
                    # Handle clarification response for study guide
                    if st.session_state.clarification_tool == 'study_guide_expert':
                        expert = agent.tools['study_guide_expert']
                        
                        # Use the built-in method to declare user's response
                        expert.declare_user_response(prompt)
                        
                        # Run the expert system
                        expert.run()
                        
                        # Check if still needs clarification or diagnosis complete
                        if expert.requires_clarification():
                            result = {
                                'response': expert.get_clarification_question(),
                                'tool_used': 'study_guide_expert',
                                'needs_clarification': True,
                                'success': True
                            }
                            # Keep awaiting_clarification True for next response
                            st.session_state.awaiting_clarification = True
                            st.session_state.clarification_tool = 'study_guide_expert'
                            print(f"   → Still needs clarification (keeping state)")
                        elif expert.is_diagnosis_complete():
                            result = {
                                'response': expert.get_response(),
                                'tool_used': 'study_guide_expert',
                                'needs_clarification': False,
                                'success': True
                            }
                            # Clear clarification state - diagnosis complete
                            st.session_state.awaiting_clarification = False
                            st.session_state.clarification_tool = None
                            print(f"   → Diagnosis complete! (clearing state)")
                        else:
                            result = {
                                'response': "Let me help you with that...",
                                'tool_used': 'study_guide_expert',
                                'needs_clarification': False,
                                'success': False
                            }
                            # Clear clarification state - something went wrong
                            st.session_state.awaiting_clarification = False
                            st.session_state.clarification_tool = None
                            print(f"   → Unknown state (clearing state)")
                    else:
                        # Other clarification handlers can go here
                        result = agent.process_query(prompt)
                        st.session_state.awaiting_clarification = False
                        st.session_state.clarification_tool = None
                else:
                    print(f"   → Handling as new query")
                    # Normal query processing
                    result = agent.process_query(prompt)
                    
                    # Check if result needs clarification
                    if result.get('needs_clarification'):
                        st.session_state.awaiting_clarification = True
                        st.session_state.clarification_tool = result.get('tool_used')
                        print(f"   → Set awaiting_clarification=True for {result.get('tool_used')}")
                
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
        if st.button("Acids and bases"):
            st.session_state.messages.append({"role": "user", "content": "Acids and bases"})
            st.rerun()
    
    with col4:
        if st.button("Cell division"):
            st.session_state.messages.append({"role": "user", "content": "Cell division"})
            st.rerun()

def study_guide_tab():
    """Comprehensive study guide and wellness tab."""
    from experts.study_guide_expert import StudyGuideExpert
    
    # Initialize study guide expert in session state
    if 'study_guide_expert' not in st.session_state:
        st.session_state.study_guide_expert = StudyGuideExpert()
        st.session_state.study_guide_expert.reset()
    
    study_expert = st.session_state.study_guide_expert
    
    # Sidebar for study guide
    with st.sidebar:
        st.markdown("## 🧠 Study Guide Features")
        st.markdown("""
        **Available Guidance:**
        
        📚 **Study Techniques**
        - Progressive questioning diagnosis
        - Weak area identification
        - Personalized study plans
        - Subject-specific strategies
        
        🧘 **Stress Management**
        - Exam anxiety guidance
        - Relaxation techniques
        - Time pressure handling
        - Mental health tips
        
        💪 **Motivation & Psychology**
        - Overcoming procrastination
        - Building study habits
        - Goal setting strategies
        - Confidence building
        
        ⏰ **Time Management**
        - Study schedules
        - Priority management
        - Avoiding burnout
        - Work-life balance
        
        🎯 **Exam Preparation**
        - Last-minute strategies
        - Memory techniques
        - Exam day tips
        - Answer writing skills
        """)
        
        st.markdown("---")
        
        if st.button("🔄 Start New Session", key="study_guide_reset"):
            st.session_state.study_guide_expert.reset()
            st.session_state.study_guide_messages = []
            st.success("Study guide session reset!")
            st.rerun()
    
    # Main content
    st.markdown("## 🧠 Your Personal Study & Wellness Guide")
    st.markdown("""
    Welcome to your comprehensive study companion! This expert system helps you with:
    - 📖 Study techniques and learning strategies
    - 🧘 Stress management and mental wellness
    - 💪 Motivation and psychological support
    - ⏰ Time management and productivity
    - 🎯 Exam preparation and test-taking strategies
    
    Just ask me anything about studying, stress, motivation, or exam preparation!
    """)
    
    st.markdown("---")
    
    # ====== Selection-based Study Guide UI (traditional expert system style) ======
    st.markdown("### Choose a topic and a specific question")

    CATEGORIES = {
        'Study Techniques': [
            'How can I improve my memory?',
            'What are active learning methods?',
            'How do I make effective notes?'
        ],
        'Wellness': [
            "I feel anxious about exams",
            "I'm feeling overwhelmed with studies",
            "I can't sleep well during exam time"
        ],
        'Motivation': [
            "I keep procrastinating",
            "I've lost my motivation to study",
            'How to build study confidence'
        ],
        'Time Management': [
            'Help me manage my study time',
            'Create a study schedule',
            'How to prioritise topics before exams'
        ],
        'Exam Preparation': [
            'How to prepare for exam next week',
            'What to do the night before an exam',
            'Last-minute cramming strategies'
        ],
        'Memory': [
            'How can I improve my memory?',
            'What is spaced repetition?',
            'How to use the memory palace?'
        ],
        'Confidence': [
            'I feel I am not smart',
            'How to build confidence for exams',
            'What to do after a bad test result'
        ]
    }

    category = st.selectbox("Category", list(CATEGORIES.keys()))
    question = st.selectbox("Question", CATEGORIES[category])

    # Shortcut buttons (map into selection + run)
    cols = st.columns(3)
    if cols[0].button("Exam anxiety"):
        category = 'Wellness'
        question = "I feel anxious about exams"
    if cols[1].button("Procrastination"):
        category = 'Motivation'
        question = "I keep procrastinating"
    if cols[2].button("Memory tips"):
        category = 'Memory'
        question = "How can I improve my memory?"

    st.markdown("---")

    if st.button("Get Advice"):
        with st.spinner("🤔 Consulting the study guide..."):
            # Debug: Show what's happening
            print("\n" + "="*60)
            print("🔍 [DEBUG] Study Guide Expert Called")
            print(f"   Category: {category}")
            print(f"   Question: {question}")
            print(f"   Lowercased: {question.lower()}")
            
            # Test pattern matching directly
            test_query = question.lower()
            print(f"   Testing patterns:")
            print(f"      'anxious' in query: {'anxious' in test_query}")
            print(f"      'feel anxious' in query: {'feel anxious' in test_query}")
            print(f"      'stress' in query: {'stress' in test_query}")
            print("="*60)
            
            # Reset expert and run with mapped query string
            study_expert.reset()
            from experta import Fact
            study_expert.declare(Fact(user_query=question.lower()))
            
            print("   Running expert engine...")
            study_expert.run()
            
            response = study_expert.get_response()
            print(f"   Response received: {response is not None}")
            print("="*60 + "\n")
            
            if response:
                display_study_guide_response(response)
            else:
                fallback = {
                    'concept': 'Study Guidance',
                    'explanation': """I couldn't find a specific match for that selection. Try a related question or select another topic.""",
                    'topic': 'Study Guide'
                }
                display_study_guide_response(fallback)

def display_study_guide_response(response):
    """Display study guide response with proper formatting."""
    if isinstance(response, dict):
        # Display concept/diagnosis
        if response.get('concept'):
            st.markdown(f"### {response['concept']}")
        
        if response.get('diagnosis'):
            st.info(f"**Diagnosis:** {response['diagnosis']}")
        
        # Display explanation
        if response.get('explanation'):
            st.markdown(response['explanation'])
        
        # Display recommendations
        if response.get('recommendation'):
            with st.expander("💡 Recommended Actions", expanded=True):
                st.markdown(response['recommendation'])
        
        # Display examples
        if response.get('examples'):
            with st.expander("✅ Practical Examples"):
                for example in response['examples']:
                    st.markdown(f"- {example}")
        
        # Display additional resources
        if response.get('resources'):
            with st.expander("📚 Additional Resources"):
                for resource in response['resources']:
                    st.markdown(f"- {resource}")
    else:
        st.markdown(str(response))
        if st.button("How does respiration work?"):
            st.session_state.messages.append({"role": "user", "content": "How does respiration work?"})
            st.rerun()


if __name__ == "__main__":
    main()
