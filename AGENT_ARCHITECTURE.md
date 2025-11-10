# EduMentor - Agent-Powered Expert System Tutor

An intelligent O/L tutoring system that uses a **single Expert Agent** coordinating multiple **Expert System Tools** for accurate, rule-based educational responses.

## 🏗️ Architecture

### Agent-Tool Pattern

```
┌─────────────────────────────────────────────────────────┐
│                    Expert Agent                         │
│              (Gemini LLM Coordinator)                   │
│                                                          │
│  • Analyzes student queries                             │
│  • Selects appropriate expert tool                      │
│  • Extracts query parameters                            │
│  • Enhances responses naturally                         │
└────────────────────┬────────────────────────────────────┘
                     │
        ┌────────────┴────────────┐
        │                         │
        ▼                         ▼
┌───────────────┐         ┌───────────────┐
│  Information  │         │  Diagnostic   │
│    Experts    │         │    Expert     │
│  (Tools)      │         │   (Tool)      │
├───────────────┤         ├───────────────┤
│ • Biology     │         │ • Study Guide │
│ • Physics     │         │               │
│ • Chemistry   │         │ Progressive   │
│               │         │ Questioning   │
│ @Rule-based   │         │ @Rule-based   │
└───────────────┘         └───────────────┘
```

## 🎯 How It Works

### 1. Expert Agent (Coordinator)
The main agent that orchestrates everything:

**Responsibilities:**
- **Query Analysis**: Uses Gemini LLM to understand student questions
- **Tool Selection**: Chooses the right expert system based on query
- **Parameter Extraction**: Determines exact topic to query (e.g., "photosynthesis", "wave_motion")
- **Response Enhancement**: Uses LLM to make expert responses natural and student-friendly
- **Multiple Rule Synthesis**: When multiple rules match, synthesizes them into comprehensive answers

**Key Methods:**
```python
agent = ExpertAgent()
result = agent.process_query("What is photosynthesis?")
# Returns: Enhanced response with expert system backing
```

**Multiple Rule Handling:**
When a query matches multiple expert rules (e.g., "Tell me about respiration" matches aerobic, anaerobic, and cellular respiration), the agent:
1. Collects ALL matching rules from the expert system
2. Extracts key concepts from each matched rule
3. Uses LLM to synthesize them into ONE comprehensive, integrated answer
4. Shows relationships between concepts
5. Provides complete understanding without information loss

### 2. Expert System Tools
Traditional rule-based expert systems that provide accurate knowledge:

#### Information Experts (Biology, Physics, Chemistry)
- **Pattern**: Declare `Fact(query_topic='...')` → Execute rules → Return response
- **Knowledge Base**: ~3,330 rules total from O/L textbooks
- **Response Format**: Concept, explanation, examples, topic classification

Example:
```python
biology_expert = BiologyExpert()
biology_expert.declare(Fact(query_topic='photosynthesis'))
biology_expert.run()
response = biology_expert.get_response()
```

#### Diagnostic Expert (Study Guide)
- **Pattern**: Progressive questioning to diagnose study problems
- **Method**: Multi-step conversation with state management
- **Response Format**: Diagnosis, recommendations, action plans

Example:
```python
study_guide = StudyGuideExpert()
study_guide.run()  # Asks first question
study_guide.declare_user_response("mcq")  # User responds
study_guide.run()  # Continues diagnostic
```

## 🚀 Usage

### Running the Application

```bash
# Activate virtual environment
.venv\Scripts\Activate.ps1

# Run Streamlit app
streamlit run main.py
```

### Testing the Agent

```bash
# Run test script
python test_agent.py
```

### Programmatic Usage

```python
from agents.expert_agent import ExpertAgent

# Initialize agent
agent = ExpertAgent()

# Query 1: Information request
result = agent.process_query("What is photosynthesis?")
print(result['response'])
print(f"Tool used: {result['tool_used']}")

# Query 2: Diagnostic session
result = agent.process_query("I'm struggling with MCQs")
if result['needs_clarification']:
    print(result['response'])  # Clarification question
    
    # Continue conversation
    result = agent.handle_clarification("I can't finish on time")
    print(result['response'])

# Reset for new session
agent.reset()
```

## 📊 Response Format

### Information Query Response
```python
{
    'response': 'Enhanced natural language explanation...',
    'tool_used': 'biology_expert',
    'query_topic': 'photosynthesis',
    'success': True,
    'needs_clarification': False,
    'raw_expert_response': {
        'concept': 'Photosynthesis',
        'explanation': '...',
        'examples': [...],
        'topic': 'Biology'
    },
    'analysis': {
        'tool_name': 'biology_expert',
        'query_topic': 'photosynthesis',
        'reasoning': 'Direct biology question...'
    }
}
```

### Diagnostic Query Response (Clarification)
```python
{
    'response': 'What specific area are you struggling with?...',
    'tool_used': 'study_guide_expert',
    'needs_clarification': True,
    'success': True
}
```

## 🔧 Key Features

### 1. **Proper Agent Architecture**
- Single agent coordinates multiple tools
- Clear separation: Agent = Intelligence, Tools = Knowledge
- Follows industry best practices for agent design

### 2. **LLM + Rule-Based Hybrid**
- **LLM (Gemini)**: Query understanding, tool selection, response enhancement
- **Rules (Experta)**: Accurate subject knowledge, logical inference
- Best of both worlds: Intelligence + Accuracy

### 3. **Tool Modularity**
- Expert systems are reusable tools
- Easy to add new subject experts
- Can be used independently or via agent

### 4. **Explainability**
- Shows which tool was used
- Displays agent's reasoning
- Reveals raw expert system response
- Transparent decision-making

### 5. **Progressive Questioning**
- Study Guide expert uses multi-step diagnostic
- Maintains state across questions
- Personalized recommendations

## 📁 Project Structure

```
EduMentor/
├── agents/
│   ├── __init__.py
│   └── expert_agent.py          # Main Expert Agent
├── experts/
│   ├── biology_expert.py        # Biology tool (~1,330 rules)
│   ├── physics_expert.py        # Physics tool (~1,060 rules)
│   ├── chemistry_expert.py      # Chemistry tool (~940 rules)
│   └── study_guide_expert.py    # Diagnostic tool
├── core/
│   └── orchestrator.py          # [Deprecated - use agent instead]
├── main.py                      # Streamlit interface
├── test_agent.py               # Test script
└── config.py                    # Configuration
```

## 🎓 Educational Use Cases

### Direct Questions
- "What is photosynthesis?"
- "Explain Newton's laws"
- "How do acids react with metals?"

### Study Guidance
- "I'm struggling with my studies"
- "How do I prepare for exams?"
- "I need help with MCQs"

### Concept Exploration
- "Tell me about respiration"
- "What are electromagnetic waves?"
- "Explain chemical bonding"

## 🔬 Technical Details

### Dependencies
- **Experta**: Rule-based inference engine
- **Streamlit**: Web interface
- **Google Generative AI**: LLM capabilities
- **Python 3.10+**

### Knowledge Base
- **Biology**: 1,330 rules from O/L textbook
- **Physics**: 1,060 rules from O/L textbook
- **Chemistry**: 940 rules from O/L textbook
- **Total**: 3,330+ expert rules

### Performance
- **Agent Initialization**: ~2 seconds
- **Query Analysis**: ~1-2 seconds (LLM call)
- **Expert Execution**: <100ms (rule matching)
- **Response Enhancement**: ~1-2 seconds (LLM call)
- **Total Query Time**: ~3-5 seconds

## 🛠️ Development

### Adding a New Expert Tool

1. Create expert system in `experts/`:
```python
from experta import KnowledgeEngine, Rule, Fact

class MathExpert(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.response = None
        self.needs_clarification = False
        self.clarification_question = None
    
    @Rule(Fact(query_topic='algebra'))
    def explain_algebra(self):
        self.response = {
            'concept': 'Algebra',
            'explanation': '...',
            'examples': [...],
            'topic': 'Mathematics'
        }
    
    def get_response(self):
        return self.response
```

2. Register tool in `ExpertAgent`:
```python
self.tools = {
    'biology_expert': BiologyExpert(),
    'physics_expert': PhysicsExpert(),
    'chemistry_expert': ChemistryExpert(),
    'study_guide_expert': StudyGuideExpert(),
    'math_expert': MathExpert()  # New tool
}
```

3. Update tool descriptions in `_get_tool_descriptions()`:
```python
5. **math_expert**: Use for Mathematics questions (O/L syllabus)
   - Topics: Algebra, geometry, trigonometry
   - Returns: Concept explanation, examples
   - Usage: Declare Fact(query_topic='topic_name')
```

### Testing

```bash
# Test single query
python -c "from agents.expert_agent import ExpertAgent; 
agent = ExpertAgent(); 
result = agent.process_query('What is photosynthesis?');
print(result['response'])"

# Run full test suite
python test_agent.py
```

## 📝 Advantages Over Previous Architecture

### Before (Orchestrator Pattern)
- Monolithic orchestrator handling everything
- Intent classification + expert selection + response formatting all in one class
- Harder to test individual components
- Less modular

### After (Agent-Tool Pattern)
- ✅ Clear separation: Agent coordinates, Tools execute
- ✅ Expert systems are reusable tools
- ✅ Follows industry-standard agent design
- ✅ Easier to test and maintain
- ✅ More extensible (add tools easily)
- ✅ Better explainability (see tool usage)

## 🎯 Best Practices

### When to Use Each Tool

**Biology/Physics/Chemistry Experts:**
- Factual questions about O/L syllabus
- Specific topic explanations
- Concept clarifications

**Study Guide Expert:**
- Meta-learning questions
- Study strategy advice
- Exam preparation guidance
- Diagnostic assessments

### Query Optimization

**Good Queries:**
- "What is photosynthesis?" ✅
- "Explain reflection of light" ✅
- "I struggle with MCQs" ✅

**Needs Refinement:**
- "Tell me everything about biology" ❌ (too broad)
- "Quick help" ❌ (unclear intent)
- Use specific topic names for best results

## 📚 References

- **Experta Documentation**: https://experta.readthedocs.io/
- **Streamlit Documentation**: https://docs.streamlit.io/
- **Gemini API**: https://ai.google.dev/

## 🤝 Contributing

When adding new features:
1. Keep agent logic separate from tool logic
2. Tools should be self-contained expert systems
3. Agent should only coordinate, not contain domain knowledge
4. Test both independently and integrated

## 📄 License

Educational project for O/L tutoring system development.

---

**Built with ❤️ for O/L students**
