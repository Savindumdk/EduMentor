# 🚀 Multi-Input Study Guide Expert System - Upgrade Documentation

## 📋 Overview

The Study Guide Expert System has been upgraded from a simple text-based query system to a **production-grade, multi-input expert system** that combines qualitative and quantitative reasoning for highly personalized study recommendations.

## ✨ New Features

### 1. **Multi-Input Interface**
Instead of just selecting a category and question, users now provide:

- **📝 Text Input**: Category selection + detailed question
- **📊 Numeric Input**: Study hours per day (0-12)
- **📈 Scale Input**: Stress level (1-10)
- **🎨 Multiple-Choice**: Learning style (Visual/Auditory/Kinesthetic/Reading)
- **✅ Boolean**: Upcoming exam status (Yes/No)
- **😴 Numeric**: Sleep hours per night (3-12)

### 2. **Advanced Rule-Based Reasoning**

#### 10 New Inference Rules:
1. **High Stress + Low Sleep** → Poor focus & memory impairment
2. **Low Study Hours + Upcoming Exam** → Intensive study strategy needed
3. **High Stress Alone** → Focus issues
4. **Low Sleep** → Memory weakness
5. **Moderate Stress + Good Hours** → Optimize with learning style
6. **Visual Learner + Memory** → Use visualization techniques
7. **High Hours + High Stress** → Burnout risk warning
8. **Good Sleep + Low Stress** → Optimal learning state
9. **Kinesthetic Learner** → Active learning methods
10. **Auditory Learner** → Discussion and verbal methods

### 3. **Adaptive Recommendations**

The system now generates **context-aware, personalized recommendations** based on:

- **Stress Level**: 
  - ≥8: Priority stress management
  - 7-8: Moderate stress handling
  - ≤3: Optimize for performance

- **Sleep Hours**:
  - <6: Critical sleep recovery advice
  - 6-7: Sleep improvement tips
  - ≥7: Optimal state encouragement

- **Study Hours**:
  - <3 with exam: Urgent time management
  - ≥8 with high stress: Burnout warnings
  - 4-7: Balanced optimization

- **Learning Style**:
  - Visual: Mind maps, color coding, visualization
  - Auditory: Discussions, verbal methods, recordings
  - Kinesthetic: Hands-on, movement, physical models
  - Reading: Detailed notes, outlines, summaries

### 4. **Enhanced Explainability**

Every recommendation now includes:

- **📊 User Profile Summary**: Visual display of all inputs with metrics
- **💯 Confidence Score**: 60-99% based on pattern matching and input completeness
- **💡 Personalized Diagnosis**: Context-aware analysis combining all factors
- **🔍 Reasoning Trace**: Step-by-step explanation of how the system reached its conclusion
- **🧠 Inferred Facts**: Additional insights discovered (e.g., "burnout_risk", "optimal_learning_state")
- **⚙️ Fired Rules**: Technical details showing which rules were triggered

### 5. **New Knowledge Base Category**

Added **Focus & Concentration Enhancement** category with:
- 5 specialized rules
- Pomodoro technique recommendations
- Digital distraction management
- Mindfulness and attention training
- Environment optimization strategies

## 🏗️ Technical Architecture

### File Structure
```
EduMentor/
├── experts/
│   ├── study_guide_expert.py    # Core expert system (UPGRADED)
│   ├── study_guide_kb.json      # Knowledge base (EXPANDED)
│   └── nlp_processor.py          # NLP layer (unchanged)
├── main.py                       # Streamlit UI (REDESIGNED)
├── test_multi_input.py           # Comprehensive test suite
└── UPGRADE_DOCUMENTATION.md      # This file
```

### Key Methods

#### `StudyGuideExpert.process_query_with_inputs()`
```python
def process_query_with_inputs(self, category, question, study_hours=None, 
                             stress_level=None, learning_style=None, 
                             has_upcoming_exam=None, sleep_hours=None):
    """
    Main entry point for multi-input analysis.
    
    Args:
        category (str): Topic category
        question (str): User's text question
        study_hours (int): Hours per day (0-12)
        stress_level (int): Stress on scale 1-10
        learning_style (str): Visual/Auditory/Kinesthetic/Reading
        has_upcoming_exam (bool): Exam upcoming status
        sleep_hours (int): Hours per night (3-12)
    
    Returns:
        dict: Comprehensive response with recommendations, confidence, reasoning, etc.
    """
```

#### Adaptive Recommendation Generator
```python
def _generate_adaptive_recommendations(self, category, profile):
    """
    Generates personalized recommendations based on:
    - Stress + Sleep combination patterns
    - Study hours + Exam pressure
    - Learning style preferences
    - Burnout risk detection
    - Optimal state recognition
    """
```

#### Dynamic Confidence Adjustment
```python
def _calculate_confidence_adjustment(self, profile):
    """
    Adjusts confidence based on:
    - Number of inputs provided (+2% per input)
    - Optimal learning state detected (+5%)
    - Warning conditions present (-3%)
    """
```

## 📊 Test Results

All 5 comprehensive tests pass with **99% confidence**:

1. ✅ **High Stress + Visual Learner + Memory Issues**
   - Input: stress=8, sleep=5h, study=3h, visual learner
   - Result: Detected poor focus, memory impairment, provided low-stress methods

2. ✅ **Sleep Deprivation + Focus Problems**
   - Input: sleep=4h, stress=6, study=6h, kinesthetic
   - Result: Sleep priority, kinesthetic-adapted focus techniques

3. ✅ **Burnout Risk Detection**
   - Input: study=10h, stress=9, sleep=6h
   - Result: Burnout warning, mandatory breaks, stress reduction

4. ✅ **Optimal Learning State**
   - Input: sleep=8h, stress=2, study=5h, auditory
   - Result: Optimization strategies, auditory methods, encouragement

5. ✅ **Exam Crisis Management**
   - Input: exam_tomorrow=True, study=2h, stress=9
   - Result: Intensive strategy, time pressure management, no new material

## 🎨 UI Enhancements

### New Multi-Input Interface

**Two-Column Layout:**
- **Left Column**: Category, question, learning style
- **Right Column**: Study hours, stress level, sleep hours, exam status

**Visual Indicators:**
- ⚠️ Warning for stress ≥8
- ⚠️ Warning for sleep <6
- 🚨 Error for burnout risk (high hours + high stress)

**Quick Preset Buttons:**
- 😰 High Stress → Fills stress=9, study=5
- 😴 Sleep Issues → Fills sleep=5, stress=7
- 📚 Exam Prep → Fills exam=True, stress=8
- 🎯 Focus Problems → Fills stress=6, study=3

### Enhanced Response Display

**Profile Summary Card:**
```
👤 Your Profile Summary
┌─────────────────────────────────────┐
│ 📚 Study Hours: 4h  😰 Stress: 🟡 6/10  😴 Sleep: ⚠️ 5h │
│ 🎨 Learning Style: Visual                              │
│ 📅 Upcoming Exam: Yes - using time-sensitive strategies│
└─────────────────────────────────────┘
```

**Confidence Display:**
```
💯 Confidence: 99%
```

**Expandable Sections:**
- 📚 Practical Examples
- 🔗 Additional Resources
- 🔍 Reasoning Process (Explainability)
- 🧠 Inferred Facts & Patterns
- ⚙️ Rules Applied (Technical Details)

## 🔬 Rule Examples

### Rule: High Stress + Low Sleep
```python
@Rule(
    AS.f1 << Fact(stress_level=MATCH.s & P(lambda x: x >= 7)),
    AS.f2 << Fact(sleep_hours=MATCH.h & P(lambda x: x < 6)),
    salience=20
)
def infer_high_stress_low_sleep(self, s, h):
    self.declare(Fact(condition="poor_focus"))
    self.declare(Fact(condition="memory_impaired"))
    self.inferred_facts.append("poor_focus (stress + sleep)")
    self.inferred_facts.append("memory_impaired (stress + sleep)")
    self.reasoning_trace.append(
        f"⚠️ Rule Fired: High stress ({s}/10) + Low sleep ({h}h) → Poor focus & memory"
    )
```

### Rule: Burnout Risk
```python
@Rule(
    AS.f1 << Fact(study_hours=MATCH.h & P(lambda x: x >= 8)),
    AS.f2 << Fact(stress_level=MATCH.s & P(lambda x: x >= 7)),
    salience=18
)
def infer_burnout_risk(self, h, s):
    self.declare(Fact(condition="burnout_risk"))
    self.inferred_facts.append("burnout_risk")
    self.reasoning_trace.append(
        f"⚠️ Rule Fired: High study hours ({h}h) + High stress ({s}/10) → Burnout risk!"
    )
```

## 🎯 Usage Examples

### Example 1: Memory + High Stress + Visual Learner

**Input:**
```python
response = expert.process_query_with_inputs(
    category="Memory",
    question="I struggle to remember what I studied",
    study_hours=3,
    stress_level=8,
    learning_style="Visual",
    has_upcoming_exam=True,
    sleep_hours=5
)
```

**Output:**
- **Concept**: 🧠 Memory Enhancement Techniques
- **Confidence**: 99%
- **Diagnosis**: High stress (8/10) + Sleep deprivation (5h) impacting memory
- **Inferred Facts**: poor_focus, memory_impaired, high_stress, sleep_deprived
- **Adaptive Recs**:
  1. **PRIORITY: Stress Management** - Breathing exercises
  2. **CRITICAL: Sleep Recovery** - Aim for 7-8 hours
  3. **Visual Learning Strategy** - Mind maps, memory palace
  4. Use low-stress memory methods (gentle spaced repetition)

### Example 2: Burnout Risk Scenario

**Input:**
```python
response = expert.process_query_with_inputs(
    category="Stress",
    question="I'm studying all the time but feeling exhausted",
    study_hours=10,
    stress_level=9,
    sleep_hours=6
)
```

**Output:**
- **Concept**: 🧘 Stress & Anxiety Management
- **Confidence**: 99%
- **Diagnosis**: High stress (9/10) + High study hours (10h/day) - burnout warning
- **Inferred Facts**: burnout_risk, high_stress, low_focus
- **Adaptive Recs**:
  1. **⚠️ BURNOUT WARNING** - Take mandatory 1-hour breaks every 3 hours
  2. 4-7-8 breathing technique
  3. Grounding exercises

## 📈 Performance Metrics

- **Rules**: 10+ new inference rules
- **Confidence Range**: 60-99%
- **Input Types**: 6 (text, numeric, scale, boolean, multiple-choice)
- **KB Categories**: 8 (added Focus category)
- **Adaptive Recommendations**: Dynamic based on 5+ factor combinations
- **Explainability**: 5 levels (profile, trace, facts, rules, examples)

## 🔄 Backward Compatibility

The system maintains **full backward compatibility** with the old interface:

```python
# Old method still works
response = expert.process_query("I feel anxious about my exam tomorrow")

# New method with multi-input
response = expert.process_query_with_inputs(
    category="Exam Preparation",
    question="I feel anxious about my exam tomorrow",
    stress_level=8,
    has_upcoming_exam=True
)
```

## 🚀 How to Use

### 1. Start the System
```bash
streamlit run main.py
```

### 2. Navigate to Study Guide Tab

### 3. Fill in the Multi-Input Form
- Select category (Memory, Focus, Stress, etc.)
- Write your question (minimum 10 characters)
- Adjust sliders for study hours, stress, sleep
- Select learning style
- Check upcoming exam if applicable

### 4. Click "Get Personalized Advice"

### 5. Explore the Results
- View your profile summary
- Read personalized recommendations
- Expand reasoning process for explainability
- Check inferred facts for insights

## 🎓 Key Benefits

1. **More Accurate**: Combines qualitative and quantitative data
2. **More Personalized**: Adapts to learning style, stress, sleep patterns
3. **More Explainable**: Shows reasoning process transparently
4. **More Proactive**: Detects burnout risk, optimal states
5. **More Scientific**: Rule-based inference with confidence scoring
6. **More User-Friendly**: Visual indicators, preset scenarios, structured output

## 🔮 Future Enhancements

Potential additions:
- Historical tracking (session to session)
- Machine learning for pattern recognition
- Integration with calendar/scheduling apps
- Peer comparison (anonymous aggregates)
- Adaptive learning (system improves with use)
- Mobile-optimized interface

## 📝 Conclusion

This upgrade transforms the Study Guide Expert System from a simple Q&A tool into a **sophisticated, data-driven decision support system** that combines the best of:

- **Expert Systems**: Rule-based reasoning with explainability
- **Data Science**: Quantitative analysis and confidence scoring
- **Psychology**: Evidence-based study strategies
- **UX Design**: Intuitive multi-input interface with visual feedback

The result is a production-grade system that provides **highly personalized, actionable, and explainable** study guidance.

---

**Version**: 2.0  
**Date**: November 10, 2025  
**Author**: Study Guide Expert System Team  
**Framework**: Experta + Streamlit + Python 3.10
