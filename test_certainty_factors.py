"""
Test Certainty Factors in Biology Expert System
"""
from experts.biology_expert import BiologyExpert
from experta import Fact

def print_separator(title):
    """Print a formatted separator"""
    print("\n" + "="*70)
    print(f" {title}")
    print("="*70)

def print_response_with_cf(response):
    """Print response with certainty factor information"""
    print(f"\n📚 Concept: {response.get('concept', 'N/A')}")
    print(f"📊 Certainty Factor: {response.get('certainty_factor', 'N/A'):.2f}")
    print(f"🎯 Confidence Level: {response.get('confidence_level', 'N/A')}")
    print(f"\n💡 Explanation:")
    explanation = response.get('explanation', 'N/A')
    if len(explanation) > 200:
        print(f"   {explanation[:200]}...")
    else:
        print(f"   {explanation}")
    
    if response.get('examples'):
        print(f"\n📖 Examples:")
        for ex in response['examples'][:3]:
            print(f"   - {ex}")

def test_single_topic():
    """Test certainty factor for single topic query"""
    print_separator("TEST 1: Single Topic Query - Animal Tissues")
    
    expert = BiologyExpert()
    expert.reset()
    expert.declare(Fact(query_topic='animal_tissues'))
    expert.run()
    
    responses = expert.get_response()
    if isinstance(responses, list):
        print(f"\n✅ Found {len(responses)} matching rules\n")
        for i, resp in enumerate(responses, 1):
            print(f"\n--- Response {i} ---")
            print_response_with_cf(resp)
    else:
        print_response_with_cf(responses)
    
    # Show aggregate confidence
    agg = expert.get_aggregated_confidence()
    print("\n" + "-"*70)
    print("📈 AGGREGATE CONFIDENCE METRICS:")
    print("-"*70)
    print(f"  Aggregate Certainty (Combined): {agg['aggregate_certainty']:.3f}")
    print(f"  Average Certainty: {agg['average_certainty']:.3f}")
    print(f"  Max Certainty: {agg['max_certainty']:.3f}")
    print(f"  Min Certainty: {agg['min_certainty']:.3f}")
    print(f"  Overall Confidence Level: {agg['confidence_level']}")
    print(f"  Number of Rules Fired: {agg['num_rules_fired']}")
    print(f"\n  Distribution:")
    for level, count in agg['certainty_distribution'].items():
        if count > 0:
            print(f"    {level}: {count} rules")

def test_multiple_topics():
    """Test certainty factors across multiple topics"""
    print_separator("TEST 2: Multiple Different Topics")
    
    topics = ['cell_division', 'photosynthesis', 'respiration']
    
    for topic in topics:
        print(f"\n\n{'─'*70}")
        print(f"Topic: {topic.upper()}")
        print('─'*70)
        
        expert = BiologyExpert()
        expert.reset()
        expert.declare(Fact(query_topic=topic))
        expert.run()
        
        responses = expert.get_response()
        if isinstance(responses, list) and len(responses) > 0:
            resp = responses[0]
        else:
            resp = responses if responses else {}
        
        if resp:
            print(f"  Concept: {resp.get('concept', 'N/A')}")
            print(f"  CF: {resp.get('certainty_factor', 0):.2f} | Level: {resp.get('confidence_level', 'N/A')}")
        
        # Show aggregate
        agg = expert.get_aggregated_confidence()
        print(f"  Aggregate CF: {agg['aggregate_certainty']:.3f}")
        print(f"  Rules Fired: {agg['num_rules_fired']}")

def test_cf_combination():
    """Test certainty factor combination"""
    print_separator("TEST 3: Certainty Factor Combination")
    
    expert = BiologyExpert()
    
    print("\n🧮 Testing CF Combination Algebra:")
    print("-"*70)
    
    # Test combining positive CFs
    cf1, cf2 = 0.8, 0.7
    combined = expert.combine_certainty(cf1, cf2)
    print(f"\nBoth Positive:")
    print(f"  CF1 = {cf1:.2f}, CF2 = {cf2:.2f}")
    print(f"  Combined = {combined:.3f}")
    print(f"  Formula: cf1 + cf2 * (1 - cf1) = {cf1} + {cf2} * (1 - {cf1}) = {combined:.3f}")
    
    # Test combining multiple CFs
    cfs = [0.9, 0.8, 0.75]
    result = cfs[0]
    print(f"\n\nCombining Multiple CFs: {cfs}")
    print(f"  Step 1: {cfs[0]:.2f}")
    for i, cf in enumerate(cfs[1:], 2):
        result = expert.combine_certainty(result, cf)
        print(f"  Step {i}: combine({result:.3f}, {cf:.2f}) = {result:.3f}")
    print(f"\n  Final Combined CF: {result:.3f}")
    print(f"  Confidence Level: {expert._classify_confidence(result)}")

def test_progressive_with_cf():
    """Test progressive questioning with certainty factors"""
    print_separator("TEST 4: Progressive Questioning Flow with CF")
    
    print("\n🔄 Progressive Flow: Animal Tissues → Epithelial → Structure")
    
    # Step 1: Initial query
    print("\n\n[Step 1] User asks: 'What are animal tissues?'")
    expert = BiologyExpert()
    expert.reset()
    expert.declare(Fact(query_topic='animal_tissues'))
    expert.run()
    
    responses = expert.get_response()
    if isinstance(responses, list) and len(responses) > 0:
        resp = responses[0]
        print(f"  ✅ Response: {resp.get('concept')}")
        print(f"  ✅ CF: {resp.get('certainty_factor', 0):.2f} ({resp.get('confidence_level')})")
    
    agg1 = expert.get_aggregated_confidence()
    
    # Step 2: User specifies tissue type
    print("\n[Step 2] User responds: 'epithelial'")
    expert.reset()
    expert.declare(Fact(query_topic='animal_tissues'))
    expert.declare(Fact(tissue_type='epithelial'))
    expert.run()
    
    agg2 = expert.get_aggregated_confidence()
    
    if expert.requires_clarification():
        print(f"  ✅ Asking for more details...")
        print(f"  ✅ Aggregate CF: {agg2['aggregate_certainty']:.3f}")
    
    # Step 3: User specifies detail level
    print("\n[Step 3] User responds: 'structure'")
    expert.reset()
    expert.declare(Fact(query_topic='animal_tissues'))
    expert.declare(Fact(tissue_type='epithelial'))
    expert.declare(Fact(detail_level='structure'))
    expert.run()
    
    agg3 = expert.get_aggregated_confidence()
    
    print(f"  ✅ Final detailed answer")
    print(f"  ✅ Aggregate CF: {agg3['aggregate_certainty']:.3f}")
    print(f"  ✅ Rules Fired: {agg3['num_rules_fired']}")
    
    # Compare confidence progression
    print("\n\n📊 CONFIDENCE PROGRESSION:")
    print("-"*70)
    print(f"  Step 1 (Overview):        CF = {agg1['aggregate_certainty']:.3f} ({agg1['confidence_level']})")
    print(f"  Step 2 (Tissue Type):     CF = {agg2['aggregate_certainty']:.3f} ({agg2['confidence_level']})")
    print(f"  Step 3 (Specific Detail): CF = {agg3['aggregate_certainty']:.3f} ({agg3['confidence_level']})")
    print("\n  💡 Note: More specific queries can lead to higher confidence!")

def main():
    """Run all tests"""
    print("\n")
    print("╔" + "="*68 + "╗")
    print("║" + " "*15 + "CERTAINTY FACTOR TESTING" + " "*29 + "║")
    print("║" + " "*15 + "Biology Expert System" + " "*32 + "║")
    print("╚" + "="*68 + "╝")
    
    test_single_topic()
    test_multiple_topics()
    test_cf_combination()
    test_progressive_with_cf()
    
    print("\n\n" + "="*70)
    print(" ✅ ALL TESTS COMPLETED")
    print("="*70)
    print("\n💡 Key Insights:")
    print("   - Each rule has an explicit Certainty Factor (CF)")
    print("   - CF ranges from 0.0 (unknown) to 1.0 (certain)")
    print("   - Multiple matching rules combine using CF algebra")
    print("   - Progressive questioning can increase specificity and confidence")
    print("   - Aggregate CF represents overall confidence in the answer")
    print("\n")

if __name__ == "__main__":
    main()
