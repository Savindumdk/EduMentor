"""
Language Detector
-----------------
Automatically detects the language of student questions.
Supports English, Sinhala, and Tamil.
"""

import re


class LanguageDetector:
    """Detects language of text input."""
    
    # Unicode ranges for Sinhala and Tamil
    SINHALA_RANGE = (0x0D80, 0x0DFF)
    TAMIL_RANGE = (0x0B80, 0x0BFF)
    
    def __init__(self):
        self.language_map = {
            'en': 'English',
            'si': 'Sinhala',
            'ta': 'Tamil'
        }
    
    def detect(self, text):
        """
        Detect language of text.
        
        Args:
            text (str): Text to analyze
        
        Returns:
            str: Language code ('en', 'si', 'ta')
        """
        if not text:
            return 'en'
        
        # Count characters in each script
        sinhala_count = self._count_script(text, self.SINHALA_RANGE)
        tamil_count = self._count_script(text, self.TAMIL_RANGE)
        
        # Check which script dominates
        if sinhala_count > 2:  # At least a few Sinhala characters
            return 'si'
        elif tamil_count > 2:  # At least a few Tamil characters
            return 'ta'
        else:
            return 'en'  # Default to English
    
    def _count_script(self, text, unicode_range):
        """Count characters in a specific Unicode range."""
        start, end = unicode_range
        count = 0
        for char in text:
            if start <= ord(char) <= end:
                count += 1
        return count
    
    def get_language_name(self, code):
        """Get full language name from code."""
        return self.language_map.get(code, 'English')
    
    def is_supported(self, code):
        """Check if language code is supported."""
        return code in self.language_map


# Singleton instance
detector = LanguageDetector()


def detect_language(text):
    """Convenience function to detect language."""
    return detector.detect(text)
