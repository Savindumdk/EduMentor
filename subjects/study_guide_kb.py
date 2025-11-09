"""
Study Guide Knowledge Base
--------------------------
Contains general study tips, exam strategies, and learning techniques.
"""

STUDY_GUIDE_RULES = {
    "time_management": {
        "keywords": ["time", "management", "schedule", "plan", "organize", "study", "routine"],
        "explanation": """Effective time management is crucial for academic success.
Create a study schedule with specific times for each subject.
Use techniques like Pomodoro (25 min study, 5 min break).
Prioritize difficult subjects when you're most alert.
Balance study time with rest and recreation.""",
        "topic": "Study Guide",
        "subtopic": "Study Skills",
        "examples": [
            "Study difficult subjects in the morning when fresh",
            "Use a planner or calendar to track assignments",
            "Break large tasks into smaller, manageable chunks"
        ]
    },
    "memory_techniques": {
        "keywords": ["memory", "remember", "memorize", "recall", "mnemonics", "forget"],
        "explanation": """Improve memory using proven techniques:
- Mnemonics: Create acronyms or phrases to remember lists
- Visualization: Create mental images of concepts
- Spaced Repetition: Review material at increasing intervals
- Active Recall: Test yourself instead of just re-reading
- Teach Others: Explaining concepts reinforces learning""",
        "topic": "Study Guide",
        "subtopic": "Memory",
        "examples": [
            "ROY G BIV for colors of rainbow (Red, Orange, Yellow...)",
            "Mind maps help visualize connections between concepts",
            "Review notes after 1 day, 3 days, 1 week, 1 month"
        ]
    },
    "exam_preparation": {
        "keywords": ["exam", "test", "preparation", "revision", "practice", "past", "papers"],
        "explanation": """Effective exam preparation strategies:
- Start early, don't cram at the last minute
- Practice with past papers under timed conditions
- Identify weak areas and focus revision there
- Create summary notes and flashcards
- Get enough sleep before the exam
- Stay calm and manage exam stress""",
        "topic": "Study Guide",
        "subtopic": "Exams",
        "examples": [
            "Do past papers to understand question patterns",
            "Create one-page summaries of each topic",
            "Sleep 7-8 hours before exam day"
        ]
    },
    "note_taking": {
        "keywords": ["notes", "note-taking", "write", "summarize", "organize"],
        "explanation": """Effective note-taking improves learning:
- Cornell Method: Divide page into cues, notes, and summary
- Mind Mapping: Visual diagrams showing relationships
- Outline Method: Hierarchical organization with main points and sub-points
- Review and revise notes within 24 hours
- Use colors, highlighters, and diagrams""",
        "topic": "Study Guide",
        "subtopic": "Study Skills",
        "examples": [
            "Use headings and bullet points for clarity",
            "Draw diagrams for visual concepts",
            "Rewrite notes in your own words to improve understanding"
        ]
    },
    "motivation": {
        "keywords": ["motivation", "motivated", "focus", "concentration", "distraction", "goals"],
        "explanation": """Stay motivated and focused on your studies:
- Set clear, achievable goals (SMART goals)
- Create a distraction-free study environment
- Reward yourself after completing study sessions
- Study with friends for accountability (study groups)
- Remember your long-term goals and aspirations
- Take breaks to avoid burnout""",
        "topic": "Study Guide",
        "subtopic": "Motivation",
        "examples": [
            "Set a goal: 'Complete 3 math problems in 30 minutes'",
            "Remove phone from study area to avoid distractions",
            "Reward: Watch a favorite show after 2 hours of study"
        ]
    }
}

def get_study_guide_rules():
    """Return all study guide rules."""
    return STUDY_GUIDE_RULES

def get_study_guide_keywords():
    """Return mapping of keywords to concepts."""
    keyword_map = {}
    for concept, rule_data in STUDY_GUIDE_RULES.items():
        for keyword in rule_data["keywords"]:
            if keyword not in keyword_map:
                keyword_map[keyword] = []
            keyword_map[keyword].append(concept)
    return keyword_map
