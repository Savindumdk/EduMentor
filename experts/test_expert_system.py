"""
Test Suite for Advanced Study Guide Expert System
--------------------------------------------------
Demonstrates all features:
1. Knowledge Base loading
2. NLP processing
3. Multi-step inference
4. Confidence scoring
5. Explanation facility
6. User profiling
7. Dynamic learning
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from study_guide_expert import StudyGuideExpert


def print_section(title):
    """Print section header."""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70 + "\n")


def test_basic_queries():
    """Test 1: Basic query processing."""
    print_section("TEST 1: Basic Query Processing")
    
    expert = StudyGuideExpert()
    
    queries = [
        "How can I improve my memory?",
        "I feel very anxious about my exam tomorrow",
        "I keep procrastinating on my assignments",
        "Help me manage my study time"
    ]
    
    for query in queries:
        print(f"📝 Query: {query}")
        response = expert.process_query(query)
        
        if response:
            print(f"   Concept: {response['concept']}")
            print(f"   Confidence: {response['confidence']:.2%}")
            print(f"   Rules Fired: {', '.join(response['fired_rules'])}")
            print()


def test_inference_chaining():
    """Test 2: Multi-step inference chaining."""
    print_section("TEST 2: Multi-Step Inference Chaining")
    
    expert = StudyGuideExpert()
    
    # This query should trigger inference chain
    query = "I'm very stressed about my exam tomorrow"
    print(f"📝 Query: {query}")
    
    response = expert.process_query(query)
    
    if response:
        print(f"\n🎯 Primary Topic: {response['topic']}")
        print(f"📈 Confidence: {response['confidence']:.2%}")
        print(f"\n🧠 Inferred Facts: {', '.join(response['inferred_facts']) if response['inferred_facts'] else 'None'}")
        print(f"\n✅ Rules Fired: {', '.join(response['fired_rules'])}")
        
        print(f"\n💡 Diagnosis:\n{response['diagnosis']}")


def test_user_profiling():
    """Test 3: User profiling with contextual reasoning."""
    print_section("TEST 3: User Profiling & Contextual Reasoning")
    
    expert = StudyGuideExpert()
    
    # Set user profile
    print("👤 Setting user profile:")
    expert.update_user_profile(
        sleep_hours=5,
        stress_level='high',
        study_hours=3
    )
    print(f"   Profile: {expert.get_user_profile()}")
    
    # Query with profile context
    query = "How can I remember more information?"
    print(f"\n📝 Query: {query}")
    
    response = expert.process_query(query)
    
    if response:
        print(f"\n🎯 Topic: {response['topic']}")
        print(f"📈 Confidence: {response['confidence']:.2%}")
        
        # The system should infer sleep affects memory
        if response['inferred_facts']:
            print(f"\n🧠 Inferred from profile:")
            for fact in response['inferred_facts']:
                print(f"   • {fact}")


def test_confidence_scoring():
    """Test 4: Confidence-weighted recommendations."""
    print_section("TEST 4: Confidence-Weighted Recommendations")
    
    expert = StudyGuideExpert()
    
    query = "I'm anxious and can't focus"
    print(f"📝 Query: {query}")
    
    response = expert.process_query(query)
    
    if response:
        print(f"\n📊 Overall Confidence: {response['confidence']:.2%}")
        print(f"\n📝 Top Recommendations:")
        print(response['recommendation'])


def test_explanation_facility():
    """Test 5: Explanation facility - trace reasoning."""
    print_section("TEST 5: Explanation Facility (Reasoning Trace)")
    
    expert = StudyGuideExpert()
    
    query = "I sleep 4 hours and feel stressed about exams"
    print(f"📝 Query: {query}\n")
    
    response = expert.process_query(query)
    
    # Get detailed explanation
    explanation = expert.get_explanation()
    print(explanation)


def test_nlp_processing():
    """Test 6: NLP entity extraction and intent detection."""
    print_section("TEST 6: NLP Processing")
    
    expert = StudyGuideExpert()
    
    queries = [
        "I only sleep 5 hours and have an exam tomorrow",
        "I'm extremely stressed and can't concentrate",
        "How do I stop procrastinating on my homework?"
    ]
    
    for query in queries:
        nlp_result = expert.nlp.process_query(query, expert.kb)
        
        print(f"📝 Query: {query}")
        print(f"   Entities: {nlp_result['entities']}")
        print(f"   Intents: {nlp_result['intents'][:2]}")
        print(f"   Conditions: {nlp_result['conditions']}")
        print()


def test_dynamic_learning():
    """Test 7: Dynamic learning - add new rule to KB."""
    print_section("TEST 7: Dynamic Learning (Add Rule to KB)")
    
    expert = StudyGuideExpert()
    
    print("📚 Current memory rules:")
    memory_rules = expert.kb.get('memory', {}).get('rules', [])
    print(f"   Count: {len(memory_rules)}")
    for rule in memory_rules:
        print(f"   • {rule['id']}: {rule['recommend'][:50]}...")
    
    # Add new rule
    print("\n➕ Adding new rule...")
    new_rule = {
        'id': 'memory_004',
        'condition': 'visual_learner',
        'recommend': 'Use diagrams and mind maps for visual memory encoding',
        'confidence': 0.87,
        'priority': 4
    }
    
    success = expert.add_rule_to_kb('memory', new_rule)
    
    if success:
        print(f"   ✅ Rule '{new_rule['id']}' added successfully!")
        print(f"   New count: {len(expert.kb['memory']['rules'])}")
    else:
        print("   ❌ Failed to add rule")


def test_full_workflow():
    """Test 8: Complete workflow demonstration."""
    print_section("TEST 8: Complete Workflow Example")
    
    expert = StudyGuideExpert()
    
    # Step 1: Set user context
    print("STEP 1: Set User Profile")
    expert.update_user_profile(
        user_type='university_student',
        sleep_hours=6,
        stress_level='high',
        exam_in_days=3
    )
    print(f"   Profile: {expert.get_user_profile()}\n")
    
    # Step 2: Process query
    print("STEP 2: Process Query")
    query = "I need help preparing for my exam but I'm too stressed"
    print(f"   Query: {query}\n")
    
    response = expert.process_query(query)
    
    # Step 3: Show results
    print("STEP 3: Results")
    if response:
        print(f"   📊 Confidence: {response['confidence']:.2%}")
        print(f"   🎯 Concept: {response['concept']}")
        print(f"   🧠 Inferred: {', '.join(response['inferred_facts'])}")
        print(f"   ✅ Rules: {', '.join(response['fired_rules'])}")
        
        print(f"\n   💡 Diagnosis:")
        print(f"   {response['diagnosis']}")
        
        print(f"\n   📝 Recommendations:")
        for i, line in enumerate(response['recommendation'].split('\n\n'), 1):
            print(f"      {line}")


def run_all_tests():
    """Run complete test suite."""
    print("\n" + "🧪 "*20)
    print("  ADVANCED STUDY GUIDE EXPERT SYSTEM - TEST SUITE")
    print("🧪 "*20)
    
    try:
        test_basic_queries()
        test_inference_chaining()
        test_user_profiling()
        test_confidence_scoring()
        test_explanation_facility()
        test_nlp_processing()
        test_dynamic_learning()
        test_full_workflow()
        
        print_section("✅ ALL TESTS COMPLETED SUCCESSFULLY")
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    run_all_tests()
