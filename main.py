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
    
    # Main content - simplified header
    st.markdown("### 📊 Personalized Study Analysis")
    st.markdown("*Provide your information to get personalized study recommendations*")
    
    st.markdown("---")
    
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
        st.caption("💡 *Leave fields empty to test uncertainty handling*")
        
        # Numeric inputs as number_input (can be left empty)
        study_hours = st.number_input(
            "📚 Study hours per day (0-12):", 
            min_value=0, 
            max_value=12, 
            value=None,
            step=1,
            help="How many hours do you typically study each day? Leave empty if unsure.",
            placeholder="e.g., 4"
        )
        
        stress_level = st.number_input(
            "😰 Current stress level (1-10):", 
            min_value=1, 
            max_value=10, 
            value=None,
            step=1,
            help="1 = Very relaxed, 10 = Extremely stressed. Leave empty if unsure.",
            placeholder="e.g., 5"
        )
        
        sleep_hours = st.number_input(
            "😴 Sleep hours per night (1-12):", 
            min_value=1, 
            max_value=12, 
            value=None,
            step=1,
            help="How many hours of sleep do you get on average? Leave empty if unsure.",
            placeholder="e.g., 7"
        )
        
        # Boolean input with tri-state (Yes/No/Not Sure)
        exam_option = st.radio(
            "📅 Do you have an exam coming up soon (within 2 weeks)?",
            ["Not sure", "Yes", "No"],
            horizontal=True
        )
        has_upcoming_exam = None if exam_option == "Not sure" else (exam_option == "Yes")
        
        # Visual indicators (only show if values are provided)
        st.markdown("---")
        warnings_shown = False
        if stress_level is not None and stress_level >= 8:
            st.warning("⚠️ High stress detected!")
            warnings_shown = True
        if sleep_hours is not None and sleep_hours < 6:
            st.warning("⚠️ Sleep deprivation alert!")
            warnings_shown = True
        if study_hours is not None and stress_level is not None and study_hours >= 8 and stress_level >= 7:
            st.error("🚨 Burnout risk detected!")
            warnings_shown = True
        
        if not warnings_shown:
            st.info("ℹ️ Provide more data for personalized insights")
    
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
    """Display study guide response with proper formatting and LLM refinement."""
    if isinstance(response, dict):
        
        # Display uncertainty explanation (prominent)
        if response.get('uncertainty_explanation'):
            st.markdown(response['uncertainty_explanation'])
        
        # Display confidence score
        if response.get('confidence'):
            st.metric("💯 Confidence", f"{response['confidence']:.0%}")
        
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
        
        # Display LLM reasoning explanation - STEP-BY-STEP INFERENCE PROCESS
        if response.get('reasoning_trace') and len(response['reasoning_trace']) > 0:
            st.markdown("### 🤔 Why These Recommendations?")
            st.markdown("*Understanding how the expert system analyzed your profile*")
            
            with st.spinner("🧠 Analyzing inference process..."):
                reasoning = generate_reasoning_explanation(response)
                
                # Display step-by-step reasoning
                st.markdown("#### 📊 Step-by-Step Reasoning Process")
                st.info(reasoning)
                
                # Show detailed rule firing in expandable section
                with st.expander("🔍 View Detailed Rule Firing Sequence", expanded=False):
                    st.markdown("**How the inference engine analyzed your data:**")
                    
                    # Organize rules by category
                    critical_rules = [r for r in response['reasoning_trace'] if r.strip() and ("🚨" in r or "CRITICAL" in r)]
                    warning_rules = [r for r in response['reasoning_trace'] if r.strip() and "⚠️" in r and "🚨" not in r]
                    optimal_rules = [r for r in response['reasoning_trace'] if r.strip() and ("✓" in r or "✅" in r)]
                    other_rules = [r for r in response['reasoning_trace'] if r.strip() and r not in critical_rules + warning_rules + optimal_rules]
                    
                    if critical_rules:
                        st.markdown("**🚨 Critical Patterns Detected:**")
                        for rule in critical_rules:
                            st.markdown(f"- {rule}")
                        st.markdown("")
                    
                    if warning_rules:
                        st.markdown("**⚠️ Warning Patterns Detected:**")
                        for rule in warning_rules:
                            st.markdown(f"- {rule}")
                        st.markdown("")
                    
                    if optimal_rules:
                        st.markdown("**✅ Positive Patterns Detected:**")
                        for rule in optimal_rules:
                            st.markdown(f"- {rule}")
                        st.markdown("")
                    
                    if other_rules:
                        st.markdown("**🔍 Additional Inferences:**")
                        for rule in other_rules:
                            st.markdown(f"- {rule}")
                    
                    # Show inferred facts
                    if response.get('inferred_facts'):
                        st.markdown("---")
                        st.markdown("**🎯 Patterns Identified:**")
                        for fact in response['inferred_facts']:
                            st.markdown(f"✓ `{fact}`")
        
        # Display explanation
        if response.get('explanation'):
            st.markdown(f"**📝 Explanation:**\n\n{response['explanation']}")
        
        # Display recommendations - REFINED WITH LLM
        if response.get('recommendation'):
            st.markdown("### ✅ Personalized Recommendations")
            
            # Show original expert system recommendations
            with st.spinner("🤖 Refining recommendations with AI..."):
                # Refine with LLM
                refined = refine_study_guide_with_llm(response)
                st.markdown(refined)
        
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
    else:
        st.markdown(str(response))
        if st.button("How does respiration work?"):
            st.session_state.messages.append({"role": "user", "content": "How does respiration work?"})
            st.rerun()


def refine_study_guide_with_llm(response: dict) -> str:
    """
    Refine study guide recommendations using LLM to make them more personalized and actionable.
    
    Args:
        response: The expert system response dictionary
        
    Returns:
        Refined recommendation text
    """
    from openai import OpenAI
    import os
    
    # Get OpenAI client
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    # Extract information from response
    category = response.get('concept', 'Study Guidance')
    diagnosis = response.get('diagnosis', '')
    explanation = response.get('explanation', '')
    recommendations = response.get('recommendation', '')
    user_profile = response.get('user_profile', {})
    
    # Build context for LLM
    context_parts = [f"**Category:** {category}"]
    
    if diagnosis:
        context_parts.append(f"**Diagnosis:** {diagnosis}")
    
    if user_profile:
        profile_str = []
        if user_profile.get('study_hours'):
            profile_str.append(f"Studies {user_profile['study_hours']} hours/day")
        if user_profile.get('stress_level'):
            profile_str.append(f"Stress level: {user_profile['stress_level']}/10")
        if user_profile.get('sleep_hours'):
            profile_str.append(f"Gets {user_profile['sleep_hours']} hours sleep")
        if user_profile.get('learning_style'):
            profile_str.append(f"Learning style: {user_profile['learning_style']}")
        if user_profile.get('has_upcoming_exam'):
            profile_str.append("Has upcoming exam")
        
        if profile_str:
            context_parts.append(f"**Student Profile:** {', '.join(profile_str)}")
    
    context = "\n".join(context_parts)
    
    # Create prompt for LLM
    prompt = f"""You are an expert educational advisor helping a student with their study challenges.

Based on the expert system analysis:

{context}

**Expert System Recommendations:**
{recommendations}

**Scientific Explanation:**
{explanation}

CRITICAL INSTRUCTIONS:
- Use ONLY the information provided above from the expert system
- Do NOT add any external knowledge, techniques, or recommendations not mentioned in the expert system output
- Do NOT introduce new concepts, methods, or resources
- Your role is to REPHRASE and REORGANIZE the existing recommendations only

Please refine these recommendations to make them:
1. More personalized and empathetic (using the student profile provided)
2. Action-oriented with clear next steps (based on the expert recommendations)
3. Encouraging and motivating (but stay true to the expert system's advice)
4. Easy to understand and implement (simplify the language only)

Transform the expert system's recommendations into a conversational, supportive format.
Use bullet points for clarity. Focus on what the student should DO RIGHT NOW and THIS WEEK.
Remember: ONLY use information from the expert system above - do not add new suggestions.

Refined Recommendations:"""

    try:
        # Call OpenAI API
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an empathetic educational advisor who rephrases expert system recommendations. You MUST use only the information provided by the expert system - do not add external knowledge or new suggestions. Your role is to make the existing recommendations more conversational, personalized, and actionable while staying strictly faithful to the source material."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=800
        )
        
        refined_text = completion.choices[0].message.content.strip()
        return refined_text
        
    except Exception as e:
        # Fallback to original recommendations if LLM fails
        st.warning(f"Could not refine recommendations with AI: {str(e)}")
        return recommendations


def generate_reasoning_explanation(response: dict) -> str:
    """
    Generate LLM-powered step-by-step explanation of the inference process.
    Shows which rules fired and why specific recommendations were chosen.
    
    Args:
        response: The expert system response dictionary
        
    Returns:
        Detailed step-by-step reasoning explanation
    """
    from openai import OpenAI
    import os
    
    # Get OpenAI client
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    # Extract analysis information
    fired_rules = response.get('fired_rules', [])
    inferred_facts = response.get('inferred_facts', [])
    reasoning_trace = response.get('reasoning_trace', [])
    user_profile = response.get('user_profile', {})
    diagnosis = response.get('diagnosis', '')
    confidence = response.get('confidence', 0)
    
    # Build detailed context for step-by-step reasoning
    profile_items = [f"**{k.replace('_', ' ').title()}**: {v}" for k, v in user_profile.items() if v is not None]
    profile_str = "\n".join(profile_items)
    
    # Organize reasoning trace by type (warnings, optimal, inferences)
    critical_rules = []
    warning_rules = []
    optimal_rules = []
    inference_rules = []
    
    for rule in reasoning_trace:
        if rule.strip():
            if "🚨" in rule or "CRITICAL" in rule or "EMERGENCY" in rule:
                critical_rules.append(rule)
            elif "⚠️" in rule or "Rule Fired:" in rule:
                warning_rules.append(rule)
            elif "✓" in rule or "✅" in rule:
                optimal_rules.append(rule)
            elif "Infer:" in rule or "→" in rule:
                inference_rules.append(rule)
            else:
                inference_rules.append(rule)
    
    # Build organized rules string
    rules_sections = []
    if critical_rules:
        rules_sections.append("**🚨 CRITICAL PATTERNS:**\n" + "\n".join([f"  • {r.replace('🚨', '').strip()}" for r in critical_rules]))
    if warning_rules:
        rules_sections.append("**⚠️ WARNING PATTERNS:**\n" + "\n".join([f"  • {r.replace('⚠️', '').strip()}" for r in warning_rules]))
    if optimal_rules:
        rules_sections.append("**✅ OPTIMAL PATTERNS:**\n" + "\n".join([f"  • {r.replace('✓', '').replace('✅', '').strip()}" for r in optimal_rules]))
    if inference_rules:
        rules_sections.append("**🔍 INFERENCES:**\n" + "\n".join([f"  • {r.strip()}" for r in inference_rules]))
    
    rules_str = "\n\n".join(rules_sections) if rules_sections else "No specific rules fired"
    
    facts_str = "\n".join([f"  • {fact}" for fact in inferred_facts]) if inferred_facts else "baseline assessment"
    
    # Create detailed step-by-step prompt
    prompt = f"""You are analyzing an expert system's inference process. Provide a clear, step-by-step explanation of HOW and WHY the system arrived at its recommendations.

**📊 STUDENT PROFILE (INPUT DATA):**
{profile_str}

**🔍 INFERENCE ENGINE RESULTS:**

{rules_str}

**🎯 DETECTED PATTERNS:**
{facts_str}

**💡 FINAL DIAGNOSIS:**
{diagnosis}

**📈 CONFIDENCE LEVEL:** {confidence:.0%}

---

**YOUR TASK:**
Write a step-by-step explanation (3-5 sentences) that walks through the reasoning process:

1. **Start with the input**: What data did the student provide?
2. **Rule firing sequence**: Which rules were triggered and in what order (mention specific patterns like "0h study", "7h sleep", "1/10 stress")?
3. **Pattern detection logic**: Why did those specific rules fire? What thresholds or conditions were met?
4. **Priority explanation**: Why are certain recommendations prioritized over others?
5. **Conclusion**: How do these patterns together inform the final recommendations?

**CRITICAL CONSTRAINTS:**
- Use ONLY the information provided above from the expert system
- Reference specific numbers from the profile (e.g., "0 hours of study", "7 hours of sleep")
- Explain the LOGIC behind each rule firing
- Be precise about which patterns triggered which rules
- Do NOT add external knowledge or new recommendations
- Be conversational but technically accurate

**FORMAT:**
Present as a flowing narrative that connects: Input Data → Rules Fired → Patterns Detected → Recommendations Logic"""

    try:
        # Call GPT-4o-mini for detailed reasoning explanation
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert system explainer. You provide clear, step-by-step explanations of inference processes, showing how input data triggers specific rules and leads to recommendations. Use only the provided information."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,  # Lower temperature for factual explanation
            max_tokens=400  # Increased for detailed explanation
        )
        
        return completion.choices[0].message.content.strip()
    
    except Exception as e:
        # Fallback to structured explanation if LLM fails
        fallback = f"**Analysis of Your Profile:**\n\n"
        fallback += f"Your input data: {', '.join([f'{k}={v}' for k, v in user_profile.items() if v is not None])}\n\n"
        fallback += f"**Rules Triggered:**\n"
        for rule in reasoning_trace[:5]:
            if rule.strip():
                fallback += f"• {rule}\n"
        fallback += f"\n**Result:** {diagnosis}"
        return fallback


if __name__ == "__main__":
    main()
