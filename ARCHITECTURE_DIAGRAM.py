"""# EduMentor Architecture Diagram

Agent Architecture Visualization# ================================

---------------------------------

Visual representation of the Expert Agent + Tools pattern"""

"""┌─────────────────────────────────────────────────────────────────────────────┐

│                           STREAMLIT WEB UI (main_new.py)                    │

def print_architecture():│                                                                             │

    """Print ASCII art of the architecture."""│  ┌─────────────────┐  ┌──────────────────┐  ┌──────────────────────┐      │

    │  │ Chat Interface  │  │ Example Questions│  │ Conversation Stats   │      │

    diagram = """│  │ - User input    │  │ - Biology        │  │ - Turn count         │      │

    │  │ - Message hist  │  │ - Physics        │  │ - Topics discussed   │      │

╔══════════════════════════════════════════════════════════════════════════╗│  │ - Clarifications│  │ - Study Guide    │  │ - Memory context     │      │

║                          EXPERT AGENT ARCHITECTURE                       ║│  └─────────────────┘  └──────────────────┘  └──────────────────────┘      │

╚══════════════════════════════════════════════════════════════════════════╝│                                     │                                       │

└─────────────────────────────────────┼───────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────┐                                      │

│                          🤖 EXPERT AGENT                                 │                                      ▼

│                      (Gemini LLM Coordinator)                            │┌─────────────────────────────────────────────────────────────────────────────┐

│                                                                          ││                    SYSTEM ORCHESTRATOR (core/orchestrator.py)               │

│  ┌────────────────────────────────────────────────────────────────────┐ ││                                                                             │

│  │ STEP 1: Query Analysis                                             │ ││  Main coordinator that manages the complete flow:                          │

│  │ • Understands student's question                                   │ ││                                                                             │

│  │ • Identifies key concepts and intent                               │ ││  1. Receives user input                                                    │

│  │ • Determines query type (information vs diagnostic)                │ ││  2. Updates conversation memory                                            │

│  └────────────────────────────────────────────────────────────────────┘ ││  3. Calls Intent Classifier                                                │

│                                                                          ││  4. Routes to appropriate Expert System                                    │

│  ┌────────────────────────────────────────────────────────────────────┐ ││  5. Handles clarification loops                                            │

│  │ STEP 2: Tool Selection                                             │ ││  6. Calls Response Refiner                                                 │

│  │ • Chooses appropriate expert system tool                           │ ││  7. Returns formatted response                                             │

│  │ • Options: Biology, Physics, Chemistry, Study Guide                │ ││                                                                             │

│  │ • Provides reasoning for selection                                 │ │└────┬──────────────┬──────────────┬──────────────┬──────────────────────────┘

│  └────────────────────────────────────────────────────────────────────┘ │     │              │              │              │

│                                                                          │     │              │              │              │

│  ┌────────────────────────────────────────────────────────────────────┐ │     ▼              ▼              ▼              ▼

│  │ STEP 3: Parameter Extraction                                       │ │┌──────────┐  ┌──────────┐  ┌────────────┐  ┌──────────────┐

│  │ • Determines exact query_topic                                     │ ││ Memory   │  │ Intent   │  │  Expert    │  │  Response    │

│  │ • Examples: 'photosynthesis', 'wave_motion', 'diagnostic'          │ ││          │  │Classifier│  │  Systems   │  │  Refiner     │

│  │ • Ensures topic matches expert system rules                        │ │└──────────┘  └──────────┘  └────────────┘  └──────────────┘

│  └────────────────────────────────────────────────────────────────────┘ │

│                                                                          │

└──────────────────────────┬───────────────────────────────────────────────┘═══════════════════════════════════════════════════════════════════════════════

                           │COMPONENT 1: CONVERSATION MEMORY (core/memory.py)

              ┌────────────┴────────────┐═══════════════════════════════════════════════════════════════════════════════

              │                         │

              ▼                         ▼    ConversationMemory

┏━━━━━━━━━━━━━━━━━━━━━┓    ┏━━━━━━━━━━━━━━━━━━━━━┓    ├── history: List[ConversationTurn]

┃  INFORMATION TOOLS  ┃    ┃   DIAGNOSTIC TOOL   ┃    ├── max_history: int (10)

┃   (Rule-Based)      ┃    ┃    (Rule-Based)     ┃    │

┗━━━━━━━━━━━━━━━━━━━━━┛    ┗━━━━━━━━━━━━━━━━━━━━━┛    ├── Methods:

           │                         │    │   ├── start_turn(question)

  ┌────────┴────────┐               │    │   ├── complete_turn(response, expert_used)

  │                 │                │    │   ├── add_clarification_to_current(clarification, response)

  ▼                 ▼                ▼    │   ├── get_context_summary(n)

┌─────────┐  ┌─────────┐  ┌──────────────┐    │   └── get_full_context_for_llm(n)

│ Biology │  │ Physics │  │ Study Guide  │    │

│ Expert  │  │ Expert  │  │   Expert     │    └── Purpose:

├─────────┤  ├─────────┤  ├──────────────┤        • Tracks conversation history

│ 1,330   │  │ 1,060   │  │ Progressive  │        • Enables pronoun resolution ("it", "that", "this")

│ Rules   │  │ Rules   │  │ Questioning  │        • Provides context for Intent Classifier

└─────────┘  └─────────┘  └──────────────┘        • Supports multi-turn clarification

                 │

          ┌──────┴──────┐

          │             │═══════════════════════════════════════════════════════════════════════════════

          ▼             ▼COMPONENT 2: INTENT CLASSIFIER (core/intent_classifier.py)

     ┌─────────┐  ┌─────────┐═══════════════════════════════════════════════════════════════════════════════

     │Chemistry│  │  Math   │

     │ Expert  │  │ Expert  │    IntentClassifierAgent (LLM-powered)

     ├─────────┤  ├─────────┤    │

     │  940    │  │ Coming  │    ├── AVAILABLE_SUBJECTS:

     │ Rules   │  │  Soon   │    │   ├── Biology: [photosynthesis, respiration, digestion, ...]

     └─────────┘  └─────────┘    │   ├── Physics: [forces, energy, electricity, ...]

    │   ├── Chemistry: [acids, bases, reactions, ...]

═══════════════════════════════════════════════════════════════════════════    │   ├── Mathematics: [algebra, geometry, fractions, ...]

    │   ├── History: [civilizations, wars, revolutions, ...]

                          EXECUTION FLOW    │   └── StudyGuide: [study techniques, exam prep, memory, ...]

    │

Student Query: "What is photosynthesis?"    ├── classify_intent(question) → Returns:

    │    │   {

    ▼    │       'subject': 'Biology',           ← Which expert system

┌─────────────────────────────────────────────────────────┐    │       'confidence': 0.95,             ← Confidence (0-1)

│ 1. AGENT ANALYSIS (LLM)                                 │    │       'is_clarification': False,      ← Answering clarification?

│    → Tool: biology_expert                               │    │       'extracted_topic': 'forces',    ← Specific topic

│    → Topic: photosynthesis                              │    │       'reasoning': '...'              ← Why this classification

│    → Reasoning: Direct biology question                 │    │   }

└─────────────────────────────────────────────────────────┘    │

    │    ├── Methods:

    ▼    │   ├── _build_classification_prompt()

┌─────────────────────────────────────────────────────────┐    │   ├── _parse_classification_response()

│ 2. EXPERT EXECUTION (@Rule Matching)                    │    │   └── _fallback_classification()      ← Keyword-based backup

│    → Declare: Fact(query_topic='photosynthesis')        │    │

│    → Run inference engine                               │    └── Purpose:

│    → Match @Rule decorated methods                      │        • Determines which expert system to call

│    → Return: {concept, explanation, examples}           │        • Extracts specific topic from user's question

└─────────────────────────────────────────────────────────┘        • Uses conversation context for ambiguity resolution

    │        • Falls back to keywords if LLM fails

    ▼

┌─────────────────────────────────────────────────────────┐

│ 3. RESPONSE ENHANCEMENT (LLM)                           │═══════════════════════════════════════════════════════════════════════════════

│    → Takes expert response                              │COMPONENT 3: EXPERT SYSTEMS (experts/*.py)

│    → Makes natural and conversational                   │═══════════════════════════════════════════════════════════════════════════════

│    → Adds source attribution                            │

│    → Returns enhanced response                          │┌─────────────────────────────────────────────────────────────────────────────┐

└─────────────────────────────────────────────────────────┘│                          TWO TYPES OF EXPERT SYSTEMS                        │

    │└─────────────────────────────────────────────────────────────────────────────┘

    ▼

Student receives: Enhanced, accurate, cited answer┌────────────────────────────────────┐  ┌──────────────────────────────────────┐

│  INFORMATION EXPERTS               │  │  DIAGNOSTIC EXPERTS                  │

═══════════════════════════════════════════════════════════════════════════│  (Biology, Physics, Chemistry)     │  │  (Study Guide)                       │

├────────────────────────────────────┤  ├──────────────────────────────────────┤

                      KEY ARCHITECTURAL BENEFITS│                                    │  │                                      │

│  Pattern: Direct Q&A               │  │  Pattern: Progressive Questioning    │

✓ SEPARATION OF CONCERNS│                                    │  │                                      │

  • Agent = Intelligence & Coordination│  @Rule(Fact(query_topic='...'))   │  │  @Rule(                              │

  • Tools = Domain Knowledge & Rules│  def rule_photosynthesis(self):    │  │      Fact(action='diagnose'),        │

  • Clear boundaries and responsibilities│      self.response = {             │  │      NOT(Fact(weak_area=W())),       │

│          'concept': '...',         │  │      salience=100                    │

✓ MODULARITY│          'explanation': '...',     │  │  )                                   │

  • Expert systems are independent tools│          'examples': [...]         │  │  def ask_weak_area(self):            │

  • Can add/remove tools without affecting agent│      }                             │  │      self.needs_clarification = True │

  • Tools can be tested in isolation│                                    │  │      self.clarification_question =..│

│  Single inference run              │  │                                      │

✓ REUSABILITY│  ↓                                 │  │  Multiple inference runs             │

  • Same expert tools can be used:│  Response ready                    │  │  ↓                                   │

    - Via agent (normal usage)│                                    │  │  Question → Answer → Question → ...  │

    - Directly (programmatic access)│  Use when:                         │  │  ↓                                   │

    - In other applications│  • User wants to learn concept     │  │  Final diagnosis                     │

│  • Clear question                  │  │                                      │

✓ EXPLAINABILITY│  • "What is photosynthesis?"       │  │  Use when:                           │

  • Shows which tool was selected│                                    │  │  • User has problem to solve         │

  • Displays agent's reasoning│                                    │  │  • Needs information gathering       │

  • Reveals expert system's raw response│                                    │  │  • "I'm struggling with studies"     │

  • Transparent decision making└────────────────────────────────────┘  └──────────────────────────────────────┘



✓ EXTENSIBILITY┌─────────────────────────────────────────────────────────────────────────────┐

  • Easy to add new expert tools│                     CURRENT EXPERT SYSTEMS                                  │

  • Simple tool registration├─────────────────────────────────────────────────────────────────────────────┤

  • Minimal code changes needed│                                                                             │

│  BiologyExpert (Information) - 5 rules                                      │

✓ ACCURACY + INTELLIGENCE│  ├── Photosynthesis                                                         │

  • LLM provides understanding & enhancement│  ├── Respiration                                                            │

  • Expert systems provide verified knowledge│  ├── Digestion                                                              │

  • Best of both worlds: Smart + Accurate│  ├── Cell Structure                                                         │

│  └── Reproduction                                                           │

═══════════════════════════════════════════════════════════════════════════│                                                                             │

│  PhysicsExpert (Information) - 4 rules                                      │

                        TOOL INTERFACE│  ├── Forces                                                                 │

│  ├── Energy                                                                 │

All expert system tools implement:│  ├── Electricity                                                            │

│  └── No Match (fallback)                                                    │

class ExpertTool(KnowledgeEngine):│                                                                             │

    def __init__(self):│  StudyGuideExpert (Diagnostic) - 12 rules                                   │

        self.response = None│  ├── Progressive Questioning (5 rules, salience=100-90)                     │

        self.needs_clarification = False│  │   ├── ask_weak_area()                                                    │

        self.clarification_question = None│  │   ├── ask_math_subject()                                                 │

    │  │   ├── ask_essay_difficulty()                                             │

    def get_response(self):│  │   ├── ask_mcq_issue()                                                    │

        return self.response│  │   └── ask_theory_subject()                                               │

    │  │                                                                           │

    def requires_clarification(self):│  ├── Clear Diagnoses (5 rules, normal salience)                             │

        return self.needs_clarification│  │   ├── diagnose_physics_math()                                            │

    │  │   ├── diagnose_chemistry_math()                                          │

    def get_clarification_question(self):│  │   ├── diagnose_essay_memory()                                            │

        return self.clarification_question│  │   ├── diagnose_essay_structure()                                         │

│  │   └── diagnose_mcq_speed()                                               │

═══════════════════════════════════════════════════════════════════════════│  │                                                                           │

"""│  └── Uncertain Diagnoses (2 rules, normal salience)                         │

    │      ├── diagnose_math_fundamental() - Complex case                         │

    print(diagram)│      └── diagnose_general_understanding() - Multiple possible causes        │

│                                                                             │

if __name__ == "__main__":└─────────────────────────────────────────────────────────────────────────────┘

    print_architecture()


═══════════════════════════════════════════════════════════════════════════════
COMPONENT 4: RESPONSE REFINER (core/response_refiner.py)
═══════════════════════════════════════════════════════════════════════════════

    ResponseRefinementAgent (LLM-powered)
    │
    ├── refine_response(expert_output, user_question) → Returns:
    │   {
    │       'original_rule': {...},           ← Expert system output
    │       'refined_explanation': '...',     ← Natural language version
    │       'concept': '...',
    │       'topic': '...',
    │       'examples': [...]
    │   }
    │
    ├── Critical Constraints:
    │   • "ONLY use information from the rule below"
    │   • "DO NOT add any new facts"
    │   • "You are NOT a knowledge source"
    │   • "You are ONLY making the output more readable"
    │
    ├── Purpose:
    │   • Converts expert system output to natural language
    │   • Maintains factual accuracy (no hallucinations)
    │   • Makes response conversational
    │   • Preserves all examples and details
    │
    └── Optional for diagnostic responses
        (Diagnostics already in natural language)


═══════════════════════════════════════════════════════════════════════════════
COMPLETE FLOW DIAGRAMS
═══════════════════════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────────────────────┐
│  FLOW 1: INFORMATION EXPERT (Biology, Physics)                             │
└─────────────────────────────────────────────────────────────────────────────┘

    User: "What is photosynthesis?"
      │
      ▼
    ┌─────────────────────┐
    │ System Orchestrator │
    │ - start_turn()      │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │ Intent Classifier   │
    │ (LLM)               │
    │                     │
    │ Result:             │
    │ - subject: Biology  │
    │ - topic: photosynth │
    │ - confidence: 0.95  │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │ BiologyExpert       │
    │ (Experta)           │
    │                     │
    │ 1. declare(Fact(    │
    │      keywords=[...],│
    │      query_topic='  │
    │      photosynthesis'│
    │    ))               │
    │ 2. engine.run()     │
    │ 3. Rule fires!      │
    │                     │
    │ Response:           │
    │ - concept           │
    │ - explanation       │
    │ - examples          │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │ Response Refiner    │
    │ (LLM)               │
    │                     │
    │ - Polishes output   │
    │ - No new facts      │
    │ - Natural language  │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │ Display to User     │
    │                     │
    │ Expert Rule: [exp]  │
    │ AI Response: [ref]  │
    │ Examples: [...]     │
    └─────────────────────┘

    Total: ~2-3 seconds


┌─────────────────────────────────────────────────────────────────────────────┐
│  FLOW 2: DIAGNOSTIC EXPERT (Study Guide) - Multi-Turn                      │
└─────────────────────────────────────────────────────────────────────────────┘

    TURN 1:
    User: "I'm struggling with science"
      │
      ▼
    Intent Classifier → subject: 'StudyGuide'
      │
      ▼
    StudyGuideExpert
    ├── reset()
    ├── run() → Questioning rule fires (salience=100)
    │
    └── Result: needs_clarification = True
        clarification_question = "What area do you struggle with?"
      │
      ▼
    Display question to user
    Store engine state


    TURN 2:
    User: "math"
      │
      ▼
    Retrieve stored engine
      │
      ▼
    StudyGuideExpert
    ├── declare(Fact(weak_area='math'))
    ├── run() → Next questioning rule fires (salience=90)
    │
    └── Result: needs_clarification = True
        clarification_question = "Which subject's math?"
      │
      ▼
    Display question to user
    Store engine state


    TURN 3:
    User: "physics"
      │
      ▼
    Retrieve stored engine
      │
      ▼
    StudyGuideExpert
    ├── declare(Fact(math_subject='physics'))
    ├── run() → Diagnosis rule fires (normal salience)
    │
    └── Result: diagnosis_complete = True
        response = {
            'diagnosis': '...',
            'explanation': '...',
            'recommendation': '...',
            'reasoning_chain': [...]
        }
      │
      ▼
    Display diagnosis + recommendations
    Clear stored engine


    Total: 3-5 turns depending on complexity


═══════════════════════════════════════════════════════════════════════════════
CLARIFICATION HANDLING
═══════════════════════════════════════════════════════════════════════════════

┌────────────────────────────────────┐  ┌──────────────────────────────────────┐
│  SUBJECT CLARIFICATION             │  │  DIAGNOSTIC CLARIFICATION            │
│  (Intent Classifier level)         │  │  (Expert System level)               │
├────────────────────────────────────┤  ├──────────────────────────────────────┤
│                                    │  │                                      │
│  User: "Tell me about energy"      │  │  User: "I'm struggling"              │
│    ↓                               │  │    ↓                                 │
│  Intent Classifier:                │  │  Intent Classifier:                  │
│    - Confidence too low            │  │    - Subject: StudyGuide             │
│    - Could be Physics OR Biology   │  │    - Confidence: High                │
│    ↓                               │  │    ↓                                 │
│  Orchestrator:                     │  │  StudyGuideExpert:                   │
│    - awaiting_clarification = True│  │    - needs_clarification = True      │
│    - pending_subjects = [...]      │  │    - clarification_question = "..."  │
│    ↓                               │  │    ↓                                 │
│  UI displays:                      │  │  UI displays:                        │
│    "Do you mean:                   │  │    Question from expert              │
│     - Physics (energy transfer)    │  │    - What area do you struggle?      │
│     - Biology (cellular energy)"   │  │    - MCQ / Essay / Math / Theory     │
│    ↓                               │  │    ↓                                 │
│  User: "Physics"                   │  │  User: "Math"                        │
│    ↓                               │  │    ↓                                 │
│  Route to PhysicsExpert            │  │  Declare Fact(weak_area='math')      │
│                                    │  │  Continue diagnostic process         │
└────────────────────────────────────┘  └──────────────────────────────────────┘


═══════════════════════════════════════════════════════════════════════════════
KEY ARCHITECTURAL DECISIONS
═══════════════════════════════════════════════════════════════════════════════

1. HYBRID APPROACH: LLM + Expert Systems
   ├── LLM handles: Intent classification, natural language, ambiguity
   └── Expert Systems handle: Structured reasoning, rules, explainability

2. SEPARATION OF CONCERNS:
   ├── Intent Classifier: What subject?
   ├── Expert Systems: What knowledge?
   └── Response Refiner: How to say it?

3. CONVERSATION MEMORY:
   ├── Enables: Multi-turn conversations
   ├── Supports: Pronoun resolution, context tracking
   └── Limit: 10 turns (prevents token overflow)

4. TWO EXPERT PATTERNS:
   ├── Information: Direct Q&A, single run
   └── Diagnostic: Progressive questioning, multi-turn

5. EXPLAINABILITY:
   ├── Show expert rules (original output)
   ├── Show reasoning chains (diagnostic)
   └── LLM refinement optional and clearly labeled

6. SIMPLIFICATION:
   ├── Removed complex MATCH patterns
   ├── Use simple Fact(query_topic='...')
   └── Intent Classifier handles keyword → topic mapping


═══════════════════════════════════════════════════════════════════════════════
SYSTEM STATUS
═══════════════════════════════════════════════════════════════════════════════

✅ FULLY IMPLEMENTED:
   • Intent Classifier (LLM-powered)
   • Conversation Memory
   • Response Refiner (LLM-powered)
   • BiologyExpert (5 rules, simplified)
   • PhysicsExpert (4 rules, simplified)
   • StudyGuideExpert (12 rules, diagnostic)
   • Streamlit UI (basic chat interface)
   • System Orchestrator (core coordination)

⏳ PARTIALLY IMPLEMENTED:
   • Diagnostic flow in orchestrator (logic designed, needs coding)
   • UI for diagnostic questions (design ready, needs implementation)

❌ NOT YET IMPLEMENTED:
   • ChemistryExpert, MathematicsExpert, HistoryExpert
   • Multi-turn diagnostic UI flow
   • Diagnostic report export
   • Visual diagnostic flowcharts


═══════════════════════════════════════════════════════════════════════════════
INTEGRATION PRIORITY
═══════════════════════════════════════════════════════════════════════════════

HIGH PRIORITY (Complete core functionality):
  1. ⏳ Update orchestrator for diagnostic flow (1-2 hours)
  2. ⏳ Update UI for diagnostic questions (1 hour)
  3. ⏳ Test end-to-end diagnostic flow (30 min)

MEDIUM PRIORITY (Polish):
  4. Add more diagnostic rules (test anxiety, time management)
  5. Create remaining subject experts (Chemistry, Math, History)
  6. Add confidence visualization in UI
  7. Cleanup old files (agents/, subjects/, llm/)

LOW PRIORITY (Future enhancements):
  8. Visual diagnostic flowchart
  9. Diagnostic report PDF export
  10. Historical tracking of common problems
  11. Mini-diagnostics in subject experts


═══════════════════════════════════════════════════════════════════════════════
"""
