#!/usr/bin/env python
# Update display function in main.py

with open(r'main.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the function and replace it
output = []
skip = False
indent = "    "

for i, line in enumerate(lines):
    if 'def display_study_guide_response(response):' in line:
        # Write new function
        output.append('def display_study_guide_response(response):\n')
        output.append('    """Display study guide response with proper formatting."""\n')
        output.append('    if isinstance(response, dict):\n')
        output.append('        # Display user profile summary if available\n')
        output.append('        if response.get(\'user_profile\'):\n')
        output.append('            profile = response[\'user_profile\']\n')
        output.append('            with st.expander("👤 Your Profile Summary", expanded=False):\n')
        output.append('                cols = st.columns(3)\n')
        output.append('                if profile.get(\'study_hours\'):\n')
        output.append('                    cols[0].metric("📚 Study Hours/Day", f"{profile[\'study_hours\']}h")\n')
        output.append('                if profile.get(\'stress_level\'):\n')
        output.append('                    stress_color = "🔴" if profile[\'stress_level\'] >= 7 else "🟡" if profile[\'stress_level\'] >= 4 else "🟢"\n')
        output.append('                    cols[1].metric("😰 Stress Level", f"{stress_color} {profile[\'stress_level\']}/10")\n')
        output.append('                if profile.get(\'sleep_hours\'):\n')
        output.append('                    sleep_emoji = "✅" if profile[\'sleep_hours\'] >= 7 else "⚠️"\n')
        output.append('                    cols[2].metric("😴 Sleep Hours", f"{sleep_emoji} {profile[\'sleep_hours\']}h")\n')
        output.append('                \n')
        output.append('                if profile.get(\'learning_style\'):\n')
        output.append('                    st.info(f"🎨 **Learning Style:** {profile[\'learning_style\'].capitalize()}")\n')
        output.append('                if profile.get(\'has_upcoming_exam\'):\n')
        output.append('                    st.warning("📅 **Upcoming Exam:** Yes - using time-sensitive strategies")\n')
        output.append('        \n')
        output.append('        # Display confidence score\n')
        output.append('        if response.get(\'confidence\'):\n')
        output.append('            st.info(f"💯 **Confidence:** {response[\'confidence\']:.0%}")\n')
        output.append('        \n')
        output.append('        # Display concept/diagnosis\n')
        output.append('        if response.get(\'concept\'):\n')
        output.append('            st.success(f"### {response[\'concept\']}")\n')
        output.append('        \n')
        output.append('        if response.get(\'diagnosis\'):\n')
        output.append('            st.markdown(f"**💡 Diagnosis:** {response[\'diagnosis\']}")\n')
        output.append('        \n')
        output.append('        # Display explanation\n')
        output.append('        if response.get(\'explanation\'):\n')
        output.append('            st.markdown(f"**📝 Explanation:**\\n\\n{response[\'explanation\']}")\n')
        output.append('        \n')
        output.append('        # Display recommendations (highlighted)\n')
        output.append('        if response.get(\'recommendation\'):\n')
        output.append('            st.markdown("### ✅ Personalized Recommendations")\n')
        output.append('            st.markdown(response[\'recommendation\'])\n')
        output.append('        \n')
        output.append('        # Display examples\n')
        output.append('        if response.get(\'examples\') and len(response[\'examples\']) > 0:\n')
        output.append('            with st.expander("📚 Practical Examples"):\n')
        output.append('                for example in response[\'examples\']:\n')
        output.append('                    st.markdown(f"• {example}")\n')
        output.append('        \n')
        output.append('        # Display additional resources\n')
        output.append('        if response.get(\'resources\') and len(response[\'resources\']) > 0:\n')
        output.append('            with st.expander("🔗 Additional Resources"):\n')
        output.append('                for resource in response[\'resources\']:\n')
        output.append('                    st.markdown(f"• {resource}")\n')
        output.append('        \n')
        output.append('        # Display reasoning trace (optional expander)\n')
        output.append('        if response.get(\'reasoning_trace\') and len(response[\'reasoning_trace\']) > 0:\n')
        output.append('            with st.expander("🔍 View Reasoning Process (Explainability)"):\n')
        output.append('                st.markdown("**How the system arrived at this conclusion:**")\n')
        output.append('                for step in response[\'reasoning_trace\']:\n')
        output.append('                    st.markdown(f"- {step}")\n')
        output.append('        \n')
        output.append('        # Display inferred facts (for advanced users)\n')
        output.append('        if response.get(\'inferred_facts\') and len(response[\'inferred_facts\']) > 0:\n')
        output.append('            with st.expander("🧠 Inferred Facts & Patterns"):\n')
        output.append('                st.markdown("**Additional insights discovered from your inputs:**")\n')
        output.append('                for fact in response[\'inferred_facts\']:\n')
        output.append('                    st.markdown(f"• {fact}")\n')
        output.append('        \n')
        output.append('        # Display fired rules (for debugging/transparency)\n')
        output.append('        if response.get(\'fired_rules\') and len(response[\'fired_rules\']) > 0:\n')
        output.append('            with st.expander("⚙️ Rules Applied (Technical Details)"):\n')
        output.append('                st.markdown(f"**{len(response[\'fired_rules\'])} rules were triggered:**")\n')
        output.append('                for rule_id in response[\'fired_rules\']:\n')
        output.append('                    st.code(rule_id)\n')
        
        skip = True
        continue
    
    if skip:
        # Look for the end of the function (next function or class def)
        if line.strip().startswith('if st.button("How does respiration work?")'):
            output.append('    else:\n')
            output.append('        st.markdown(str(response))\n')
            output.append(line)
            skip = False
        continue
    
    output.append(line)

with open(r'main.py', 'w', encoding='utf-8') as f:
    f.writelines(output)

print("✅ Display function updated successfully!")
