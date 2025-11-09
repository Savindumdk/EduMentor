"""
Base Agent Class
----------------
Common functionality for all subject agents.
"""

from experta import *
import re


class Question(Fact):
    """Fact class for student questions."""
    pass


class BaseAgent(KnowledgeEngine):
    """
    Base class for all subject-specific agents.
    Provides common functionality and structure.
    """
    
    def __init__(self, subject_name, knowledge_base):
        super().__init__()
        self.subject_name = subject_name
        self.knowledge_base = knowledge_base
        self.response = None
        self.matched_concept = None
        self.confidence = 0.0
    
    def reset_response(self):
        """Reset response data for new query."""
        self.response = None
        self.matched_concept = None
        self.confidence = 0.0
    
    def extract_keywords(self, question_text):
        """Extract keywords from question."""
        words = re.findall(r'\b\w+\b', question_text.lower())
        stop_words = {'is', 'are', 'the', 'a', 'an', 'what', 'why', 'how', 'does', 
                     'do', 'can', 'could', 'would', 'should', 'will', 'when', 'where',
                     'tell', 'me', 'about', 'explain', 'describe'}
        keywords = [w for w in words if w not in stop_words and len(w) > 2]
        return keywords
    
    def match_concept(self, keywords):
        """
        Match keywords to concepts in knowledge base.
        Returns best matching concept with confidence score.
        """
        best_match = None
        best_score = 0
        
        for concept, rule_data in self.knowledge_base.items():
            rule_keywords = rule_data["keywords"]
            # Count matching keywords
            matches = sum(1 for kw in keywords if kw in rule_keywords)
            
            if matches > best_score:
                best_score = matches
                best_match = concept
        
        if best_match and best_score > 0:
            # Calculate confidence based on match quality
            total_keywords = len(self.knowledge_base[best_match]["keywords"])
            confidence = min(best_score / total_keywords * 1.0, 0.95)
            return best_match, confidence
        
        return None, 0.0
    
    def set_response(self, concept, confidence):
        """Set response based on matched concept."""
        if concept in self.knowledge_base:
            rule_data = self.knowledge_base[concept]
            self.response = {
                'concept': concept,
                'explanation': rule_data['explanation'],
                'topic': rule_data['topic'],
                'subtopic': rule_data.get('subtopic', ''),
                'examples': rule_data.get('examples', []),
                'confidence': confidence,
                'agent': self.subject_name
            }
            self.matched_concept = concept
            self.confidence = confidence
    
    def process_question(self, question_text):
        """
        Main method to process a question.
        Returns response with explanation.
        """
        self.reset()
        self.reset_response()
        
        # Extract keywords
        keywords = self.extract_keywords(question_text)
        
        # Match to concept
        concept, confidence = self.match_concept(keywords)
        
        if concept:
            self.set_response(concept, confidence)
            return self.response
        
        # No match found
        return {
            'concept': None,
            'explanation': f"I couldn't find a matching {self.subject_name} topic for your question.",
            'topic': self.subject_name,
            'confidence': 0.0,
            'agent': self.subject_name
        }
    
    def get_response(self):
        """Get the current response."""
        return self.response
    
    def can_answer(self, keywords):
        """
        Check if this agent can answer based on keywords.
        Returns confidence score.
        """
        concept, confidence = self.match_concept(keywords)
        return confidence
