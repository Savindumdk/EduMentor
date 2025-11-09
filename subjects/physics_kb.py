"""
Physics Knowledge Base
----------------------
Contains rules and facts for O/L Physics topics.
"""

PHYSICS_RULES = {
    "friction": {
        "keywords": ["friction", "stop", "rolling", "sliding", "resistance", "surface", "rough", "smooth"],
        "explanation": """Friction is a force that opposes motion between two surfaces in contact.
When a ball rolls and stops, friction converts kinetic energy into heat.
Rough surfaces create more friction than smooth surfaces.
Friction can be useful (walking, braking) or a problem (wear and tear in machines).""",
        "topic": "Physics",
        "subtopic": "Forces and Motion",
        "examples": [
            "A rolling ball slows down due to friction with the ground",
            "Brake pads use friction to stop vehicles",
            "Rubbing hands creates warmth due to friction"
        ]
    },
    "gravity": {
        "keywords": ["gravity", "fall", "weight", "attraction", "earth", "pull", "mass"],
        "explanation": """Gravity is the force of attraction between objects with mass.
Earth's gravity pulls objects toward its center, giving them weight.
All objects fall at the same rate in vacuum (9.8 m/s² acceleration).
Weight = Mass × Gravitational Field Strength (W = mg)""",
        "topic": "Physics",
        "subtopic": "Forces",
        "examples": [
            "An apple falls from a tree due to gravity",
            "The Moon orbits Earth due to gravitational attraction",
            "Astronauts feel weightless in space (free fall)"
        ]
    },
    "electricity": {
        "keywords": ["electricity", "current", "voltage", "circuit", "battery", "electrons", "wire", "power"],
        "explanation": """Electric current is the flow of electrons through a conductor.
Voltage (potential difference) is the driving force that pushes electrons.
Current flows in a complete circuit from positive to negative terminal.
Measured in: Current (Amperes), Voltage (Volts), Resistance (Ohms).
Ohm's Law: V = IR (Voltage = Current × Resistance)""",
        "topic": "Physics",
        "subtopic": "Electricity",
        "examples": [
            "A battery pushes electrons through a wire to light a bulb",
            "Higher voltage means more electrical pressure",
            "Insulators prevent electric current flow"
        ]
    },
    "motion": {
        "keywords": ["motion", "speed", "velocity", "acceleration", "distance", "displacement"],
        "explanation": """Motion is the change in position of an object over time.
Speed = Distance / Time (scalar quantity)
Velocity = Displacement / Time (vector quantity with direction)
Acceleration is the rate of change of velocity.""",
        "topic": "Physics",
        "subtopic": "Kinematics",
        "examples": [
            "A car moving at 60 km/h has constant speed",
            "Throwing a ball upward shows acceleration due to gravity",
            "Circular motion involves changing direction"
        ]
    },
    "energy": {
        "keywords": ["energy", "work", "power", "kinetic", "potential", "conservation"],
        "explanation": """Energy is the ability to do work.
Kinetic Energy = ½mv² (energy of motion)
Potential Energy = mgh (stored energy due to position)
Law of Conservation: Energy cannot be created or destroyed, only transformed.""",
        "topic": "Physics",
        "subtopic": "Energy",
        "examples": [
            "A moving car has kinetic energy",
            "Water at the top of a waterfall has potential energy",
            "A pendulum converts between kinetic and potential energy"
        ]
    }
}

def get_physics_rules():
    """Return all physics rules."""
    return PHYSICS_RULES

def get_physics_keywords():
    """Return mapping of keywords to concepts."""
    keyword_map = {}
    for concept, rule_data in PHYSICS_RULES.items():
        for keyword in rule_data["keywords"]:
            if keyword not in keyword_map:
                keyword_map[keyword] = []
            keyword_map[keyword].append(concept)
    return keyword_map
