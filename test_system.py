"""
Test Suite for Phase 2+3: Multi-Agent System + LLM
---------------------------------------------------
Tests the MAS coordinator, specialized agents, and LLM integration.
"""

import sys
sys.path.append('.')

from agents.coordinator_agent import CoordinatorAgent
from llm.gemini_interface import GeminiInterface, HybridSystem
from utils.language_detector import detect_language
from utils.response_formatter import format_response
import os


def print_section(title):
    """Print a formatted section header."""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70 + "\n")


def test_coordinator_routing():
    """Test 1: Coordinator routing to correct agents."""
    print_section("TEST 1: Coordinator Agent Routing")
    
    coordinator = CoordinatorAgent()
    
    test_questions = [
        ("What is friction?", "PhysicsAgent"),
        ("Explain photosynthesis", "BiologyAgent"),
        ("What are acids?", "ChemistryAgent"),
        ("How do I solve quadratic equations?", "MathematicsAgent"),
        ("Tell me about ancient Sri Lanka", "HistoryAgent"),
        ("How can I manage my time better?", "StudyGuideAgent"),
    ]
    
    print("Testing question routing to correct agents...\n")
    
    passed = 0
    failed = 0
    
    for question, expected_agent in test_questions:
        response = coordinator.process_question(question)
        actual_agent = response.get('agent', 'Unknown')
        
        if expected_agent in actual_agent:
            print(f"✓ PASS: '{question}'")
            print(f"  → Routed to: {actual_agent}\n")
            passed += 1
        else:
            print(f"✗ FAIL: '{question}'")
            print(f"  → Expected: {expected_agent}, Got: {actual_agent}\n")
            failed += 1
    
    print(f"\nRouting Test Results: {passed} passed, {failed} failed")
    return passed, failed


def test_agent_responses():
    """Test 2: Agent knowledge base responses."""
    print_section("TEST 2: Agent Knowledge Base Responses")
    
    coordinator = CoordinatorAgent()
    
    test_cases = [
        {
            'question': 'What is photosynthesis?',
            'expected_keywords': ['photosynthesis', 'plants', 'chlorophyll', 'sunlight'],
            'agent': 'Biology'
        },
        {
            'question': 'Explain gravity',
            'expected_keywords': ['gravity', 'force', 'mass', 'attraction'],
            'agent': 'Physics'
        },
        {
            'question': 'What is combustion?',
            'expected_keywords': ['combustion', 'burning', 'oxygen', 'heat'],
            'agent': 'Chemistry'
        }
    ]
    
    print("Testing agent knowledge base responses...\n")
    
    passed = 0
    failed = 0
    
    for case in test_cases:
        response = coordinator.process_question(case['question'])
        explanation = response.get('explanation', '').lower()
        
        # Check if at least 2 expected keywords are in explanation
        found_keywords = sum(1 for kw in case['expected_keywords'] if kw in explanation)
        
        if found_keywords >= 2:
            print(f"✓ PASS: {case['question']}")
            print(f"  → Found {found_keywords}/{len(case['expected_keywords'])} keywords")
            print(f"  → Agent: {response.get('agent')}\n")
            passed += 1
        else:
            print(f"✗ FAIL: {case['question']}")
            print(f"  → Only found {found_keywords}/{len(case['expected_keywords'])} keywords")
            print(f"  → Explanation: {explanation[:100]}...\n")
            failed += 1
    
    print(f"\nKnowledge Base Test Results: {passed} passed, {failed} failed")
    return passed, failed


def test_language_detection():
    """Test 3: Language detection utility."""
    print_section("TEST 3: Language Detection")
    
    test_cases = [
        ("What is photosynthesis?", "en"),
        ("How do I study better?", "en"),
        # Note: Without actual Sinhala/Tamil text, these will default to 'en'
        # In production, you'd test with real Sinhala/Tamil questions
    ]
    
    print("Testing language detection...\n")
    
    passed = 0
    failed = 0
    
    for text, expected_lang in test_cases:
        detected = detect_language(text)
        
        if detected == expected_lang:
            print(f"✓ PASS: Detected '{expected_lang}' for: {text[:50]}")
            passed += 1
        else:
            print(f"✗ FAIL: Expected '{expected_lang}', got '{detected}' for: {text[:50]}")
            failed += 1
    
    print(f"\nLanguage Detection Results: {passed} passed, {failed} failed")
    return passed, failed


def test_response_formatting():
    """Test 4: Response formatter utility."""
    print_section("TEST 4: Response Formatting")
    
    sample_response = {
        'matched': True,
        'concept': 'photosynthesis',
        'topic': 'Biology',
        'explanation': 'Photosynthesis is the process by which plants make food.',
        'examples': ['Plants use sunlight', 'Chlorophyll is green'],
        'agent': 'BiologyAgent',
        'llm_enhanced': False,
        'language': 'en'
    }
    
    print("Testing response formatting...\n")
    
    formatted = format_response(sample_response)
    
    required_fields = ['timestamp', 'success', 'concept', 'explanation', 'agent_used']
    missing_fields = [field for field in required_fields if field not in formatted]
    
    if not missing_fields:
        print("✓ PASS: All required fields present in formatted response")
        print(f"  → Fields: {', '.join(formatted.keys())}")
        passed = 1
        failed = 0
    else:
        print(f"✗ FAIL: Missing fields: {', '.join(missing_fields)}")
        passed = 0
        failed = 1
    
    print(f"\nResponse Formatting Results: {passed} passed, {failed} failed")
    return passed, failed


def test_llm_interface():
    """Test 5: LLM interface initialization."""
    print_section("TEST 5: LLM Interface")
    
    print("Testing Gemini LLM interface...\n")
    
    api_key = os.getenv('GEMINI_API_KEY')
    
    if not api_key or api_key == 'your_gemini_api_key_here':
        print("⚠️ SKIP: GEMINI_API_KEY not configured")
        print("  → Set GEMINI_API_KEY in .env file to test LLM features")
        return 0, 0
    
    llm = GeminiInterface(api_key)
    
    if llm.is_enabled():
        print("✓ PASS: LLM interface initialized successfully")
        print(f"  → Provider: Google Gemini")
        print(f"  → Model: gemini-pro")
        
        # Test basic enhancement (without actually calling API to save quota)
        print("\n  Testing enhancement method availability...")
        
        if hasattr(llm, 'enhance_explanation'):
            print("  ✓ enhance_explanation() method available")
        if hasattr(llm, 'translate_response'):
            print("  ✓ translate_response() method available")
        if hasattr(llm, 'generate_practice_questions'):
            print("  ✓ generate_practice_questions() method available")
        
        passed = 1
        failed = 0
    else:
        print("✗ FAIL: LLM interface failed to initialize")
        passed = 0
        failed = 1
    
    print(f"\nLLM Interface Results: {passed} passed, {failed} failed")
    return passed, failed


def test_hybrid_system():
    """Test 6: Hybrid system (MAS + LLM)."""
    print_section("TEST 6: Hybrid System Integration")
    
    print("Testing hybrid system (MAS + LLM)...\n")
    
    coordinator = CoordinatorAgent()
    llm = GeminiInterface()
    hybrid = HybridSystem(coordinator, llm)
    
    # Test without LLM (should work even if LLM not configured)
    test_question = "What is friction?"
    response = hybrid.process_question(test_question, language='en', use_llm=False)
    
    if response.get('explanation'):
        print("✓ PASS: Hybrid system processed question (Expert System mode)")
        print(f"  → Question: {test_question}")
        print(f"  → Agent: {response.get('agent')}")
        print(f"  → LLM Enhanced: {response.get('llm_enhanced')}")
        passed = 1
        failed = 0
    else:
        print("✗ FAIL: Hybrid system did not return explanation")
        passed = 0
        failed = 1
    
    # Test system info
    info = hybrid.get_system_info()
    print(f"\n  System Info:")
    print(f"  → MAS Enabled: {info['mas_enabled']}")
    print(f"  → LLM Enabled: {info['llm_enabled']}")
    print(f"  → Agents: {info['agents_available']}")
    print(f"  → Languages: {', '.join(info['languages_supported'])}")
    
    print(f"\nHybrid System Results: {passed} passed, {failed} failed")
    return passed, failed


def test_agent_statistics():
    """Test 7: Agent usage statistics."""
    print_section("TEST 7: Agent Statistics")
    
    print("Testing agent statistics tracking...\n")
    
    coordinator = CoordinatorAgent()
    
    # Ask multiple questions to different agents
    questions = [
        "What is friction?",
        "Explain photosynthesis",
        "What is gravity?",
        "What are acids?",
    ]
    
    for q in questions:
        coordinator.process_question(q)
    
    stats = coordinator.get_agent_statistics()
    
    if stats:
        print("✓ PASS: Statistics tracking working")
        print("\n  Agent Usage:")
        for agent, count in stats.items():
            print(f"  → {agent}: {count} questions")
        passed = 1
        failed = 0
    else:
        print("✗ FAIL: No statistics recorded")
        passed = 0
        failed = 1
    
    print(f"\nStatistics Results: {passed} passed, {failed} failed")
    return passed, failed


def run_all_tests():
    """Run all test suites."""
    print("""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║         EduMentor Phase 2+3 Test Suite                          ║
║         Multi-Agent System + LLM Integration Tests              ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
""")
    
    total_passed = 0
    total_failed = 0
    
    # Run all tests
    tests = [
        test_coordinator_routing,
        test_agent_responses,
        test_language_detection,
        test_response_formatting,
        test_llm_interface,
        test_hybrid_system,
        test_agent_statistics,
    ]
    
    for test_func in tests:
        try:
            passed, failed = test_func()
            total_passed += passed
            total_failed += failed
        except Exception as e:
            print(f"\n❌ Test crashed: {test_func.__name__}")
            print(f"   Error: {e}")
            total_failed += 1
    
    # Final summary
    print_section("FINAL TEST SUMMARY")
    print(f"Total Tests Passed: {total_passed}")
    print(f"Total Tests Failed: {total_failed}")
    print(f"Success Rate: {total_passed/(total_passed+total_failed)*100:.1f}%")
    
    if total_failed == 0:
        print("\n🎉 All tests passed! System is ready for use.")
    else:
        print(f"\n⚠️ {total_failed} tests failed. Please review the errors above.")
    
    print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    run_all_tests()
