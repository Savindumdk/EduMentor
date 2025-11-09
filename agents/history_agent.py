"""
History Agent
-------------
Specialized agent for History questions using Experta.
"""

from agents.base_agent import BaseAgent
from subjects.history_kb import get_history_rules


class HistoryAgent(BaseAgent):
    """Agent specialized in History topics."""
    
    def __init__(self):
        super().__init__("History", get_history_rules())
        self.subject_keywords = [
            'history', 'ancient', 'civilization', 'kingdom', 'king', 'queen',
            'colonial', 'independence', 'war', 'battle', 'empire', 'dynasty',
            'culture', 'heritage', 'tradition', 'portuguese', 'dutch', 'british',
            'anuradhapura', 'polonnaruwa', 'ceylon', 'sri lanka', 'past', 'historical'
        ]
    
    def is_relevant(self, question_text):
        """Check if question is related to History."""
        keywords = self.extract_keywords(question_text)
        return any(kw in self.subject_keywords for kw in keywords)
