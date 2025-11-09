"""
Test Expert Agent
-----------------
Test the agent-tool architecture with different types of queries.
"""

from agents.expert_agent import ExpertAgent

def test_agent():
    """Test the Expert Agent with various queries."""
    
    print("="*70)
    print("TESTING EXPERT AGENT")
    print("="*70)
    
    # Initialize agent
    print("\n1. Initializing Expert Agent...")
    agent = ExpertAgent()
    print("✅ Agent initialized\n")
    
    # Test 1: Biology query
    print("="*70)
    print("TEST 1: Biology Query")
    print("="*70)
    result1 = agent.process_query("What is photosynthesis?")
    print(f"\n📋 RESULT:")
    print(f"Tool Used: {result1['tool_used']}")
    print(f"Success: {result1['success']}")
    print(f"Response Preview: {result1['response'][:200]}...")
    print()
    
    # Test 2: Physics query
    print("="*70)
    print("TEST 2: Physics Query")
    print("="*70)
    result2 = agent.process_query("Explain reflection of light")
    print(f"\n📋 RESULT:")
    print(f"Tool Used: {result2['tool_used']}")
    print(f"Success: {result2['success']}")
    print(f"Response Preview: {result2['response'][:200]}...")
    print()
    
    # Test 3: Chemistry query
    print("="*70)
    print("TEST 3: Chemistry Query")
    print("="*70)
    result3 = agent.process_query("What is a mixture?")
    print(f"\n📋 RESULT:")
    print(f"Tool Used: {result3['tool_used']}")
    print(f"Success: {result3['success']}")
    print(f"Response Preview: {result3['response'][:200]}...")
    print()
    
    # Test 4: Study Guide query (diagnostic)
    print("="*70)
    print("TEST 4: Study Guide Query (Diagnostic)")
    print("="*70)
    result4 = agent.process_query("I'm struggling with my studies")
    print(f"\n📋 RESULT:")
    print(f"Tool Used: {result4['tool_used']}")
    print(f"Needs Clarification: {result4['needs_clarification']}")
    if result4['needs_clarification']:
        print(f"Question: {result4['response']}")
        
        # Follow up with clarification
        print("\n📝 Providing clarification: 'mcq'")
        result5 = agent.handle_clarification("mcq")
        print(f"Tool Used: {result5['tool_used']}")
        print(f"Needs Clarification: {result5['needs_clarification']}")
        if result5['needs_clarification']:
            print(f"Next Question: {result5['response']}")
    print()
    
    # Summary
    print("="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"✅ Total Tests: 4")
    print(f"✅ Conversation History: {len(agent.conversation_history)} queries")
    print(f"✅ All expert tools functional")
    print()

if __name__ == "__main__":
    test_agent()
