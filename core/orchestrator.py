"""
System Orchestrator
------------------
Coordinates the flow between Intent Classifier → Expert Systems → Response Refinement.
"""

import re
from experta import Fact
from core.memory import ConversationMemory
from core.intent_classifier import IntentClassifierAgent
from core.response_refiner import ResponseRefinementAgent
from experts.biology_expert import BiologyExpert
from experts.physics_expert import PhysicsExpert
from experts.chemistry_expert import ChemistryExpert
from experts.study_guide_expert import StudyGuideExpert


class SystemOrchestrator:
    """
    Main coordinator for the new architecture.
    
    Flow:
    1. User Question → Memory
    2. Intent Classifier (LLM) → Determine subject
    3. Route to Expert System (@Rule-based)
    4. Expert System → Facts + Inference → Response/Clarification
    5. If clarification needed → Ask user → Go back to step 3
    6. Response Refinement (LLM) → Natural language
    7. Return to user
    """
    
    def __init__(self):
        """Initialize all components."""
        print("\n" + "="*60)
        print("🚀 Initializing New Expert System Architecture")
        print("="*60)
        
        # Core components
        self.memory = ConversationMemory(max_history=10)
        self.intent_classifier = IntentClassifierAgent(self.memory)
        self.response_refiner = ResponseRefinementAgent()
        
        # Expert systems
        self.experts = {
            'Biology': BiologyExpert,
            'Physics': PhysicsExpert,
            'Chemistry': ChemistryExpert,
            'StudyGuide': StudyGuideExpert,
            # TODO: Add Mathematics, History
        }
        
        # State management for clarification flow
        self.awaiting_clarification = False
        self.pending_expert = None
        self.pending_facts = None
        self.pending_expert_instance = None  # For diagnostic experts
        
        print("✓ System Orchestrator initialized successfully\n")
    
    def process_query(self, user_input: str) -> dict:
        """
        Main entry point for processing user queries.
        
        Args:
            user_input: User's question or clarification response
        
        Returns:
            {
                'response_type': 'answer' | 'clarification_request' | 'error',
                'content': '...',
                'concept': '...',
                'topic': '...',
                'expert_rule': '...',  # Original expert system output
                'refined_response': '...',  # LLM-refined version
                'examples': [...],
                'conversation_context': '...'
            }
        """
        
        print(f"\n{'='*60}")
        print(f"📝 USER INPUT: {user_input}")
        print(f"{'='*60}\n")
        
        # Start new conversation turn
        self.memory.start_turn(user_input)
        
        # Check if we're awaiting clarification response
        if self.awaiting_clarification:
            return self._handle_clarification_response(user_input)
        
        # Step 1: Classify intent
        classification = self.intent_classifier.classify_intent(user_input)
        
        # Check if we need clarification from user
        if self.intent_classifier.should_request_clarification(classification):
            clarification_q = self.intent_classifier.generate_clarification_question(user_input)
            
            self.awaiting_clarification = True
            self.memory.add_clarification_to_current(clarification_q, "(awaiting user response)")
            
            return {
                'response_type': 'clarification_request',
                'content': clarification_q,
                'concept': 'Intent Clarification',
                'topic': 'System',
                'conversation_context': self.memory.get_context_summary()
            }
        
        subject = classification['subject']
        
        if not subject or subject not in self.experts:
            return self._handle_unknown_subject(user_input)
        
        # Step 2: Route to expert system
        expert_result = self._query_expert_system(subject, user_input, classification)
        
        # Step 3: Check if expert needs clarification
        if expert_result.get('needs_clarification'):
            self.awaiting_clarification = True
            self.pending_expert = subject
            self.pending_facts = expert_result.get('pending_facts')
            
            clarification_q = expert_result['clarification_question']
            self.memory.add_clarification_to_current(clarification_q, "(awaiting user response)")
            
            return {
                'response_type': 'clarification_request',
                'content': clarification_q,
                'concept': 'Expert System Clarification',
                'topic': subject,
                'conversation_context': self.memory.get_context_summary()
            }
        
        # Step 4: Refine response with LLM
        refined = self.response_refiner.refine_response(user_input, expert_result)
        
        # Complete conversation turn
        self.memory.complete_turn(
            answer=refined['refined_explanation'],
            subject=subject,
            needed_clarification=False
        )
        
        return {
            'response_type': 'answer',
            'content': refined['refined_explanation'],
            'concept': refined['concept'],
            'topic': refined['topic'],
            'expert_rule': refined['original_rule'],
            'refined_response': refined['refined_explanation'],
            'examples': refined['examples'],
            'conversation_context': self.memory.get_context_summary(),
            'subject': subject
        }
    
    def _query_expert_system(self, subject: str, question: str, classification: dict) -> dict:
        """
        Query the appropriate expert system using Experta's inference engine.
        
        Args:
            subject: Which expert system to use
            question: User's question
            classification: Intent classification results
        
        Returns:
            Expert system output or clarification request
        """
        
        print(f"\n🎓 EXPERT SYSTEM: Routing to {subject}Expert")
        
        # Check if this is a diagnostic expert (StudyGuide)
        if subject == 'StudyGuide':
            return self._handle_diagnostic_expert(subject, question)
        else:
            return self._handle_information_expert(subject, question, classification)
    
    def _handle_diagnostic_expert(self, subject: str, question: str) -> dict:
        """
        Handle diagnostic expert with progressive questioning.
        
        Diagnostic experts (like StudyGuide) ask multiple questions
        before providing a diagnosis.
        """
        print("   Mode: DIAGNOSTIC (progressive questioning)")
        
        # Check if we're continuing a previous diagnostic session
        if self.pending_expert_instance and self.pending_expert == subject:
            print("   Continuing previous diagnostic session...")
            expert = self.pending_expert_instance
            
            # Declare fact based on user's response
            expert.declare_user_response(question)
            
            # Run engine again
            expert.run()
        else:
            print("   Starting new diagnostic session...")
            # Create new expert instance
            ExpertClass = self.experts[subject]
            expert = ExpertClass()
            expert.reset()
            expert.run()
            
            # Store for next turn
            self.pending_expert_instance = expert
        
        # Check if expert needs more information
        if expert.requires_clarification():
            clarification_q = expert.get_clarification_question()
            print(f"   ❓ Expert needs clarification")
            print(f"   Question: {clarification_q[:100]}...")
            
            return {
                'needs_clarification': True,
                'clarification_question': clarification_q,
                'pending_facts': {}
            }
        
        # Check if diagnosis is complete
        if expert.is_diagnosis_complete():
            print("   ✅ Diagnosis complete!")
            response = expert.get_response()
            
            # Add response_type for diagnostic results
            if response:
                response['response_type'] = 'diagnosis'
            
            return response
        
        # Fallback
        return {
            'concept': 'Study Guidance',
            'explanation': 'I need more information to help you effectively.',
            'topic': 'Study Skills'
        }
    
    def _handle_information_expert(self, subject: str, question: str, classification: dict) -> dict:
        """
        Handle information expert (Biology, Physics, etc.) - direct Q&A.
        
        Information experts provide direct answers to specific questions.
        """
        print("   Mode: INFORMATION (direct Q&A)")
        
        # Create expert instance
        ExpertClass = self.experts[subject]
        expert = ExpertClass()
        expert.reset()
        
        # Extract keywords from question
        keywords = self._extract_keywords(question)
        print(f"   Keywords extracted: {keywords}")
        
        # Declare facts to the expert system
        expert.declare(Fact(keywords=keywords))
        
        # If intent classifier identified a specific topic, declare it
        if classification.get('extracted_topic'):
            expert.declare(Fact(query_topic=classification['extracted_topic']))
        
        # Run the inference engine
        print("   Running inference engine...")
        expert.run()
        
        # Check results
        if expert.requires_clarification():
            print("   ⚠️ Expert system requires clarification")
            return {
                'needs_clarification': True,
                'clarification_question': expert.get_clarification_question(),
                'pending_facts': {'keywords': keywords}
            }
        
        response = expert.get_response()
        
        if response:
            print(f"   ✓ Expert system matched: {response.get('concept', 'N/A')}")
            return response
        else:
            print("   ❌ No match found in expert system")
            return {
                'concept': 'No Match',
                'explanation': f"I couldn't find information about that in my {subject} knowledge base.",
                'topic': subject,
                'examples': []
            }
    
    def _extract_keywords(self, text: str) -> list:
        """Extract keywords from user question."""
        # Remove common stop words
        stop_words = {'is', 'are', 'the', 'a', 'an', 'what', 'why', 'how', 'does', 
                     'do', 'can', 'could', 'would', 'should', 'will', 'when', 'where',
                     'tell', 'me', 'about', 'explain', 'describe', 'of', 'to', 'in', 'for'}
        
        # Extract words
        words = re.findall(r'\b\w+\b', text.lower())
        keywords = [w for w in words if w not in stop_words and len(w) > 2]
        
        return keywords
    
    def _handle_clarification_response(self, user_response: str) -> dict:
        """Handle user's response to a clarification request."""
        
        print("\n🔄 CLARIFICATION RESPONSE received")
        
        # Add clarification to memory
        if self.memory.current_turn and self.memory.current_turn.clarifications:
            last_clarif = self.memory.current_turn.clarifications[-1]
            last_clarif['response'] = user_response
        
        self.awaiting_clarification = False
        
        # If we have a pending expert system query, continue with it
        if self.pending_expert is not None:
            # Re-classify the clarification response or use the pending info
            classification = self.intent_classifier.classify_intent(user_response)
            
            # Query expert system with clarification
            expert_result = self._query_expert_system(
                self.pending_expert,
                user_response,
                classification
            )
            
            # If still needs clarification, handle it (keep pending state)
            if expert_result.get('needs_clarification'):
                self.awaiting_clarification = True
                self.pending_facts = expert_result.get('pending_facts')
                return {
                    'response_type': 'clarification_request',
                    'content': expert_result['clarification_question'],
                    'concept': 'Expert System Clarification',
                    'topic': self.pending_expert
                }
            
            # Clear pending state only when done
            subject_for_memory = self.pending_expert
            self.pending_expert = None
            self.pending_facts = None
            self.pending_expert_instance = None
            
            # Refine and return
            refined = self.response_refiner.refine_response(user_response, expert_result)
            
            self.memory.complete_turn(
                answer=refined['refined_explanation'],
                subject=subject_for_memory,
                needed_clarification=True
            )
            
            return {
                'response_type': 'answer',
                'content': refined['refined_explanation'],
                'concept': refined['concept'],
                'topic': refined['topic'],
                'expert_rule': refined['original_rule'],
                'refined_response': refined['refined_explanation'],
                'examples': refined['examples']
            }
        
        # Otherwise, process as new query
        return self.process_query(user_response)
    
    def _handle_unknown_subject(self, question: str) -> dict:
        """Handle questions that don't match any subject."""
        
        available = ', '.join(self.experts.keys())
        
        return {
            'response_type': 'error',
            'content': f"""I couldn't determine which subject your question relates to.

**Available subjects:** {available}

Please rephrase your question or specify which subject you're asking about.

**Examples:**
- "What is photosynthesis?" (Biology)
- "Explain forces" (Physics)
- "How do acids work?" (Chemistry)""",
            'concept': 'Unknown Subject',
            'topic': 'System',
            'conversation_context': self.memory.get_context_summary()
        }
    
    def get_conversation_stats(self) -> dict:
        """Get conversation statistics."""
        return self.memory.get_statistics()
    
    def clear_conversation(self):
        """Clear conversation history."""
        self.memory.clear()
        self.awaiting_clarification = False
        self.pending_expert = None
        self.pending_facts = None
        print("🗑️ Conversation history cleared")
