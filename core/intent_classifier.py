"""
Intent Classifier Agent
-----------------------
Uses LLM to understand user intent and route to appropriate expert system.
"""

import google.generativeai as genai
import os
from typing import Dict, List
from core.memory import ConversationMemory
from config import LLM_MODEL


class IntentClassifierAgent:
    """
    LLM-powered agent that classifies user intent and routes to expert systems.
    
    Responsibilities:
    - Understand what subject the user is asking about
    - Handle ambiguous queries using conversation context
    - Detect if user is providing clarification vs new question
    - Route to appropriate expert system (Physics, Biology, Chemistry, etc.)
    """
    
    AVAILABLE_SUBJECTS = {
        'Physics': {
            'topics': ['forces', 'motion', 'energy', 'electricity', 'circuits', 'magnetism', 'waves'],
            'examples': ['What is Newton\'s first law?', 'How does electricity work?']
        },
        'Biology': {
            'topics': ['cells', 'photosynthesis', 'respiration', 'digestion', 'reproduction', 'genetics'],
            'examples': ['What is photosynthesis?', 'How do cells work?']
        },
        'Chemistry': {
            'topics': ['acids', 'bases', 'elements', 'compounds', 'reactions', 'combustion', 'periodic table'],
            'examples': ['What are acids?', 'How does combustion work?']
        },
        'Mathematics': {
            'topics': ['algebra', 'geometry', 'fractions', 'percentages', 'equations', 'graphs'],
            'examples': ['How do I solve fractions?', 'What is algebra?']
        },
        'History': {
            'topics': ['ancient civilizations', 'colonial period', 'independence', 'world wars', 'revolutions'],
            'examples': ['Tell me about ancient Egypt', 'What was the colonial period?']
        },
        'StudyGuide': {
            'topics': ['study techniques', 'exam preparation', 'memory', 'time management', 'note-taking'],
            'examples': ['How to study effectively?', 'What are good exam tips?']
        }
    }
    
    def __init__(self, memory: ConversationMemory):
        """Initialize with conversation memory."""
        self.memory = memory
        self.model = None
        self._initialize_llm()
    
    def _initialize_llm(self):
        """Initialize Gemini LLM."""
        try:
            api_key = os.getenv('GEMINI_API_KEY')
            if not api_key:
                raise ValueError("GEMINI_API_KEY not found in environment variables")
            
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel(LLM_MODEL)
            print(f"✓ Intent Classifier initialized with {LLM_MODEL}")
        except Exception as e:
            print(f"❌ Failed to initialize Intent Classifier: {e}")
            self.model = None
    
    def classify_intent(self, question: str) -> Dict:
        """
        Classify user intent and determine which expert system to call.
        
        Returns:
            {
                'subject': 'Physics',  # Which expert system
                'confidence': 0.95,     # How confident (0-1)
                'is_clarification': False,  # Is this answering a clarification?
                'extracted_topic': 'forces',  # Specific topic if identified
                'reasoning': '...'     # Why this classification
            }
        """
        print(f"\n{'='*60}")
        print(f"🎯 INTENT CLASSIFIER: Analyzing question")
        print(f"   Question: {question}")
        
        # Get conversation context
        context = self.memory.get_full_context_for_llm(n=3)
        
        # Build prompt for LLM
        prompt = self._build_classification_prompt(question, context)
        
        try:
            response = self.model.generate_content(prompt)
            classification = self._parse_classification_response(response.text)
            
            print(f"   Subject identified: {classification['subject']}")
            print(f"   Confidence: {classification['confidence']:.2f}")
            print(f"   Is clarification: {classification['is_clarification']}")
            if classification['extracted_topic']:
                print(f"   Topic: {classification['extracted_topic']}")
            print(f"{'='*60}\n")
            
            return classification
            
        except Exception as e:
            print(f"❌ Intent classification failed: {e}")
            return self._fallback_classification(question)
    
    def _build_classification_prompt(self, question: str, context: str) -> str:
        """Build prompt for LLM intent classification."""
        
        subjects_info = "\n".join([
            f"- **{subject}**: {', '.join(info['topics'])}"
            for subject, info in self.AVAILABLE_SUBJECTS.items()
        ])
        
        prompt = f"""You are an intent classification system for an educational tutoring platform.
Your job is to identify which subject area the student's question belongs to.

**Available Subjects:**
{subjects_info}

**Conversation Context:**
{context}

**Current Question:**
"{question}"

**Your Task:**
1. Determine which subject this question belongs to
2. Assess your confidence (0.0 to 1.0)
3. Check if this is answering a previous clarification request
4. Extract the specific topic if possible

**Response Format (MUST follow exactly):**
SUBJECT: [Physics|Biology|Chemistry|Mathematics|History|StudyGuide]
CONFIDENCE: [0.0-1.0]
IS_CLARIFICATION: [yes|no]
TOPIC: [specific topic or "unknown"]
REASONING: [brief explanation]

**Guidelines:**
- Use conversation context to resolve ambiguous questions
- If question mentions "it", "this", "that" - refer to context
- Mark as clarification if user is answering a previous question
- Confidence < 0.7 means ambiguous or out-of-scope
- If truly unsure between subjects, choose most likely with lower confidence

Respond now:"""
        
        return prompt
    
    def _parse_classification_response(self, response_text: str) -> Dict:
        """Parse LLM response into structured classification."""
        
        lines = response_text.strip().split('\n')
        result = {
            'subject': None,
            'confidence': 0.5,
            'is_clarification': False,
            'extracted_topic': None,
            'reasoning': ''
        }
        
        for line in lines:
            line = line.strip()
            if line.startswith('SUBJECT:'):
                subject = line.split(':', 1)[1].strip()
                if subject in self.AVAILABLE_SUBJECTS:
                    result['subject'] = subject
            elif line.startswith('CONFIDENCE:'):
                try:
                    conf = float(line.split(':', 1)[1].strip())
                    result['confidence'] = max(0.0, min(1.0, conf))
                except:
                    pass
            elif line.startswith('IS_CLARIFICATION:'):
                clarif = line.split(':', 1)[1].strip().lower()
                result['is_clarification'] = clarif in ['yes', 'true']
            elif line.startswith('TOPIC:'):
                topic = line.split(':', 1)[1].strip()
                if topic.lower() != 'unknown':
                    result['extracted_topic'] = topic
            elif line.startswith('REASONING:'):
                result['reasoning'] = line.split(':', 1)[1].strip()
        
        return result
    
    def _fallback_classification(self, question: str) -> Dict:
        """Simple keyword-based fallback if LLM fails."""
        
        question_lower = question.lower()
        
        # Simple keyword matching
        subject_keywords = {
            'Physics': ['force', 'motion', 'energy', 'electricity', 'circuit', 'newton', 'gravity'],
            'Biology': ['cell', 'plant', 'animal', 'photosynthesis', 'respiration', 'organism'],
            'Chemistry': ['acid', 'base', 'element', 'chemical', 'reaction', 'compound'],
            'Mathematics': ['equation', 'solve', 'calculate', 'fraction', 'percentage', 'algebra'],
            'History': ['ancient', 'colonial', 'independence', 'civilization', 'war', 'revolution'],
            'StudyGuide': ['study', 'exam', 'memory', 'preparation', 'tips', 'learn']
        }
        
        best_match = None
        best_score = 0
        
        for subject, keywords in subject_keywords.items():
            score = sum(1 for kw in keywords if kw in question_lower)
            if score > best_score:
                best_score = score
                best_match = subject
        
        if best_match and best_score > 0:
            return {
                'subject': best_match,
                'confidence': min(0.6, best_score * 0.2),
                'is_clarification': False,
                'extracted_topic': None,
                'reasoning': 'Keyword-based fallback classification'
            }
        
        return {
            'subject': None,
            'confidence': 0.0,
            'is_clarification': False,
            'extracted_topic': None,
            'reasoning': 'Could not classify - no matching keywords'
        }
    
    def should_request_clarification(self, classification: Dict) -> bool:
        """Decide if we need to ask user for clarification."""
        return classification['confidence'] < 0.7 and classification['subject'] is None
    
    def generate_clarification_question(self, question: str, possible_subjects: List[str] = None) -> str:
        """Generate a clarification question for ambiguous intent."""
        
        if not possible_subjects:
            possible_subjects = list(self.AVAILABLE_SUBJECTS.keys())
        
        clarification = f"""🤔 I'm not sure which subject area your question relates to.

**Your question:** "{question}"

**Which subject are you asking about?**

"""
        for subject in possible_subjects[:3]:  # Show top 3
            info = self.AVAILABLE_SUBJECTS[subject]
            examples = info['examples'][:2]
            clarification += f"\n📚 **{subject}**\n"
            clarification += f"   Topics: {', '.join(info['topics'][:5])}\n"
            clarification += f"   Example: {examples[0] if examples else 'N/A'}\n"
        
        clarification += "\n**Please specify:** Which subject should I use to answer your question?"
        
        return clarification
