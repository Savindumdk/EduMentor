# 🎓 EduMentor - Intelligent O/L Tutoring System

> **A hybrid AI tutoring system combining rule-based expert systems with LLM intelligence for Sri Lankan O/L students**

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.29-red.svg)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green.svg)](https://openai.com/)
[![Experta](https://img.shields.io/badge/Experta-Rule--Based-orange.svg)](https://experta.readthedocs.io/)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Quick Start](#-quick-start)
- [Usage Guide](#-usage-guide)
- [Project Structure](#-project-structure)
- [Expert Systems](#-expert-systems)
- [Configuration](#-configuration)
- [Development](#-development)

---

## 🌟 Overview

**EduMentor** is a sophisticated AI tutoring system that combines the **reliability of rule-based expert systems** with the **natural language capabilities of large language models (LLMs)**. Built specifically for Sri Lankan O/L students, it provides:

- 📚 **Subject-specific tutoring** in Biology, Physics, and Chemistry
- 🧠 **Personalized study guidance** with adaptive recommendations
- 🔍 **Transparent reasoning** showing how conclusions were reached
- 💬 **Natural conversations** through LLM-enhanced responses
- 🎯 **Context-aware follow-ups** for progressive learning

### Why EduMentor?

| Traditional Tutoring | Generic AI Chatbots | **EduMentor** |
|---------------------|---------------------|---------------|
| ❌ Expensive | ❌ Unreliable facts | ✅ Expert system accuracy |
| ❌ Limited availability | ❌ No reasoning trace | ✅ Transparent inference |
| ❌ Generic responses | ❌ Context-less | ✅ Progressive guidance |
| ✅ Subject expertise | ✅ Natural language | ✅ **Best of both worlds** |

---

## ✨ Key Features

### 1. **Hybrid Intelligence Architecture**
- **Rule-based expert systems** ensure factual accuracy
- **GPT-4o-mini LLM** provides natural, engaging explanations
- Strict constraints prevent AI hallucination

### 2. **Dual-Mode Interface**

#### 📖 Subject Tutor
- Biology, Physics, Chemistry knowledge bases
- Intelligent topic matching with confidence scoring
- Context-aware follow-up questions
- Reasoning explanations for every answer

#### 🧠 Study Guide & Wellness
- 30 inference rules for personalized guidance
- Handles sleep, stress, and study patterns
- LLM-powered reasoning explanations
- Adaptive recommendations based on profile

### 3. **Advanced Features**
- ✅ **Semantic topic matching** - Understands intent, not just keywords
- ✅ **Multi-concept synthesis** - Combines related topics intelligently
- ✅ **Progressive questioning** - Specific follow-ups (e.g., "Shall I explain epithelial tissue next?")
- ✅ **Confirmation handling** - Simple "yes" continues the conversation
- ✅ **Confidence metrics** - Shows certainty levels for answers
- ✅ **Explainable AI** - See exactly which rules fired and why

### 4. **Knowledge Coverage**

| Domain | Topics | Rules |
|--------|--------|-------|
| **Biology** | Animal tissues, Digestion, Nutrition, Respiration, Photosynthesis, etc. | ~150+ |
| **Physics** | Motion, Forces, Energy, Electricity, Waves, etc. | ~120+ |
| **Chemistry** | Solutions, Mixtures, Acids/Bases, Reactions, etc. | ~100+ |
| **Study Guide** | Sleep patterns, Stress management, Study hours, Learning styles | 30 |

---

## 🏗️ System Architecture

### High-Level Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        STREAMLIT UI                              │
│  ┌──────────────────────┐    ┌──────────────────────────────┐  │
│  │   Subject Tutor      │    │  Study Guide & Wellness      │  │
│  │  (Biology/Physics/   │    │  (Personalized Guidance)     │  │
│  │   Chemistry)         │    │                              │  │
│  └──────────┬───────────┘    └──────────────┬───────────────┘  │
└─────────────┼──────────────────────────────┼───────────────────┘
              │                                │
              ▼                                ▼
┌─────────────────────────────┐  ┌──────────────────────────────┐
│      EXPERT AGENT           │  │   STUDY GUIDE EXPERT         │
│  (Coordinator + LLM)        │  │   (Experta Engine)           │
│                             │  │                              │
│  • Query Analysis (LLM)     │  │  • 30 Inference Rules        │
│  • Tool Selection           │  │  • Pattern Detection         │
│  • Response Enhancement     │  │  • Adaptive Recommendations  │
│  • Context Tracking         │  │  • Uncertainty Handling      │
└─────────────┬───────────────┘  └──────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    EXPERT SYSTEM TOOLS                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   Biology    │  │   Physics    │  │  Chemistry   │          │
│  │   Expert     │  │   Expert     │  │   Expert     │          │
│  │              │  │              │  │              │          │
│  │  Rules: 150+ │  │  Rules: 120+ │  │  Rules: 100+ │          │
│  │  JSON KB     │  │  JSON KB     │  │  JSON KB     │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    OPENAI GPT-4O-MINI                            │
│  • Natural language enhancement                                  │
│  • Response refinement (expert system data ONLY)                │
│  • Reasoning explanations                                       │
│  • Follow-up question generation                                │
└─────────────────────────────────────────────────────────────────┘
```

### Key Components

#### 1. **Expert Agent** (`agents/expert_agent.py`)
Orchestrates the entire tutoring workflow:
- **Query Analysis**: Uses LLM to understand student intent
- **Intelligent Routing**: Matches queries to appropriate expert systems
- **Semantic Search**: Finds best-matching topics from knowledge bases
- **Response Enhancement**: Refines expert system outputs with LLM
- **Context Management**: Tracks conversation and offered topics
- **Confirmation Handling**: Recognizes "yes/okay" and continues appropriately

#### 2. **Subject Expert Systems** (`experts/`)
Rule-based inference engines using **Experta**:
- `biology_expert.py` - Biology topics (animal tissues, digestion, etc.)
- `physics_expert.py` - Physics concepts (motion, forces, energy, etc.)
- `chemistry_expert.py` - Chemistry topics (solutions, acids/bases, etc.)
- `study_guide_expert.py` - Study patterns and wellness guidance

#### 3. **Knowledge Bases**
JSON-formatted structured knowledge:
- Concepts, explanations, examples
- Topic hierarchies and relationships
- ~16,200 words of O/L curriculum content

#### 4. **LLM Integration** (OpenAI GPT-4o-mini)
Powers natural language capabilities:
- **Query Understanding**: Extracts topics from student questions
- **Response Refinement**: Makes expert outputs conversational
- **Reasoning Generation**: Explains inference process step-by-step
- **Follow-up Creation**: Generates specific, actionable next questions

---

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.10+
pip (Python package manager)
OpenAI API key
```

### Installation

1. **Clone the repository**
```powershell
git clone https://github.com/Savindumdk/EduMentor.git
cd EduMentor
```

2. **Create virtual environment**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. **Install dependencies**
```powershell
pip install -r requirements.txt
```

4. **Configure environment**
Create a `.env` file:
```env
OPENAI_API_KEY=your_api_key_here
```

Get your API key from: https://platform.openai.com/api-keys

5. **Run the application**
```powershell
streamlit run main.py
```

The app will open at `http://localhost:8501`

---

## 📖 Usage Guide

### Subject Tutor Tab

**Ask any O/L subject question:**

```
Student: "What are animal tissues?"

EduMentor: 
Animal tissues are groups of similar cells that work together to perform 
specific functions in the body. There are four main types:

• Epithelial tissue - Lines surfaces and cavities, providing protection
• Connective tissue - Connects and supports other tissues
• Muscle tissue - Enables movement through contraction
• Nervous tissue - Transmits signals to coordinate body functions

🔍 Why this answer? The expert system matched your query to the "Animal 
Tissues" topic, which provides comprehensive coverage of tissue types.

💭 Shall I explain epithelial tissue in more detail?

Student: "yes"

EduMentor: [Detailed explanation of epithelial tissue...]
```

**Features:**
- 🎯 Specific, targeted answers (not generic overviews)
- 📊 Confidence metrics showing certainty
- 🔍 Reasoning explanation for transparency
- 💭 One actionable follow-up question
- ✅ Simple confirmations ("yes", "okay") work seamlessly

### Study Guide Tab

**Get personalized study recommendations:**

1. Select your area of concern (Memory, Focus, Stress, etc.)
2. Provide optional inputs:
   - Study hours per day (0-12)
   - Stress level (1-10)
   - Sleep hours (1-12)
   - Upcoming exam (Yes/No)
   - Learning style

3. Click "Get Personalized Advice"

**Features:**
- 🧠 30 inference rules analyze your profile
- 🔍 LLM-powered reasoning explanations
- ⚠️ Pattern detection (burnout, sleep deprivation, etc.)
- 💡 Adaptive recommendations based on your data
- 📊 Confidence scoring and uncertainty handling

---

## 📁 Project Structure

```
EduMentor/
├── agents/
│   ├── expert_agent.py          # Main coordinator agent
│   └── __init__.py
│
├── experts/
│   ├── biology_expert.py        # Biology inference engine
│   ├── physics_expert.py        # Physics inference engine
│   ├── chemistry_expert.py      # Chemistry inference engine
│   ├── study_guide_expert.py    # Study guidance engine
│   ├── study_guide_kb.json      # Study guide knowledge base
│   └── create_expert.py         # Expert creation utilities
│
├── core/
│   ├── biology/
│   │   └── biology_kb.json      # Biology knowledge (~5,400 words)
│   ├── physics/
│   │   └── physics_kb.json      # Physics knowledge (~5,200 words)
│   └── chemistry/
│       └── chemistry_kb.json    # Chemistry knowledge (~5,600 words)
│
├── utils/
│   └── (utility modules)
│
├── main.py                      # Streamlit application
├── config.py                    # Configuration settings
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables (create this)
├── .gitignore
└── README.md                    # This file
```

---

## 🔬 Expert Systems

### Biology Expert
**Topics Covered:**
- Animal tissues (epithelial, connective, muscle, nervous)
- Plant tissues and cell structure
- Digestion and digestive processes
- Nutrition and nutrients
- Respiration (aerobic and anaerobic)
- Photosynthesis and gas exchange
- Transportation and circulatory systems
- Excretion and waste removal

**Features:**
- 150+ rules
- Semantic topic matching
- Confidence scoring
- Example generation

### Physics Expert
**Topics Covered:**
- Motion and forces
- Newton's laws
- Friction and pressure
- Energy forms and conservation
- Work, power, and efficiency
- Electricity and circuits
- Heat and temperature
- Waves and sound

**Features:**
- 120+ rules
- Formula explanations
- Practical applications
- Real-world examples

### Chemistry Expert
**Topics Covered:**
- Mixtures and solutions
- Separation techniques
- Acids, bases, and pH
- Indicators and neutralization
- Chemical reactions
- Combustion and oxidation
- Elements and compounds
- Chemical properties

**Features:**
- 100+ rules
- Chemical equations
- Safety information
- Practical demonstrations

### Study Guide Expert
**Inference Rules (30 total):**

| Pattern | Rules | Salience | Detection |
|---------|-------|----------|-----------|
| Sleep Patterns | 4 | 28-30 | Severe deprivation → Optimal |
| Stress Patterns | 4 | 25-29 | Minimal → Extreme |
| Study Hours | 5 | 20-28 | Minimal → Extreme |
| Learning Styles | 4 | 15-20 | Visual, Auditory, etc. |
| Burnout Risk | 3 | 30 | Critical combinations |
| Exam Proximity | 2 | 25 | Last-minute strategies |
| Motivation | 4 | 15-18 | Low → High motivation |
| Other Patterns | 4 | 10-20 | Various diagnostics |

**Advanced Features:**
- Priority-based rule firing
- Uncertainty handling (missing data)
- Confidence scoring
- Crisis detection
- Adaptive recommendations

---

## ⚙️ Configuration

### Environment Variables (`.env`)
```env
# Required
OPENAI_API_KEY=sk-...

# Optional (defaults shown)
OPENAI_MODEL=gpt-4o-mini
OPENAI_TEMPERATURE=0.4
OPENAI_MAX_TOKENS=550
```

### Config File (`config.py`)
```python
# LLM Settings
MODEL = "gpt-4o-mini"
TEMPERATURE = 0.4  # Lower = more focused
MAX_TOKENS = 550   # Response length

# Expert System Settings
CONFIDENCE_THRESHOLD = 0.5
ENABLE_REASONING = True
ENABLE_FOLLOW_UPS = True

# UI Settings
PAGE_TITLE = "EduMentor - AI Tutor"
PAGE_ICON = "🎓"
LAYOUT = "wide"
```

---

## 🛠️ Development

### Adding New Topics

**1. Add to Knowledge Base** (e.g., `core/biology/biology_kb.json`)
```json
{
  "new_concept": {
    "concept": "New Concept Name",
    "explanation": "Detailed explanation...",
    "examples": ["Example 1", "Example 2"],
    "category": "CategoryName",
    "keywords": ["keyword1", "keyword2"]
  }
}
```

**2. Add Rule** (e.g., `experts/biology_expert.py`)
```python
@Rule(AS.f << Fact(query_topic="new_concept"))
def rule_new_concept(self, f):
    """Rule for new concept."""
    self.response = self.kb['new_concept']
```

**3. Test**
```powershell
streamlit run main.py
# Ask: "Explain new concept"
```

### Adding New Inference Rules (Study Guide)

**Edit** `experts/study_guide_expert.py`:
```python
@Rule(
    AS.f << Fact(study_hours=MATCH.h & P(lambda x: x > 10)),
    salience=25
)
def infer_excessive_study(self, h):
    """Detect excessive study hours."""
    self.declare(Fact(condition="excessive_study"))
    self.reasoning_trace.append(
        f"⚠️ Excessive study hours detected: {h}h/day"
    )
```

### Testing

**Run specific expert:**
```python
from experts.biology_expert import BiologyExpert

expert = BiologyExpert()
expert.reset()
expert.declare(Fact(query_topic="animal_tissues"))
expert.run()
response = expert.get_response()
print(response)
```

**Test agent flow:**
```python
from agents.expert_agent import ExpertAgent

agent = ExpertAgent()
result = agent.process_query("What are animal tissues?")
print(result['response'])
```

---

## 🎯 Roadmap

### ✅ Completed
- Hybrid expert system + LLM architecture
- 3 subject expert systems (Biology, Physics, Chemistry)
- Study guide with 30 inference rules
- Context-aware conversation flow
- Reasoning explanations
- Confidence metrics
- Progressive follow-up questions
- Confirmation handling

### 🚧 In Progress
- Extended knowledge bases (more topics)
- Mathematics expert system
- English language expert

### 🔮 Future
- Student progress tracking
- Personalized learning paths
- Practice question generation
- Quiz mode with scoring
- Voice input/output
- Mobile app version
- Offline mode

---

## 📊 Performance

| Metric | Value |
|--------|-------|
| **Knowledge Base Size** | ~16,200 words |
| **Total Rules** | 400+ (370+ subject + 30 study guide) |
| **Topics Covered** | 150+ concepts |
| **Average Response Time** | < 3 seconds |
| **LLM Token Usage** | 300-650 tokens/response |
| **Confidence Accuracy** | ~85% |

---

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- 📚 Expand knowledge bases with more O/L topics
- 🔧 Add new subject expert systems
- 🎨 Enhance UI/UX
- 🧪 Write unit tests
- 📖 Improve documentation

---

## 📝 License

This project is developed for educational purposes as part of the Expert Systems course at the University of Moratuwa, Faculty of Engineering.

---

## 🙏 Acknowledgments

- **OpenAI** - GPT-4o-mini for natural language capabilities
- **Experta** - Python rule-based expert system framework
- **Streamlit** - Rapid web app development framework
- **University of Moratuwa** - Expert Systems course (L3S1)

---

## 📧 Contact

**Developer:** Savindu Madugalla  
**University:** University of Moratuwa  
**Course:** L3S1 Expert Systems  
**Repository:** https://github.com/Savindumdk/EduMentor

---

<div align="center">

**EduMentor** - Where Expert Systems Meet Modern AI 🎓

*Built with ❤️ for Sri Lankan O/L Students*

</div>
