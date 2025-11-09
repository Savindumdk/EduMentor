"""
Mathematics Agent
-----------------
Specialized agent for Mathematics questions using Experta.
"""

from agents.base_agent import BaseAgent
from subjects.mathematics_kb import get_mathematics_rules


class MathematicsAgent(BaseAgent):
    """Agent specialized in Mathematics topics."""
    
    def __init__(self):
        super().__init__("Mathematics", get_mathematics_rules())
        self.subject_keywords = [
            'math', 'number', 'equation', 'algebra', 'geometry', 'calculate',
            'fraction', 'decimal', 'percentage', 'ratio', 'proportion',
            'triangle', 'circle', 'square', 'area', 'perimeter', 'volume',
            'angle', 'mean', 'median', 'mode', 'statistics', 'probability',
            'graph', 'plot', 'solve', 'simplify'
        ]
    
    def is_relevant(self, question_text):
        """Check if question is related to Mathematics."""
        keywords = self.extract_keywords(question_text)
        return any(kw in self.subject_keywords for kw in keywords)
