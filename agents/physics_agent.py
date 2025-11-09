"""
Physics Agent
-------------
Specialized agent for Physics questions using Experta.
"""

from agents.base_agent import BaseAgent
from subjects.physics_kb import get_physics_rules


class PhysicsAgent(BaseAgent):
    """Agent specialized in Physics topics."""
    
    def __init__(self):
        super().__init__("Physics", get_physics_rules())
        self.subject_keywords = [
            'force', 'motion', 'energy', 'friction', 'gravity', 'electricity',
            'magnetism', 'light', 'sound', 'heat', 'power', 'work', 'speed',
            'velocity', 'acceleration', 'momentum', 'pressure', 'circuit',
            'current', 'voltage', 'resistance'
        ]
    
    def is_relevant(self, question_text):
        """Check if question is related to Physics."""
        keywords = self.extract_keywords(question_text)
        return any(kw in self.subject_keywords for kw in keywords)
