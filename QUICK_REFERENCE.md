# 🚀 EduMentor Phase 2+3 - Quick Reference

## 📦 What's New

### ✨ Phase 2: Multi-Agent System (MAS)
- **6 Specialized Agents**: Physics, Biology, Chemistry, Mathematics, History, Study Guide
- **Coordinator Agent**: Intelligently routes questions to the right expert
- **30 Knowledge Rules**: 5 rules per subject with detailed explanations

### 🌟 Phase 3: LLM Integration
- **Gemini AI**: Natural language enhancement for conversational responses
- **Multilingual**: English, Sinhala, Tamil support
- **Auto-Detection**: Automatically detects question language
- **Hybrid System**: Expert system accuracy + AI naturalness

---

## ⚡ Quick Start (3 Steps)

### 1️⃣ Install
```powershell
cd "c:\UOM\L3S1\Expert Systems\EduMentor"
python setup.py
```

### 2️⃣ Configure
1. Get API key: https://makersuite.google.com/app/apikey
2. Open `.env` file
3. Replace: `GEMINI_API_KEY=your_actual_key_here`

### 3️⃣ Run
```powershell
streamlit run main.py
```
OR
```powershell
python start.py
```

---

## 📁 File Structure

```
EduMentor/
│
├── 🤖 agents/              Multi-Agent System
│   ├── coordinator_agent.py    Routes questions
│   ├── base_agent.py            Common agent logic
│   ├── physics_agent.py         Physics expert
│   ├── biology_agent.py         Biology expert
│   ├── chemistry_agent.py       Chemistry expert
│   ├── mathematics_agent.py     Math expert
│   ├── history_agent.py         History expert
│   └── study_guide_agent.py     Study tips expert
│
├── 📚 subjects/            Knowledge Bases
│   ├── physics_kb.py            5 physics rules
│   ├── biology_kb.py            5 biology rules
│   ├── chemistry_kb.py          5 chemistry rules
│   ├── mathematics_kb.py        5 math rules
│   ├── history_kb.py            5 history rules
│   └── study_guide_kb.py        5 study tips
│
├── 🌟 llm/                 LLM Integration
│   └── gemini_interface.py      Gemini AI interface
│
├── 🛠️ utils/               Utilities
│   ├── language_detector.py     Auto language detection
│   └── response_formatter.py    Format responses
│
├── 🖥️ main_v2.py            NEW Streamlit UI
├── ⚙️ config.py             Configuration
├── 🧪 test_phase2_3.py      Test suite
├── 📦 setup.py              Setup script
└── 🎯 start.py              Quick launcher
```

---

## 🎮 Using the Application

### Main Interface

**Question Input**:
- Type your question in any language
- Click "🚀 Ask" button
- Get instant answer with AI enhancement

**Sidebar Controls**:
- 🌍 **Language**: Choose response language
- 🌟 **AI Enhancement**: Toggle Gemini on/off
- 📚 **Subjects**: See available agents
- 📊 **Statistics**: View agent usage
- 🗑️ **Clear History**: Reset conversation

### Example Questions

| Subject | Example Question |
|---------|-----------------|
| ⚛️ Physics | "What is Newton's law of motion?" |
| 🧬 Biology | "Explain photosynthesis" |
| 🧪 Chemistry | "What are acids and bases?" |
| 📐 Math | "How do I solve quadratic equations?" |
| 📜 History | "Tell me about Sri Lankan independence" |
| 📖 Study | "How can I improve my memory?" |

---

## 🧪 Testing

Run comprehensive tests:
```powershell
python test_phase2_3.py
```

**Tests Include**:
1. ✅ Coordinator routing
2. ✅ Agent responses
3. ✅ Language detection
4. ✅ Response formatting
5. ✅ LLM initialization
6. ✅ Hybrid system
7. ✅ Agent statistics

---

## ⚙️ Configuration

Edit `config.py`:

```python
# Feature toggles
MAS_ENABLED = True           # Multi-Agent System
LLM_ENABLED = True           # Gemini AI
MULTILINGUAL_ENABLED = True  # Language support
AUTO_DETECT_LANGUAGE = True  # Auto language detection

# LLM settings
LLM_MODEL = "gemini-pro"
LLM_TEMPERATURE = 0.7        # Response creativity
FALLBACK_TO_EXPERT_SYSTEM = True
```

---

## 🐛 Troubleshooting

### LLM Not Working?
```
✓ Check .env has GEMINI_API_KEY
✓ Verify API key is valid
✓ Check internet connection
```

### Agent Not Responding?
```
✓ Check question has relevant keywords
✓ Try rephrasing question
✓ View agent statistics
```

### Installation Failed?
```
✓ Python 3.8+ installed?
✓ Run: python -m pip install --upgrade pip
✓ Run: pip install -r requirements.txt
```

---

## 📊 System Architecture

```
Student Question
      ↓
Language Detection (auto)
      ↓
CoordinatorAgent (routes)
      ↓
Specialized Agent (processes)
      ↓
Experta Rules (reasoning)
      ↓
Gemini AI (enhancement)
      ↓
Translation (if needed)
      ↓
Enhanced Response
```

---

## 🎯 Key Features

| Feature | Description |
|---------|-------------|
| **6 Agents** | Physics, Biology, Chemistry, Math, History, Study |
| **30 Rules** | 5 detailed rules per subject |
| **Smart Routing** | Coordinator finds best agent |
| **AI Enhancement** | Gemini makes responses natural |
| **3 Languages** | English, Sinhala, Tamil |
| **Auto-Detect** | Knows your question language |
| **Statistics** | Track which agents used most |
| **History** | Review past Q&A pairs |

---

## 📚 Documentation Files

| File | Purpose |
|------|---------|
| `README.md` | Complete system overview |
| `IMPLEMENTATION_SUMMARY.md` | What was built |
| `QUICK_REFERENCE.md` | Quick reference (this file) |
| `ARCHITECTURE.md` | System design |

---

## 🔑 Important Commands

```powershell
# Setup (first time)
python setup.py

# Run application
streamlit run main.py

# Or use launcher
python start.py

# Run tests
python test_system.py

# Check Python version
python --version

# Check installed packages
pip list

# Update pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

---

## 💡 Tips & Tricks

### For Best Results:
1. ✅ Use specific keywords in questions
2. ✅ Enable AI enhancement for natural responses
3. ✅ Try questions in your native language
4. ✅ Check agent statistics to see coverage
5. ✅ Review history for learning patterns

### To Extend the System:
1. **Add Rules**: Edit knowledge base files in `subjects/`
2. **Add Agents**: Create new agent in `agents/`
3. **Customize UI**: Edit `main_v2.py`
4. **Change Config**: Modify `config.py`

---

## 🎓 What You've Learned

- ✅ Expert Systems (Experta)
- ✅ Multi-Agent Systems (MAS)
- ✅ LLM Integration (Gemini)
- ✅ Knowledge Representation
- ✅ Natural Language Processing
- ✅ Web UI Development (Streamlit)
- ✅ Software Architecture
- ✅ Python Best Practices

---

## 📞 Quick Help

**Problem**: "Module not found"
**Solution**: Run `python setup.py`

**Problem**: "LLM not responding"
**Solution**: Check `.env` has valid GEMINI_API_KEY

**Problem**: "Agent gives no answer"
**Solution**: Rephrase question with subject keywords

**Problem**: "Port already in use"
**Solution**: `streamlit run main.py --server.port 8502`

---

## ✅ Version Info

- **Version**: 2.0.0
- **Phase**: 2+3 (MAS + LLM)
- **Agents**: 6 specialized + 1 coordinator
- **Rules**: 30 total (5 per subject)
- **Languages**: 3 (English, Sinhala, Tamil)
- **Framework**: Experta + Gemini + Streamlit

---

## 🚀 Ready to Go!

You now have everything you need to:
1. ✅ Run the application
2. ✅ Test all features
3. ✅ Understand the architecture
4. ✅ Extend the system
5. ✅ Help O/L students learn!

**Happy Teaching and Learning!** 🎓

---

*For detailed information, see README.md*
