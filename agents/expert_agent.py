"""
Expert Agent
------------
Main agent that coordinates subject expert systems (Biology, Physics, Chemistry).
Study Guide is now a standalone system in a separate tab.
Uses OpenAI LLM to understand queries and select appropriate expert tools.
"""

from openai import OpenAI
from typing import Dict, Any, List
import os
from dotenv import load_dotenv

from experts.biology_expert import BiologyExpert
from experts.physics_expert import PhysicsExpert
from experts.chemistry_expert import ChemistryExpert

load_dotenv()


class ExpertAgent:
    """
    Main agent that uses subject expert systems as tools.
    
    The agent:
    1. Receives a user query
    2. Analyzes which expert system tool to use
    3. Extracts appropriate query parameters
    4. Calls the expert system tool
    5. Returns the result
    
    Note: Study Guide Expert is now standalone in separate tab.
    """
    
    def __init__(self):
        """Initialize the Expert Agent with subject expert tools."""
        # Initialize OpenAI
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4o-mini"  # Using GPT-4o-mini for cost efficiency
        
        # Initialize subject expert system tools (Study Guide moved to separate tab)
        self.tools = {
            'biology_expert': BiologyExpert(),
            'physics_expert': PhysicsExpert(),
            'chemistry_expert': ChemistryExpert()
        }
        
        # Reset all expert systems
        for tool in self.tools.values():
            tool.reset()
        
        # Conversation history for context
        self.conversation_history = []
        
        # Track the last offered topic for follow-up confirmations
        self.last_offered_topic = None
        self.last_tool_used = None
        
        print("✅ Expert Agent initialized with tools:")
        print("   - Biology Expert (Knowledge Base)")
        print("   - Physics Expert (Knowledge Base)")
        print("   - Chemistry Expert (Knowledge Base)")
    
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

NOTE: Study Guide expert is now handled in a separate tab and not available through this agent.

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
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert system coordinator for an O/L tutoring system."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=500
            )
            text = response.choices[0].message.content.strip()
            
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
        
        # Information experts (Biology, Physics, Chemistry) use query_topic
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
        
        # Use LLM to create natural response that targets the specific question
        prompt = f"""You are an O/L tutor helping a student. The student asked: "{user_query}"

**EXPERT SYSTEM OUTPUT (YOUR ONLY SOURCE OF INFORMATION):**
- Concept: {concept}
- Explanation: {explanation}
- Examples: {', '.join(examples[:3]) if examples else 'None'}
- Subject: {topic}

**YOUR TASK:**

1. **Answer the SPECIFIC question asked** - Don't provide a general overview. Target exactly what the student wants to know.

2. **Prioritize relevance** - Start with the most relevant information from the expert system that directly addresses their question.

3. **Use ONLY the expert system information** - Do NOT add external facts, concepts, or examples not provided above.

4. **Progressive guidance with ONE SPECIFIC actionable question** - After answering, ask exactly 1 follow-up question that:
   - Is SPECIFIC and ACTIONABLE (e.g., "Shall I explain epithelial tissue next?" not "Which tissue interests you?")
   - Offers to explain a specific sub-topic or related concept from the expert system
   - Guides them to the next logical learning step
   - Uses phrases like "Shall I...", "Would you like me to...", "Let me know if you'd like..."
   - References a specific topic/concept from the expert system output
   - Can be answered with a simple "yes" or short response

5. **Format:**
   - Start with direct answer (2-3 paragraphs max)
   - Include relevant examples from expert system
   - Add brief reasoning (1 sentence explaining why expert system gave this answer)
   - End with EXACTLY 1 SPECIFIC actionable question (prefix with "💭 ")

**CRITICAL CONSTRAINTS:**
- Use ONLY information from the expert system output above
- Do NOT introduce new concepts, facts, or examples
- Do NOT provide information beyond what the expert system provided
- Target the specific question, not a general explanation
- Keep response focused and concise (under 400 words)
- Follow-up questions MUST be specific offers to explain particular topics

**Example Good Response Format:**
[Direct targeted answer based on expert system]

[Relevant example from expert system]

🔍 **Why this answer?** The expert system matched your query to the "{concept}" topic, which provides comprehensive coverage of what you asked about.

 Shall I explain [specific sub-topic from expert system] in more detail?"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system", 
                        "content": "You are an O/L tutor. You MUST use ONLY the expert system information provided. Never add external knowledge. Focus on answering the specific question asked, not providing general overviews. Guide students with EXACTLY 1 SPECIFIC actionable follow-up question (e.g., 'Shall I explain X next?' not 'What interests you?'). The question should be answerable with a simple 'yes'. Always include brief reasoning about why the expert system gave this answer."
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.4,  # Lower temperature for more focused responses
                max_tokens=550  # Slightly increased to accommodate reasoning
            )
            enhanced = response.choices[0].message.content.strip()
            
            # Add attribution
            return f"{enhanced}\n\n---\n*📚 Source: {topic} Expert System*"
            
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
        
        # Create synthesis prompt focused on answering the specific question
        prompt = f"""You are an O/L tutor. The student asked: "{user_query}"

**EXPERT SYSTEM OUTPUT (YOUR ONLY SOURCE):**

The expert system found {len(responses)} related concepts:

CONCEPTS:
{chr(10).join(all_concepts)}

DETAILED INFORMATION:
{chr(10).join(all_explanations)}

EXAMPLES:
{', '.join(all_examples[:10]) if all_examples else 'None'}

**YOUR TASK:**

1. **Answer the SPECIFIC question** - Don't provide a general overview. Focus on what the student actually asked.

2. **Prioritize by relevance** - Start with the most relevant concept that directly answers their question. Mention related concepts only if they help explain the answer.

3. **Use ONLY expert system information** - Do NOT add external facts, concepts, or examples not provided above.

4. **Show connections** - If multiple concepts are needed to answer, explain how they relate, but keep it focused on answering the question.

5. **Progressive guidance with ONE SPECIFIC actionable question** - After answering, ask exactly 1 follow-up question that:
   - Is SPECIFIC and ACTIONABLE (e.g., "Shall I explain mechanical digestion next?" not "What interests you?")
   - Offers to explain a specific sub-topic or related concept from the expert system output
   - Guides them to the next logical learning step
   - Uses phrases like "Shall I...", "Would you like me to...", "Let me know if you'd like..."
   - References a specific topic/concept from the expert system output
   - Can be answered with a simple "yes" or short response

6. **Format:**
   - Start with most relevant information (2-3 paragraphs)
   - Include 1-2 relevant examples from expert system
   - Show concept connections if needed for the answer
   - Add brief reasoning (1 sentence explaining why these concepts were selected)
   - End with EXACTLY 1 SPECIFIC actionable question (prefix with "💭 ")

**CRITICAL CONSTRAINTS:**
- Use ONLY the information from expert system output above
- Do NOT introduce new concepts beyond what's provided
- Target the specific question, not a comprehensive lesson
- Keep focused and concise (under 500 words)
- Don't just list concepts - integrate them to answer the question
- Follow-up questions MUST be specific offers to explain particular topics

**Example Format:**
[Direct answer to the specific question using most relevant concept]

[Supporting explanation using related concepts if needed]

[1-2 relevant examples from expert system]

🔍 **Why this answer?** The expert system identified {len(responses)} related concepts because [brief reasoning about why these concepts match the query].

💭 Shall I explain [specific sub-topic 1 from concepts] in more detail?"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system", 
                        "content": "You are an O/L tutor. CRITICAL: Use ONLY expert system information. Never add external knowledge. Answer the specific question asked - prioritize relevance over comprehensiveness. Guide students with EXACTLY 1 SPECIFIC actionable follow-up question (e.g., 'Shall I explain X next?' not 'What interests you?'). The question should be answerable with a simple 'yes'. Always include brief reasoning about why the expert system selected these concepts."
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.4,  # Lower for more focused responses
                max_tokens=650  # Slightly increased to accommodate reasoning
            )
            synthesized = response.choices[0].message.content.strip()
            
            # Add metadata
            topic_str = ', '.join(topics) if topics else tool_used.replace('_', ' ').title()
            match_count = f"\n\n---\n*📚 Source: {topic_str} Expert System ({len(responses)} related concepts)*"
            
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
    
    def _is_confirmation(self, text: str) -> bool:
        """
        Check if the user's response is a confirmation (yes, okay, sure, etc.).
        
        Args:
            text: User's response
            
        Returns:
            True if it's a confirmation
        """
        text_lower = text.lower().strip()
        confirmations = [
            'yes', 'yeah', 'yep', 'sure', 'ok', 'okay', 'alright', 'fine', 
            'please', 'go ahead', 'continue', 'proceed', 'tell me', 'explain'
        ]
        # Check for exact match or if text is very short and contains a confirmation word
        return text_lower in confirmations or (len(text_lower) < 20 and any(conf in text_lower for conf in confirmations))
    
    def _extract_topic_from_response(self, response_text: str) -> str:
        """
        Extract the topic that was offered in the last response.
        Looks for phrases like "Shall I explain [topic]..." or "Would you like me to... [topic]..."
        
        Args:
            response_text: The last assistant response
            
        Returns:
            Extracted topic name or None
        """
        import re
        
        # Pattern 1: "Shall I explain [topic]..."
        match = re.search(r"Shall I explain (.+?) (?:in more detail|next)", response_text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        
        # Pattern 2: "Would you like me to... [topic]..."
        match = re.search(r"Would you like me to (?:walk you through|explain) (.+?)\?", response_text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        
        # Pattern 3: "Let me know if you'd like... [topic]..."
        match = re.search(r"Let me know if you'd like (?:to learn about|me to explain) (.+?)[.?]", response_text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        
        return None
    
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
        
        # Check if this is a confirmation response to a previous offer
        if self._is_confirmation(user_query) and self.last_offered_topic and self.last_tool_used:
            print(f"✅ Detected confirmation to explain: {self.last_offered_topic}")
            print(f"   Using tool: {self.last_tool_used}\n")
            
            # Create a query for the offered topic
            query_for_topic = self.last_offered_topic
            tool_to_use = self.last_tool_used
            
            # Clear the last offered topic
            self.last_offered_topic = None
            self.last_tool_used = None
            
            # Execute the tool with the offered topic
            print(f"🔧 Executing expert tool for confirmed topic...")
            tool_result = self._execute_tool(tool_to_use, query_for_topic)
            
            if tool_result.get('success'):
                response = tool_result.get('response')
                all_responses = [response] if not isinstance(response, list) else response
                
                # Enhance the response
                print("✨ Enhancing response...")
                if len(all_responses) > 1:
                    enhanced_response = self._synthesize_multiple_rules(
                        all_responses, 
                        f"Explain {query_for_topic}",
                        tool_to_use,
                        [query_for_topic]
                    )
                else:
                    fake_result = {'success': True, 'response': all_responses[0]}
                    enhanced_response = self._enhance_response(fake_result, f"Explain {query_for_topic}")
                
                print(f"   ✅ Response enhanced\n")
                print(f"{'='*60}\n")
                
                # Extract and store new offered topic from the response
                self.last_offered_topic = self._extract_topic_from_response(enhanced_response)
                self.last_tool_used = tool_to_use if self.last_offered_topic else None
                
                result = {
                    'response': enhanced_response,
                    'tool_used': tool_to_use,
                    'query_topics': [query_for_topic],
                    'success': True,
                    'needs_clarification': False,
                    'raw_expert_response': all_responses,
                    'analysis': {'tool_name': tool_to_use, 'topics': [query_for_topic], 'reasoning': 'User confirmed interest in previously offered topic'},
                    'confidence_metrics': None
                }
                
                self.conversation_history.append({'query': user_query, 'result': result})
                return result
            else:
                print(f"   ⚠️ Could not find information about {query_for_topic}\n")
                # Fall through to normal processing
        
        # Step 1: Analyze query to determine tool and parameters
        print("📊 Step 1: Analyzing query...")
        analysis = self._analyze_query(user_query)
        topics = analysis.get('topics', [])
        print(f"   Selected Tool: {analysis['tool_name']}")
        print(f"   Query Topics: {', '.join(topics)}")
        print(f"   Reasoning: {analysis['reasoning']}\n")
        
        # NOTE: Study Guide is now in a separate tab and not handled by this agent
        # Only Biology, Physics, and Chemistry experts are available here
        
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
        
        # Get confidence metrics from the expert if available
        confidence_metrics = None
        if len(all_responses) > 0 and hasattr(self.tools[analysis['tool_name']], 'get_aggregated_confidence'):
            try:
                confidence_metrics = self.tools[analysis['tool_name']].get_aggregated_confidence()
                print(f"📊 Confidence Metrics:")
                print(f"   Aggregate CF: {confidence_metrics.get('aggregate_certainty', 0):.3f}")
                print(f"   Confidence Level: {confidence_metrics.get('confidence_level', 'N/A')}")
                print(f"   Rules Fired: {confidence_metrics.get('num_rules_fired', 0)}\n")
            except Exception as e:
                print(f"⚠️ Could not get confidence metrics: {e}\n")
        
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
        
        # Extract and store the offered topic from the response for next interaction
        self.last_offered_topic = self._extract_topic_from_response(enhanced_response)
        self.last_tool_used = analysis['tool_name'] if self.last_offered_topic else None
        
        if self.last_offered_topic:
            print(f"💡 Stored offered topic for next interaction: '{self.last_offered_topic}'\n")
        
        # Build final result
        result = {
            'response': enhanced_response,
            'tool_used': analysis['tool_name'],
            'query_topics': topics,  # Changed to plural
            'success': len(all_responses) > 0,
            'needs_clarification': False,
            'raw_expert_response': all_responses,
            'analysis': analysis,
            'confidence_metrics': confidence_metrics  # Add confidence metrics
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
        self.last_offered_topic = None
        self.last_tool_used = None
        print("🔄 Expert Agent reset complete")
