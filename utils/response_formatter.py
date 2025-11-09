"""
Response Formatter
------------------
Formats responses consistently across the system.
"""

from datetime import datetime


class ResponseFormatter:
    """Formats system responses for consistent output."""
    
    @staticmethod
    def format_response(response_data):
        """
        Format a response dictionary into a structured output.
        
        Args:
            response_data (dict): Response from MAS/LLM pipeline
        
        Returns:
            dict: Formatted response
        """
        # Get both original and enhanced explanations
        original_explanation = response_data.get('explanation', '')
        enhanced_explanation = response_data.get('enhanced_explanation', '')
        llm_enhanced = response_data.get('llm_enhanced', False)
        needs_clarification = response_data.get('needs_clarification', False)
        
        # If LLM enhanced, show both original KB rule and LLM enhancement
        if llm_enhanced and enhanced_explanation and original_explanation:
            explanation = f"**📖 Knowledge Base Rule:**\n\n{original_explanation}\n\n---\n\n**🌟 AI-Enhanced Explanation:**\n\n{enhanced_explanation}"
        else:
            explanation = enhanced_explanation or original_explanation
        
        formatted = {
            'timestamp': datetime.now().isoformat(),
            'success': response_data.get('matched', False),
            'concept': response_data.get('concept', 'Unknown'),
            'topic': response_data.get('topic', 'General'),
            'explanation': explanation,
            'original_explanation': original_explanation,  # Keep original for reference
            'enhanced_explanation': enhanced_explanation if llm_enhanced else None,
            'examples': response_data.get('examples', []),
            'agent_used': response_data.get('agent', 'Unknown'),
            'llm_enhanced': llm_enhanced,
            'language': response_data.get('language', 'en'),
            'needs_clarification': needs_clarification
        }
        
        return formatted
    
    @staticmethod
    def format_error(error_message):
        """Format an error response."""
        return {
            'timestamp': datetime.now().isoformat(),
            'success': False,
            'error': error_message,
            'explanation': "Sorry, I couldn't process your question. Please try rephrasing it.",
            'agent_used': 'System',
            'llm_enhanced': False
        }
    
    @staticmethod
    def format_multiline_explanation(text, max_width=80):
        """
        Format long text into multiple lines.
        
        Args:
            text (str): Text to format
            max_width (int): Maximum line width
        
        Returns:
            str: Formatted text
        """
        words = text.split()
        lines = []
        current_line = []
        current_length = 0
        
        for word in words:
            word_length = len(word)
            if current_length + word_length + 1 <= max_width:
                current_line.append(word)
                current_length += word_length + 1
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
                current_length = word_length
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return '\n'.join(lines)
    
    @staticmethod
    def format_examples(examples):
        """Format examples list into readable text."""
        if not examples:
            return "No examples available."
        
        formatted = "Examples:\n"
        for i, example in enumerate(examples, 1):
            formatted += f"{i}. {example}\n"
        
        return formatted.strip()
    
    @staticmethod
    def create_display_dict(formatted_response):
        """
        Create a dictionary optimized for UI display.
        
        Args:
            formatted_response (dict): Formatted response
        
        Returns:
            dict: Display-optimized dictionary
        """
        # Check if this is a clarification request
        needs_clarification = formatted_response.get('needs_clarification', False)
        
        if needs_clarification:
            display = {
                'status': '❓ Needs Clarification',
                'topic': f"📚 {formatted_response['topic']}",
                'concept': '💡 Clarification Needed',
                'explanation': formatted_response['explanation'],
                'agent': f"🤖 {formatted_response['agent_used']}",
                'enhancement': '❓ Awaiting Clarification',
                'language': formatted_response['language'].upper(),
                'needs_clarification': True
            }
        else:
            display = {
                'status': '✓ Success' if formatted_response['success'] else '✗ Failed',
                'topic': f"📚 {formatted_response['topic']}",
                'concept': f"💡 {formatted_response['concept']}",
                'explanation': formatted_response['explanation'],
                'agent': f"🤖 {formatted_response['agent_used']}",
                'enhancement': '🌟 LLM Enhanced' if formatted_response['llm_enhanced'] else '📖 Expert System',
                'language': formatted_response['language'].upper(),
                'needs_clarification': False
            }
        
        if formatted_response.get('examples'):
            display['examples'] = ResponseFormatter.format_examples(
                formatted_response['examples']
            )
        
        return display


# Convenience functions
def format_response(response_data):
    """Format a response."""
    return ResponseFormatter.format_response(response_data)


def format_error(error_message):
    """Format an error."""
    return ResponseFormatter.format_error(error_message)


def create_display(response_data):
    """Create display-optimized response."""
    formatted = ResponseFormatter.format_response(response_data)
    return ResponseFormatter.create_display_dict(formatted)
