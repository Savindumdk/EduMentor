"""
Study Guide Expert System - Clean & Simple
------------------------------------------
A straightforward expert system for study guidance using Experta.
"""

from experta import *


class StudyGuideExpert(KnowledgeEngine):
    """Simple study guide expert system."""
    
    def __init__(self):
        super().__init__()
        self.response = None
    
    @Rule(AS.f << Fact(user_query=W()))
    def handle_query(self, f):
        """Main rule to handle all study queries."""
        query = f['user_query'].lower()
        
        # Memory queries
        if any(word in query for word in ['memory', 'remember', 'forget', 'memorize', 'recall']):
            self.response = {
                'concept': ' Memory Enhancement',
                'diagnosis': 'You need proven memory techniques!',
                'explanation': 'Memory works in 3 stages: Encoding  Storage  Retrieval. Use these techniques to strengthen each stage.',
                'recommendation': '1. Spaced Repetition (Day 1, 3, 7, 14)\n2. Active Recall (Test yourself)\n3. Elaborative Encoding (Connect to existing knowledge)',
                'examples': ['Use Anki for spaced repetition', 'Teach concepts to others'],
                'resources': ['Anki app', 'Book: Make It Stick']
            }
        
        # Stress queries
        elif any(word in query for word in ['stress', 'anxious', 'anxiety', 'nervous', 'panic']):
            self.response = {
                'concept': ' Stress Management',
                'diagnosis': 'Exam stress is normal and manageable!',
                'explanation': 'Your body enters fight-or-flight mode. This is natural but can be controlled.',
                'recommendation': '1. 4-7-8 Breathing\n2. Grounding Technique (5-4-3-2-1)\n3. Regular exercise\n4. Proper sleep',
                'examples': ['Practice breathing before exams', 'Exercise 30min daily'],
                'resources': ['Headspace app', 'Calm app']
            }
        
        # Default
        else:
            self.response = {
                'concept': 'Study Guidance',
                'explanation': f'I can help with: Memory, Stress, Time Management, Exams, Motivation, Confidence, Sleep.\n\nYour question: "{f["user_query"]}"',
                'topic': 'General'
            }
    
    def get_response(self):
        """Return the expert response."""
        return self.response
