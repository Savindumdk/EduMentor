"""
Mathematics Knowledge Base
--------------------------
Contains rules and facts for O/L Mathematics topics.
"""

MATHEMATICS_RULES = {
    "algebra": {
        "keywords": ["algebra", "equation", "variable", "solve", "x", "y", "expression", "simplify"],
        "explanation": """Algebra uses letters (variables) to represent unknown numbers.
Equations show relationships between variables.
Solving equations means finding the value of the variable.
Basic operations: addition, subtraction, multiplication, division apply to variables.""",
        "topic": "Mathematics",
        "subtopic": "Algebra",
        "examples": [
            "2x + 5 = 15, solve for x → x = 5",
            "Factoring: x² - 9 = (x+3)(x-3)",
            "Linear equations form straight lines when graphed"
        ]
    },
    "geometry": {
        "keywords": ["geometry", "shape", "triangle", "circle", "angle", "area", "perimeter", "volume"],
        "explanation": """Geometry studies shapes, sizes, and properties of space.
Basic shapes: triangles, circles, squares, rectangles.
Perimeter is the distance around a shape.
Area is the space inside a 2D shape.
Volume is the space inside a 3D object.""",
        "topic": "Mathematics",
        "subtopic": "Geometry",
        "examples": [
            "Area of rectangle = length × width",
            "Area of circle = πr²",
            "Sum of angles in a triangle = 180°"
        ]
    },
    "fractions": {
        "keywords": ["fraction", "numerator", "denominator", "divide", "half", "quarter", "decimal"],
        "explanation": """Fractions represent parts of a whole.
Numerator (top) shows how many parts you have.
Denominator (bottom) shows how many parts make a whole.
Operations: find common denominators for addition/subtraction.""",
        "topic": "Mathematics",
        "subtopic": "Numbers",
        "examples": [
            "½ + ¼ = ²⁄₄ + ¼ = ¾",
            "½ = 0.5 = 50%",
            "Multiplying fractions: ½ × ⅓ = ⅙"
        ]
    },
    "percentages": {
        "keywords": ["percentage", "percent", "%", "discount", "increase", "decrease", "ratio"],
        "explanation": """Percentages express a number as a fraction of 100.
% means 'out of 100'.
To find percentage: (part/whole) × 100
Percentage increase/decrease shows relative change.""",
        "topic": "Mathematics",
        "subtopic": "Numbers",
        "examples": [
            "50% = 50/100 = 0.5 = ½",
            "20% discount on $100 = $100 - $20 = $80",
            "50% increase on 40 = 40 + 20 = 60"
        ]
    },
    "statistics": {
        "keywords": ["statistics", "mean", "average", "median", "mode", "data", "graph"],
        "explanation": """Statistics deals with collecting and analyzing data.
Mean (average) = sum of values / number of values
Median is the middle value when arranged in order.
Mode is the most frequently occurring value.""",
        "topic": "Mathematics",
        "subtopic": "Statistics",
        "examples": [
            "Mean of 2,4,6,8 = (2+4+6+8)/4 = 5",
            "Median of 1,3,5,7,9 = 5 (middle value)",
            "Mode of 1,2,2,3,4 = 2 (most frequent)"
        ]
    }
}

def get_mathematics_rules():
    """Return all mathematics rules."""
    return MATHEMATICS_RULES

def get_mathematics_keywords():
    """Return mapping of keywords to concepts."""
    keyword_map = {}
    for concept, rule_data in MATHEMATICS_RULES.items():
        for keyword in rule_data["keywords"]:
            if keyword not in keyword_map:
                keyword_map[keyword] = []
            keyword_map[keyword].append(concept)
    return keyword_map
