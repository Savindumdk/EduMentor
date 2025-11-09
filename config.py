"""
Configuration settings for EduMentor
-------------------------------------
Central configuration file for system parameters.
"""

# System Information
SYSTEM_NAME = "EduMentor"
SYSTEM_VERSION = "2.0.0"
PHASE = "Phase 2+3: Multi-Agent System + LLM Integration"

# Application Settings
DEBUG_MODE = False
LOG_LEVEL = "INFO"

# Knowledge Base Settings
MAX_RULES = 100  # Maximum number of rules (for Phase 1)
CONFIDENCE_THRESHOLD = 0.5  # Minimum confidence for valid response
DEFAULT_LANGUAGE = "en"  # English (Phase 3 will add 'si', 'ta')

# UI Settings
PAGE_TITLE = "EduMentor - O/L Science Tutor"
PAGE_ICON = "🎓"
MAX_HISTORY_ITEMS = 20
SHOW_CONFIDENCE = True

# Response Settings
RESPONSE_TIMEOUT = 5  # seconds
MAX_RESPONSE_LENGTH = 1000  # characters

# Subjects Configuration (Phase 2+3: Expanded)
SUBJECTS = {
    "Physics": {
        "icon": "⚛️",
        "color": "#2196F3",
        "enabled": True,
        "agent": "PhysicsAgent"
    },
    "Biology": {
        "icon": "🧬",
        "color": "#4CAF50",
        "enabled": True,
        "agent": "BiologyAgent"
    },
    "Chemistry": {
        "icon": "🧪",
        "color": "#FF9800",
        "enabled": True,
        "agent": "ChemistryAgent"
    },
    "Mathematics": {
        "icon": "📐",
        "color": "#9C27B0",
        "enabled": True,
        "agent": "MathematicsAgent"
    },
    "History": {
        "icon": "📜",
        "color": "#795548",
        "enabled": True,
        "agent": "HistoryAgent"
    },
    "Study Guide": {
        "icon": "📖",
        "color": "#607D8B",
        "enabled": True,
        "agent": "StudyGuideAgent"
    }
}

# Phase 2: Multi-Agent System Configuration
MAS_ENABLED = True
COORDINATOR_ENABLED = True
MAX_CONCURRENT_AGENTS = 6  # One per subject
AGENT_TIMEOUT = 5  # seconds
ENABLE_AGENT_STATISTICS = True

# Phase 3: LLM Configuration
LLM_ENABLED = True  # Set to False to use only expert system
LLM_PROVIDER = "gemini"  # Using Google Gemini
LLM_MODEL = "gemini-pro"
LLM_TEMPERATURE = 0.7
LLM_MAX_TOKENS = 500
FALLBACK_TO_EXPERT_SYSTEM = True  # If LLM fails, use expert system

# Multilingual Support
MULTILINGUAL_ENABLED = True
SUPPORTED_LANGUAGES = ["en", "si", "ta"]
AUTO_DETECT_LANGUAGE = True
DEFAULT_LANGUAGE = "en"

# Language Display Names
LANGUAGE_NAMES = {
    "en": "English",
    "si": "සිංහල (Sinhala)",
    "ta": "தமிழ் (Tamil)"
}

# Analytics (Future)
TRACK_USAGE = False
TRACK_STUDENT_PROGRESS = False

# Development Settings
DEV_MODE = True
AUTO_RELOAD = True
