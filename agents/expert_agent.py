"""
Expert Agent
------------
Main agent that coordinates all expert systems using them as tools.
Uses Gemini LLM to understand queries and select appropriate expert tools.
"""

import google.generativeai as genai
from typing import Dict, Any, List
import os
from dotenv import load_dotenv

from experts.biology_expert import BiologyExpert
from experts.physics_expert import PhysicsExpert
from experts.chemistry_expert import ChemistryExpert
from experts.study_guide_expert import StudyGuideExpert

load_dotenv()


class ExpertAgent:
    """
    Main agent that uses expert systems as tools.
    
    The agent:
    1. Receives a user query
    2. Analyzes which expert system tool to use
    3. Extracts appropriate query parameters
    4. Calls the expert system tool
    5. Returns the result
    """
    
    def __init__(self):
        """Initialize the Expert Agent with all tools."""
        # Initialize Gemini
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash-exp')
        
        # Initialize expert system tools
        self.tools = {
            'biology_expert': BiologyExpert(),
            'physics_expert': PhysicsExpert(),
            'chemistry_expert': ChemistryExpert(),
            'study_guide_expert': StudyGuideExpert()
        }
        
        # Reset all expert systems
        for tool in self.tools.values():
            tool.reset()
        
        # Conversation history for context
        self.conversation_history = []
        
        print("✅ Expert Agent initialized with tools:")
        print(f"   - Biology Expert (Knowledge Base)")
        print(f"   - Physics Expert (Knowledge Base)")
        print(f"   - Chemistry Expert (Knowledge Base)")
        print(f"   - Study Guide Expert (Diagnostic)")
    
    def _get_available_topics(self, expert_name: str) -> List[str]:
        """
        Extract all available topics from an expert system by inspecting its rules.
        
        Args:
            expert_name: Name of the expert ('biology_expert', etc.)
            
        Returns:
            List of topic names
        """
        expert = self.tools.get(expert_name)
        if not expert:
            return []
        
        topics = []
        # Get all methods that start with 'rule_'
        for attr_name in dir(expert):
            if attr_name.startswith('rule_'):
                # Extract topic from method name (e.g., 'rule_digestion_of_food' -> 'digestion_of_food')
                topic = attr_name.replace('rule_', '')
                topics.append(topic)
        
        return sorted(topics)
    
    def _find_matching_topics(self, query: str, expert_name: str, max_results: int = 10) -> List[Dict[str, Any]]:
        """
        Find topics that match keywords in the user query.
        
        Args:
            query: User's query
            expert_name: Expert to search topics in
            max_results: Maximum number of matches to return
            
        Returns:
            List of {topic: str, score: int} dictionaries sorted by relevance
        """
        # Get all topics
        all_topics = self._get_available_topics(expert_name)
        
        # Extract keywords from query (lowercase, remove common words)
        query_lower = query.lower()
        stop_words = {'what', 'are', 'is', 'the', 'a', 'an', 'of', 'in', 'on', 'at', 'to', 'for', 'with', 'about', 'tell', 'me', 'explain', 'describe', 'available'}
        query_words = [w for w in query_lower.split() if w not in stop_words and len(w) > 2]
        
        # Score each topic
        matches = []
        for topic in all_topics:
            score = 0
            topic_lower = topic.lower()
            topic_words = topic_lower.split('_')
            
            # HIGHEST PRIORITY: Multiple key words match exactly
            exact_word_matches = sum(1 for word in query_words if word in topic_words)
            score += exact_word_matches * 50  # 50 points per exact word match
            
            # MEDIUM PRIORITY: Word appears anywhere in topic (substring)
            for word in query_words:
                if word in topic_lower and word not in topic_words:
                    score += 20
            
            # LOW PRIORITY: Partial word matches (e.g., "digest" in "digestion")
            for word in query_words:
                if len(word) > 4:  # Only for longer words
                    for topic_word in topic_words:
                        if len(topic_word) > 4 and (word in topic_word or topic_word in word):
                            if word not in topic_words:  # Don't double count exact matches
                                score += 5
            
            if score > 0:
                matches.append({'topic': topic, 'score': score})
        
        # Sort by score (descending) and return top results
        matches.sort(key=lambda x: x['score'], reverse=True)
        return matches[:max_results]
    
    def _get_tool_descriptions(self) -> str:
        """Get descriptions of available tools for the LLM."""
        return """
Available Expert System Tools:

1. **biology_expert**: Use for Biology questions (O/L syllabus)
   - Topics: Living tissues, animal tissues, plant tissues, photosynthesis, respiration, digestion, cells, reproduction, nervous system
   - Returns: Concept explanation, examples, topic classification
   - Usage: Declare Fact(query_topic='topic_name') where topic_name matches the specific biology concept
   
   **IMPORTANT - Be SPECIFIC with topic names:**
   - For "tissues in animals" → use 'animal_tissues' or 'main_types_of_animal_tissues' (NOT 'living_tissues')
   - For "plant tissues" → use 'plant_tissues' (NOT 'living_tissues')
   - For "epithelial tissue" → use 'epithelial_tissue'
   - For "types of respiration" → use 'types_of_respiration' or 'aerobic_respiration'
   - Always choose the MOST SPECIFIC topic that matches the query

2. **physics_expert**: Use for Physics questions (O/L syllabus)
   - Topics: Waves, sound, light, optics, forces, motion, energy, electricity, heat
   - Returns: Concept explanation, examples, topic classification
   - Usage: Declare Fact(query_topic='topic_name') where topic_name matches the specific physics concept

3. **chemistry_expert**: Use for Chemistry questions (O/L syllabus)
   - Topics: Mixtures, solutions, separation techniques, acids, bases, chemical reactions
   - Returns: Concept explanation, examples, topic classification
   - Usage: Declare Fact(query_topic='topic_name') where topic_name matches the specific chemistry concept

4. **study_guide_expert**: Use for study guidance and diagnostic questions
   - Topics: Study weaknesses, MCQ strategies, essay writing, exam preparation
   - Returns: Personalized diagnosis through progressive questioning
   - Usage: Progressive questioning system - responds to student's study problems

CRITICAL - Topic Selection Strategy:
- ALWAYS choose the MOST SPECIFIC topic available
- If query asks about "animal tissues", use 'animal_tissues' NOT 'living_tissues'
- If query asks about "types of X", look for 'types_of_x' or 'main_types_of_x'
- Broad topics like 'living_tissues' should only be used for very general questions
- Use underscore_separated lowercase names
"""
    
    def _analyze_query(self, user_query: str) -> Dict[str, Any]:
        """
        Use LLM to analyze which tool to use and extract parameters.
        Can detect MULTIPLE topics in a single query.
        NOW WITH INTELLIGENT TOPIC MATCHING!
        
        Args:
            user_query: User's question
            
        Returns:
            Dict with tool_name, topics (list), and reasoning
        """
        # STEP 1: Pre-search for matching topics in each expert
        bio_matches = self._find_matching_topics(user_query, 'biology_expert', max_results=5)
        phys_matches = self._find_matching_topics(user_query, 'physics_expert', max_results=5)
        chem_matches = self._find_matching_topics(user_query, 'chemistry_expert', max_results=5)
        
        # Build suggested topics string
        suggested_topics = ""
        if bio_matches:
            suggested_topics += "\n**Suggested Biology Topics (ranked by relevance):**\n"
            for match in bio_matches:
                suggested_topics += f"  - '{match['topic']}' (relevance: {match['score']})\n"
        if phys_matches:
            suggested_topics += "\n**Suggested Physics Topics (ranked by relevance):**\n"
            for match in phys_matches:
                suggested_topics += f"  - '{match['topic']}' (relevance: {match['score']})\n"
        if chem_matches:
            suggested_topics += "\n**Suggested Chemistry Topics (ranked by relevance):**\n"
            for match in chem_matches:
                suggested_topics += f"  - '{match['topic']}' (relevance: {match['score']})\n"
        
        # STEP 2: Ask LLM to choose from the suggested topics
        prompt = f"""You are an expert system coordinator. Analyze this student query and determine:
1. Which expert tool to use
2. What query_topic(s) to pass (MUST choose from the suggested topics below)
3. Your reasoning

User Query: "{user_query}"

{suggested_topics if suggested_topics else "No matching topics found - use your best judgment."}

⚠️ CRITICAL INSTRUCTIONS:
1. You MUST choose topic names from the "Suggested Topics" list above
2. The suggested topics are ACTUAL topics available in the expert systems (ranked by relevance)
3. Choose the MOST RELEVANT topic(s) that best answer the user's question
4. You can select MULTIPLE topics if the query asks about multiple things
5. Higher relevance scores indicate better matches

{self._get_tool_descriptions()}

Respond in this EXACT format (use multiple TOPIC lines if multiple topics needed):
TOOL: <tool_name>
TOPIC: <query_topic_1_from_suggestions>
TOPIC: <query_topic_2_from_suggestions>
...
REASONING: <your reasoning - explain which suggested topics you chose and why>

Example Response:
Query: "What are the digestive processes?"
Suggested Topics show: 'digestion_of_food', 'mechanical_process__digestion_', 'chemical_process__digestion_'

TOOL: biology_expert
TOPIC: digestion_of_food
TOPIC: mechanical_process__digestion_
TOPIC: chemical_process__digestion_
REASONING: The query asks about digestive "processes" (plural), which includes both mechanical and chemical digestion. Selected all three most relevant topics to provide comprehensive answer."""

        try:
            response = self.model.generate_content(prompt)
            text = response.text.strip()
            
            # Parse response - NOW SUPPORTS MULTIPLE TOPICS
            lines = text.split('\n')
            result = {
                'tool_name': None,
                'topics': [],  # Changed from query_topic to topics (list)
                'reasoning': None
            }
            
            for line in lines:
                if line.startswith('TOOL:'):
                    result['tool_name'] = line.replace('TOOL:', '').strip()
                elif line.startswith('TOPIC:'):
                    # Collect all TOPIC lines
                    topic = line.replace('TOPIC:', '').strip()
                    if topic:
                        result['topics'].append(topic)
                elif line.startswith('REASONING:'):
                    result['reasoning'] = line.replace('REASONING:', '').strip()
            
            # Backward compatibility: if no topics found, try old format
            if not result['topics']:
                result['topics'] = ['general']
            
            return result
            
        except Exception as e:
            print(f"❌ Error analyzing query: {e}")
            return {
                'tool_name': 'biology_expert',  # Default fallback
                'topics': ['general'],
                'reasoning': f'Error in analysis: {e}'
            }
    
    def _execute_tool(self, tool_name: str, query_topic: str) -> Dict[str, Any]:
        """
        Execute the selected expert system tool.
        
        Args:
            tool_name: Name of the tool to use
            query_topic: Topic to query
            
        Returns:
            Expert system response
        """
        if tool_name not in self.tools:
            return {
                'success': False,
                'error': f"Tool '{tool_name}' not found",
                'available_tools': list(self.tools.keys())
            }
        
        expert = self.tools[tool_name]
        
        # Reset and prepare expert
        expert.reset()
        
        # Handle different expert types
        if tool_name == 'study_guide_expert':
            # Study guide uses diagnostic questioning
            expert.run()
            
            if expert.requires_clarification():
                return {
                    'success': True,
                    'needs_clarification': True,
                    'clarification_question': expert.get_clarification_question(),
                    'tool_used': tool_name
                }
            elif expert.is_diagnosis_complete():
                return {
                    'success': True,
                    'response': expert.get_response(),
                    'tool_used': tool_name
                }
        else:
            # Information experts use query_topic
            from experta import Fact
            expert.declare(Fact(query_topic=query_topic))
            expert.run()
            
            response = expert.get_response()
            
            if response:
                return {
                    'success': True,
                    'response': response,
                    'tool_used': tool_name,
                    'query_topic': query_topic
                }
            else:
                return {
                    'success': False,
                    'error': f"No match found for topic '{query_topic}'",
                    'tool_used': tool_name,
                    'suggestion': 'Try rephrasing or using more specific terms'
                }
        
        return {
            'success': False,
            'error': 'Unknown expert state',
            'tool_used': tool_name
        }
    
    def _enhance_response(self, tool_result: Dict[str, Any], user_query: str) -> str:
        """
        Use LLM to enhance the expert system response.
        
        Args:
            tool_result: Result from expert system tool
            user_query: Original user query
            
        Returns:
            Enhanced natural language response
        """
        if not tool_result.get('success'):
            # Handle errors
            error_msg = tool_result.get('error', 'Unknown error')
            return f"I encountered an issue: {error_msg}\n\nPlease try rephrasing your question or asking about a different topic."
        
        if tool_result.get('needs_clarification'):
            # Return clarification question as-is
            return tool_result['clarification_question']
        
        # Get the expert response
        expert_response = tool_result.get('response', {})
        
        if not expert_response:
            return "I couldn't find specific information about that. Could you rephrase your question?"
        
        # Check if we have multiple matching rules
        if isinstance(expert_response, list) and len(expert_response) > 1:
            # Multiple rules matched - synthesize them
            return self._synthesize_multiple_rules(expert_response, user_query, tool_result.get('tool_used'))
        
        # Single response - handle normally
        if isinstance(expert_response, list):
            expert_response = expert_response[0]
        
        # Extract information
        concept = expert_response.get('concept', 'Unknown')
        explanation = expert_response.get('explanation', '')
        examples = expert_response.get('examples', [])
        topic = expert_response.get('topic', '')
        
        # Use LLM to create natural response
        prompt = f"""You are an O/L tutor. A student asked: "{user_query}"

The expert system provided this information:
- Concept: {concept}
- Explanation: {explanation}
- Examples: {', '.join(examples) if examples else 'None'}
- Subject: {topic}

Create a clear, natural response that:
1. Directly answers the student's question
2. Uses the EXACT information from the expert system (don't add new facts)
3. Incorporates the examples naturally
4. Is conversational and encouraging
5. Stays within O/L syllabus scope

Keep it concise (3-4 paragraphs max)."""

        try:
            response = self.model.generate_content(prompt)
            enhanced = response.text.strip()
            
            # Add attribution
            return f"{enhanced}\n\n---\n*Source: {topic} Expert System*"
            
        except Exception as e:
            print(f"⚠️ Error enhancing response: {e}")
            # Fallback to raw expert response
            result = f"**{concept}**\n\n{explanation}"
            if examples:
                result += f"\n\n**Examples:**\n" + "\n".join(f"- {ex}" for ex in examples)
            return result
    
    def _synthesize_multiple_rules(self, responses: list, user_query: str, tool_used: str, topics: list = None) -> str:
        """
        Synthesize multiple matching rules into a comprehensive response.
        
        Args:
            responses: List of expert system responses
            user_query: Original user query
            tool_used: Name of the tool that was used
            topics: Optional list of query topics that were searched
            
        Returns:
            Synthesized comprehensive response
        """
        print(f"   🔍 Multiple rules matched: {len(responses)} responses found")
        print(f"   📚 Synthesizing comprehensive answer...")
        
        # Build comprehensive information from all responses
        all_concepts = []
        all_explanations = []
        all_examples = []
        topics = set()
        
        for i, resp in enumerate(responses, 1):
            concept = resp.get('concept', f'Concept {i}')
            explanation = resp.get('explanation', '')
            examples = resp.get('examples', [])
            topic = resp.get('topic', '')
            
            all_concepts.append(f"{i}. {concept}")
            if explanation:
                all_explanations.append(f"**{concept}:** {explanation}")
            all_examples.extend(examples)
            if topic:
                topics.add(topic)
        
        # Create synthesis prompt
        prompt = f"""You are an O/L tutor. A student asked: "{user_query}"

The expert system found {len(responses)} RELATED concepts that match this query. Your task is to synthesize these into ONE comprehensive, well-organized answer.

MATCHED CONCEPTS:
{chr(10).join(all_concepts)}

DETAILED INFORMATION:
{chr(10).join(all_explanations)}

EXAMPLES FROM ALL CONCEPTS:
{', '.join(all_examples[:10]) if all_examples else 'None'}

TASK: Create a comprehensive response that:
1. Acknowledges that the query relates to multiple interconnected concepts
2. Synthesizes the information into a coherent, logical flow
3. Shows how the concepts relate to each other
4. Uses ONLY the information provided (don't add new facts)
5. Incorporates relevant examples naturally
6. Organizes with clear sections/headings if needed
7. Is conversational and student-friendly
8. Stays within O/L syllabus scope

IMPORTANT: Don't just list the concepts separately - INTEGRATE them into a unified explanation that shows their relationships and provides a complete understanding.

Keep it well-structured but concise (4-6 paragraphs or use sections)."""

        try:
            response = self.model.generate_content(prompt)
            synthesized = response.text.strip()
            
            # Add metadata
            topic_str = ', '.join(topics) if topics else tool_used.replace('_', ' ').title()
            match_count = f"\n\n---\n*Source: {topic_str} Expert System ({len(responses)} related concepts)*"
            
            return f"{synthesized}{match_count}"
            
        except Exception as e:
            print(f"⚠️ Error synthesizing responses: {e}")
            # Fallback to listing all responses
            result = f"I found {len(responses)} related concepts:\n\n"
            for i, resp in enumerate(responses, 1):
                concept = resp.get('concept', 'Concept')
                explanation = resp.get('explanation', '')
                result += f"**{i}. {concept}**\n{explanation}\n\n"
            return result
    
    def process_query(self, user_query: str) -> Dict[str, Any]:
        """
        Main entry point: Process a user query using expert tools.
        NOW SUPPORTS MULTIPLE TOPICS in a single query.
        
        Args:
            user_query: User's question
            
        Returns:
            Dict with response and metadata
        """
        print(f"\n{'='*60}")
        print(f"🤖 EXPERT AGENT: Processing query")
        print(f"{'='*60}")
        print(f"Query: {user_query}\n")
        
        # Step 1: Analyze query to determine tool and parameters
        print("📊 Step 1: Analyzing query...")
        analysis = self._analyze_query(user_query)
        topics = analysis.get('topics', [])
        print(f"   Selected Tool: {analysis['tool_name']}")
        print(f"   Query Topics: {', '.join(topics)}")
        print(f"   Reasoning: {analysis['reasoning']}\n")
        
        # Step 2: Execute expert system tool for EACH topic
        print(f"🔧 Step 2: Executing expert tool for {len(topics)} topic(s)...")
        all_responses = []
        all_tool_results = []
        
        for i, topic in enumerate(topics, 1):
            print(f"   [{i}/{len(topics)}] Querying topic: {topic}")
            tool_result = self._execute_tool(
                analysis['tool_name'],
                topic
            )
            all_tool_results.append(tool_result)
            
            if tool_result.get('success'):
                response = tool_result.get('response')
                if isinstance(response, list):
                    # Multiple matches for this topic
                    all_responses.extend(response)
                    print(f"       ✅ Found {len(response)} matches")
                elif response:
                    all_responses.append(response)
                    print(f"       ✅ Found 1 match")
            else:
                print(f"       ⚠️ No match found")
        
        print(f"   Total matches: {len(all_responses)}\n")
        
        # Step 3: Synthesize if multiple topics or multiple matches
        if len(all_responses) > 1:
            print("✨ Step 3: Synthesizing multiple responses...")
            enhanced_response = self._synthesize_multiple_rules(
                all_responses, 
                user_query, 
                analysis['tool_name'],
                topics
            )
            print(f"   ✅ Synthesized {len(all_responses)} concepts\n")
        elif len(all_responses) == 1:
            print("✨ Step 3: Enhancing single response...")
            # Create a fake tool_result for compatibility
            fake_result = {
                'success': True,
                'response': all_responses[0]
            }
            enhanced_response = self._enhance_response(fake_result, user_query)
            print(f"   ✅ Response enhanced\n")
        else:
            print("⚠️ Step 3: No responses found")
            enhanced_response = "I couldn't find information about that topic. Could you rephrase your question?"
            print()
        
        print(f"{'='*60}\n")
        
        # Build final result
        result = {
            'response': enhanced_response,
            'tool_used': analysis['tool_name'],
            'query_topics': topics,  # Changed to plural
            'success': len(all_responses) > 0,
            'needs_clarification': False,
            'raw_expert_response': all_responses,
            'analysis': analysis
        }
        
        # Store in conversation history
        self.conversation_history.append({
            'query': user_query,
            'result': result
        })
        
        return result
    
    def handle_clarification(self, user_response: str) -> Dict[str, Any]:
        """
        Handle user's response to a clarification question.
        
        Args:
            user_response: User's answer to clarification
            
        Returns:
            Dict with response and metadata
        """
        print(f"\n🔄 Handling clarification response: {user_response}")
        
        # For study guide expert, continue diagnostic
        expert = self.tools['study_guide_expert']
        expert.declare_user_response(user_response)
        expert.run()
        
        if expert.requires_clarification():
            return {
                'response': expert.get_clarification_question(),
                'needs_clarification': True,
                'tool_used': 'study_guide_expert'
            }
        elif expert.is_diagnosis_complete():
            response = expert.get_response()
            enhanced = self._enhance_response(
                {'success': True, 'response': response},
                user_response
            )
            return {
                'response': enhanced,
                'needs_clarification': False,
                'tool_used': 'study_guide_expert',
                'diagnosis_complete': True
            }
        
        return {
            'response': "Let me help you with that...",
            'needs_clarification': False
        }
    
    def reset(self):
        """Reset all expert systems and clear history."""
        for tool in self.tools.values():
            tool.reset()
        self.conversation_history = []
        print("🔄 Expert Agent reset complete")
