# EduMentor Phase 2+3: Multi-Agent System + LLM Integration

## 🎓 Overview

**EduMentor v2.0** is an advanced AI-powered tutoring system for O/L students in Sri Lanka. It combines:

- **Multi-Agent System (MAS)** with 6 specialized subject agents
- **Google Gemini AI** for natural language enhancement
- **Multilingual Support** (English, Sinhala, Tamil)
- **Expert System** with 30+ knowledge rules

## 🌟 Features

### Phase 2: Multi-Agent System
- ✅ **CoordinatorAgent**: Routes questions to appropriate subject agents
- ✅ **6 Specialized Agents**:
  - 🧬 **BiologyAgent**: Photosynthesis, respiration, cell biology
  - ⚛️ **PhysicsAgent**: Motion, gravity, electricity, energy
  - 🧪 **ChemistryAgent**: Acids, bases, combustion, elements
  - 📐 **MathematicsAgent**: Algebra, geometry, statistics
  - 📜 **HistoryAgent**: Sri Lankan history and culture
  - 📖 **StudyGuideAgent**: Study tips and learning strategies

### Phase 3: LLM Integration
- ✅ **Gemini AI Enhancement**: Converts expert system responses to natural language
- ✅ **Multilingual Translation**: Automatic translation to Sinhala and Tamil
- ✅ **Language Auto-Detection**: Detects question language automatically
- ✅ **Hybrid System**: Expert system facts + AI natural language

## 📁 Project Structure

```
EduMentor/
├── agents/                      # MAS agents
│   ├── base_agent.py           # Base agent class
│   ├── coordinator_agent.py    # MAS coordinator
│   ├── physics_agent.py        # Physics specialist
│   ├── biology_agent.py        # Biology specialist
│   ├── chemistry_agent.py      # Chemistry specialist
│   ├── mathematics_agent.py    # Mathematics specialist
│   ├── history_agent.py        # History specialist
│   └── study_guide_agent.py    # Study tips specialist
│
├── subjects/                    # Knowledge bases
│   ├── physics_kb.py           # Physics rules
│   ├── biology_kb.py           # Biology rules
│   ├── chemistry_kb.py         # Chemistry rules
│   ├── mathematics_kb.py       # Mathematics rules
│   ├── history_kb.py           # History rules
│   └── study_guide_kb.py       # Study guide rules
│
├── llm/                         # LLM integration
│   └── gemini_interface.py     # Gemini AI interface
│
├── utils/                       # Utilities
│   ├── language_detector.py    # Language detection
│   └── response_formatter.py   # Response formatting
│
├── main_v2.py                   # Phase 2+3 Streamlit UI
├── config.py                    # Configuration
├── requirements.txt             # Dependencies
├── setup.py                     # Setup script
├── test_phase2_3.py            # Test suite
└── .env.example                 # Environment template
```

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Google Gemini API key (free at [Google AI Studio](https://makersuite.google.com/app/apikey))

### 2. Installation

```powershell
# Clone or navigate to the project directory
cd "c:\UOM\L3S1\Expert Systems\EduMentor"

# Run setup script
python setup.py
```

The setup script will:
- ✅ Check Python version
- ✅ Install all dependencies
- ✅ Create .env configuration file
- ✅ Verify installation

### 3. Configuration

1. **Get Gemini API Key**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a free API key
   - Copy the key

2. **Configure Environment**:
   - Open `.env` file
   - Replace `your_gemini_api_key_here` with your actual API key:
   ```
   GEMINI_API_KEY=your_actual_key_here
   ```
   - Save the file

### 4. Run the Application

```powershell
streamlit run main_v2.py
```

Your browser will open automatically at `http://localhost:8501`

## 📖 Usage Guide

### Asking Questions

1. **Type your question** in any supported language (English, Sinhala, Tamil)
2. **Select response language** from the sidebar
3. **Toggle AI enhancement** on/off as needed
4. **Click "Ask"** to get your answer

### Example Questions

**Physics:**
- "What is Newton's law of motion?"
- "Explain friction"
- "How does electricity work?"

**Biology:**
- "What is photosynthesis?"
- "Explain cellular respiration"
- "What is the structure of a cell?"

**Chemistry:**
- "What are acids and bases?"
- "Explain combustion"
- "What is a chemical reaction?"

**Mathematics:**
- "How do I solve quadratic equations?"
- "Explain percentages"
- "What is probability?"

**History:**
- "Tell me about Sri Lankan independence"
- "What was the colonial period?"
- "Explain ancient civilizations"

**Study Tips:**
- "How can I improve my memory?"
- "What are good time management strategies?"
- "How should I prepare for exams?"

### Features in the UI

**Sidebar:**
- 🌍 **Language Selection**: Choose English, Sinhala, or Tamil
- 🌟 **AI Enhancement Toggle**: Turn LLM features on/off
- 📚 **Available Subjects**: See all 6 subject agents
- ℹ️ **System Info**: View MAS and LLM status
- 📊 **Agent Statistics**: See which agents are most used
- 🗑️ **Clear History**: Reset conversation history

**Main Interface:**
- 💬 **Question Input**: Type your questions here
- 📝 **Enhanced Answers**: Get natural language explanations
- 📚 **Examples**: See practical examples for each concept
- 📜 **History**: Review previous Q&A pairs
- 💡 **Quick Examples**: Click to try sample questions

## 🧪 Testing

Run the comprehensive test suite:

```powershell
python test_phase2_3.py
```

Tests include:
1. ✅ Coordinator routing to correct agents
2. ✅ Agent knowledge base responses
3. ✅ Language detection
4. ✅ Response formatting
5. ✅ LLM interface initialization
6. ✅ Hybrid system integration
7. ✅ Agent statistics tracking

## ⚙️ Configuration

Edit `config.py` to customize:

```python
# Enable/disable features
MAS_ENABLED = True              # Multi-Agent System
LLM_ENABLED = True              # Gemini AI enhancement
MULTILINGUAL_ENABLED = True     # Language support
AUTO_DETECT_LANGUAGE = True     # Auto-detect question language

# LLM settings
LLM_MODEL = "gemini-pro"        # Gemini model
LLM_TEMPERATURE = 0.7           # Response creativity (0-1)
LLM_MAX_TOKENS = 500            # Max response length
FALLBACK_TO_EXPERT_SYSTEM = True  # Use expert system if LLM fails

# Supported languages
SUPPORTED_LANGUAGES = ["en", "si", "ta"]
DEFAULT_LANGUAGE = "en"
```

## 🏗️ Architecture

### System Flow

```
Student Question
       ↓
Language Detection (auto)
       ↓
CoordinatorAgent (MAS Routing)
       ↓
Specialized Agent (Physics/Biology/etc.)
       ↓
Expert System (Experta Rules)
       ↓
Gemini AI (Natural Language Enhancement)
       ↓
Translation (if needed)
       ↓
Enhanced Response
```

### Components

**1. Multi-Agent System (MAS)**
- **CoordinatorAgent**: Routes questions based on keyword matching
- **BaseAgent**: Common functionality for all agents
- **Specialized Agents**: Subject-specific agents with domain knowledge

**2. Expert System (Experta)**
- 30+ knowledge rules across 6 subjects
- Rule-based inference engine
- Fact-based reasoning

**3. LLM Integration (Gemini)**
- Natural language enhancement
- Multilingual translation
- Conversational explanations
- Practice question generation

**4. Utilities**
- **LanguageDetector**: Auto-detects Sinhala, Tamil, English
- **ResponseFormatter**: Consistent output formatting

## 📊 Knowledge Base

### Current Rules (30 total)

**Physics (5 rules):**
- Friction
- Gravity
- Electricity
- Motion
- Energy

**Biology (5 rules):**
- Photosynthesis
- Cellular Respiration
- Digestion
- Cell Structure
- Reproduction

**Chemistry (5 rules):**
- Acids
- Bases
- Combustion
- Elements
- Chemical Reactions

**Mathematics (5 rules):**
- Algebra
- Geometry
- Fractions
- Percentages
- Statistics

**History (5 rules):**
- Ancient Civilizations
- Colonial Period
- Independence Movement
- World Wars
- Cultural Heritage

**Study Guide (5 rules):**
- Time Management
- Memory Techniques
- Exam Preparation
- Note Taking
- Motivation

### Expanding the Knowledge Base

To add new rules:

1. **Edit the subject knowledge base** (e.g., `subjects/physics_kb.py`)
2. **Add new rule dictionary**:
```python
PHYSICS_RULES['new_concept'] = {
    'keywords': ['keyword1', 'keyword2'],
    'explanation': 'Detailed explanation...',
    'examples': ['Example 1', 'Example 2']
}
```
3. **Update keywords list** in the corresponding agent
4. **Test with**: `python test_phase2_3.py`

## 🔧 Troubleshooting

### LLM Features Not Working
- ✅ Check `.env` file has valid `GEMINI_API_KEY`
- ✅ Verify API key at [Google AI Studio](https://makersuite.google.com/app/apikey)
- ✅ Check internet connection
- ✅ Review console for error messages

### Agent Not Responding
- ✅ Check if question contains relevant keywords
- ✅ Try rephrasing the question
- ✅ View agent statistics to see if agent is active
- ✅ Check `config.py` - ensure subject is enabled

### Installation Issues
- ✅ Verify Python 3.8+ is installed: `python --version`
- ✅ Update pip: `python -m pip install --upgrade pip`
- ✅ Install dependencies manually: `pip install -r requirements.txt`
- ✅ Check for error messages during setup

### Streamlit Not Starting
- ✅ Verify Streamlit is installed: `streamlit --version`
- ✅ Try running on different port: `streamlit run main_v2.py --server.port 8502`
- ✅ Check if port 8501 is already in use

## 🎯 Roadmap

### Completed ✅
- Phase 1: Basic expert system (3 subjects)
- Phase 2: Multi-Agent System (6 agents)
- Phase 3: Gemini AI + multilingual support

### Future Enhancements 🚀
- Student progress tracking
- Personalized learning paths
- Practice question generation
- Interactive quizzes
- More subjects (English, Mathematics advanced topics)
- Voice input/output
- Mobile app version

## 📚 Documentation

- **README.md** (this file): Complete system overview
- **QUICKSTART.md**: Quick start guide for beginners
- **ARCHITECTURE.md**: Detailed system architecture
- **PHASE2_3_GUIDE.md**: Phase 2+3 development guide

## 🤝 Contributing

To extend EduMentor:

1. **Add new subjects**: Create new knowledge base + agent
2. **Improve knowledge**: Add more rules to existing subjects
3. **Enhance UI**: Modify `main_v2.py`
4. **Add features**: Extend `HybridSystem` class

## 📝 License

This project is developed for educational purposes as part of the Expert Systems course at University of Moratuwa.

## 🙏 Acknowledgments

- **Experta**: Rule-based expert system framework
- **Streamlit**: Web UI framework
- **Google Gemini**: LLM for natural language enhancement
- **University of Moratuwa**: L3S1 Expert Systems course

---

**EduMentor v2.0** - Powered by Experta + Gemini AI | Multi-Agent System with 6 Specialized Agents

Happy Learning! 🎓
