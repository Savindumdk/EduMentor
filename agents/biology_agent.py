"""
Biology Agent
-------------
Specialized agent for Biology questions using Experta.
"""

from agents.base_agent import BaseAgent
from subjects.biology_kb import get_biology_rules


class BiologyAgent(BaseAgent):
    """Agent specialized in Biology topics."""
    
    def __init__(self):
        super().__init__("Biology", get_biology_rules())
        self.subject_keywords = [
            'cell', 'organism', 'plant', 'animal', 'photosynthesis', 'respiration',
            'digestion', 'reproduction', 'evolution', 'ecosystem', 'genetics',
            'enzyme', 'protein', 'dna', 'tissue', 'organ', 'chlorophyll',
            'oxygen', 'carbon', 'nutrient', 'species', 'bacteria', 'virus'
        ]
    
    def is_relevant(self, question_text):
        """Check if question is related to Biology."""
        keywords = self.extract_keywords(question_text)
        return any(kw in self.subject_keywords for kw in keywords)
