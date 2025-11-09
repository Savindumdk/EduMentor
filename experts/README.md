# Advanced Study Guide Expert System

A production-grade expert system built with **Experta** featuring data-driven knowledge management, multi-step inference, confidence scoring, and NLP integration.

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    User Interface                        │
│                     (main.py)                           │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│              Study Guide Expert System                   │
│           (study_guide_expert.py)                       │
│                                                          │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────┐   │
│  │   Working   │  │  Inference   │  │ Explanation│   │
│  │   Memory    │  │   Engine     │  │  Facility  │   │
│  └─────────────┘  └──────────────┘  └────────────┘   │
└──────┬───────────────────┬──────────────────┬──────────┘
       │                   │                  │
       ▼                   ▼                  ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│     NLP      │   │  Knowledge   │   │    User      │
│  Processor   │   │     Base     │   │   Profile    │
│   (.py)      │   │   (.json)    │   │  (Runtime)   │
└──────────────┘   └──────────────┘   └──────────────┘
```

## ✨ Key Features

### 1. **External Knowledge Base** (study_guide_kb.json)
- **Data-driven architecture**: All domain knowledge stored in JSON
- **Extensible**: Add new topics, rules, and inferences without code changes
- **Structure per topic**:
  - Keywords for intent detection
  - Multiple rules with conditions
  - Confidence scores
  - Recommendations with priorities
  - Examples and resources
  - Inference triggers for chaining

### 2. **NLP Processing** (nlp_processor.py)
- **Entity Extraction**: Sleep hours, time periods, stress levels
- **Intent Detection**: Matches queries to topics with confidence
- **Condition Mapping**: Maps natural language to Experta Facts
- **Negation Detection**: Handles "not", "don't", "can't"

### 3. **Multi-Step Inference Chaining**
Automatic fact inference through forward chaining:
```
Fact(exam_anxiety=True) → Fact(stress_level=high)
Fact(stress_level=high) → Fact(focus_level=low)
Fact(sleep_hours=5) → Fact(memory_consolidation=weak)
```

### 4. **Confidence-Weighted Reasoning**
- Each rule has confidence score (0.0-1.0)
- Multiple rules combined using weighted selection
- Final confidence reflects system certainty
- Low confidence (<0.85) displayed to user

### 5. **Explanation Facility**
Complete reasoning transparency:
- Which rules fired
- What facts were inferred
- Why decisions were made
- Full reasoning trace available

### 6. **Working Memory & User Profiling**
Persistent user state across queries:
```python
expert.update_user_profile(
    sleep_hours=6,
    stress_level='high',
    study_hours=4
)
```

### 7. **Dynamic Learning**
Add new rules at runtime:
```python
expert.add_rule_to_kb('memory', {
    'id': 'memory_005',
    'condition': 'visual_learner',
    'recommend': 'Use diagrams and mind maps',
    'confidence': 0.87,
    'priority': 5
})
```

## 📁 File Structure

```
experts/
├── study_guide_kb.json       # Knowledge Base (editable)
├── study_guide_expert.py     # Expert System Engine
├── nlp_processor.py           # Natural Language Processing
└── test_expert_system.py     # Comprehensive Test Suite
```

## 🚀 Usage

### Basic Query

```python
from study_guide_expert import StudyGuideExpert

expert = StudyGuideExpert()
response = expert.process_query("I feel anxious about my exam tomorrow")

print(f"Concept: {response['concept']}")
print(f"Confidence: {response['confidence']:.2%}")
print(f"Recommendations: {response['recommendation']}")
```

### With User Profile

```python
expert = StudyGuideExpert()

# Set user context
expert.update_user_profile(
    sleep_hours=5,
    stress_level='high',
    exam_in_days=2
)

# Query with context
response = expert.process_query("How can I improve my memory?")

# System automatically infers: low sleep → weak memory consolidation
```

### Get Explanation

```python
response = expert.process_query("I'm stressed and can't focus")

# View reasoning process
print(expert.get_explanation())

# Output:
# 🔍 Reasoning Trace:
#   1. 📥 Query: 'I'm stressed and can't focus'
#   2. 🔍 Intents: [('stress', 0.88)]
#   3. ✅ Conditions: ['high_stress']
#   4. 💡 Fact: condition=high_stress
#   5. 🧠 Infer: high_stress → low_focus (0.85)
#   6. ✅ Rule stress_001: high_stress (0.90)
#   7. 📈 Confidence: 90%
```

### Dynamic Learning

```python
# Add new rule to knowledge base
expert.add_rule_to_kb('motivation', {
    'id': 'motivation_005',
    'condition': 'group_study',
    'recommend': 'Join study groups for accountability',
    'confidence': 0.80,
    'priority': 5
})

# Rule is saved to JSON and immediately available
```

## 🧪 Testing

Run comprehensive test suite:

```bash
cd experts
python test_expert_system.py
```

Tests cover:
1. Basic query processing
2. Multi-step inference chaining
3. User profiling
4. Confidence scoring
5. Explanation facility
6. NLP processing
7. Dynamic learning
8. Complete workflow

## 📊 Response Structure

```python
{
    'concept': '🧘 Managing Exam Stress & Anxiety',
    'diagnosis': 'You are experiencing exam-related stress...',
    'explanation': 'Your body enters fight-or-flight mode...',
    'recommendation': '1. Practice 4-7-8 breathing\n2. Use grounding...',
    'examples': ['Before exam: 3 rounds of 4-7-8 breathing', ...],
    'resources': ['Headspace app', 'Book: Why Zebras...'],
    'confidence': 0.90,
    'reasoning_trace': ['📥 Query: ...', '🔍 Intents: ...', ...],
    'fired_rules': ['stress_001', 'stress_002'],
    'inferred_facts': ['low_focus'],
    'topic': 'stress'
}
```

## 🎯 Topics Covered

1. **Memory Enhancement** - Spaced repetition, active recall, encoding
2. **Stress Management** - Breathing, grounding, mindfulness
3. **Procrastination** - 2-minute rule, Pomodoro, task breakdown
4. **Time Management** - Time blocking, Eisenhower matrix, energy management
5. **Exam Preparation** - Past papers, timeline-based prep, exam day strategies
6. **Motivation** - Goal reconnection, micro-goals, progress tracking
7. **Confidence** - Growth mindset, wins journal, comparison detox
8. **Sleep Optimization** - Sleep hygiene, circadian rhythm, pre-sleep routine

## 🔧 Configuration

### Knowledge Base Location
```python
# Default: experts/study_guide_kb.json
expert = StudyGuideExpert()

# Custom path
expert = StudyGuideExpert(kb_path='/path/to/custom_kb.json')
```

### Adding New Topics

Edit `study_guide_kb.json`:

```json
{
  "new_topic": {
    "keywords": ["keyword1", "keyword2"],
    "concept": "Topic Name",
    "confidence": 0.85,
    "rules": [
      {
        "id": "topic_001",
        "condition": "some_condition",
        "recommend": "Recommendation text",
        "confidence": 0.90,
        "priority": 1,
        "triggers": ["inferred_fact"]
      }
    ],
    "explanation": "Detailed explanation...",
    "examples": ["Example 1", "Example 2"],
    "resources": ["Resource 1", "Resource 2"]
  }
}
```

## 🔄 Inference Rules

Defined in `kb['inferences']`:

```json
{
  "inferences": {
    "rule_name": {
      "from_fact": "condition_a",
      "infer_fact": "condition_b",
      "confidence": 0.85,
      "explanation": "Why this inference is valid"
    }
  }
}
```

## 📈 Confidence Interpretation

- **0.90-1.00**: High confidence, well-established relationship
- **0.80-0.89**: Good confidence, evidence-based
- **0.70-0.79**: Moderate confidence, contextual
- **0.60-0.69**: Low confidence, general advice
- **<0.60**: Very uncertain, default fallback

## 🎓 Integration with main.py

```python
# In main.py
from experts.study_guide_expert import StudyGuideExpert

# Initialize once
study_expert = StudyGuideExpert()

# In Streamlit UI
if st.button("Get Advice"):
    response = study_expert.process_query(question)
    
    if response:
        st.success(response['concept'])
        st.info(f"Confidence: {response['confidence']:.0%}")
        st.markdown(f"**Diagnosis:** {response['diagnosis']}")
        st.markdown(f"**Recommendations:**\n{response['recommendation']}")
        
        with st.expander("🔍 See Reasoning"):
            st.code(study_expert.get_explanation())
```

## 🚀 Advanced Features

### Salience for Rule Priority
Higher salience = fires first
```python
@Rule(Fact(condition='high_stress'), salience=10)  # Fires before salience=5
```

### Pattern Matching
```python
@Rule(Fact(sleep_hours=MATCH.hours & P(lambda x: x < 7)))
```

### Fact Binding
```python
@Rule(AS.fact << Fact(condition='stress'))
def handle_stress(self, fact):
    # Access the specific fact
```

## 📚 References

- **Experta Documentation**: https://experta.readthedocs.io/
- **Expert Systems**: Russell & Norvig, "Artificial Intelligence: A Modern Approach"
- **Knowledge Representation**: "Knowledge Representation and Reasoning" by Brachman & Levesque

## 🤝 Contributing

To add new knowledge:
1. Edit `study_guide_kb.json`
2. Add keywords, rules, and examples
3. Test with `test_expert_system.py`
4. Deploy (no code changes needed!)

## 📄 License

Part of the EduMentor project.

---

**Built with ❤️ using Experta Expert System Framework**
