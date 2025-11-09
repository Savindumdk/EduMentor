"""
Study Guide Expert System
-------------------------
An interactive diagnostic expert system that helps students identify their
study weaknesses and provides personalized recommendations.

Demonstrates:
1. Problem Solving (Diagnosing study weak-points)
2. Missing Information (Progressive questioning)
3. Uncertainty (Multiple possible diagnoses)
4. Explainability (Reasoning chain logging)

Based on the O/L Science Tutor pattern but adapted for the EduMentor architecture.
"""

from experta import *


class StudyGuideExpert(KnowledgeEngine):
    """
    Expert system for diagnosing student study weaknesses.
    
    Uses progressive questioning to identify:
    - Weak areas (question types, subjects)
    - Root causes (memory, understanding, time management)
    - Personalized recommendations
    
    This expert works differently from subject experts - it's diagnostic
    rather than informational.
    """
    
    def __init__(self):
        super().__init__()
        self.response = None
        self.needs_clarification = False
        self.clarification_question = None
        self.explanation_log = []  # Tracks reasoning steps
        self.diagnosis_complete = False
        self.collected_facts = {}  # Store facts for explanation
    
    @DefFacts()
    def _initial_facts(self):
        """Starting facts for study diagnosis."""
        self.explanation_log = []  # Clear log on reset
        yield Fact(action='diagnose_study_problem')
    
    # ==================== PROGRESSIVE QUESTIONING RULES ====================
    # These rules fire in sequence to gather information
    
    @Rule(
        Fact(action='diagnose_study_problem'),
        NOT(Fact(weak_area=W())),
        salience=100  # High priority - ask first
    )
    def ask_weak_area(self):
        """Ask what type of questions/content is most difficult."""
        self.needs_clarification = True
        self.clarification_question = """I'll help you identify your study weaknesses! 
        
**What area do you struggle with most?**

Please choose one:
- **mcq** - Multiple Choice Questions
- **essay** - Long-form written answers
- **math** - Calculations and problem-solving
- **theory** - Understanding concepts"""
        
        self.explanation_log.append("Starting diagnostic session - need to identify weak area")
    
    @Rule(
        Fact(weak_area='math'),
        NOT(Fact(math_subject=W())),
        salience=90
    )
    def ask_math_subject(self):
        """If math is the problem, which subject?"""
        self.needs_clarification = True
        self.clarification_question = """You mentioned **math** is challenging.

**Which subject's math problems are hardest?**

Please specify:
- **physics** - Physics calculations (V=IR, F=ma, etc.)
- **chemistry** - Chemistry calculations (mole concept, stoichiometry)
- **both** - Both are equally difficult
- **general** - Basic math skills overall"""
        
        self.collected_facts['weak_area'] = 'math'
        self.explanation_log.append("Student struggles with math-type questions - determining which subject")
    
    @Rule(
        Fact(weak_area='essay'),
        NOT(Fact(essay_difficulty=W())),
        salience=90
    )
    def ask_essay_difficulty(self):
        """If essays are the problem, is it memory or structure?"""
        self.needs_clarification = True
        self.clarification_question = """You mentioned **essay** questions are challenging.

**What makes essays difficult for you?**

Please choose:
- **memory** - Hard to remember definitions and processes
- **structure** - Know the facts but can't organize the answer
- **understanding** - Don't fully understand the concepts
- **time** - Run out of time during exams"""
        
        self.collected_facts['weak_area'] = 'essay'
        self.explanation_log.append("Student struggles with essay questions - determining root cause")
    
    @Rule(
        Fact(weak_area='mcq'),
        NOT(Fact(mcq_issue=W())),
        salience=90
    )
    def ask_mcq_issue(self):
        """If MCQs are the problem, what's the specific issue?"""
        self.needs_clarification = True
        self.clarification_question = """You mentioned **MCQ** (Multiple Choice) is challenging.

**What's your main issue with MCQs?**

Please choose:
- **speed** - Too slow to finish all questions
- **confusion** - Get confused by similar-looking answers
- **theory** - Don't understand the concepts well enough
- **tricks** - Fall for distractor/trick answers"""
        
        self.collected_facts['weak_area'] = 'mcq'
        self.explanation_log.append("Student struggles with MCQs - determining specific issue")
    
    @Rule(
        Fact(weak_area='theory'),
        NOT(Fact(theory_subject=W())),
        salience=90
    )
    def ask_theory_subject(self):
        """If theory is the problem, which subject?"""
        self.needs_clarification = True
        self.clarification_question = """You mentioned **theory/concepts** are challenging.

**Which subject's theory is hardest to understand?**

Please specify:
- **biology** - Biology concepts (cells, systems, processes)
- **physics** - Physics concepts (forces, energy, electricity)
- **chemistry** - Chemistry concepts (atoms, reactions, matter)
- **all** - All subjects are difficult to understand"""
        
        self.collected_facts['weak_area'] = 'theory'
        self.explanation_log.append("Student struggles with theoretical understanding - determining subject")
    
    # ==================== DIAGNOSIS RULES ====================
    # These rules fire when enough facts are collected
    
    @Rule(
        Fact(weak_area='math'),
        Fact(math_subject='physics')
    )
    def diagnose_physics_math(self):
        """Diagnosis: Weak in Physics calculations."""
        self.collected_facts['math_subject'] = 'physics'
        self.explanation_log.append("Identified specific weakness: Physics mathematical problem-solving")
        
        self.response = {
            'concept': 'Physics Calculation Weakness',
            'diagnosis': 'Difficulty with Physics calculations and formula application',
            'explanation': """**Identified Problem:** You struggle with Physics calculations.

**Why this happens:**
• Physics requires understanding both concepts AND math skills
• Common weak areas: V=IR (Ohm's Law), F=ma (Newton's 2nd Law), P=W/t (Power)
• Many students memorize formulas but struggle with unit conversion
• Word problems require translating scenarios into equations

**Root causes:**
1. Not enough practice with formula application
2. Weak foundation in O/L Mathematics
3. Confusion about when to use which formula
4. Difficulty with unit conversion (m/s, km/h, etc.)""",
            
            'recommendation': """**Action Plan:**

**Immediate Steps:**
1. **Formula mastery**: Create a formula sheet with all physics equations
2. **Practice daily**: Solve 5 physics calculation problems every day
3. **Unit conversion**: Master converting units (this is WHERE most marks are lost)
4. **Past papers**: Focus on calculation-heavy past paper questions

**Study Strategy:**
• Start with simple numerical substitution problems
• Progress to word problems that require formula selection
• Practice under timed conditions
• Review marking schemes to understand step-by-step solutions

**Resources:**
• Chapter-specific problem sets from your textbook
• Past paper calculation questions (categorized by topic)
• Khan Academy Physics (for concept review)""",
            
            'topic': 'Study Skills',
            'subtopic': 'Physics Mathematics',
            'confidence': 'High',
            'reasoning_chain': self.explanation_log.copy(),
            'examples': [
                "If you struggle with V=IR problems, practice 10 Ohm's Law questions",
                "For F=ma problems, draw force diagrams BEFORE calculating",
                "Always write units in your calculations to avoid conversion errors"
            ]
        }
        self.diagnosis_complete = True
    
    @Rule(
        Fact(weak_area='math'),
        Fact(math_subject='chemistry')
    )
    def diagnose_chemistry_math(self):
        """Diagnosis: Weak in Chemistry calculations."""
        self.collected_facts['math_subject'] = 'chemistry'
        self.explanation_log.append("Identified specific weakness: Chemistry mole concept and stoichiometry")
        
        self.response = {
            'concept': 'Chemistry Calculation Weakness',
            'diagnosis': 'Difficulty with Chemistry calculations (especially mole concept)',
            'explanation': """**Identified Problem:** You struggle with Chemistry calculations.

**Why this happens:**
• The mole concept is THE MOST IMPORTANT and difficult concept in O/L Chemistry
• Requires understanding: moles, mass, volume, concentration, and their relationships
• Many students get lost in multi-step stoichiometry problems
• Confusion between molar mass, molecular mass, and atomic mass

**Root causes:**
1. Mole concept not fully understood (what IS a mole?)
2. Difficulty with ratio-based calculations
3. Too many formulas to remember (n=m/M, n=V/24, n=C×V)
4. Weak skills in balancing chemical equations""",
            
            'recommendation': """**Action Plan:**

**MASTER THE MOLE FIRST:**
1. **Understand the concept**: 1 mole = 6.02 × 10²³ particles = 24dm³ of gas = molar mass in grams
2. **Triangle method**: Learn the n=m/M triangle (covers 80% of problems)
3. **Practice sequence**: 
   - Week 1: Simple mole-to-mass conversions
   - Week 2: Mole-to-volume (gas calculations)
   - Week 3: Concentration calculations
   - Week 4: Stoichiometry (multi-step)

**Study Strategy:**
• Write out the formula triangle on EVERY problem
• Always identify what you're looking for BEFORE calculating
• Practice balancing equations separately (10 per day)
• Review the periodic table to memorize common molar masses

**Critical Success Factor:**
If you master mole concept calculations, you'll score 40-50% higher on Chemistry exams!""",
            
            'topic': 'Study Skills',
            'subtopic': 'Chemistry Mathematics',
            'confidence': 'High',
            'reasoning_chain': self.explanation_log.copy(),
            'examples': [
                "Practice: Calculate moles when given mass (n = m/M)",
                "Practice: Find volume of gas from moles (V = n × 24)",
                "Practice: Stoichiometry with 2:1 and 1:3 ratios"
            ]
        }
        self.diagnosis_complete = True
    
    @Rule(
        Fact(weak_area='essay'),
        Fact(essay_difficulty='memory')
    )
    def diagnose_essay_memory(self):
        """Diagnosis: Memory/recall weakness for essays."""
        self.collected_facts['essay_difficulty'] = 'memory'
        self.explanation_log.append("Identified root cause: Difficulty with long-term recall for essay content")
        
        self.response = {
            'concept': 'Essay Writing - Memory Issue',
            'diagnosis': 'Difficulty remembering definitions and processes for long-form answers',
            'explanation': """**Identified Problem:** You know what to study but struggle to recall it during exams.

**Why this happens:**
• Biology and Chemistry require memorizing large amounts of information
• Passive reading doesn't create strong memory traces
• Information gets "mixed up" between similar topics
• Exam pressure causes memory blanks

**Root causes:**
1. Using passive study methods (re-reading, highlighting)
2. Not testing yourself regularly
3. Cramming instead of spaced repetition
4. Not organizing information into memorable patterns""",
            
            'recommendation': """**Action Plan - Active Recall Methods:**

**1. FLASHCARDS (Most Effective):**
• Create flashcards for all definitions and key processes
• Test yourself DAILY (not just before exams)
• Separate into "know well" and "struggling" piles
• Review struggling pile 3x more often

**2. MIND MAPS:**
• Create visual mind maps for each chapter
• Use colors, drawings, connections
• Recreate the map from memory weekly

**3. SELF-TESTING:**
• Close your book and write everything you remember
• Compare with actual content - fill gaps
• Repeat for topics you missed

**4. TEACH SOMEONE:**
• Explain concepts to a friend/family member
• If you can teach it, you truly understand it

**Study Schedule:**
• Daily: 30 min flashcard review
• Weekly: Recreate 2 mind maps from memory
• Before exams: Full self-tests on all chapters

**Critical Insight:**
Testing yourself is 300% more effective than re-reading!""",
            
            'topic': 'Study Skills',
            'subtopic': 'Memory and Recall',
            'confidence': 'High',
            'reasoning_chain': self.explanation_log.copy(),
            'examples': [
                "Flashcard: Front='What is photosynthesis?', Back=Full definition",
                "Mind map: Digestive system with all organs and their functions",
                "Self-test: Write out all parts of a cell from memory"
            ]
        }
        self.diagnosis_complete = True
    
    @Rule(
        Fact(weak_area='essay'),
        Fact(essay_difficulty='structure')
    )
    def diagnose_essay_structure(self):
        """Diagnosis: Essay structuring problem."""
        self.collected_facts['essay_difficulty'] = 'structure'
        self.explanation_log.append("Identified root cause: Knows facts but cannot organize coherent answers")
        
        self.response = {
            'concept': 'Essay Writing - Structure Issue',
            'diagnosis': 'Difficulty organizing knowledge into well-structured answers',
            'explanation': """**Identified Problem:** You know the content but lose marks on essay structure.

**Why this happens:**
• O/L Science essays have specific formats that examiners expect
• Keywords like "describe," "explain," and "compare" require different answer styles
• Students write everything they know instead of answering the question
• Lack of practice with marking schemes

**Root causes:**
1. Not identifying the command word in the question
2. Writing in paragraphs instead of clear points
3. Not following the mark allocation (e.g., 5 marks = 5 points)
4. Missing diagrams where required""",
            
            'recommendation': """**Action Plan - Master Essay Structure:**

**1. UNDERSTAND COMMAND WORDS:**
• **Describe**: State what you observe (appearance, characteristics)
• **Explain**: Give reasons WHY something happens (cause and effect)
• **Compare**: Show similarities AND differences
• **List/State**: Brief points (no explanation needed)

**2. POINT-BASED STRUCTURE:**
```
Question: "Explain photosynthesis" (5 marks)

Your answer should have 5 clear points:
1. Process in plants that makes food
2. Occurs in chloroplasts
3. Needs sunlight, water, CO₂
4. Produces glucose and oxygen
5. Chemical equation: 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂
```

**3. MARKING SCHEME PRACTICE:**
• Get past paper marking schemes
• Compare your answers line-by-line
• Identify patterns in model answers
• Note how marks are distributed

**4. ANSWER TEMPLATE:**
For any essay question:
- Read the question TWICE
- Underline the command word
- Count the marks (5 marks = 5 points needed)
- Number your points clearly
- Add a diagram if relevant

**Critical Success Factor:**
Practice with marking schemes transforms essay performance!""",
            
            'topic': 'Study Skills',
            'subtopic': 'Essay Structure',
            'confidence': 'High',
            'reasoning_chain': self.explanation_log.copy(),
            'examples': [
                "For 'Explain digestion (8 marks)', write 8 numbered points",
                "For 'Describe a cell', focus on structure, not function",
                "Always check: Does my answer match the command word?"
            ]
        }
        self.diagnosis_complete = True
    
    @Rule(
        Fact(weak_area='mcq'),
        Fact(mcq_issue='speed')
    )
    def diagnose_mcq_speed(self):
        """Diagnosis: Too slow with MCQs."""
        self.collected_facts['mcq_issue'] = 'speed'
        self.explanation_log.append("Identified specific issue: Time management on MCQ sections")
        
        self.response = {
            'concept': 'MCQ Speed Issue',
            'diagnosis': 'Taking too long to answer Multiple Choice Questions',
            'explanation': """**Identified Problem:** You run out of time on MCQ sections.

**Why this happens:**
• Reading every question multiple times
• Second-guessing correct answers
• Spending too long on difficult questions
• Not familiar enough with question patterns

**Root causes:**
1. Insufficient practice with timed conditions
2. Weak foundational knowledge (requires thinking instead of knowing)
3. Perfectionism (wanting to be 100% sure before moving on)
4. Not using elimination strategies""",
            
            'recommendation': """**Action Plan - Speed Up MCQs:**

**1. TIMING STRATEGY:**
• O/L Science MCQ: Usually 40 questions in 40 minutes
• Allocate: 30 seconds per easy question, 1 min per hard question
• First pass: Answer all questions you KNOW immediately (20-25 min)
• Second pass: Tackle difficult questions (15-20 min)
• Never spend more than 2 minutes on any single question

**2. ELIMINATION TECHNIQUE:**
• Read the question carefully ONCE
• Eliminate obviously wrong answers immediately
• Choose between remaining 2-3 options
• Trust your first instinct (changing answers usually makes it worse)

**3. BUILD SPEED THROUGH PRACTICE:**
• Week 1-2: Untimed practice (focus on accuracy)
• Week 3-4: Timed practice (40 questions in 45 min)
• Week 5+: Full speed (40 questions in 40 min)
• Track your time per question

**4. KNOW YOUR CONTENT COLD:**
• MCQ speed comes from instant recognition
• If you have to "figure out" every answer, you're too slow
• Master definitions and basic concepts first

**Critical Success Factor:**
Speed comes from knowledge + practice, not from rushing!""",
            
            'topic': 'Study Skills',
            'subtopic': 'MCQ Time Management',
            'confidence': 'High',
            'reasoning_chain': self.explanation_log.copy(),
            'examples': [
                "Practice: Set a timer for 40 min and complete a full past paper MCQ",
                "Strategy: Skip hard questions on first pass, mark them, return later",
                "Elimination: Cross out 2 wrong answers, guess between remaining 2"
            ]
        }
        self.diagnosis_complete = True
    
    # ==================== UNCERTAINTY HANDLING ====================
    
    @Rule(
        Fact(weak_area='math'),
        Fact(math_subject='both')
    )
    def diagnose_math_fundamental(self):
        """Uncertain diagnosis: Math weakness spans multiple subjects."""
        self.collected_facts['math_subject'] = 'both'
        self.explanation_log.append("Complex issue detected: Math struggles across Physics AND Chemistry")
        
        self.response = {
            'concept': 'Fundamental Math Weakness',
            'diagnosis': 'General mathematical foundation issue affecting multiple subjects',
            'explanation': """**Identified Problem:** You struggle with math in BOTH Physics and Chemistry.

**This suggests a deeper issue:**
This isn't just about science - it points to foundational O/L Mathematics weaknesses.

**Possible root causes:**
1. **Weak algebra skills** (rearranging equations, solving for x)
2. **Ratio and proportion confusion** (common in mole and force problems)
3. **Unit conversion difficulties** (m/s to km/h, g to kg, etc.)
4. **Difficulty translating word problems into equations**

**Why this matters:**
When the foundation is weak, EVERY science calculation becomes harder.
You're not just learning science - you're also trying to figure out the math at the same time.""",
            
            'recommendation': """**Two-Track Action Plan:**

**TRACK 1: Strengthen Math Foundation (30 min daily)**
1. Review O/L Math topics:
   - Algebraic manipulation
   - Ratios and proportions
   - Unit conversions
   - Scientific notation
2. Use Khan Academy or similar for targeted practice
3. Master calculator use (order of operations, memory functions)

**TRACK 2: Subject-Specific Practice (30 min daily)**
1. Start with ONE subject at a time
2. Break down complex problems into steps
3. Create a formula sheet with worked examples
4. Practice mixed problems from both subjects

**Weekly Schedule:**
- Mon/Wed/Fri: Physics math problems (30 min)
- Tue/Thu: Chemistry math problems (30 min)
- Sat: Mixed practice from both subjects (1 hour)
- Sun: Review O/L Math foundations (30 min)

**Critical Insight:**
Fixing the foundation takes time, but it's worth it! Students who strengthen their basic math see 30-40% improvement in both Physics and Chemistry within 2-3 months.

**Recommendation Priority:**
🔴 URGENT: Focus on basic math skills first
🟡 THEN: Subject-specific practice""",
            
            'topic': 'Study Skills',
            'subtopic': 'Mathematical Foundation',
            'confidence': 'Medium (Complex Issue)',
            'reasoning_chain': self.explanation_log.copy(),
            'examples': [
                "Math foundation: Practice rearranging formulas (if a=b/c, then b=?)",
                "Unit conversion: Convert 36 km/h to m/s (answer: 10 m/s)",
                "Mixed practice: Alternate between mole problems and force problems"
            ]
        }
        self.diagnosis_complete = True
    
    @Rule(
        Fact(weak_area='theory'),
        Fact(theory_subject='biology')
    )
    def diagnose_biology_theory(self):
        """Diagnosis: Difficulty understanding Biology concepts."""
        self.collected_facts['theory_subject'] = 'biology'
        self.explanation_log.append("Identified specific weakness: Biology conceptual understanding")
        
        self.response = {
            'concept': 'Biology Theory Understanding Issue',
            'diagnosis': 'Difficulty grasping Biology concepts and processes',
            'explanation': """**Identified Problem:** You struggle with understanding Biology theory.

**Why Biology theory is challenging:**
• Biology involves understanding LIVING SYSTEMS (complex and interconnected)
• Many invisible processes (cellular respiration, photosynthesis, digestion)
• Multiple levels: cell → tissue → organ → system → organism
• Cause-and-effect chains (e.g., enzyme deficiency → no digestion → malnutrition)
• Abstract concepts with unfamiliar terminology

**Common difficulties:**
1. Can't visualize microscopic processes (what REALLY happens in a cell?)
2. Too many technical terms (mitochondria, chloroplast, homeostasis...)
3. Processes seem arbitrary (WHY does photosynthesis need light?)
4. Difficulty seeing connections between topics""",
            
            'recommendation': """**Biology Mastery Strategy:**

**1. VISUAL LEARNING (CRITICAL):**
• Watch animated videos BEFORE reading:
  - CrashCourse Biology (entertaining + accurate)
  - Bozeman Science (detailed explanations)
  - Amoeba Sisters (simple + memorable)
• Draw diagrams while watching (reinforces memory)
• Use the "pause and predict" method (pause video, guess what happens next)

**2. UNDERSTAND THE "WHY" (Not Just "What"):**
Instead of memorizing:
```
❌ "Mitochondria is the powerhouse of the cell"
✅ "Cells need energy to function. Mitochondria breaks down glucose 
   using oxygen, releasing energy (ATP) that powers all cell activities.
   Without it, the cell would die."
```

**3. USE ANALOGIES:**
• Cell = Factory (nucleus = control room, ribosomes = assembly line)
• Blood circulation = Delivery service (oxygen = packages, heart = warehouse)
• Digestive system = Food processing factory
• Nervous system = Electrical wiring + computer network

**4. CONCEPT MAPPING:**
Create flowcharts showing cause → effect:
```
Photosynthesis Flow:
Sunlight → Chlorophyll absorbs → Energy splits H₂O → 
Hydrogen + CO₂ → Glucose formed → O₂ released
```

**5. ACTIVE READING TECHNIQUE:**
• Read ONE paragraph → Close book → Explain aloud → Check
• Ask questions: "Why? How? What if?"
• Relate to real life (Why do I breathe faster when running?)

**Study Schedule:**
• Week 1: Cell structure (foundation)
• Week 2: Tissues and organs
• Week 3: Systems (digestion, respiration, circulation)
• Week 4: Review and connect all topics

**Quick Win Topics** (Start here for confidence boost):
1. Animal tissues (easiest to understand)
2. Blood and circulation (relatable)
3. Photosynthesis (visual and logical)""",
            
            'topic': 'Study Skills',
            'subtopic': 'Biology Conceptual Understanding',
            'confidence': 'High',
            'reasoning_chain': self.explanation_log.copy(),
            'examples': [
                "Watch: 'Cell Biology in 5 Minutes' before reading textbook",
                "Analogy: Explain blood circulation like Amazon delivery service",
                "Draw: Create your own diagram of the digestive system with labels"
            ]
        }
        self.diagnosis_complete = True
    
    @Rule(
        Fact(weak_area='theory'),
        Fact(theory_subject='physics')
    )
    def diagnose_physics_theory(self):
        """Diagnosis: Difficulty understanding Physics concepts."""
        self.collected_facts['theory_subject'] = 'physics'
        self.explanation_log.append("Identified specific weakness: Physics conceptual understanding")
        
        self.response = {
            'concept': 'Physics Theory Understanding Issue',
            'diagnosis': 'Difficulty grasping Physics concepts and principles',
            'explanation': """**Identified Problem:** You struggle with understanding Physics theory.

**Why Physics theory is challenging:**
• Physics deals with INVISIBLE FORCES and energy (can't directly see them)
• Requires abstract thinking (force, acceleration, current, voltage)
• Mathematical concepts mixed with physical understanding
• Counter-intuitive principles (heavier and lighter objects fall at same speed?)
• Need to visualize things you can't see (electric current, magnetic fields)

**Common difficulties:**
1. Can't "see" forces acting on objects
2. Formulas seem disconnected from reality (What IS V=IR really saying?)
3. Difficulty applying concepts to real-world situations
4. Abstract terms with no concrete examples (what IS potential difference?)""",
            
            'recommendation': """**Physics Mastery Strategy:**

**1. VISUALIZATION IS KEY:**
• Watch demonstrations and experiments:
  - Khan Academy Physics (step-by-step)
  - Physics Girl (real-world examples)
  - Michel van Biezen (concept clarity)
• Draw diagrams for EVERY problem (force diagrams, circuit diagrams)
• Use simulations: PhET Interactive Simulations (FREE online)

**2. UNDERSTAND FORMULAS CONCEPTUALLY:**
Don't just memorize V=IR, understand it:
```
V = I × R means:
"Voltage is like water pressure pushing electrons through a wire.
Higher resistance = harder to push through = need more pressure (voltage)
More current flowing = more electrons moving per second"
```

**3. REAL-WORLD CONNECTIONS:**
• Force (F=ma): Car acceleration (heavier car needs more force to accelerate)
• Electricity: Your phone charger (voltage × current = power)
• Energy: Why you get tired climbing stairs (potential energy increase)
• Pressure: Why your ears pop on airplanes

**4. THE "PREDICT-OBSERVE-EXPLAIN" METHOD:**
Before learning a topic:
1. PREDICT: What do you think will happen?
2. OBSERVE: Watch experiment/demo
3. EXPLAIN: Why did that happen? (forced thinking)

**5. CONCEPT BEFORE CALCULATION:**
Before solving any problem:
• Draw the situation
• Identify what's happening physically
• Then apply formulas

**Study Sequence (Build Foundation First):**
• Week 1: Forces and motion (foundation)
• Week 2: Energy and work
• Week 3: Electricity basics
• Week 4: Magnetism and applications

**Pro Tips:**
• Use everyday examples (car brakes = friction, phone charger = electricity)
• Watch physics demos on YouTube DAILY (3-5 min videos)
• Explain concepts to someone else (forces you to understand deeply)""",
            
            'topic': 'Study Skills',
            'subtopic': 'Physics Conceptual Understanding',
            'confidence': 'High',
            'reasoning_chain': self.explanation_log.copy(),
            'examples': [
                "Watch: 'Force and Motion Explained Simply' before reading Newton's Laws",
                "Real-world: Explain why you feel pushed back when a car accelerates",
                "Simulation: Use PhET to build circuits and see how voltage/current relate"
            ]
        }
        self.diagnosis_complete = True
    
    @Rule(
        Fact(weak_area='theory'),
        Fact(theory_subject='chemistry')
    )
    def diagnose_chemistry_theory(self):
        """Diagnosis: Difficulty understanding Chemistry concepts."""
        self.collected_facts['theory_subject'] = 'chemistry'
        self.explanation_log.append("Identified specific weakness: Chemistry conceptual understanding")
        
        self.response = {
            'concept': 'Chemistry Theory Understanding Issue',
            'diagnosis': 'Difficulty grasping Chemistry concepts and reactions',
            'explanation': """**Identified Problem:** You struggle with understanding Chemistry theory.

**Why Chemistry theory is challenging:**
• Chemistry happens at ATOMIC LEVEL (can't see atoms/molecules)
• Requires thinking at multiple scales (atoms → molecules → reactions → observable changes)
• Abstract concepts (bonding, valency, electron transfer)
• Need to visualize 3D structures from 2D diagrams
• Balancing equations seems like magic (where do those numbers come from?)

**Common difficulties:**
1. Can't visualize atoms and molecules
2. Don't understand WHY reactions happen
3. Ionic vs covalent bonding seems arbitrary
4. Periodic table is overwhelming
5. Can't connect micro-level (atoms) with macro-level (test tube reactions)""",
            
            'recommendation': """**Chemistry Mastery Strategy:**

**1. MASTER THE ATOM FIRST (Foundation):**
• Everything in chemistry is about atoms wanting to be stable
• Atoms form bonds to complete their outer shell (octet rule)
• This explains 90% of chemistry!

**2. VISUAL LEARNING:**
• Watch animations of atoms bonding:
  - Tyler DeWitt (makes chemistry FUN and simple)
  - Professor Dave Explains (clear and detailed)
  - CrashCourse Chemistry
• Use molecular model kits (or online simulators)
• Draw electron dot diagrams for everything

**3. UNDERSTAND THE "WHY":**
Instead of memorizing:
```
❌ "Sodium chloride is ionic"
✅ "Sodium has 1 outer electron (wants to lose it)
   Chlorine needs 1 electron (wants to gain it)
   Sodium GIVES electron to Chlorine → Both become stable
   Opposite charges attract → Ionic bond formed"
```

**4. THE STORY METHOD:**
Treat every reaction like a story:
• Characters: Atoms/molecules
• Problem: They're unstable
• Solution: Bond/react
• Outcome: New stable substances formed

Example: Rusting of iron is a story of iron atoms meeting oxygen and combining to form iron oxide because both become more stable together.

**5. CONNECT MICRO TO MACRO:**
Always link atomic view to real observations:
• Atoms bonding → Heat released (observable)
• Electrons transferring → Electricity flows (measurable)
• Breaking bonds → Color change in test tube (visible)

**Study Sequence:**
• Week 1: Atomic structure and periodic table
• Week 2: Bonding (ionic and covalent)
• Week 3: Chemical reactions and equations
• Week 4: Specific reactions (acids/bases, metals)

**Quick Win Strategy:**
1. Master atomic structure FIRST (everything builds on this)
2. Learn the first 20 elements (foundation for understanding reactions)
3. Practice drawing electron configurations daily
4. Watch ONE 5-minute chemistry animation daily

**Pro Tips:**
• Use mnemonics for periodic table (Happy Henry Lives Beside...)
• Create a "reaction library" with diagrams
• Explain reactions aloud (forces understanding)
• Connect to everyday life (cooking = chemical reactions!)""",
            
            'topic': 'Study Skills',
            'subtopic': 'Chemistry Conceptual Understanding',
            'confidence': 'High',
            'reasoning_chain': self.explanation_log.copy(),
            'examples': [
                "Watch: 'Why Do Atoms Bond?' before studying chemical bonding",
                "Visual: Draw electron dot diagrams for water (H₂O) formation",
                "Story: Explain rusting as 'iron atoms finding oxygen partners'"
            ]
        }
        self.diagnosis_complete = True
    
    @Rule(
        Fact(weak_area='theory'),
        Fact(theory_subject='all')
    )
    def diagnose_general_understanding(self):
        """Uncertain diagnosis: Struggles with theory across all subjects."""
        self.collected_facts['theory_subject'] = 'all'
        self.explanation_log.append("Complex issue: Difficulty understanding concepts across ALL science subjects")
        
        self.response = {
            'concept': 'General Conceptual Understanding Issue',
            'diagnosis': 'Difficulty grasping scientific concepts across multiple subjects',
            'explanation': """**Identified Problem:** You struggle with understanding theory in ALL science subjects.

**This suggests multiple possible causes:**

**Possible Issues:**
1. **Learning style mismatch**: Your teachers might explain in ways that don't match how you learn
2. **Language barrier**: Scientific terminology is confusing
3. **Abstract thinking difficulty**: Science concepts are often invisible (atoms, forces, energy)
4. **Passive learning**: Reading textbooks without active engagement
5. **Foundation gaps**: Missing key concepts from earlier grades

**Why this is common:**
Many students struggle because science requires:
- Visualizing invisible processes
- Understanding cause-and-effect chains
- Connecting multiple concepts together
- Thinking at microscopic and macroscopic levels simultaneously""",
            
            'recommendation': """**Multi-Modal Learning Strategy:**

**1. VISUAL LEARNING (Most Important):**
• Watch YouTube videos for EVERY topic before reading textbook
• Recommended channels:
  - CrashCourse (Biology, Chemistry, Physics)
  - Khan Academy
  - Bozeman Science
• Draw diagrams while watching
• Use animations to understand invisible processes

**2. ACTIVE READING TECHNIQUE:**
Instead of passive reading:
```
❌ Don't: Read chapter → highlight → move on
✅ Do: Read paragraph → Close book → Explain it aloud → Check if correct
```

**3. CONCEPT MAPPING:**
• For each topic, create a "cause → effect" flowchart
• Example: Photosynthesis flowchart:
  Sunlight → Chlorophyll absorbs light → Energy splits water →
  Hydrogen + CO₂ → Glucose formed → Oxygen released

**4. TEACH-BACK METHOD:**
• After studying, teach the concept to someone
• If you can't explain it simply, you don't understand it yet
• Use analogies from everyday life

**5. QUESTION-BASED LEARNING:**
• Don't just read about cells - ask:
  - WHY do cells have membranes?
  - HOW does the nucleus control the cell?
  - WHAT would happen if mitochondria stopped working?

**Long-term Strategy:**
This is NOT a quick fix. Build understanding gradually:
- Week 1-2: Focus on ONE subject (choose your favorite)
- Week 3-4: Add second subject
- Week 5+: All subjects with the same method
- Track topics you've mastered vs. still struggling

**Get Help:**
Consider finding a tutor or study group. Sometimes peer explanation works better than teacher explanation!""",
            
            'topic': 'Study Skills',
            'subtopic': 'Conceptual Understanding',
            'confidence': 'Medium (Multiple Possible Causes)',
            'reasoning_chain': self.explanation_log.copy(),
            'examples': [
                "Visual: Watch 'Photosynthesis in 3 Minutes' video before reading textbook",
                "Active: Explain the water cycle to your parent/sibling",
                "Analogy: Cell is like a factory (nucleus = office, mitochondria = power plant)"
            ]
        }
        self.diagnosis_complete = True
    
    # ==================== STRESS MANAGEMENT & MENTAL HEALTH RULES ====================
    
    @Rule(
        OR(
            Fact(user_query=MATCH.query & L(lambda x: 'stress' in x or 'anxious' in x or 'anxiety' in x or 'nervous' in x or 'panic' in x)),
            Fact(user_query=MATCH.query & L(lambda x: 'exam anxiety' in x or 'test anxiety' in x or 'exam stress' in x))
        )
    )
    def handle_exam_anxiety(self, query):
        """Handle exam anxiety and stress."""
        self.response = {
            'concept': '🧘 Exam Anxiety & Stress Management',
            'diagnosis': 'You're experiencing exam-related anxiety - this is VERY common!',
            'explanation': """**Why Exam Anxiety Happens:**

• **Physical**: Your body enters "fight or flight" mode (racing heart, sweaty palms, mind blanks)
• **Psychological**: Fear of failure, pressure from parents/self, comparing to others
• **Situational**: Time pressure, difficult questions, unfamiliar exam environment

**This affects 60-70% of students** - you're NOT alone!

**What's happening in your brain:**
- Amygdala (fear center) is overactive
- Prefrontal cortex (thinking center) shuts down
- Stress hormones (cortisol) block memory retrieval
- This is why you "know it" at home but "forget" in exam!""",
            
            'recommendation': """**Immediate Techniques (Use These IN the Exam):**

**1. 4-7-8 Breathing (Calms nerves in 30 seconds):**
```
Breathe IN for 4 seconds
HOLD for 7 seconds  
Breathe OUT for 8 seconds
Repeat 3 times
```

**2. The "5-4-3-2-1" Grounding Technique:**
- Name 5 things you can SEE
- Name 4 things you can TOUCH
- Name 3 things you can HEAR
- Name 2 things you can SMELL
- Name 1 thing you can TASTE
(Brings you back to present moment)

**3. Positive Self-Talk:**
❌ "I'm going to fail"
✅ "I've prepared well. I can do this one question at a time."

**4. Progressive Muscle Relaxation:**
- Tense shoulders for 5 seconds, then release
- Tense fists for 5 seconds, then release
- Repeat until calm

**Long-Term Strategies (Build These Habits):**

**Before Exam Day:**
1. **Practice Exams** in exam conditions (timed, no notes)
   - Reduces fear of the unknown
   - Your brain learns "exams aren't dangerous"

2. **Visualization** (5 minutes daily):
   - Close eyes, imagine walking into exam room calmly
   - See yourself reading questions confidently
   - Feel yourself writing answers smoothly
   - This "tricks" your brain into thinking it's familiar

3. **Physical Exercise** (30 min, 3x/week):
   - Reduces cortisol (stress hormone)
   - Releases endorphins (feel-good chemicals)
   - Try: jogging, dancing, sports, yoga

4. **Sleep Hygiene**:
   - 7-8 hours per night
   - No screens 1 hour before bed
   - Consistent sleep schedule

**On Exam Day:**
- Eat protein breakfast (eggs, nuts, milk)
- Arrive 20 minutes early (avoid rushing)
- Avoid "last-minute cramming" (increases panic)
- Don't talk to anxious classmates before exam

**Emergency Help:**
If anxiety is severe (affecting daily life, panic attacks), PLEASE talk to:
- School counselor
- Parents
- Doctor (anxiety is treatable!)

**Remember:** Anxiety doesn't mean you're weak or unprepared. It means you CARE about doing well. That's a good thing! Now let's channel that energy positively.""",
            
            'examples': [
                "Before exam: Visualize success for 5 minutes while listening to calm music",
                "During exam: Feel anxiety rising? Do 4-7-8 breathing before reading next question",
                "Night before: No studying after 8pm. Watch something light, sleep by 10pm",
                "Panic moment: Use 5-4-3-2-1 grounding to return to present"
            ],
            
            'resources': [
                "Headspace app: Guided meditation for exam stress (free student version)",
                "YouTube: 'Exam Anxiety Relief' guided meditations",
                "Talk to school counselor - they've helped 100s of students with this!"
            ],
            
            'topic': 'Mental Health',
            'subtopic': 'Exam Anxiety',
            'confidence': 'High'
        }
        self.diagnosis_complete = True
    
    @Rule(
        Fact(user_query=MATCH.query & L(lambda x: 'overwhelm' in x or 'too much' in x or 'can\'t handle' in x or 'drowning' in x))
    )
    def handle_feeling_overwhelmed(self, query):
        """Handle feeling overwhelmed with studies."""
        self.response = {
            'concept': '🌊 Managing Study Overwhelm',
            'diagnosis': 'You're experiencing cognitive overload - too much to do, too little time!',
            'explanation': """**Why You Feel Overwhelmed:**

• **Too many subjects** to study simultaneously
• **No clear priorities** (everything feels urgent)
• **Perfectionism** (trying to learn EVERYTHING perfectly)
• **Comparison** (others seem to have it together)
• **Sleep deprivation** (tired brain can't process information)

**The Overwhelm Cycle:**
```
Too much to do → Feel anxious → Procrastinate → 
Fall further behind → More anxiety → More overwhelm
```

**Good news:** This is fixable with the right strategy!""",
            
            'recommendation': """**STOP THE CYCLE - Emergency Protocol:**

**STEP 1: Brain Dump (10 minutes)**
Write down EVERYTHING you need to do:
- All subjects
- All chapters
- All assignments
- All exams

**STEP 2: The 80/20 Rule**
Ask: "Which 20% of topics give me 80% of marks?"
- Focus on HIGH-WEIGHTAGE topics first
- Let go of perfectionism (you don't need 100%)

**STEP 3: Break It Down**
❌ "Study Biology" (overwhelming!)
✅ "Read 5 pages on photosynthesis" (doable!)

**STEP 4: The MIT Method (Most Important Task)**
Each morning, identify your ONE most important task
- Do it FIRST (when brain is fresh)
- Everything else is bonus

**STEP 5: Time Blocking**
```
8am-10am: Biology (2 chapters)
10am-10:30am: BREAK (walk outside!)
10:30am-12pm: Math (practice 10 problems)
12pm-1pm: Lunch + rest
1pm-3pm: Chemistry (summary notes)
3pm-3:30pm: BREAK
3pm-5pm: Revision of today's topics
```

**STEP 6: The 2-Minute Rule**
If task takes <2 minutes, do it NOW
- Prevents task pile-up

**STEP 7: Say NO**
- Skip that movie with friends (temporarily)
- Reduce social media to 15 min/day
- Focus season is SHORT (few months)

**Mental Health Tips:**

1. **Daily Non-Negotiables:**
   - 7 hours sleep (MINIMUM)
   - 3 meals (brain needs fuel)
   - 20 minutes outdoor time

2. **Weekly Reset:**
   - One day (Sunday?) for rest & hobbies
   - Prevents burnout

3. **Ask for Help:**
   - Parents: "Can you handle chores this month?"
   - Teachers: "Can you explain this topic again?"
   - Friends: "Let's study together"

**Remember:** You can't pour from an empty cup. Rest is PRODUCTIVE!""",
            
            'examples': [
                "Morning routine: Write 3 MIT (Most Important Tasks) on sticky note",
                "Feeling overwhelmed? Go outside for 10-minute walk (resets brain)",
                "Sunday evening: Plan next week's study blocks (reduces decision fatigue)",
                "Before bed: Write tomorrow's top 3 tasks (sleep better knowing plan exists)"
            ],
            
            'resources': [
                "Notion/Google Sheets: Create study tracker to visualize progress",
                "Forest app: Blocks phone distractions during study sessions",
                "Pomodoro Technique: 25-min focus, 5-min break (prevents overwhelm)"
            ],
            
            'topic': 'Mental Health',
            'subtopic': 'Overwhelm Management'
        }
        self.diagnosis_complete = True
    
    @Rule(
        Fact(user_query=MATCH.query & L(lambda x: 'sleep' in x and ('can\'t' in x or 'problem' in x or 'insomnia' in x or 'difficult' in x)))
    )
    def handle_sleep_problems(self, query):
        """Handle sleep problems during exam period."""
        self.response = {
            'concept': '😴 Sleep Problems & Solutions',
            'diagnosis': 'Poor sleep is sabotaging your study effectiveness!',
            'explanation': """**Why Sleep Matters for Students:**

**One night of bad sleep causes:**
- 40% reduction in memory formation
- 30% slower problem-solving
- Increased anxiety and irritability
- Poor focus and concentration

**Sleep deprivation** is like being drunk while studying - waste of time!

**Why Students Can't Sleep:**
• **Racing thoughts** (worrying about exams)
• **Blue light** from phones/laptops (suppresses melatonin)
• **Late-night caffeine** (coffee after 2pm affects sleep)
• **Irregular schedule** (confuses body clock)
• **Study in bed** (brain associates bed with stress, not sleep)""",
            
            'recommendation': """**The Perfect Sleep Protocol:**

**2-3 Weeks Before Exams:**

**6:00 PM - Dinner**
- Light meal (heavy food disrupts sleep)
- No caffeine after 2pm

**7:00 PM - Study Session**
- Bright lights, desk (not bed!)
- Hardest subjects (brain still fresh)

**9:00 PM - Wind Down Begins**
- ✅ Light review/flashcards
- ❌ New difficult topics (creates anxiety)

**10:00 PM - Digital Sunset**
- Put phone away (use alarm clock, not phone)
- Blue light blockers if must use device
- No social media (prevents FOMO anxiety)

**10:30 PM - Bedtime Routine**

**Option A - The 4-7-8 Method:**
```
Lie down in dark room
Breathe in for 4 seconds
Hold for 7 seconds
Breathe out for 8 seconds
Repeat 10 times (you'll fall asleep!)
```

**Option B - Progressive Muscle Relaxation:**
```
Tense toes for 5 sec → Release
Tense calves for 5 sec → Release
Tense thighs for 5 sec → Release
Continue up body to head
```

**Option C - Mental Imagery:**
```
Imagine peaceful place (beach, forest)
Engage all senses (What do you see, hear, smell?)
Stay in that imagery
```

**11:00 PM - ASLEEP**
- Dark room (blackout curtains)
- Cool temperature (18-20°C ideal)
- No clock visible (checking time creates anxiety)

**7:00 AM - WAKE UP**
- Same time daily (even weekends!)
- Sunlight exposure immediately (resets body clock)
- Cold water splash on face

**Emergency: Can't Sleep?**

If lying awake >20 minutes:
1. Get UP (don't stay in bed frustrated)
2. Do BORING activity (read textbook, fold clothes)
3. Return to bed when sleepy
4. Repeat if needed

**What NOT to Do:**
❌ Study until 2am (you'll forget everything)
❌ Scroll phone in bed (reactivates brain)
❌ Take naps >30 minutes (ruins night sleep)
❌ Drink energy drinks (anxiety + poor sleep)

**Quick Wins:**
✅ Magnesium supplement (200mg before bed - natural relaxant)
✅ Chamomile tea (calming effect)
✅ Write "worry list" before bed (empties racing mind)
✅ Same sleep/wake time 7 days/week""",
            
            'examples': [
                "Racing thoughts? Keep notebook by bed. Write worries down, deal with them tomorrow.",
                "Can't fall asleep? Try 'body scan meditation' - YouTube has 10-minute versions",
                "Exam tomorrow? Still sleep 7 hours! Sleep = better performance than 2 more hours of study",
                "Sunday rule: Same wake-up time as weekdays (consistency is KEY)"
            ],
            
            'topic': 'Mental Health',
            'subtopic': 'Sleep Hygiene'
        }
        self.diagnosis_complete = True
    
    # ==================== PROCRASTINATION & MOTIVATION RULES ====================
    
    @Rule(
        Fact(user_query=MATCH.query & L(lambda x: 'procrastinat' in x or 'delay' in x or 'distract' in x or 'avoid study' in x or 'can\'t start' in x))
    )
    def handle_procrastination(self, query):
        """Handle procrastination issues."""
        self.response = {
            'concept': '⏰ Overcoming Procrastination',
            'diagnosis': 'You're avoiding studying due to psychological barriers!',
            'explanation': """**Why We Procrastinate:**

**It's NOT about laziness!** It's about:

1. **Task Aversion** - Study feels painful/boring
2. **Perfectionism** - "If I can't do it perfectly, why start?"
3. **Overwhelm** - Task seems too big
4. **Instant Gratification** - Phone/games = instant pleasure, studying = delayed reward
5. **Fear of Failure** - "What if I study hard and still fail?"

**The Procrastination Equation:**
```
Low Expectancy (won't work anyway) +
Low Value (not important to me) +
High Impulsiveness (want pleasure NOW) +
Delay (exam far away)
= PROCRASTINATION!
```

**Your Brain's Trick:**
Present You: "I'll study tomorrow" (feels good now!)
Future You: "Why did I do this?!" (pain later)""",
            
            'recommendation': """**Anti-Procrastination System:**

**STRATEGY 1: The 2-Minute Rule**
"I'll just study for 2 minutes"
- Trick your brain (starting is hardest part)
- After 2 minutes, usually continue
- Lower the barrier to START

**STRATEGY 2: Implementation Intentions**
❌ "I'll study tomorrow"
✅ "Tomorrow at 9am, after breakfast, I'll sit at desk and open Biology textbook to page 45"
- Specific = more likely to happen

**STRATEGY 3: Temptation Bundling**
Pair studying with something pleasant:
- Favorite tea/coffee while studying
- Instrumental music you love
- Study in pleasant location (library, café)

**STRATEGY 4: The Procrastination Equation Fix**

**Increase Expectancy:**
- Remember past successes
- "I CAN learn this if I try"

**Increase Value:**
- Connect to goals: "This biology knowledge helps me become a doctor"
- Visualize success: "Imagine feeling proud when results come"

**Decrease Impulsiveness:**
- Remove phone from room
- Use website blockers (Cold Turkey, Freedom)
- Study buddy (accountability)

**Decrease Delay:**
- Make deadlines REAL: "If I don't study today, I'll have 20 chapters tomorrow"

**STRATEGY 5: The Pomodoro Technique**
```
25 minutes FOCUSED study
5 minutes BREAK (stretch, water, snack)
Repeat 4 times
Then take 30-minute break
```

**Why it works:**
- Breaks seem doable
- Focus is easier (just 25 min!)
- Prevents burnout

**STRATEGY 6: Environment Design**
**Create "Cues" for studying:**
- Specific desk = study only
- Specific playlist = focus time
- Specific drink = study mode

**Remove "Cues" for distraction:**
- Phone in another room
- TV unplugged
- Social media logged out

**STRATEGY 7: Pre-commitment Devices**
- Tell friend: "I'll send you summary notes by 5pm"
- Set appointment: "Study group at 2pm (can't skip!)"
- Public declaration: Post study goals on social media

**The 5-Second Rule (Mel Robbins):**
When you feel urge to procrastinate:
Count backwards: 5-4-3-2-1-GO!
Physically move toward study desk
Don't give brain time to make excuses

**Remember:** You don't need motivation to start. You need to start to GET motivation!""",
            
            'examples': [
                "Can't start? Say 'Just 2 minutes on first paragraph' - usually leads to 30 minutes",
                "Phone temptation? Put it in kitchen with note: 'I can get this after 25-min Pomodoro'",
                "Study buddy system: Daily 8am message 'Starting now!' (accountability)",
                "Reward system: After 2 hours study → 20 min gaming (AFTER, not before!)"
            ],
            
            'resources': [
                "Forest app: Plant virtual trees during study (dies if you leave app)",
                "Cold Turkey: Blocks distracting websites for set time",
                "Focusmate: Video study buddy (stranger studying with you, no talking)"
            ],
            
            'topic': 'Psychology',
            'subtopic': 'Procrastination'
        }
        self.diagnosis_complete = True
    
    @Rule(
        Fact(user_query=MATCH.query & L(lambda x: 'motivat' in x or 'not interested' in x or 'lost interest' in x or 'don\'t care' in x or 'give up' in x))
    )
    def handle_motivation_loss(self, query):
        """Handle lost motivation."""
        self.response = {
            'concept': '💪 Rebuilding Study Motivation',
            'diagnosis': 'You've lost your "why" - let's reconnect you to your goals!',
            'explanation': """**Why Motivation Fades:**

1. **Disconnected from Goals** - Forgot WHY you're studying
2. **Past Failures** - Previous bad results killed confidence
3. **Comparison** - Everyone seems smarter
4. **Burnout** - Studied too hard without breaks
5. **No Visible Progress** - Feels like nothing's improving

**Types of Motivation:**

**Extrinsic** (External rewards):
- Parents' approval ❌ (fades quickly)
- Good marks ❌ (only lasts until result day)
- Avoiding punishment ❌ (fear-based, unsustainable)

**Intrinsic** (Internal drive):
- Genuine curiosity ✅
- Personal growth ✅
- Achieving your dreams ✅

**We need to rebuild INTRINSIC motivation!**""",
            
            'recommendation': """**Motivation Rebuilding Protocol:**

**PHASE 1: Reconnect With Your "Why"**

**Exercise: Future Self Visualization (10 minutes)**
Close your eyes. Imagine:
- Where do you want to be in 5 years?
- What job/career?
- How do you want to feel about yourself?
- What kind of life do you want?

Now ask: "Does studying help me get there?"

**Write this down:**
```
I'm studying because...
[Your personal reason - NOT your parents' reason!]

Example: "I want to become a doctor to help people"
Example: "I want to prove to myself I can do hard things"
Example: "I want financial independence"
```

**PHASE 2: Set SMART Goals**

❌ "I want good results"
✅ "I want to score B grade or higher in Biology by improving MCQ score from 40% to 70% in 2 months"

**SMART = Specific, Measurable, Achievable, Relevant, Time-bound**

**PHASE 3: Create "Motivation Anchors"**

**Visual Reminders:**
- Dream university poster on wall
- Photo of role model (doctor, scientist, whoever you admire)
- Written goal on desk: "I'm working toward [GOAL]"

**Daily Affirmations** (say aloud each morning):
- "I am capable of learning anything"
- "Every day I study, I'm closer to my goal"
- "Temporary effort = permanent results"

**PHASE 4: Track Progress**

**Create Visible Progress:**
- Checklist of chapters (crossing off feels GOOD!)
- Graph of practice test scores (see improvement!)
- "Days studied" calendar (don't break the chain!)

**Why this works:**
- Brain loves seeing progress
- Small wins build momentum
- Visible improvement = natural motivation

**PHASE 5: Build Study Momentum**

**Start Small (Tiny Habits Method):**
Week 1: Study 15 min/day
Week 2: Study 30 min/day
Week 3: Study 1 hour/day
Week 4: Study 2 hours/day

**Don't go 0 to 100!** Build gradually.

**PHASE 6: Find Your Study "Why" Daily**

**Before each study session, ask:**
"How does THIS topic help my future?"

Example: "Learning photosynthesis → understanding biology → becoming better at science → medical school → doctor career"

**PHASE 7: Celebrate Small Wins**

After completing study goal:
- ✅ Favorite snack
- ✅ 20 min gaming
- ✅ Episode of favorite show
- ✅ Chat with friend

**Train brain:** Study = Reward!

**PHASE 8: Study Buddy / Accountability Partner**

Find someone with similar goals:
- Daily check-ins
- Share progress
- Encourage each other
- Healthy competition

**When Motivation Fails (Emergency Kit):**

**1. Motivation Follows Action**
- Don't wait to "feel motivated"
- Start studying → Motivation appears!

**2. The 5-Minute Rule**
- Study for just 5 minutes
- Usually leads to more

**3. Watch Motivational Content**
- YouTube: Study motivation videos
- Success stories of students who struggled
- Remember: They were once where you are!

**4. Remember Your Future Self**
- Future You will thank Present You
- Or Future You will regret Present You's choices
- Which do you want?

**Mindset Shifts:**

❌ "I have to study" → ✅ "I GET to study"
❌ "This is hard" → ✅ "This is making me stronger"
❌ "I'm not smart" → ✅ "I'm not smart YET"

**Remember:** Motivation is like a muscle. The more you use it, the stronger it gets!""",
            
            'examples': [
                "Morning routine: Read your written goal aloud before breakfast",
                "Feeling unmotivated? Watch 5-min success story video, then immediate start",
                "Sunday reset: Review week's progress, celebrate wins, plan next week",
                "Accountability: Daily 8pm WhatsApp message to study buddy: 'Studied X hours today'"
            ],
            
            'resources': [
                "YouTube: Thomas Frank (study tips from successful student)",
                "YouTube: Ali Abdaal (ex-doctor, study strategies)",
                "Book: 'Atomic Habits' by James Clear (habit building)"
            ],
            
            'topic': 'Psychology',
            'subtopic': 'Motivation'
        }
        self.diagnosis_complete = True
    
    # ==================== TIME MANAGEMENT & PRODUCTIVITY RULES ====================
    
    @Rule(
        Fact(user_query=MATCH.query & L(lambda x: 'time management' in x or 'manage time' in x or 'schedule' in x or 'plan' in x or 'organize' in x))
    )
    def handle_time_management(self, query):
        """Handle time management requests."""
        self.response = {
            'concept': '⏰ Effective Time Management for Students',
            'diagnosis': 'You need a structured study system!',
            'explanation': """**Why Time Management Matters:**

**Without system:**
- Study randomly → Forget what you studied
- Cram before exam → High stress, poor retention
- Waste time deciding "what to study now?"

**With system:**
- Clear plan → Less stress
- Spaced repetition → Better memory
- Balanced coverage → All topics covered

**The biggest time wasters:**
1. Social media (avg 3 hours/day!)
2. Perfectionism (spending 2 hours on one question)
3. Multitasking (actually SLOWER than focused work)
4. No priorities (studying easy topics, avoiding hard ones)""",
            
            'recommendation': """**Complete Time Management System:**

**STEP 1: Calculate Available Time**

Example student:
```
24 hours/day
- 8 hours sleep
- 6 hours school
- 2 hours meals/hygiene
- 1 hour family time
= 7 hours available for study
```

**Realistic study time: 4-5 hours/day** (includes breaks)

**STEP 2: Priority Matrix**

**Urgent & Important** → DO NOW
- Exam tomorrow
- Assignment due today

**Important, Not Urgent** → SCHEDULE
- Regular study
- Long-term preparation
← **SPEND 80% OF TIME HERE!**

**Urgent, Not Important** → DELEGATE/MINIMIZE
- Friend wants help with homework
- Social media message

**Not Urgent, Not Important** → ELIMINATE
- Scrolling Instagram
- Watching random YouTube

**STEP 3: Create Weekly Study Schedule**

**Example Schedule (Adjust to your needs):**

**Monday-Friday:**
```
6:30 AM - Wake up
7:00 AM - School preparation
1:30 PM - Return from school
2:00 PM - Lunch + Rest
3:00 PM - Study Block 1 (2 hours)
  - Subject 1 (1 hour)
  - Break (15 min)
  - Subject 2 (45 min)
5:00 PM - Break/Exercise (30 min)
5:30 PM - Study Block 2 (2 hours)
  - Subject 3 (1 hour)
  - Break (15 min)
  - Practice/Revision (45 min)
7:30 PM - Dinner
8:30 PM - Study Block 3 (1.5 hours)
  - Weaker subject (1 hour)
  - Review today's topics (30 min)
10:00 PM - Wind down
10:30 PM - Sleep
```

**Saturday:**
- Morning: 3-hour deep study session
- Afternoon: Practice tests
- Evening: Free time (social life!)

**Sunday:**
- Light revision only
- Plan next week
- REST (crucial!)

**STEP 4: Time Blocking Technique**

**Block similar tasks together:**
- All Math problems in one block
- All note-making in one block
- All memorization in one block

**Why it works:**
- Reduces context switching
- Maintains focus
- More efficient

**STEP 5: The Pomodoro Method**
```
25 min focused study (NO distractions)
5 min break (stretch, water, snack)

After 4 Pomodoros:
30 min break (walk, relaxation)
```

**STEP 6: Subject Rotation System**

**Daily rotation:**
Monday: Biology, Chemistry, Math
Tuesday: Physics, Biology, English
Wednesday: Chemistry, Math, Biology
...

**Why it works:**
- Prevents boredom
- Spaced repetition (best for memory!)
- All subjects get attention

**STEP 7: Energy Management**

**High Energy Times** (morning):
- Difficult subjects
- New topics
- Problem-solving

**Medium Energy** (afternoon):
- Revision
- Practice questions
- Note-making

**Low Energy** (night):
- Light revision
- Flashcards
- Reading

**STEP 8: Time Tracking**

Track for one week:
- Where does time actually go?
- Phone usage? (Check screen time!)
- Actual study time vs. perceived?

**Eye-opener:** Most students think they study 5 hours, actually study 2 hours (distractions!)

**STEP 9: Buffer Time**

**Always add 25% buffer:**
- Think task takes 1 hour? Schedule 1.25 hours
- Things take longer than expected
- Prevents schedule collapse

**STEP 10: Time Management Tools**

**Digital:**
- Google Calendar (color-code subjects)
- Forest app (focus sessions)
- Notion (task management)

**Analog:**
- Physical planner (some prefer this!)
- Sticky notes for daily MITs
- Wall calendar for visual overview

**Common Time Management Mistakes:**

❌ **Mistake 1:** Planning every minute (too rigid, leads to failure)
✅ **Fix:** Plan blocks, be flexible within blocks

❌ **Mistake 2:** No breaks (burnout!)
✅ **Fix:** Mandatory 10 min break/hour

❌ **Mistake 3:** Studying late night (poor sleep, poor memory)
✅ **Fix:** Early morning study (brain is fresh!)

❌ **Mistake 4:** Same schedule every day (boredom)
✅ **Fix:** Rotate subjects, vary study locations

**Emergency: Behind on Schedule?**

**Triage System:**
1. Identify HIGH-WEIGHTAGE topics only
2. Focus on understanding, not perfection
3. Use study guides/summaries (save time)
4. Skip low-weightage topics (temporary!)

**Remember:** Time management isn't about doing MORE. It's about doing the RIGHT things EFFICIENTLY!""",
            
            'examples': [
                "Sunday evening: Create next week's study blocks in Google Calendar",
                "Start day: Write top 3 MITs (Most Important Tasks) on sticky note",
                "Track time: Use Forest app for all study sessions this week",
                "Energy optimization: Chemistry (hardest for me) at 8am when brain is fresh"
            ],
            
            'resources': [
                "Notion: Pre-made student dashboard templates (FREE)",
                "Google Calendar: Color-code subjects (Biology=green, Physics=blue...)",
                "RescueTime: Tracks where your computer time goes (eye-opening!)"
            ],
            
            'topic': 'Productivity',
            'subtopic': 'Time Management'
        }
        self.diagnosis_complete = True
    
    # ==================== MEMORY & LEARNING TECHNIQUES RULES ====================
    
    @Rule(
        Fact(user_query=MATCH.query & L(lambda x: 'memory' in x or 'remember' in x or 'forget' in x or 'memorize' in x or 'recall' in x))
    )
    def handle_memory_techniques(self, query):
        """Handle memory improvement requests."""
        self.response = {
            'concept': '🧠 Memory Enhancement Techniques',
            'diagnosis': 'You need scientifically-proven memory techniques!',
            'explanation': """**How Memory Works:**

**Three Types of Memory:**

1. **Sensory** (1-2 seconds)
   - What you just saw/heard
   - Most information is LOST here

2. **Short-term / Working Memory** (20-30 seconds)
   - Can hold 5-9 items
   - Quickly forgotten unless...

3. **Long-term Memory** (permanent!)
   - Unlimited capacity
   - THIS is what we want!

**The Challenge:** Moving information from short-term → long-term

**Why We Forget:**
- **Encoding failure:** Never properly learned it
- **Decay:** Not used → Lost
- **Interference:** New learning confuses old learning
- **Retrieval failure:** It's there, but can't access it

**Good News:** You can TRAIN your memory!""",
            
            'recommendation': """**Evidence-Based Memory Techniques:**

**TECHNIQUE 1: Spaced Repetition (THE MOST POWERFUL!)**

**Wrong way:**
Study topic once → Never review → Forget

**Right way:**
```
Day 1: Learn new topic
Day 2: Review (quick)
Day 4: Review again
Day 7: Review again
Day 14: Review again
Day 30: Review again
```

**Why it works:**
- Each review strengthens neural pathways
- Timed before you forget (optimal!)
- Becomes permanent memory

**Tool:** Anki app (automated spaced repetition)

**TECHNIQUE 2: Active Recall**

**Passive (WEAK memory):**
❌ Re-reading notes
❌ Highlighting textbooks
❌ Watching videos

**Active (STRONG memory):**
✅ Close book → Write what you remember
✅ Teach concept to someone
✅ Answer practice questions
✅ Create flashcards, test yourself

**Why it works:**
- Forces brain to RETRIEVE (strengthens memory)
- Reveals what you DON'T know
- Practice for exams!

**TECHNIQUE 3: Elaborative Encoding**

**Shallow encoding:** "Mitochondria is powerhouse of cell"
(Just words, easily forgotten)

**Deep encoding:** "Mitochondria is like a power plant in a factory (cell). It takes in raw materials (glucose + oxygen) and produces energy (ATP) that powers all cell activities. Without it, the cell would die because it has no energy source."

**Connect to:**
- Things you already know (analogies)
- Real-life examples
- Why it matters

**TECHNIQUE 4: Dual Coding**

**Use BOTH words AND visuals:**
- Draw diagrams while reading
- Watch animations of processes
- Create mind maps
- Use color coding

**Why it works:**
- Two memory pathways (verbal + visual)
- Easier retrieval (access from either path)

**TECHNIQUE 5: Chunking**

**Hard to remember:**
149217761865

**Easy to remember:**
1492 1776 1865 (chunk into groups)

**For studying:**
- Group related concepts
- Create acronyms (PEMDAS, ROY G BIV)
- Pattern recognition

**TECHNIQUE 6: Method of Loci (Memory Palace)**

**Ancient technique (still works!):**

1. Choose familiar place (your house)
2. Create mental route (front door → living room → kitchen...)
3. Place information at locations
4. Mentally walk route to recall

**Example for Digestive System:**
- Front door: Mouth (food enters)
- Hall: Esophagus (passage)
- Living room: Stomach (acid breaks down)
- Kitchen: Small intestine (nutrients absorbed)
- Garage: Large intestine (waste)

**TECHNIQUE 7: Mnemonic Devices**

**Acronyms:**
- Planets: My Very Educated Mother Just Served Us Noodles
- Biology: Kings Play Chess On Fine Grain Sand (Kingdom, Phylum, Class, Order, Family, Genus, Species)

**Rhymes:**
- "I before E except after C"

**Stories:**
- Create bizarre story linking concepts
- Weirder = more memorable!

**TECHNIQUE 8: Feynman Technique**

**4 Steps:**
1. Choose concept
2. Explain it to a child (simple language!)
3. Identify gaps (where you struggled)
4. Review and simplify further

**Why it works:**
- If you can explain simply, you understand deeply
- Reveals weak points
- Forces active processing

**TECHNIQUE 9: Testing Effect**

**Taking practice tests IMPROVES memory:**
- More effective than re-studying
- Low-stakes practice (don't worry about marks)
- Frequent small tests > One big test

**Do:** Past papers weekly!

**TECHNIQUE 10: Sleep Consolidation**

**Study → Sleep → Memory strengthens**

**Why:**
- Brain replays information during sleep
- Consolidates into long-term memory
- This is WHY cramming fails!

**Best practice:**
- Study hard during day
- Sleep 7-8 hours
- Wake up remembering better!

**TECHNIQUE 11: Multi-Sensory Learning**

**Engage multiple senses:**
- Say information aloud (auditory)
- Write it down (kinesthetic)
- Draw diagrams (visual)
- Walk while reciting (physical)

**More senses = stronger memory!**

**TECHNIQUE 12: Interleaving**

**Blocked practice:**
Study Math Ch1, Ch1, Ch1, then Ch2, Ch2, Ch2

**Interleaved practice:**
Study Math Ch1, Ch2, Ch3, Ch1, Ch3, Ch2...

**Why interleaving wins:**
- Forced to distinguish between concepts
- Better retention
- More like exam conditions

**Memory-Killing Habits to AVOID:**

❌ All-night cramming (forget in days)
❌ Passive re-reading (weak encoding)
❌ Studying one subject for hours (boredom kills memory)
❌ No review system (forget in weeks)
❌ Multitasking (dilutes focus)

**Quick Win Actions:**

✅ Create Anki deck TODAY for current topics
✅ Close book after each paragraph → Recall aloud
✅ Draw one diagram for every concept learned
✅ Teach today's topic to friend/parent tonight
✅ Test yourself before next study session""",
            
            'examples': [
                "Spaced repetition: Learn photosynthesis today, review Day 2, 4, 7, 14",
                "Active recall: After reading chapter, close book and write summary from memory",
                "Memory palace: Map digestive system to rooms in your house",
                "Feynman: Explain cell division to younger sibling in simple words"
            ],
            
            'resources': [
                "Anki: FREE spaced repetition flashcard app (mobile + desktop)",
                "Quizlet: Create online flashcards with games/tests",
                "YouTube: 'Memory Techniques' playlist (visual learning)"
            ],
            
            'topic': 'Learning Techniques',
            'subtopic': 'Memory Enhancement'
        }
        self.diagnosis_complete = True
    
    # ==================== EXAM PREPARATION RULES ====================
    
    @Rule(
        Fact(user_query=MATCH.query & L(lambda x: 'exam prep' in x or 'exam tomorrow' in x or 'test tomorrow' in x or 'last minute' in x or 'exam next week' in x))
    )
    def handle_exam_preparation(self, query):
        """Handle exam preparation strategies."""
        self.response = {
            'concept': '🎯 Exam Preparation Strategies',
            'diagnosis': 'You need a strategic exam preparation plan!',
            'explanation': """**Exam Preparation Timeline:**

**3 Months Before:** Foundation building
**1 Month Before:** Intensive revision
**1 Week Before:** Practice & polish
**1 Day Before:** Light review & mental prep
**Exam Day:** Execution!

**Different preparation for each phase!**""",
            
            'recommendation': """**COMPLETE EXAM PREPARATION SYSTEM:**

**3 MONTHS BEFORE EXAM:**

**Goal:** Learn all topics at least once

**Strategy:**
- Follow teacher's pace
- Make detailed notes
- Understand > Memorize
- Ask questions immediately

**Weekly routine:**
- 2 hours/day regular study
- Sunday: Review week's topics

**1 MONTH BEFORE EXAM:**

**Goal:** Cover everything, identify weak areas

**Week 1-2: First Pass**
- Quick revision of all chapters
- Use notes/summaries (not full textbook)
- Mark difficult topics

**Week 3-4: Second Pass**
- Focus on weak areas
- Practice questions for each topic
- Make flashcards

**Daily routine:**
- 4-5 hours/day study
- Mixed subjects (prevent boredom)
- 1 practice test/week

**1 WEEK BEFORE EXAM:**

**Goal:** Peak performance, polish weak areas

**Monday-Wednesday: Final Revision**
- High-weightage topics (80/20 rule)
- Past papers (timed conditions!)
- Review mistakes immediately

**Thursday: Targeted Practice**
- Focus ONLY on repeated weak areas
- Do NOT learn new topics!

**Friday: Light Review**
- Flashcards, summaries
- Confidence-building (easy questions)
- Early sleep (10pm)

**Saturday (Day Before Exam):**

**Morning:** Light revision (2 hours MAX)
**Afternoon:** Prepare materials
- Pens (2-3, working!)
- Pencils, eraser, ruler
- Calculator (if needed)
- ID card
- Admit card

**Evening:** RELAX
- No studying after 6pm!
- Light walk
- Favorite meal
- Watch something light (comedy)

**Night:** Early sleep (by 10pm)

**EXAM DAY:**

**Morning Routine:**
```
6:30 AM - Wake up (not rushed!)
7:00 AM - Protein breakfast (eggs, nuts, milk)
7:30 AM - Light 10-min review (formulas, key points)
8:00 AM - Leave for exam (arrive 20 min early)
```

**Before Entering:**
- Bathroom (don't waste exam time!)
- Water (stay hydrated)
- Deep breaths (calm nerves)
- Avoid anxious classmates

**DURING EXAM:**

**First 5 Minutes (Crucial!):**
1. Write name/details
2. Read ALL questions quickly
3. Identify easy questions (do these first!)
4. Plan time per question

**Time Management:**
- If 40 questions in 2 hours → 3 min/question
- Stick to time limit
- If stuck, SKIP and return later

**Question Strategy:**

**MCQ:**
- Read question twice
- Eliminate wrong answers first
- Guess if unsure (blank = 0, guess = 25% chance)

**Essay/Theory:**
- Plan answer (1 min outline)
- Introduction → Main points → Conclusion
- Use subheadings
- Diagrams if applicable

**Calculations:**
- Write given values
- Write formula
- Show working (partial marks!)
- Check units

**Last 10 Minutes:**
- Review answers
- Check name on every page
- Ensure all questions attempted

**EMERGENCY: EXAM TOMORROW & HAVEN'T STUDIED!**

**Damage control mode:**

**Tonight (6 hours available):**

**Hour 1-2:** Identify high-weightage topics
- Check past papers
- What repeats every year?
- Focus ONLY on these!

**Hour 3-4:** Speed learning
- Read summaries (not full chapters)
- Watch YouTube summaries (2x speed)
- Make quick flashcards

**Hour 5:** Practice
- Solve one past paper
- Note what you got wrong

**Hour 6:** Flashcard review
- Test yourself
- Focus on formulas/definitions

**10 PM:** STOP and SLEEP
- Sleep > Cramming
- Brain consolidates while sleeping

**Tomorrow Morning:**
- Wake 6am
- 1 hour quick review
- Breakfast
- EXAM

**Realistic expectation:** With 6 hours, aim for PASS grade, not perfect score. Better than nothing!

**POST-EXAM:**

**Immediately after:**
- DON'T discuss answers with friends (too late to change, creates anxiety)
- Relax!
- Prepare for next exam

**General Exam Tips:**

✅ **Trust your first instinct** (changing answers often makes it worse)
✅ **Easy questions first** (builds confidence, guarantees marks)
✅ **Show all working** (partial marks save you!)
✅ **Neat handwriting** (examiner mood = your marks!)
✅ **Use exam time fully** (don't leave early!)

❌ **Don't panic if others finish early** (they might be wrong!)
❌ **Don't leave questions blank** (attempt something!)
❌ **Don't compare during exam** (focus on YOUR paper!)

**Mindset:**
"I've prepared as best as I could. Now I'll do my best in the time given. The result will take care of itself."

**Remember:** Exam is just ONE measure of knowledge, not your worth as a person!""",
            
            'examples': [
                "3-2-1 method: 3 months out, 2 revisions per topic, 1 week intensive practice",
                "Night before: No studying after 6pm, prepare materials, sleep by 10pm",
                "Exam day: Arrive 20 min early, bathroom first, avoid anxious students",
                "During exam: Read all questions first, do easy ones first, keep moving"
            ],
            
            'resources': [
                "Past papers: Repeat exam board's official past papers (BEST preparation)",
                "YouTube: Subject-specific exam tips (search '[subject] exam tips')",
                "Marking schemes: Understand what examiners want to see"
            ],
            
            'topic': 'Exam Preparation',
            'subtopic': 'Test-Taking Strategies'
        }
        self.diagnosis_complete = True
    
    # ==================== CONFIDENCE & PSYCHOLOGY RULES ====================
    
    @Rule(
        Fact(user_query=MATCH.query & L(lambda x: 'confidence' in x or 'not smart' in x or 'dumb' in x or 'can\'t do' in x or 'feel stupid' in x))
    )
    def handle_confidence_building(self, query):
        """Handle confidence and self-belief issues."""
        self.response = {
            'concept': '💎 Building Study Confidence',
            'diagnosis': 'Low confidence is blocking your potential!',
            'explanation': """**Confidence Myths:**

❌ **Myth 1:** "Smart people are born smart"
✅ **Truth:** Intelligence is built through effort (Growth Mindset)

❌ **Myth 2:** "I'm just not good at [subject]"
✅ **Truth:** You haven't learned it the right way YET

❌ **Myth 3:** "Others are smarter than me"
✅ **Truth:** You're seeing their highlight reel, not their struggles

**Why Confidence Matters:**
- Confident students try harder
- They persist through difficulty
- They ask for help
- They take risks (which leads to learning!)

**Your Confidence Formula:**
Small Wins → Positive Feelings → More Effort → Bigger Wins → CONFIDENCE!""",
            
            'recommendation': """**Confidence-Building System:**

**PILLAR 1: Adopt Growth Mindset**

**Fixed Mindset (LOW confidence):**
- "I'm bad at math" (permanent)
- "I failed" (identity)
- "This proves I'm dumb"

**Growth Mindset (HIGH confidence):**
- "I'm not good at math YET" (temporary)
- "I got a low mark on THIS test" (specific event)
- "This shows me what to improve"

**Language swap:**
❌ "I can't do this" → ✅ "I can't do this YET"
❌ "I'm not smart" → ✅ "I'm not smart in this area YET"
❌ "This is too hard" → ✅ "This will take time and strategy"

**PILLAR 2: Collect Evidence of Competence**

**Start a "Wins Journal":**

Every day, write 3 things:
1. One thing I learned today
2. One problem I solved
3. One thing I did better than yesterday

**Example:**
```
Nov 10:
- Learned photosynthesis equation
- Solved 5/10 math problems (yesterday was 3/10!)
- Explained cell division to friend (understood it better!)
```

**After 1 month:** 90 pieces of evidence that you're capable!

**PILLAR 3: The Confidence Staircase**

**Don't jump to hardest task!** Build up:

**Step 1:** Very easy question (100% success)
**Step 2:** Easy question (confident!)
**Step 3:** Medium question (challenging but doable)
**Step 4:** Hard question (stretch goal)

**Each success = confidence boost for next level!**

**PILLAR 4: Reframe "Failure"**

**Failure ≠ Proof you're dumb**
**Failure = Feedback for improvement**

Thomas Edison (inventor):
"I didn't fail 10,000 times. I successfully found 10,000 ways that don't work."

**New approach to mistakes:**
1. What went wrong?
2. Why did it go wrong?
3. How can I fix it?
4. Try again with new strategy

**PILLAR 5: Comparison Detox**

**Stop comparing to:**
- Smartest kid in class
- Perfect Instagram students
- Genius scientists in textbooks

**Start comparing to:**
- Yourself yesterday
- Yourself last month
- Your starting point

**The only competition: PAST YOU!**

**PILLAR 6: Positive Self-Talk**

**Your brain believes what you tell it!**

**Morning Affirmations** (say aloud):
- "I am capable of learning anything"
- "My effort determines my results, not my starting point"
- "Every mistake teaches me something"
- "I am becoming smarter every day"

**During study:**
Instead of: "I don't understand this" (stops brain)
Say: "I don't understand this YET. Let me try another approach" (activates problem-solving)

**PILLAR 7: Master One Topic Completely**

**Choose ONE topic that's:**
- Not too hard
- Not too easy
- High-weightage

**Study until you MASTER it:**
- Can explain it simply
- Can teach it to someone
- Can ace practice questions

**Result:** "If I can master THIS, I can master ANYTHING!" (confidence boost!)

**PILLAR 8: Visualize Success**

**Daily 5-minute practice:**
- Close eyes
- Imagine yourself confidently answering exam questions
- Feel the satisfaction of understanding
- See yourself getting good results
- FEEL the pride

**Brain doesn't distinguish imagined success from real success!** (Builds neural pathways)

**PILLAR 9: Dress for Success**

**Psychological trick:**
- Study in "smart clothes" (not pajamas!)
- Clean desk, organized notes
- Act like successful student

**How you present = How you feel!**

**PILLAR 10: Get Small Wins FAST**

**Quick confidence boosters:**
- Solve 5 easy problems → Feel competent!
- Make perfect summary notes → Feel organized!
- Quiz yourself and get 8/10 → Feel smart!

**Momentum = Motivation = Confidence!**

**When Confidence Crashes:**

**Emergency Confidence Restorers:**

1. **Review past successes**
   - Look at wins journal
   - Remember times you succeeded

2. **Talk to supporter**
   - Friend/family who believes in you
   - Their confidence = temporary loan for yours

3. **Do something you're good at**
   - Sport, hobby, game
   - Reminds you you're capable of mastery

4. **Watch inspirational content**
   - Success stories of people who struggled
   - Proves: Struggle → Success (not Struggle → Failure)

**Remember These Facts:**

✅ **Every expert was once a beginner**
✅ **Struggle = Sign of learning, NOT stupidity**
✅ **Intelligence is BUILT, not inherited**
✅ **Your worth ≠ Your marks**
✅ **Confidence follows competence** (so build competence!)

**Final Truth:**
You're reading this guide, which means you CARE about improving. That caring is the first sign of intelligence. The rest is just strategy and time!

**You've got this! 💪**""",
            
            'examples': [
                "Morning ritual: Look in mirror, say 'I am capable of learning anything' 3x",
                "After study session: Write 3 wins in journal (even tiny ones count!)",
                "Confidence staircase: Start day with 5 easy problems (builds momentum)",
                "Comparison detox: Unfollow 'perfect student' accounts on social media"
            ],
            
            'resources': [
                "Book: 'Mindset' by Carol Dweck (Growth Mindset concept)",
                "YouTube: 'The Science of Success' (evidence-based confidence)",
                "TED Talk: 'The Power of Believing You Can Improve' (Carol Dweck)"
            ],
            
            'topic': 'Psychology',
            'subtopic': 'Confidence Building'
        }
        self.diagnosis_complete = True
    
    # ==================== NO MATCH / FINAL OUTPUT ====================
    
    @Rule(
        NOT(Fact(weak_area=W()))  # No weak area identified
    )
    def no_diagnosis_possible(self):
        """No sufficient information for diagnosis."""
        self.response = {
            'concept': 'Study Guidance',
            'explanation': """I need more information to help you effectively.

Please tell me specifically what you're struggling with:
- Are you having trouble with a particular type of question? (MCQ, essay, calculations)
- Is there a specific subject that's challenging?
- Are you struggling with understanding concepts or remembering them?

The more specific you are, the better I can help!""",
            'topic': 'Study Skills',
            'subtopic': 'General Guidance'
        }
    
    # ==================== INTERFACE METHODS ====================
    # These methods allow the orchestrator to interact with the expert
    
    def get_response(self):
        """Return the expert's response (diagnosis/clarification)."""
        return self.response
    
    def requires_clarification(self):
        """Check if expert needs more information."""
        return self.needs_clarification and not self.diagnosis_complete
    
    def get_clarification_question(self):
        """Get the clarification question to ask user."""
        return self.clarification_question
    
    def is_diagnosis_complete(self):
        """Check if diagnostic process is complete."""
        return self.diagnosis_complete
    
    def has_active_session(self):
        """
        Check if there's an active diagnostic session in progress.
        Returns True if facts have been declared beyond the initial action fact.
        """
        # Check if any diagnostic facts exist (beyond the initial action fact)
        facts_str = str(self.facts.values())
        diagnostic_keywords = ['weak_area', 'math_subject', 'essay_difficulty', 
                               'mcq_subject', 'theory_subject', 'essay_weak_point',
                               'math_struggle']
        
        return any(keyword in facts_str for keyword in diagnostic_keywords)
    
    def declare_user_response(self, response_text: str):
        """
        Declare appropriate fact based on user's response.
        
        Maps user's text response to the appropriate Fact for the engine.
        """
        response = response_text.lower().strip()
        
        # Determine what type of response this is based on collected facts
        facts_str = str(self.facts.values())
        
        # First question: weak_area
        if 'weak_area' not in facts_str:
            self.declare(Fact(weak_area=response))
        
        # Math subject question
        elif 'math' in facts_str and 'math_subject' not in facts_str:
            self.declare(Fact(math_subject=response))
        
        # Essay difficulty question
        elif 'essay' in facts_str and 'essay_difficulty' not in facts_str:
            self.declare(Fact(essay_difficulty=response))
        
        # MCQ issue question
        elif 'mcq' in facts_str and 'mcq_issue' not in facts_str:
            self.declare(Fact(mcq_issue=response))
        
        # Theory subject question
        elif 'theory' in facts_str and 'theory_subject' not in facts_str:
            self.declare(Fact(theory_subject=response))
