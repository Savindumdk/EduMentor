"""
Study Guide Agent
-----------------
Specialized agent for study tips and learning strategies.
"""

from agents.base_agent import BaseAgent
from subjects.study_guide_kb import get_study_guide_rules


class StudyGuideAgent(BaseAgent):
    """Agent specialized in study tips and strategies."""
    
    def __init__(self):
        super().__init__("Study Guide", get_study_guide_rules())
        self.subject_keywords = [
            'study', 'learn', 'exam', 'test', 'revision', 'prepare', 'practice',
            'memory', 'remember', 'notes', 'time', 'management', 'schedule',
            'motivation', 'focus', 'concentration', 'tips', 'help', 'improve',
            'better', 'grades', 'score', 'mnemonics'
        ]
    
    def is_relevant(self, question_text):
        """Check if question is related to study guidance."""
        keywords = self.extract_keywords(question_text)
        return any(kw in self.subject_keywords for kw in keywords)
