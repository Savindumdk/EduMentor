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
