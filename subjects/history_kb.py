"""
History Knowledge Base
----------------------
Contains rules and facts for O/L History topics (Sri Lankan focus).
"""

HISTORY_RULES = {
    "ancient_civilization": {
        "keywords": ["ancient", "civilization", "anuradhapura", "polonnaruwa", "kingdom", "king", "dynasty"],
        "explanation": """Ancient Sri Lankan civilizations flourished in Anuradhapura and Polonnaruwa.
The Anuradhapura Kingdom (377 BC - 1017 AD) was one of the longest-lasting kingdoms.
Advanced hydraulic systems (tanks, canals) supported agriculture.
Buddhism was introduced in 3rd century BC by Arahat Mahinda.""",
        "topic": "History",
        "subtopic": "Ancient Sri Lanka",
        "examples": [
            "King Devanampiya Tissa established Buddhism in Sri Lanka",
            "Parakramabahu I built great irrigation works",
            "Ruwanwelisaya is an ancient Buddhist stupa"
        ]
    },
    "colonial_period": {
        "keywords": ["colonial", "portuguese", "dutch", "british", "colonization", "independence", "empire"],
        "explanation": """Sri Lanka faced European colonization from 16th to 20th century.
Portuguese (1505-1658) controlled coastal areas.
Dutch (1658-1796) expanded spice trade and infrastructure.
British (1796-1948) unified the island and established plantation economy.
Independence achieved on February 4, 1948.""",
        "topic": "History",
        "subtopic": "Colonial Era",
        "examples": [
            "Portuguese built forts in Colombo and Galle",
            "Dutch introduced Roman-Dutch law",
            "British introduced tea and rubber plantations"
        ]
    },
    "independence": {
        "keywords": ["independence", "freedom", "1948", "ceylon", "self-rule", "dominion"],
        "explanation": """Sri Lanka (then Ceylon) gained independence from Britain on February 4, 1948.
Peaceful transfer of power, unlike many colonies.
Don Stephen Senanayake became the first Prime Minister.
Became a republic in 1972, changing name to Sri Lanka.""",
        "topic": "History",
        "subtopic": "Modern History",
        "examples": [
            "D.S. Senanayake is called the Father of the Nation",
            "Ceylon became Sri Lanka in 1972",
            "First constitution in 1948, new constitution in 1972"
        ]
    },
    "world_wars": {
        "keywords": ["world", "war", "ww1", "ww2", "first", "second", "conflict", "global"],
        "explanation": """World War I (1914-1918): European conflict that spread globally.
Caused by nationalism, imperialism, and alliance systems.
World War II (1939-1945): Most devastating war in history.
Caused by rise of fascism, Treaty of Versailles consequences.
Sri Lanka (Ceylon) supported Allies in both wars.""",
        "topic": "History",
        "subtopic": "World History",
        "examples": [
            "WWI started with assassination of Archduke Franz Ferdinand",
            "WWII ended with atomic bombs on Japan",
            "United Nations formed after WWII to prevent future wars"
        ]
    },
    "cultural_heritage": {
        "keywords": ["culture", "heritage", "tradition", "festival", "temple", "religion", "buddhist"],
        "explanation": """Sri Lanka has rich cultural heritage spanning over 2500 years.
Buddhism, Hinduism, Islam, and Christianity coexist.
UNESCO World Heritage Sites include Sigiriya, Galle Fort, Temple of the Tooth.
Traditional arts include Kandyan dance, mask-making, and handicrafts.""",
        "topic": "History",
        "subtopic": "Cultural History",
        "examples": [
            "Sigiriya rock fortress built in 5th century",
            "Esala Perahera is annual Buddhist festival in Kandy",
            "Traditional New Year (Sinhala/Tamil) celebrated in April"
        ]
    }
}

def get_history_rules():
    """Return all history rules."""
    return HISTORY_RULES

def get_history_keywords():
    """Return mapping of keywords to concepts."""
    keyword_map = {}
    for concept, rule_data in HISTORY_RULES.items():
        for keyword in rule_data["keywords"]:
            if keyword not in keyword_map:
                keyword_map[keyword] = []
            keyword_map[keyword].append(concept)
    return keyword_map
