"""
Coordinator Agent (Multi-Agent System Router)
----------------------------------------------
Routes student questions to appropriate subject agents.
Aggregates responses from multiple agents if needed.
"""

from agents.physics_agent import PhysicsAgent
from agents.biology_agent import BiologyAgent
from agents.chemistry_agent import ChemistryAgent
from agents.mathematics_agent import MathematicsAgent
from agents.history_agent import HistoryAgent
from agents.study_guide_agent import StudyGuideAgent


class CoordinatorAgent:
    """
    Master agent that coordinates question routing and response aggregation.
    Implements Multi-Agent System (MAS) architecture.
    """
    
    def __init__(self):
        # Initialize all subject agents
        self.agents = {
            'physics': PhysicsAgent(),
            'biology': BiologyAgent(),
            'chemistry': ChemistryAgent(),
            'mathematics': MathematicsAgent(),
            'history': HistoryAgent(),
            'study_guide': StudyGuideAgent()
        }
        
        self.agent_priority = [
            'physics', 'biology', 'chemistry', 
            'mathematics', 'history', 'study_guide'
        ]
    
    def classify_question(self, question_text):
        """
        Classify question and determine which agents can answer it.
        Returns list of (agent_name, confidence) tuples.
        """
        keywords = self.agents['physics'].extract_keywords(question_text)
        agent_confidences = []
        
        for agent_name, agent in self.agents.items():
            confidence = agent.can_answer(keywords)
            if confidence > 0:
                agent_confidences.append((agent_name, confidence))
        
        # Sort by confidence (highest first)
        agent_confidences.sort(key=lambda x: x[1], reverse=True)
        
        return agent_confidences
    
    def route_question(self, question_text):
        """
        Route question to the most appropriate agent.
        Returns response from the best matching agent.
        """
        agent_rankings = self.classify_question(question_text)
        
        if not agent_rankings:
            # No agent can answer - return default response
            return {
                'concept': None,
                'explanation': """I couldn't find a specific topic matching your question.
                
I can help with:
• Physics (forces, motion, energy, electricity)
• Biology (cells, photosynthesis, respiration, digestion)
• Chemistry (acids, bases, elements, reactions)
• Mathematics (algebra, geometry, fractions, percentages)
• History (ancient civilizations, colonial period, independence)
• Study Guide (study tips, exam preparation, memory techniques)

Please rephrase your question or ask about one of these subjects.""",
                'topic': 'Unknown',
                'confidence': 0.0,
                'agent': 'Coordinator',
                'agents_consulted': []
            }
        
        # Get response from best matching agent
        best_agent_name, best_confidence = agent_rankings[0]
        best_agent = self.agents[best_agent_name]
        
        response = best_agent.process_question(question_text)
        response['agents_consulted'] = [best_agent_name]
        response['routing_confidence'] = best_confidence
        
        return response
    
    def aggregate_responses(self, question_text, top_n=2):
        """
        Get responses from multiple agents and aggregate.
        Useful for cross-disciplinary questions.
        """
        agent_rankings = self.classify_question(question_text)
        
        if not agent_rankings:
            return self.route_question(question_text)
        
        # Get responses from top N agents
        responses = []
        for agent_name, confidence in agent_rankings[:top_n]:
            if confidence > 0.3:  # Minimum threshold
                agent = self.agents[agent_name]
                response = agent.process_question(question_text)
                response['routing_confidence'] = confidence
                responses.append(response)
        
        if len(responses) == 1:
            responses[0]['agents_consulted'] = [responses[0]['agent']]
            return responses[0]
        
        if len(responses) > 1:
            # Combine multiple perspectives
            combined_explanation = "Here are insights from multiple subjects:\n\n"
            agents_used = []
            
            for i, resp in enumerate(responses, 1):
                combined_explanation += f"**{resp['agent']} Perspective:**\n"
                combined_explanation += f"{resp['explanation']}\n\n"
                agents_used.append(resp['agent'])
            
            return {
                'concept': 'multi_agent',
                'explanation': combined_explanation,
                'topic': 'Multi-Subject',
                'confidence': max(r['confidence'] for r in responses),
                'agent': 'Coordinator (Multi-Agent)',
                'agents_consulted': agents_used,
                'individual_responses': responses
            }
        
        return self.route_question(question_text)
    
    def get_agent_statistics(self):
        """Get statistics about available agents."""
        stats = {
            'total_agents': len(self.agents),
            'agents': {}
        }
        
        for name, agent in self.agents.items():
            stats['agents'][name] = {
                'subject': agent.subject_name,
                'topics': len(agent.knowledge_base),
                'available': True
            }
        
        return stats
    
    def process_question(self, question_text, multi_agent=False):
        """
        Main method to process a student question.
        
        Args:
            question_text (str): Student's question
            multi_agent (bool): Whether to use multiple agents
        
        Returns:
            dict: Response with explanation and metadata
        """
        if multi_agent:
            return self.aggregate_responses(question_text)
        else:
            return self.route_question(question_text)
