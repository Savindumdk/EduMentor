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
    
    # Display chat history FIRST
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            if message["role"] == "assistant":
                display_response(message["content"])
            else:
                st.markdown(message["content"])
    
    # Chat input at the END (this keeps it at bottom)
    if prompt := st.chat_input("Ask me anything about O/L subjects..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Debug: Show current state
        print(f"\n🔍 DEBUG: Processing '{prompt}'")
        print(f"   Awaiting clarification: {st.session_state.awaiting_clarification}")
        print(f"   Clarification tool: {st.session_state.clarification_tool}")
        
        # Process query with spinner
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
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": result})
        
        # Rerun to display the new messages
        st.rerun()

def study_guide_tab():
    """Comprehensive study guide and wellness tab."""
    from experts.study_guide_expert import StudyGuideExpert
    
    # Initialize study guide expert in session state
    if 'study_guide_expert' not in st.session_state:
        st.session_state.study_guide_expert = StudyGuideExpert()
    
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
    
    **NEW: Multi-Input Analysis** - Provide detailed information for highly personalized recommendations!
    """)
    
    st.markdown("---")
    
    # ====== ENHANCED Multi-Input Study Guide UI ======
    st.markdown("### 📊 Personalized Study Analysis")
    st.markdown("*Fill in as many fields as you can for better recommendations*")
    
    # Create two columns for inputs
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📝 Basic Information")
        
        # Category selection
        CATEGORIES = {
            'Memory': 'Memory & Retention',
            'Focus': 'Focus & Concentration',
            'Stress': 'Stress Management',
            'Time Management': 'Time Management',
            'Sleep': 'Sleep & Recovery',
            'Motivation': 'Motivation & Psychology',
            'Exam Preparation': 'Exam Strategies',
            'Confidence': 'Confidence Building'
        }
        
        category = st.selectbox("🎯 What area do you need help with?", list(CATEGORIES.keys()), 
                                format_func=lambda x: CATEGORIES[x])
        
        # Learning style
        learning_style = st.selectbox("🎨 What's your preferred learning style?",
                                      ["Not sure", "Visual", "Auditory", "Kinesthetic", "Reading/Writing"])
        learning_style = None if learning_style == "Not sure" else learning_style.replace("/", " ")
    
    with col2:
        st.markdown("#### 📈 Quantitative Inputs")
        
        # Numeric inputs
        study_hours = st.slider("📚 Study hours per day:", 0, 12, 4, 
                                help="How many hours do you typically study each day?")
        
        stress_level = st.slider("😰 Current stress level (1-10):", 1, 10, 5,
                                 help="1 = Very relaxed, 10 = Extremely stressed")
        
        sleep_hours = st.slider("😴 Sleep hours per night:", 3, 12, 7,
                                help="How many hours of sleep do you get on average?")
        
        # Boolean input
        has_upcoming_exam = st.checkbox("📅 I have an exam coming up soon (within 2 weeks)")
        
        # Visual indicators
        st.markdown("---")
        if stress_level >= 8:
            st.warning("⚠️ High stress detected!")
        if sleep_hours < 6:
            st.warning("⚠️ Sleep deprivation alert!")
        if study_hours >= 8 and stress_level >= 7:
            st.error("🚨 Burnout risk detected!")
    
    st.markdown("---")
    
    # Default question based on category
    question = f"I need help with {category.lower()}"

    # Get Advice button
    if st.button("🔍 Get Personalized Advice", type="primary", use_container_width=True):
        with st.spinner("🤔 Analyzing your situation with advanced rule-based reasoning..."):
            # Use the new multi-input method
            response = study_expert.process_query_with_inputs(
                category=category,
                question=question,
                study_hours=study_hours,
                stress_level=stress_level,
                learning_style=learning_style,
                has_upcoming_exam=has_upcoming_exam,
                sleep_hours=sleep_hours
            )
            
            if response:
                display_study_guide_response(response)
            else:
                st.error("❌ Unable to generate recommendations. Please try again.")

def display_study_guide_response(response):
    """Display study guide response with proper formatting."""
    if isinstance(response, dict):
        # Display user profile summary if available
        if response.get('user_profile'):
            profile = response['user_profile']
            with st.expander("👤 Your Profile Summary", expanded=False):
                cols = st.columns(3)
                if profile.get('study_hours'):
                    cols[0].metric("📚 Study Hours/Day", f"{profile['study_hours']}h")
                if profile.get('stress_level'):
                    stress_color = "🔴" if profile['stress_level'] >= 7 else "🟡" if profile['stress_level'] >= 4 else "🟢"
                    cols[1].metric("😰 Stress Level", f"{stress_color} {profile['stress_level']}/10")
                if profile.get('sleep_hours'):
                    sleep_emoji = "✅" if profile['sleep_hours'] >= 7 else "⚠️"
                    cols[2].metric("😴 Sleep Hours", f"{sleep_emoji} {profile['sleep_hours']}h")
                
                if profile.get('learning_style'):
                    st.info(f"🎨 **Learning Style:** {profile['learning_style'].capitalize()}")
                if profile.get('has_upcoming_exam'):
                    st.warning("📅 **Upcoming Exam:** Yes - using time-sensitive strategies")
        
        # Display uncertainty explanation (prominent)
        if response.get('uncertainty_explanation'):
            st.markdown(response['uncertainty_explanation'])
        
        # Display confidence score with breakdown
        if response.get('confidence'):
            conf_col1, conf_col2 = st.columns([1, 2])
            with conf_col1:
                st.metric("💯 Confidence", f"{response['confidence']:.0%}")
            with conf_col2:
                if response.get('confidence_breakdown'):
                    breakdown = response['confidence_breakdown']
                    with st.expander("� Confidence Breakdown"):
                        st.markdown(f"**Base Inputs:** +{breakdown.get('base_inputs', 0)*100:.0f}%")
                        st.markdown(f"**Missing Data Penalty:** {breakdown.get('missing_data_penalty', 0)*100:.0f}%")
                        st.markdown(f"**Pattern Bonus:** +{breakdown.get('pattern_bonus', 0)*100:.0f}%")
                        st.markdown(f"**Risk Penalty:** {breakdown.get('risk_penalty', 0)*100:.0f}%")
        
        # Display missing information warnings
        if response.get('missing_info_suggestions') and len(response['missing_info_suggestions']) > 0:
            with st.expander("💡 Improve Recommendations by Providing", expanded=True):
                st.markdown("**Adding this information would significantly improve recommendation quality:**")
                for suggestion in response['missing_info_suggestions']:
                    st.markdown(f"• {suggestion}")
        
        # Display concept/diagnosis
        if response.get('concept'):
            st.success(f"### {response['concept']}")
        
        if response.get('diagnosis'):
            st.markdown(f"**💡 Diagnosis:** {response['diagnosis']}")
        
        # Display explanation
        if response.get('explanation'):
            st.markdown(f"**📝 Explanation:**\n\n{response['explanation']}")
        
        # Display recommendations (highlighted)
        if response.get('recommendation'):
            st.markdown("### ✅ Personalized Recommendations")
            st.markdown(response['recommendation'])
        
        # Display examples
        if response.get('examples') and len(response['examples']) > 0:
            with st.expander("📚 Practical Examples"):
                for example in response['examples']:
                    st.markdown(f"• {example}")
        
        # Display additional resources
        if response.get('resources') and len(response['resources']) > 0:
            with st.expander("🔗 Additional Resources"):
                for resource in response['resources']:
                    st.markdown(f"• {resource}")
        
        # Display reasoning trace (optional expander)
        if response.get('reasoning_trace') and len(response['reasoning_trace']) > 0:
            with st.expander("🔍 View Reasoning Process (Explainability)"):
                st.markdown("**How the system arrived at this conclusion:**")
                for step in response['reasoning_trace']:
                    st.markdown(f"- {step}")
        
        # Display inferred facts (for advanced users)
        if response.get('inferred_facts') and len(response['inferred_facts']) > 0:
            with st.expander("🧠 Inferred Facts & Patterns"):
                st.markdown("**Additional insights discovered from your inputs:**")
                for fact in response['inferred_facts']:
                    st.markdown(f"• {fact}")
        
        # Display fired rules (for debugging/transparency)
        if response.get('fired_rules') and len(response['fired_rules']) > 0:
            with st.expander("⚙️ Rules Applied (Technical Details)"):
                st.markdown(f"**{len(response['fired_rules'])} rules were triggered:**")
                for rule_id in response['fired_rules']:
                    st.code(rule_id)
    else:
        st.markdown(str(response))
        if st.button("How does respiration work?"):
            st.session_state.messages.append({"role": "user", "content": "How does respiration work?"})
            st.rerun()


if __name__ == "__main__":
    main()
