# 🚀 Quick Reference Guide: Multi-Input Study Guide Expert System

## ⚡ Quick Start

```bash
# 1. Navigate to project
cd "c:\UOM\L3S1\Expert Systems\EduMentor"

# 2. Activate virtual environment
.\.venv\Scripts\Activate.ps1

# 3. Run Streamlit app
streamlit run main.py

# 4. Open browser to http://localhost:8501
# 5. Go to "Study Guide" tab
# 6. Fill multi-input form and get personalized advice!
```

## 📋 Input Cheat Sheet

| Input Type | Options/Range | Purpose |
|------------|---------------|---------|
| 🎯 **Category** | Memory, Focus, Stress, Time Mgmt, Sleep, Motivation, Exam Prep, Confidence | Main topic area |
| ❓ **Question** | Text (min 10 chars) | Specific concern |
| 📚 **Study Hours** | 0-12 (slider) | Daily study time |
| 😰 **Stress Level** | 1-10 (slider) | Current stress state |
| 😴 **Sleep Hours** | 3-12 (slider) | Nightly sleep |
| 🎨 **Learning Style** | Visual, Auditory, Kinesthetic, Reading | Preferred method |
| 📅 **Upcoming Exam** | Checkbox | Time pressure indicator |

## 🎯 Quick Presets

Click these for instant scenarios:

- **😰 High Stress**: stress=9, study=5
- **😴 Sleep Issues**: sleep=5, stress=7  
- **📚 Exam Prep**: exam=True, stress=8
- **🎯 Focus Problems**: stress=6, study=3

## 🧠 Key Rules (Priority Order)

| Priority | Rule | Triggers When | Result |
|----------|------|---------------|--------|
| 20 | **Stress + Sleep** | stress≥7 AND sleep<6 | poor_focus, memory_impaired |
| 18 | **Low Study + Exam** | study<3 AND exam=True | needs_intensive_study |
| 18 | **Burnout Risk** | study≥8 AND stress≥7 | ⚠️ BURNOUT WARNING |
| 15 | **High Stress** | stress≥8 | high_stress, low_focus |
| 15 | **Low Sleep** | sleep<7 | sleep_deprived, memory_weak |
| 12 | **Optimal + Style** | stress 4-6 AND study≥4 | optimize_with_style |
| 10 | **Visual Memory** | memory + visual | use_visualization |
| 10 | **Optimal State** | sleep≥7 AND stress≤3 | ✅ optimal_state |
| 8 | **Kinesthetic** | style=kinesthetic | active_learning |
| 8 | **Auditory** | style=auditory | verbal_learning |

## 📊 Stress Level Guide

| Level | Color | Meaning | Triggers |
|-------|-------|---------|----------|
| 1-3 | 🟢 | Low - Optimal | Optimal state bonus |
| 4-6 | 🟡 | Moderate | Style optimization |
| 7-8 | 🔴 | High | Focus issues, combine warnings |
| 9-10 | 🚨 | Critical | Burnout risk if high hours |

## 😴 Sleep Hours Guide

| Hours | Status | Effect | Recommendations |
|-------|--------|--------|-----------------|
| <6 | ⚠️ Critical | Memory/focus impaired | PRIORITY: Sleep recovery |
| 6-7 | ⚠️ Low | Suboptimal performance | Improve to 7-8 hours |
| 7-8 | ✅ Good | Optimal cognitive function | Maintain current |
| 8+ | ✅ Excellent | Peak performance | Excellent conditions |

## 🎨 Learning Style Strategies

### Visual 👁️
- Mind maps, diagrams
- Color-coded notes
- Memory palace technique
- Flowcharts, infographics

### Auditory 🎧
- Record explanations
- Discussion groups
- Verbal mnemonics
- Podcasts, lectures

### Kinesthetic 🏃
- Physical flashcards
- Walk while reviewing
- Hands-on demonstrations
- Active experimentation

### Reading/Writing 📖
- Rewrite notes
- Detailed outlines
- Written summaries
- Textbook-based study

## 🚨 Warning Indicators

### ⚠️ High Stress (stress ≥ 8)
```
Triggers:
  • Stress management recommendations
  • Low-stress method adaptations
  • Breathing exercises priority

Combinations:
  + Low sleep → Poor focus + memory impaired
  + High hours → BURNOUT RISK
```

### ⚠️ Sleep Deprivation (sleep < 6)
```
Triggers:
  • Sleep recovery priority
  • Memory consolidation warnings
  • Cognitive performance alerts

Combinations:
  + High stress → Poor focus + memory impaired
  + Memory category → Power naps recommended
```

### 🚨 Burnout Risk (study ≥ 8 AND stress ≥ 7)
```
Triggers:
  • BURNOUT WARNING message
  • Mandatory break recommendations
  • Sustainability concerns

Action:
  Take 1-hour breaks every 3 hours
  Reduce study hours or stress
```

### ✅ Optimal State (sleep ≥ 7 AND stress ≤ 3)
```
Triggers:
  • Encouragement messages
  • Performance optimization tips
  • Advanced technique suggestions

Action:
  Maximize with active recall
  Use peak cognitive state
```

## 💡 Example Scenarios

### Scenario 1: Exam Crisis
```
Input:
  Category: Exam Preparation
  Question: "Exam tomorrow, not prepared!"
  Study: 2h, Stress: 9, Sleep: 6h
  Exam: True

Output:
  Confidence: 99%
  Inferred: needs_intensive_study, time_pressure, high_stress
  Recommendations:
    1. Practice past papers (most effective)
    2. Focus on high-weightage topics (80/20)
    3. Light review only - no new material
    4. Sleep by 10pm for memory consolidation
```

### Scenario 2: Memory + Visual
```
Input:
  Category: Memory
  Question: "How to remember better?"
  Study: 4h, Stress: 5, Sleep: 7h
  Style: Visual

Output:
  Confidence: 99%
  Inferred: optimize_with_visual_learning, use_visualization
  Recommendations:
    1. Spaced repetition (Day 1, 3, 7, 14, 30)
    2. Active recall practice
    3. Visual Learning Strategy: mind maps, memory palace
    4. Color-coded notes for organization
```

### Scenario 3: Burnout Warning
```
Input:
  Category: Stress
  Question: "Exhausted from studying"
  Study: 10h, Stress: 9, Sleep: 6h

Output:
  Confidence: 99%
  Inferred: burnout_risk, high_stress, sleep_deprived
  Recommendations:
    1. ⚠️ BURNOUT WARNING - mandatory 1h breaks every 3h
    2. 4-7-8 breathing technique
    3. Reduce study hours to sustainable level
    4. Improve sleep for recovery
```

## 🔍 Understanding the Response

### Profile Summary
```
👤 Your Profile Summary
┌──────────────────────────────────┐
│ 📚 Study: 4h  😰 Stress: 🟡 6/10  │
│ 😴 Sleep: ✅ 7h                   │
│ 🎨 Style: Visual                 │
│ 📅 Exam: Yes                     │
└──────────────────────────────────┘
```

### Confidence Interpretation
- **90-99%**: High confidence, comprehensive analysis
- **80-89%**: Good confidence, solid recommendations
- **70-79%**: Moderate confidence, general advice
- **60-69%**: Lower confidence, may need more inputs

### Reasoning Trace Example
```
🔍 View Reasoning Process
  - 📋 Input Analysis:
  - Category: Memory
  - Stress Level: 8/10
  - Sleep Hours: 5
  
  - 🔍 Inference Engine Running...
  - ⚠️ Rule Fired: High stress (8/10) + Low sleep (5h) → Poor focus & memory
  - ⚠️ Rule Fired: Low sleep (5h) → Weak memory
  
  - 🎯 Generating Recommendations for: MEMORY
  - 📊 Confidence: 99% (Base: 90%, Adjustment: +9%)
```

## 🎓 Best Practices

### For Best Results:
1. ✅ **Be specific** in your question (>10 characters)
2. ✅ **Fill all inputs** for maximum confidence
3. ✅ **Choose accurate values** (realistic stress/sleep)
4. ✅ **Select correct learning style** for personalized tips
5. ✅ **Check "Upcoming exam"** if within 2 weeks

### What to Expect:
- **99% confidence** with complete, consistent inputs
- **6+ recommendations** (base + adaptive)
- **Inferred facts** showing pattern recognition
- **Learning style adaptations** in recommendations
- **Warning alerts** for burnout/stress/sleep issues

### Explainability Features:
- Expand **"Reasoning Process"** to see how system decided
- Check **"Inferred Facts"** for additional insights
- View **"Rules Applied"** for technical transparency
- Review **"Profile Summary"** for input verification

## 🛠️ Testing

### Run Test Suite:
```bash
python test_multi_input.py
```

### Expected Output:
```
Test 1: High Stress + Visual + Memory      ✅ 99%
Test 2: Sleep Deprivation + Focus          ✅ 99%
Test 3: Burnout Risk Detection             ✅ 99%
Test 4: Optimal Learning State             ✅ 99%
Test 5: Exam Crisis Management             ✅ 99%
```

## 📚 Documentation Files

- **`UPGRADE_SUMMARY.md`**: Complete upgrade overview
- **`UPGRADE_DOCUMENTATION.md`**: Technical documentation
- **`ARCHITECTURE_DIAGRAM.md`**: System architecture
- **`QUICK_REFERENCE.md`**: This guide (quick lookup)

## 🆘 Troubleshooting

### Issue: "Can't find focus category"
**Solution**: Focus category added. Restart Streamlit.

### Issue: Low confidence (<70%)
**Solution**: Fill more input fields, be specific in question.

### Issue: Generic recommendations
**Solution**: Set learning style, adjust stress/sleep sliders.

### Issue: No adaptive recommendations
**Solution**: Check if extreme values (stress ≥8, sleep <6, study ≥8).

## 📞 Quick Support

### Check System Status:
```bash
# Test expert system
python test_multi_input.py

# Verify KB loaded
python -c "from experts.study_guide_expert import StudyGuideExpert; print('✅ OK' if StudyGuideExpert().kb else '❌ ERROR')"
```

### Restart Streamlit:
```bash
# If app freezes or errors
Ctrl+C  (to stop)
streamlit run main.py  (to restart)
```

---

**Quick Access**: http://localhost:8501  
**Status**: ✅ Production Ready  
**Version**: 2.0  
**Last Updated**: November 10, 2025
