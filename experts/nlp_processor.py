"""
Natural Language Processing Module for Study Guide Expert System
-----------------------------------------------------------------
Extracts entities, intents, and maps queries to facts.
"""

import re
from typing import Dict, List, Tuple


class NLPProcessor:
    """Lightweight NLP for query understanding."""
    
    def __init__(self):
        # Entity patterns
        self.entity_patterns = {
            'sleep_hours': r'(\d+)\s*hours?\s*(?:of\s*)?sleep',
            'stress_level': r'(very|extremely|really|highly)\s*(stress|anxious)',
            'time_period': r'(tomorrow|week|month|tonight|day)',
            'exam_timing': r'exam\s*(tomorrow|next\s*week|in\s*\d+\s*days?)'
        }
        
        # Negation patterns
        self.negations = ['no', 'not', 'never', 'can\'t', 'cannot', 'don\'t', 'won\'t']
        
    def extract_entities(self, query: str) -> Dict[str, any]:
        """Extract structured entities from query."""
        entities = {}
        query_lower = query.lower()
        
        # Extract sleep hours
        sleep_match = re.search(self.entity_patterns['sleep_hours'], query_lower)
        if sleep_match:
            entities['sleep_hours'] = int(sleep_match.group(1))
        
        # Extract stress level
        stress_match = re.search(self.entity_patterns['stress_level'], query_lower)
        if stress_match:
            entities['stress_level'] = 'high'
        
        # Extract time period
        time_match = re.search(self.entity_patterns['time_period'], query_lower)
        if time_match:
            entities['time_period'] = time_match.group(1)
        
        # Extract exam timing
        exam_match = re.search(self.entity_patterns['exam_timing'], query_lower)
        if exam_match:
            entities['exam_timing'] = exam_match.group(1)
            entities['exam_anxiety'] = True
        
        return entities
    
    def detect_intent(self, query: str, kb: Dict) -> List[Tuple[str, float]]:
        """
        Detect intent by matching keywords from knowledge base.
        Returns list of (topic, confidence) tuples sorted by confidence.
        """
        query_lower = query.lower()
        query_words = set(re.findall(r'\w+', query_lower))
        
        intent_scores = []
        
        for topic, data in kb.items():
            if topic == 'inferences':
                continue
                
            keywords = data.get('keywords', [])
            
            # Count keyword matches
            matches = sum(1 for keyword in keywords if keyword in query_lower)
            
            if matches > 0:
                # Calculate confidence based on matches and keyword specificity
                base_confidence = data.get('confidence', 0.8)
                match_boost = min(matches * 0.05, 0.15)  # Up to 15% boost
                
                # Check for exact phrase matches (higher confidence)
                exact_matches = sum(1 for keyword in keywords if len(keyword.split()) > 1 and keyword in query_lower)
                exact_boost = exact_matches * 0.1
                
                total_confidence = min(base_confidence + match_boost + exact_boost, 1.0)
                intent_scores.append((topic, total_confidence))
        
        # Sort by confidence (highest first)
        intent_scores.sort(key=lambda x: x[1], reverse=True)
        
        return intent_scores
    
    def detect_negation(self, query: str) -> bool:
        """Check if query contains negation."""
        query_lower = query.lower()
        return any(neg in query_lower.split() for neg in self.negations)
    
    def extract_conditions(self, query: str, entities: Dict) -> List[str]:
        """
        Extract conditions that can be used as Facts.
        Combines keyword matching with entity extraction.
        """
        conditions = []
        query_lower = query.lower()
        
        # Stress-related conditions
        if any(word in query_lower for word in ['stress', 'anxious', 'anxiety', 'nervous', 'panic']):
            conditions.append('high_stress')
            if 'exam' in query_lower:
                conditions.append('exam_anxiety')
        
        # Memory-related conditions
        if any(word in query_lower for word in ['memory', 'remember', 'forget', 'recall']):
            conditions.append('mentions_memory')
        
        # Sleep-related conditions
        if any(word in query_lower for word in ['sleep', 'tired', 'exhausted']):
            conditions.append('poor_sleep')
            if entities.get('sleep_hours', 8) < 7:
                conditions.append('low_sleep')
        
        # Procrastination-related conditions
        if any(word in query_lower for word in ['procrastinate', 'delay', 'distracted', 'avoid']):
            conditions.append('procrastinating')
            conditions.append('task_aversion')
        
        # Time management conditions
        if any(word in query_lower for word in ['time management', 'schedule', 'organize', 'plan']):
            conditions.append('poor_time_management')
        
        # Motivation conditions
        if any(word in query_lower for word in ['motivation', 'motivate', 'give up', 'lost interest']):
            conditions.append('low_motivation')
        
        # Confidence conditions
        if any(word in query_lower for word in ['confidence', 'stupid', 'dumb', 'not smart']):
            conditions.append('low_confidence')
            if any(word in query_lower for word in ['compare', 'comparing', 'everyone else']):
                conditions.append('comparison_trap')
        
        # Exam conditions
        if 'exam' in query_lower or 'test' in query_lower:
            conditions.append('exam_coming')
            if entities.get('exam_timing') == 'tomorrow' or 'night before' in query_lower:
                conditions.append('night_before')
            elif 'week' in entities.get('exam_timing', ''):
                conditions.append('one_week_before')
        
        # Racing thoughts condition
        if any(phrase in query_lower for phrase in ['racing thoughts', 'can\'t stop thinking', 'mind racing']):
            conditions.append('racing_thoughts')
        
        return conditions
    
    def process_query(self, query: str, kb: Dict) -> Dict:
        """
        Complete NLP processing pipeline.
        Returns structured data ready for expert system.
        """
        # Extract entities
        entities = self.extract_entities(query)
        
        # Detect intents
        intents = self.detect_intent(query, kb)
        
        # Extract conditions
        conditions = self.extract_conditions(query, entities)
        
        # Detect negation
        has_negation = self.detect_negation(query)
        
        return {
            'query': query,
            'entities': entities,
            'intents': intents,
            'conditions': conditions,
            'has_negation': has_negation,
            'primary_intent': intents[0] if intents else None,
            'intent_confidence': intents[0][1] if intents else 0.0
        }
