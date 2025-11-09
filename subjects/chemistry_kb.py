"""
Chemistry Knowledge Base
------------------------
Contains rules and facts for O/L Chemistry topics.
"""

CHEMISTRY_RULES = {
    "acids": {
        "keywords": ["acid", "sour", "pH", "hydrogen", "corrosive", "lemon", "vinegar", "H+"],
        "explanation": """Acids are substances that produce hydrogen ions (H+) when dissolved in water.
They have pH values less than 7 and taste sour.
Common acids: Hydrochloric acid (HCl), Sulfuric acid (H₂SO₄), Citric acid (in lemons).
Acids turn blue litmus paper red and react with metals to produce hydrogen gas.""",
        "topic": "Chemistry",
        "subtopic": "Acids and Bases",
        "examples": [
            "Lemon juice contains citric acid (pH ~2-3)",
            "Stomach acid (HCl) helps digest food",
            "Acid rain damages buildings and plants"
        ]
    },
    "bases": {
        "keywords": ["base", "alkali", "bitter", "soap", "hydroxide", "pH", "OH-", "slippery"],
        "explanation": """Bases (alkalis) are substances that produce hydroxide ions (OH-) in water.
They have pH values greater than 7 and feel slippery.
Common bases: Sodium hydroxide (NaOH), Calcium hydroxide (Ca(OH)₂), Ammonia.
Bases turn red litmus paper blue and neutralize acids.""",
        "topic": "Chemistry",
        "subtopic": "Acids and Bases",
        "examples": [
            "Soap solution is basic (pH ~9-10)",
            "Baking soda neutralizes acid in cooking",
            "Antacids use bases to neutralize stomach acid"
        ]
    },
    "combustion": {
        "keywords": ["combustion", "burning", "fire", "oxygen", "heat", "flame", "oxidation"],
        "explanation": """Combustion is a chemical reaction where a substance reacts with oxygen and releases heat.
Complete combustion produces carbon dioxide and water (for hydrocarbons).
Three requirements for combustion: Fuel, Oxygen, and Heat (Fire Triangle).
Example: Methane + Oxygen → Carbon Dioxide + Water + Heat Energy
CH₄ + 2O₂ → CO₂ + 2H₂O + Energy""",
        "topic": "Chemistry",
        "subtopic": "Chemical Reactions",
        "examples": [
            "Wood burning releases heat and light",
            "Car engines use combustion of petrol/diesel",
            "Incomplete combustion produces carbon monoxide (dangerous)"
        ]
    },
    "elements": {
        "keywords": ["element", "atom", "periodic", "table", "metal", "non-metal", "compound"],
        "explanation": """Elements are pure substances made of only one type of atom.
Cannot be broken down into simpler substances by chemical means.
Organized in the Periodic Table by atomic number.
Metals conduct electricity, non-metals are insulators.""",
        "topic": "Chemistry",
        "subtopic": "Matter and Atoms",
        "examples": [
            "Gold (Au), Silver (Ag), Copper (Cu) are metal elements",
            "Oxygen (O₂), Nitrogen (N₂) are non-metal elements",
            "There are 118 known elements"
        ]
    },
    "chemical_reactions": {
        "keywords": ["reaction", "chemical", "change", "reactant", "product", "equation"],
        "explanation": """Chemical reactions involve breaking and forming bonds between atoms.
Reactants are starting materials, products are substances formed.
Signs of chemical reaction: color change, gas production, heat/light, precipitate.
Law of Conservation of Mass: Mass is conserved in reactions.""",
        "topic": "Chemistry",
        "subtopic": "Chemical Reactions",
        "examples": [
            "Iron rusting is a chemical reaction with oxygen",
            "Baking a cake involves chemical reactions",
            "Photosynthesis is a chemical reaction in plants"
        ]
    }
}

def get_chemistry_rules():
    """Return all chemistry rules."""
    return CHEMISTRY_RULES

def get_chemistry_keywords():
    """Return mapping of keywords to concepts."""
    keyword_map = {}
    for concept, rule_data in CHEMISTRY_RULES.items():
        for keyword in rule_data["keywords"]:
            if keyword not in keyword_map:
                keyword_map[keyword] = []
            keyword_map[keyword].append(concept)
    return keyword_map
