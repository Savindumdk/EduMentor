"""
Test Progressive Questioning for Biology Expert
"""
from experts.biology_expert import BiologyExpert
from experta import Fact

def test_animal_tissues():
    """Test progressive questioning for animal tissues."""
    print("=" * 60)
    print("Testing: What are the types of tissues in animals?")
    print("=" * 60)
    
    # Initialize the expert
    expert = BiologyExpert()
    expert.reset()
    expert.declare(Fact(query_topic='animal_tissues'))
    expert.run()
    
    print("\n--- Response ---")
    responses = expert.get_response()
    if isinstance(responses, list):
        for i, resp in enumerate(responses, 1):
            print(f"\nResponse {i}:")
            print(f"Concept: {resp.get('concept', 'N/A')}")
            print(f"Explanation: {resp.get('explanation', 'N/A')}")
            if resp.get('examples'):
                print(f"Examples: {', '.join(resp['examples'])}")
    else:
        print(f"Concept: {responses.get('concept', 'N/A')}")
        print(f"Explanation: {responses.get('explanation', 'N/A')}")
        if responses.get('examples'):
            print(f"Examples: {', '.join(responses['examples'])}")
    
    print(f"\n--- Clarification Needed: {expert.requires_clarification()} ---")
    if expert.requires_clarification():
        print(f"Question: {expert.get_clarification_question()}")
    
    print("\n" + "=" * 60)

def test_cell_division():
    """Test progressive questioning for cell division."""
    print("=" * 60)
    print("Testing: Tell me about cell division")
    print("=" * 60)
    
    # Initialize the expert
    expert = BiologyExpert()
    expert.reset()
    expert.declare(Fact(query_topic='cell_division'))
    expert.run()
    
    print("\n--- Response ---")
    responses = expert.get_response()
    if isinstance(responses, list):
        for i, resp in enumerate(responses, 1):
            print(f"\nResponse {i}:")
            print(f"Concept: {resp.get('concept', 'N/A')}")
            print(f"Explanation: {resp.get('explanation', 'N/A')}")
            if resp.get('examples'):
                print(f"Examples: {', '.join(resp['examples'])}")
    else:
        print(f"Concept: {responses.get('concept', 'N/A')}")
        print(f"Explanation: {responses.get('explanation', 'N/A')}")
        if responses.get('examples'):
            print(f"Examples: {', '.join(responses['examples'])}")
    
    print(f"\n--- Clarification Needed: {expert.requires_clarification()} ---")
    if expert.requires_clarification():
        print(f"Question: {expert.get_clarification_question()}")
    
    print("\n" + "=" * 60)

def test_progressive_flow():
    """Test the full progressive flow for animal tissues."""
    print("\n" + "=" * 60)
    print("Testing FULL Progressive Flow: Animal Tissues → Epithelial")
    print("=" * 60)
    
    # Step 1: Initial query
    print("\n[User asks: What are animal tissues?]")
    expert = BiologyExpert()
    expert.reset()
    expert.declare(Fact(query_topic='animal_tissues'))
    expert.run()
    
    print("\n--- System Response ---")
    responses = expert.get_response()
    if isinstance(responses, list) and len(responses) > 0:
        print(f"Concept: {responses[0].get('concept', 'N/A')}")
        print(f"Explanation: {responses[0].get('explanation', 'N/A')[:200]}...")
    
    if expert.requires_clarification():
        print(f"\n--- Clarification Question ---")
        print(expert.get_clarification_question())
    
    # Step 2: User chooses epithelial
    print("\n\n[User responds: epithelial]")
    expert.reset()
    expert.declare(Fact(query_topic='animal_tissues'))
    expert.declare(Fact(tissue_type='epithelial'))
    expert.run()
    
    if expert.requires_clarification():
        print("\n--- Clarification Question ---")
        print(expert.get_clarification_question())
    
    # Step 3: User chooses classification
    print("\n\n[User responds: classification]")
    expert.reset()
    expert.declare(Fact(query_topic='animal_tissues'))
    expert.declare(Fact(tissue_type='epithelial'))
    expert.declare(Fact(detail_level='classification'))
    expert.run()
    
    print("\n--- Final Detailed Response ---")
    responses = expert.get_response()
    if isinstance(responses, list):
        for i, resp in enumerate(responses, 1):
            print(f"\nResponse {i}:")
            print(f"Concept: {resp.get('concept', 'N/A')}")
            print(f"Explanation: {resp.get('explanation', 'N/A')[:300]}...")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    test_animal_tissues()
    print("\n\n")
    test_cell_division()
    print("\n\n")
    test_progressive_flow()
