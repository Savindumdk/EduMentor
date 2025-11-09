"""
Conversation Memory System
--------------------------
Tracks conversation history for context-aware clarifications and intent classification.
"""

from datetime import datetime
from typing import List, Dict, Optional


class ConversationTurn:
    """Represents a single turn in the conversation."""
    
    def __init__(self, question: str, answer: str = None, subject: str = None, 
                 needed_clarification: bool = False, timestamp: datetime = None):
        self.question = question
        self.answer = answer
        self.subject = subject
        self.needed_clarification = needed_clarification
        self.timestamp = timestamp or datetime.now()
        self.clarifications = []  # List of clarification exchanges
    
    def add_clarification(self, clarification_question: str, user_response: str):
        """Add a clarification exchange to this turn."""
        self.clarifications.append({
            'question': clarification_question,
            'response': user_response,
            'timestamp': datetime.now()
        })
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization."""
        return {
            'question': self.question,
            'answer': self.answer,
            'subject': self.subject,
            'needed_clarification': self.needed_clarification,
            'clarifications': self.clarifications,
            'timestamp': self.timestamp.isoformat()
        }


class ConversationMemory:
    """
    Manages conversation history and context.
    Helps with:
    - Intent classification (what did user ask about before?)
    - Clarification handling (use previous context)
    - Pronoun resolution ("tell me more about it" -> what is "it"?)
    """
    
    def __init__(self, max_history: int = 10):
        self.max_history = max_history
        self.turns: List[ConversationTurn] = []
        self.current_turn: Optional[ConversationTurn] = None
        self.session_start = datetime.now()
    
    def start_turn(self, question: str):
        """Start a new conversation turn."""
        self.current_turn = ConversationTurn(question=question)
    
    def complete_turn(self, answer: str, subject: str = None, needed_clarification: bool = False):
        """Complete the current turn and add to history."""
        if self.current_turn:
            self.current_turn.answer = answer
            self.current_turn.subject = subject
            self.current_turn.needed_clarification = needed_clarification
            
            self.turns.append(self.current_turn)
            
            # Keep only last N turns
            if len(self.turns) > self.max_history:
                self.turns = self.turns[-self.max_history:]
            
            self.current_turn = None
    
    def add_clarification_to_current(self, clarification_question: str, user_response: str):
        """Add a clarification exchange to the current turn."""
        if self.current_turn:
            self.current_turn.add_clarification(clarification_question, user_response)
    
    def get_recent_context(self, n: int = 3) -> List[ConversationTurn]:
        """Get the last N conversation turns."""
        return self.turns[-n:] if self.turns else []
    
    def get_last_subject(self) -> Optional[str]:
        """Get the subject from the most recent turn."""
        if self.turns:
            return self.turns[-1].subject
        return None
    
    def get_last_question(self) -> Optional[str]:
        """Get the most recent question."""
        if self.turns:
            return self.turns[-1].question
        return None
    
    def get_context_summary(self, n: int = 3) -> str:
        """
        Get a text summary of recent conversation context.
        Useful for passing to LLM for intent classification.
        """
        recent = self.get_recent_context(n)
        
        if not recent:
            return "No previous conversation history."
        
        summary_lines = ["Recent conversation context:"]
        for i, turn in enumerate(recent, 1):
            summary_lines.append(f"\n{i}. User asked about: {turn.subject or 'Unknown'}")
            summary_lines.append(f"   Question: {turn.question[:100]}...")
            if turn.needed_clarification:
                summary_lines.append(f"   (Needed clarification)")
        
        return "\n".join(summary_lines)
    
    def get_full_context_for_llm(self, n: int = 3) -> str:
        """
        Get detailed context for LLM intent classification.
        Includes questions, subjects, and clarifications.
        """
        recent = self.get_recent_context(n)
        
        if not recent:
            return "This is the first question in the conversation."
        
        context_lines = ["Previous conversation:"]
        for i, turn in enumerate(recent, 1):
            context_lines.append(f"\n--- Turn {i} ---")
            context_lines.append(f"User: {turn.question}")
            if turn.subject:
                context_lines.append(f"Subject identified: {turn.subject}")
            if turn.clarifications:
                context_lines.append("Clarifications needed:")
                for clarif in turn.clarifications:
                    context_lines.append(f"  System: {clarif['question']}")
                    context_lines.append(f"  User: {clarif['response']}")
            if turn.answer:
                answer_preview = turn.answer[:150] + "..." if len(turn.answer) > 150 else turn.answer
                context_lines.append(f"Answer provided: {answer_preview}")
        
        return "\n".join(context_lines)
    
    def has_recent_subject_context(self, subject: str, lookback: int = 2) -> bool:
        """Check if a subject was recently discussed."""
        recent = self.get_recent_context(lookback)
        return any(turn.subject == subject for turn in recent)
    
    def clear(self):
        """Clear all conversation history."""
        self.turns = []
        self.current_turn = None
        self.session_start = datetime.now()
    
    def get_statistics(self) -> Dict:
        """Get conversation statistics."""
        total_turns = len(self.turns)
        turns_with_clarification = sum(1 for turn in self.turns if turn.needed_clarification)
        subjects_discussed = set(turn.subject for turn in self.turns if turn.subject)
        
        return {
            'total_turns': total_turns,
            'turns_with_clarification': turns_with_clarification,
            'subjects_discussed': list(subjects_discussed),
            'session_duration': (datetime.now() - self.session_start).total_seconds(),
            'session_start': self.session_start.isoformat()
        }
    
    def __str__(self) -> str:
        """String representation of memory state."""
        stats = self.get_statistics()
        return (f"ConversationMemory(turns={stats['total_turns']}, "
                f"subjects={stats['subjects_discussed']}, "
                f"with_clarifications={stats['turns_with_clarification']})")
    
    def __repr__(self) -> str:
        return self.__str__()
