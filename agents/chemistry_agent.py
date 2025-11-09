"""
Chemistry Agent
---------------
Specialized agent for Chemistry questions using Experta.
"""

from agents.base_agent import BaseAgent
from subjects.chemistry_kb import get_chemistry_rules


class ChemistryAgent(BaseAgent):
    """Agent specialized in Chemistry topics."""
    
    def __init__(self):
        super().__init__("Chemistry", get_chemistry_rules())
        self.subject_keywords = [
            'acid', 'base', 'alkali', 'chemical', 'reaction', 'element', 'compound',
            'molecule', 'atom', 'ion', 'bond', 'combustion', 'oxidation', 'reduction',
            'periodic', 'table', 'metal', 'non-metal', 'solution', 'mixture',
            'ph', 'indicator', 'catalyst', 'equation'
        ]
    
    def is_relevant(self, question_text):
        """Check if question is related to Chemistry."""
        keywords = self.extract_keywords(question_text)
        return any(kw in self.subject_keywords for kw in keywords)
