"""
Biology Knowledge Base
----------------------
Contains rules and facts for O/L Biology topics.
"""

BIOLOGY_RULES = {
    "photosynthesis": {
        "keywords": ["photosynthesis", "plants", "sunlight", "food", "chlorophyll", "light", "energy", "glucose", "leaves"],
        "explanation": """Plants use sunlight to produce food through photosynthesis.
Light energy is converted into chemical energy stored in glucose.
This process occurs in chloroplasts, which contain chlorophyll (the green pigment).
The equation: Carbon Dioxide + Water + Light Energy → Glucose + Oxygen
6CO₂ + 6H₂O + Light → C₆H₁₂O₆ + 6O₂""",
        "topic": "Biology",
        "subtopic": "Plant Nutrition",
        "examples": [
            "Green leaves capture sunlight for photosynthesis",
            "Plants release oxygen as a byproduct",
            "Chlorophyll gives plants their green color"
        ]
    },
    "respiration": {
        "keywords": ["respiration", "breathing", "oxygen", "energy", "cells", "glucose", "breakdown", "cellular"],
        "explanation": """Respiration is the process where cells break down glucose to release energy.
This happens in all living organisms, not just animals.
Aerobic respiration uses oxygen: Glucose + Oxygen → Carbon Dioxide + Water + Energy (ATP)
The energy released is used for all life processes like growth, movement, and reproduction.
C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + Energy""",
        "topic": "Biology",
        "subtopic": "Respiration",
        "examples": [
            "Muscles use cellular respiration during exercise",
            "Yeast performs anaerobic respiration (fermentation)",
            "Mitochondria are the powerhouses where respiration occurs"
        ]
    },
    "digestion": {
        "keywords": ["digestion", "food", "nutrients", "stomach", "enzymes", "absorption", "intestine"],
        "explanation": """Digestion is the breakdown of large food molecules into smaller, absorbable nutrients.
Mechanical digestion (chewing) and chemical digestion (enzymes) work together.
Enzymes like amylase, protease, and lipase break down carbohydrates, proteins, and fats.
Nutrients are absorbed in the small intestine and transported via blood.""",
        "topic": "Biology",
        "subtopic": "Nutrition",
        "examples": [
            "Saliva contains amylase that starts starch digestion",
            "Stomach acid helps break down proteins",
            "Small intestine absorbs digested nutrients into blood"
        ]
    },
    "cell_structure": {
        "keywords": ["cell", "nucleus", "membrane", "cytoplasm", "organelle", "tissue"],
        "explanation": """Cells are the basic units of life.
Cell membrane controls what enters and leaves the cell.
Nucleus contains DNA and controls cell activities.
Cytoplasm is where chemical reactions occur.
Organelles like mitochondria, chloroplasts perform specific functions.""",
        "topic": "Biology",
        "subtopic": "Cell Biology",
        "examples": [
            "Plant cells have cell walls and chloroplasts",
            "Animal cells have centrioles but no cell wall",
            "Red blood cells lack a nucleus"
        ]
    },
    "reproduction": {
        "keywords": ["reproduction", "offspring", "sexual", "asexual", "fertilization", "gametes"],
        "explanation": """Reproduction is the production of new organisms.
Sexual reproduction involves two parents and genetic variation.
Asexual reproduction involves one parent and produces identical offspring.
In sexual reproduction, gametes (sex cells) fuse during fertilization.""",
        "topic": "Biology",
        "subtopic": "Reproduction",
        "examples": [
            "Humans reproduce sexually producing unique offspring",
            "Bacteria reproduce asexually by binary fission",
            "Plants can reproduce both sexually (seeds) and asexually (cuttings)"
        ]
    }
}

def get_biology_rules():
    """Return all biology rules."""
    return BIOLOGY_RULES

def get_biology_keywords():
    """Return mapping of keywords to concepts."""
    keyword_map = {}
    for concept, rule_data in BIOLOGY_RULES.items():
        for keyword in rule_data["keywords"]:
            if keyword not in keyword_map:
                keyword_map[keyword] = []
            keyword_map[keyword].append(concept)
    return keyword_map
