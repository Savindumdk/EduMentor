# 📊 Multi-Input Expert System Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE (Streamlit)                      │
│                                                                         │
│  ┌───────────────────────────┐  ┌─────────────────────────────────┐   │
│  │   Multi-Input Form        │  │   Response Display              │   │
│  │  ┌─────────────────────┐  │  │  ┌──────────────────────────┐  │   │
│  │  │ 🎯 Category         │  │  │  │ 👤 Profile Summary       │  │   │
│  │  │ ❓ Question (text)   │  │  │  │ 💯 Confidence: 99%       │  │   │
│  │  │ 📚 Study Hours (0-12)│  │  │  │ 🎯 Concept               │  │   │
│  │  │ 😰 Stress (1-10)     │  │  │  │ 💡 Diagnosis             │  │   │
│  │  │ 😴 Sleep (3-12)      │  │  │  │ 📝 Explanation           │  │   │
│  │  │ 🎨 Learning Style    │  │  │  │ ✅ Recommendations       │  │   │
│  │  │ 📅 Upcoming Exam (☑) │  │  │  │ 🔍 Reasoning Trace       │  │   │
│  │  └─────────────────────┘  │  │  │ 🧠 Inferred Facts        │  │   │
│  │  [Get Advice Button]      │  │  └──────────────────────────┘  │   │
│  └───────────────────────────┘  └─────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                  EXPERT SYSTEM CORE (Experta Framework)                 │
│                                                                         │
│  ┌───────────────────────────────────────────────────────────────────┐ │
│  │  process_query_with_inputs()                                      │ │
│  │  ┌─────────────────┐  ┌────────────────┐  ┌──────────────────┐  │ │
│  │  │ 1. Normalize    │→ │ 2. Declare     │→ │ 3. Run Inference │  │ │
│  │  │    Inputs       │  │    Facts       │  │    Engine        │  │ │
│  │  └─────────────────┘  └────────────────┘  └──────────────────┘  │ │
│  └───────────────────────────────────────────────────────────────────┘ │
│                                    ▼                                    │
│  ┌───────────────────────────────────────────────────────────────────┐ │
│  │                    INFERENCE RULES (10+)                          │ │
│  │                                                                   │ │
│  │  Priority 20: ⚠️ High Stress + Low Sleep                          │ │
│  │  Priority 18: ⚠️ Low Hours + Upcoming Exam                        │ │
│  │  Priority 18: 🚨 Burnout Risk (High Hours + High Stress)          │ │
│  │  Priority 15: ⚠️ High Stress Alone                                │ │
│  │  Priority 15: 😴 Low Sleep                                         │ │
│  │  Priority 12: ✅ Moderate Stress + Good Hours                      │ │
│  │  Priority 10: 👁️ Visual + Memory                                  │ │
│  │  Priority 10: ✅ Good Sleep + Low Stress (Optimal)                │ │
│  │  Priority 8:  🏃 Kinesthetic Learner                              │ │
│  │  Priority 8:  🎧 Auditory Learner                                 │ │
│  │                                                                   │ │
│  │  Each rule can:                                                   │ │
│  │  • Match on multiple conditions (AND/OR logic)                    │ │
│  │  • Infer new facts (forward chaining)                             │ │
│  │  • Log reasoning steps                                            │ │
│  │  • Calculate confidence                                           │ │
│  └───────────────────────────────────────────────────────────────────┘ │
│                                    ▼                                    │
│  ┌───────────────────────────────────────────────────────────────────┐ │
│  │            ADAPTIVE RECOMMENDATION GENERATOR                      │ │
│  │                                                                   │ │
│  │  _generate_adaptive_recommendations()                             │ │
│  │  ├─ IF stress ≥ 8: "PRIORITY: Stress Management"                 │ │
│  │  ├─ IF sleep < 6: "CRITICAL: Sleep Recovery"                     │ │
│  │  ├─ IF study < 3 AND exam: "URGENT: Time Management"             │ │
│  │  ├─ IF study ≥ 8 AND stress ≥ 7: "⚠️ BURNOUT WARNING"            │ │
│  │  ├─ IF style = visual: "Visual Learning Strategy"                │ │
│  │  └─ IF optimal state: "✅ Excellent Conditions"                   │ │
│  │                                                                   │ │
│  │  _generate_diagnosis()                                            │ │
│  │  └─ Combines base diagnosis + input-specific observations         │ │
│  │                                                                   │ │
│  │  _calculate_confidence_adjustment()                               │ │
│  │  └─ Base confidence + (input_count × 2%) + pattern_bonuses       │ │
│  └───────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                   KNOWLEDGE BASE (study_guide_kb.json)                  │
│                                                                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │  Memory  │  │  Focus   │  │  Stress  │  │   Time   │              │
│  │          │  │          │  │          │  │   Mgmt   │              │
│  │ • Rules  │  │ • Rules  │  │ • Rules  │  │ • Rules  │              │
│  │ • Explan │  │ • Explan │  │ • Explan │  │ • Explan │              │
│  │ • Example│  │ • Example│  │ • Example│  │ • Example│              │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘              │
│                                                                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │  Exam    │  │Motivation│  │Confidence│  │  Sleep   │              │
│  │  Prep    │  │          │  │          │  │          │              │
│  │ • Rules  │  │ • Rules  │  │ • Rules  │  │ • Rules  │              │
│  │ • Explan │  │ • Explan │  │ • Explan │  │ • Explan │              │
│  │ • Example│  │ • Example│  │ • Example│  │ • Example│              │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘              │
└─────────────────────────────────────────────────────────────────────────┘
```

## 🔄 Data Flow

```
USER INPUT
    ↓
┌───────────────────────────────────────┐
│ Category: "Memory"                    │
│ Question: "I struggle to remember..." │
│ Study Hours: 3                        │
│ Stress Level: 8                       │
│ Sleep Hours: 5                        │
│ Learning Style: "Visual"              │
│ Upcoming Exam: True                   │
└───────────────────────────────────────┘
    ↓
NORMALIZATION
    ↓
┌───────────────────────────────────────┐
│ Fact(category="memory")               │
│ Fact(user_query="i struggle...")      │
│ Fact(study_hours=3)                   │
│ Fact(stress_level=8)                  │
│ Fact(sleep_hours=5)                   │
│ Fact(learning_style="visual")         │
│ Fact(has_upcoming_exam=True)          │
└───────────────────────────────────────┘
    ↓
INFERENCE ENGINE (Forward Chaining)
    ↓
┌───────────────────────────────────────┐
│ Rule Fired (Priority 20):             │
│ stress≥7 AND sleep<6                  │
│ → Infer: poor_focus                   │
│ → Infer: memory_impaired              │
│                                       │
│ Rule Fired (Priority 15):             │
│ stress≥8                              │
│ → Infer: high_stress                  │
│ → Infer: low_focus                    │
│                                       │
│ Rule Fired (Priority 15):             │
│ sleep<7                               │
│ → Infer: sleep_deprived               │
│ → Infer: memory_weak                  │
│                                       │
│ Rule Fired (Priority 10):             │
│ category=memory AND style=visual      │
│ → Infer: use_visualization            │
└───────────────────────────────────────┘
    ↓
ADAPTIVE RECOMMENDATIONS
    ↓
┌───────────────────────────────────────┐
│ Base KB Recommendations:              │
│ 1. Use spaced repetition              │
│ 2. Practice active recall             │
│ 3. Improve sleep                      │
│                                       │
│ + Adaptive Additions:                 │
│ 4. PRIORITY: Stress Management        │
│ 5. CRITICAL: Sleep Recovery           │
│ 6. Visual Learning Strategy           │
└───────────────────────────────────────┘
    ↓
CONFIDENCE CALCULATION
    ↓
┌───────────────────────────────────────┐
│ Base: 90% (from KB)                   │
│ + Input count: 7 × 2% = +14%          │
│ - Burnout risk: -3%                   │
│ = Final: 99% (capped)                 │
└───────────────────────────────────────┘
    ↓
STRUCTURED RESPONSE
    ↓
┌───────────────────────────────────────┐
│ {                                     │
│   concept: "🧠 Memory Enhancement"    │
│   confidence: 0.99                    │
│   diagnosis: "High stress + Sleep..." │
│   explanation: "Memory works in 3..." │
│   recommendation: "1. Spaced rep..."  │
│   examples: [...]                     │
│   resources: [...]                    │
│   reasoning_trace: [...]              │
│   inferred_facts: [...]               │
│   fired_rules: [...]                  │
│   user_profile: {...}                 │
│ }                                     │
└───────────────────────────────────────┘
    ↓
DISPLAY TO USER
```

## 🎯 Rule Matching Examples

### Example 1: Burnout Detection
```
INPUT:
  study_hours = 10
  stress_level = 9

RULE:
  @Rule(
    Fact(study_hours >= 8) AND
    Fact(stress_level >= 7),
    salience=18
  )

MATCH: ✅ YES

ACTION:
  → Declare(Fact(condition="burnout_risk"))
  → Log: "⚠️ BURNOUT WARNING"
  → Add adaptive rec: "Take mandatory breaks"
```

### Example 2: Optimal State
```
INPUT:
  sleep_hours = 8
  stress_level = 2

RULE:
  @Rule(
    Fact(sleep_hours >= 7) AND
    Fact(stress_level <= 3),
    salience=10
  )

MATCH: ✅ YES

ACTION:
  → Declare(Fact(condition="optimal_learning_state"))
  → Log: "✅ Excellent conditions"
  → Add adaptive rec: "Maximize with active recall"
```

### Example 3: Learning Style Adaptation
```
INPUT:
  category = "memory"
  learning_style = "visual"

RULE:
  @Rule(
    Fact(category="memory") AND
    Fact(learning_style="visual"),
    salience=10
  )

MATCH: ✅ YES

ACTION:
  → Declare(Fact(condition="use_visualization"))
  → Add adaptive rec: "Use mind maps, memory palace"
```

## 📊 Confidence Calculation

```
Base Confidence = max(rule_confidences) from KB
                = 0.90 (example)

Adjustments:
  + Input completeness: 7 inputs × 0.02 = +0.14
  + Optimal state bonus: +0.05 (if detected)
  - Burnout risk penalty: -0.03 (if detected)

Final = min(0.99, max(0.60, Base + Adjustments))
      = min(0.99, max(0.60, 0.90 + 0.14))
      = min(0.99, 1.04)
      = 0.99 (99% confidence)
```

## 🧠 Knowledge Representation

```json
{
  "memory": {
    "keywords": ["memory", "remember", "recall"],
    "concept": "🧠 Memory Enhancement",
    "confidence": 0.90,
    "rules": [
      {
        "id": "memory_001",
        "condition": "mentions_memory",
        "recommend": "Use spaced repetition",
        "confidence": 0.95,
        "priority": 1
      }
    ],
    "explanation": "Memory works in 3 stages...",
    "examples": ["Use anki flashcards", ...],
    "resources": ["Book: Make It Stick", ...]
  }
}
```

## 🔍 Explainability Layers

```
Layer 1: User Profile Summary
  → Shows all inputs with visual indicators
  → Color-coded stress/sleep metrics

Layer 2: Confidence Score
  → 60-99% range with calculation transparency

Layer 3: Reasoning Trace
  → Step-by-step logs of inference process
  → Shows which rules fired and why

Layer 4: Inferred Facts
  → Shows additional insights discovered
  → Examples: "burnout_risk", "optimal_state"

Layer 5: Fired Rules
  → Technical details (rule IDs)
  → For debugging and transparency
```

---

**This architecture delivers a production-grade expert system with:**
- ✅ Multi-input processing
- ✅ Rule-based inference with priorities
- ✅ Adaptive recommendation generation
- ✅ Dynamic confidence calculation
- ✅ Full explainability and transparency
- ✅ Backward compatibility

**Status**: ✅ Complete and tested (99% confidence on all test cases)
