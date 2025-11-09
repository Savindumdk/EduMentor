"""
Response Refinement Agent
-------------------------
Takes expert system output and refines it into natural, friendly language using LLM.
"""

import google.generativeai as genai
import os
from config import LLM_MODEL


class ResponseRefinementAgent:
    """
    LLM-powered agent that takes expert system output and makes it more conversational.
    
    CRITICAL: This agent does NOT add new information - it only rephrases
    the expert system's output in a warm, student-friendly way.
    """
    
    def __init__(self):
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
            print(f"✓ Response Refinement Agent initialized with {LLM_MODEL}")
        except Exception as e:
            print(f"❌ Failed to initialize Response Refinement Agent: {e}")
            self.model = None
    
    def refine_response(self, user_question: str, expert_output: dict) -> dict:
        """
        Refine expert system output into natural language.
        
        Args:
            user_question: Original question from user
            expert_output: Dictionary from expert system with 'explanation', 'examples', etc.
        
        Returns:
            {
                'original_rule': '...',  # Original expert system output
                'refined_explanation': '...',  # LLM-refined version
                'concept': '...',
                'topic': '...',
                'examples': [...]
            }
        """
        
        if not self.model:
            # If LLM unavailable, return original
            return {
                'original_rule': expert_output.get('explanation', ''),
                'refined_explanation': expert_output.get('explanation', ''),
                'concept': expert_output.get('concept', ''),
                'topic': expert_output.get('topic', ''),
                'examples': expert_output.get('examples', [])
            }
        
        print("\n🌟 RESPONSE REFINEMENT: Enhancing expert system output")
        print("🔒 CONSTRAINT: LLM will ONLY rephrase - NO new facts")
        
        prompt = self._build_refinement_prompt(user_question, expert_output)
        
        try:
            response = self.model.generate_content(prompt)
            refined = response.text.strip()
            
            print("✓ Response refined successfully")
            
            return {
                'original_rule': expert_output.get('explanation', ''),
                'refined_explanation': refined,
                'concept': expert_output.get('concept', ''),
                'topic': expert_output.get('topic', ''),
                'examples': expert_output.get('examples', [])
            }
            
        except Exception as e:
            print(f"❌ Refinement failed: {e}")
            # Fallback to original
            return {
                'original_rule': expert_output.get('explanation', ''),
                'refined_explanation': expert_output.get('explanation', ''),
                'concept': expert_output.get('concept', ''),
                'topic': expert_output.get('topic', ''),
                'examples': expert_output.get('examples', [])
            }
    
    def _build_refinement_prompt(self, question: str, expert_output: dict) -> str:
        """Build prompt for LLM to refine the response."""
        
        explanation = expert_output.get('explanation', '')
        examples = expert_output.get('examples', [])
        examples_text = "\n".join([f"- {ex}" for ex in examples]) if examples else "No examples provided"
        
        prompt = f"""You are a language enhancement assistant for an educational expert system.
Your ONLY job is to make the expert system's rule-based output more human-friendly.

**CRITICAL INSTRUCTIONS - YOU MUST FOLLOW THESE EXACTLY:**

1. ONLY use information from the rule below - DO NOT add any new facts
2. Your job is ONLY to rephrase the rule in a warm, conversational way
3. Answer the student's specific question using ONLY the information from the rule
4. Relate the rule to the student's question explicitly
5. Keep ALL scientific equations, formulas, chemical symbols EXACTLY as shown
6. Use simple language appropriate for O/L students
7. Be encouraging and supportive in tone
8. Break long paragraphs into shorter, digestible chunks
9. Use bullet points where appropriate
10. Keep the same level of technical accuracy
11. DO NOT introduce analogies or examples that are not in the rule
12. DO NOT add real-world applications unless they're in the original rule
13. Start by directly addressing their question

REMEMBER: You are NOT a knowledge source. You are ONLY making the expert system's output more readable.

**Student's Question:**
"{question}"

**Expert System Rule (YOU MUST USE ONLY THIS INFORMATION):**
{explanation}

**Examples from Knowledge Base:**
{examples_text}

**Your Task:**
Rephrase the above rule to answer the student's question in a warm, conversational way.

**Format:**
[First paragraph: Directly answer their question using the rule]
[Following paragraphs: Elaborate using ONLY information from the rule]
[Relate concepts to the examples if provided]

Respond now with ONLY the refined explanation:"""
        
        return prompt
