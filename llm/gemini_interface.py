"""
Gemini LLM Interface
--------------------
Integrates Google Gemini AI for natural language enhancement.
Converts expert system responses into conversational, multi-lingual explanations.
"""

import os
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    print("Warning: google-generativeai not installed. LLM features will be disabled.")


class GeminiInterface:
    """
    Interface for Google Gemini API.
    Enhances expert system responses with natural language.
    """
    
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        self.model = None
        self.enabled = False
        
        if GEMINI_AVAILABLE and self.api_key:
            try:
                genai.configure(api_key=self.api_key)
                self.model = genai.GenerativeModel('gemini-pro')
                self.enabled = True
                print("✓ Gemini LLM initialized successfully")
            except Exception as e:
                print(f"Warning: Could not initialize Gemini: {e}")
                self.enabled = False
        else:
            if not GEMINI_AVAILABLE:
                print("Note: Install google-generativeai to enable LLM features")
            elif not self.api_key:
                print("Note: Set GEMINI_API_KEY environment variable to enable LLM")
    
    def enhance_explanation(self, expert_response, language='en', student_level='O/L'):
        """
        Enhance expert system response with natural language.
        
        Args:
            expert_response (dict): Response from expert system/MAS
            language (str): Target language ('en', 'si', 'ta')
            student_level (str): Student level for appropriate complexity
        
        Returns:
            str: Enhanced explanation
        """
        if not self.enabled:
            # Fallback to original explanation
            return expert_response.get('explanation', 'No explanation available.')
        
        try:
            # Build prompt for Gemini
            prompt = self._build_prompt(expert_response, language, student_level)
            
            # Generate response
            response = self.model.generate_content(prompt)
            
            return response.text
        
        except Exception as e:
            print(f"Error enhancing with Gemini: {e}")
            # Fallback to original
            return expert_response.get('explanation', 'No explanation available.')
    
    def _build_prompt(self, expert_response, language, student_level):
        """Build prompt for Gemini based on expert response."""
        
        language_names = {
            'en': 'English',
            'si': 'Sinhala',
            'ta': 'Tamil'
        }
        
        lang_name = language_names.get(language, 'English')
        
        concept = expert_response.get('concept', 'general topic')
        topic = expert_response.get('topic', '')
        explanation = expert_response.get('explanation', '')
        examples = expert_response.get('examples', [])
        
        prompt = f"""You are an experienced {student_level} tutor helping students understand {topic}.

A student asked about: {concept}

The expert system provided this explanation:
{explanation}

Your task:
1. Rewrite this explanation in a warm, encouraging, conversational tone
2. Make it suitable for {student_level} students in Sri Lanka
3. Use simple, clear language
4. Add analogies or real-world examples to make it relatable
5. Respond in {lang_name} language
6. Keep it concise (2-3 paragraphs maximum)
7. If the original explanation mentions scientific equations, include them

"""
        
        if examples:
            prompt += f"\nThe knowledge base includes these examples:\n"
            for ex in examples:
                prompt += f"- {ex}\n"
            prompt += "\nYou can incorporate or expand on these examples.\n"
        
        prompt += "\nProvide your enhanced explanation now:"
        
        return prompt
    
    def translate_response(self, text, target_language):
        """
        Translate response to Sinhala or Tamil.
        
        Args:
            text (str): Text to translate
            target_language (str): 'si' for Sinhala, 'ta' for Tamil
        
        Returns:
            str: Translated text
        """
        if not self.enabled:
            return text
        
        lang_map = {
            'si': 'Sinhala',
            'ta': 'Tamil'
        }
        
        if target_language not in lang_map:
            return text
        
        try:
            prompt = f"""Translate the following educational content to {lang_map[target_language]}.
Preserve scientific terms and equations. Make it natural and appropriate for students.

Original text:
{text}

Translated text:"""
            
            response = self.model.generate_content(prompt)
            return response.text
        
        except Exception as e:
            print(f"Translation error: {e}")
            return text
    
    def generate_practice_questions(self, concept, topic, count=3):
        """
        Generate practice questions for a concept.
        
        Args:
            concept (str): The concept name
            topic (str): Subject/topic
            count (int): Number of questions to generate
        
        Returns:
            list: Practice questions
        """
        if not self.enabled:
            return [f"Practice question about {concept} (LLM not available)"]
        
        try:
            prompt = f"""Generate {count} practice questions about {concept} in {topic}.
Questions should be suitable for O/L students in Sri Lanka.
Include a mix of:
- Conceptual understanding questions
- Application questions
- Short answer questions

Format: Return only the questions, numbered 1, 2, 3, etc."""
            
            response = self.model.generate_content(prompt)
            questions = response.text.strip().split('\n')
            return [q.strip() for q in questions if q.strip()]
        
        except Exception as e:
            print(f"Error generating questions: {e}")
            return [f"Could not generate practice questions for {concept}"]
    
    def provide_hints(self, question):
        """
        Provide hints for solving a problem.
        
        Args:
            question (str): The question/problem
        
        Returns:
            str: Hints for solving
        """
        if not self.enabled:
            return "Hints not available (LLM not enabled)"
        
        try:
            prompt = f"""A student is stuck on this question:
{question}

Provide 2-3 helpful hints (not the full answer) to guide them toward the solution.
Make hints progressive (start with gentle nudges, then more specific).

Hints:"""
            
            response = self.model.generate_content(prompt)
            return response.text
        
        except Exception as e:
            print(f"Error generating hints: {e}")
            return "Could not generate hints"
    
    def is_enabled(self):
        """Check if LLM is available and configured."""
        return self.enabled


class HybridSystem:
    """
    Combines Expert System (MAS) with LLM enhancement.
    Provides the best of both: reliable facts + natural language.
    """
    
    def __init__(self, coordinator_agent, llm_interface):
        self.coordinator = coordinator_agent
        self.llm = llm_interface
        self.use_llm = llm_interface.is_enabled()
    
    def process_question(self, question, language='en', use_llm=None):
        """
        Process question through MAS + LLM pipeline.
        
        Args:
            question (str): Student's question
            language (str): Response language ('en', 'si', 'ta')
            use_llm (bool): Override LLM usage
        
        Returns:
            dict: Enhanced response
        """
        # Get expert system response from MAS
        expert_response = self.coordinator.process_question(question)
        
        # Determine if we should use LLM
        should_use_llm = use_llm if use_llm is not None else self.use_llm
        
        if should_use_llm:
            # Enhance with LLM
            enhanced_explanation = self.llm.enhance_explanation(
                expert_response,
                language=language
            )
            expert_response['enhanced_explanation'] = enhanced_explanation
            expert_response['llm_enhanced'] = True
        else:
            expert_response['enhanced_explanation'] = expert_response.get('explanation')
            expert_response['llm_enhanced'] = False
        
        expert_response['language'] = language
        
        return expert_response
    
    def get_system_info(self):
        """Get information about the hybrid system."""
        return {
            'mas_enabled': True,
            'llm_enabled': self.use_llm,
            'agents_available': len(self.coordinator.agents),
            'languages_supported': ['en', 'si', 'ta'] if self.use_llm else ['en']
        }
