# Script to create study_guide_expert.py
code = '''# Advanced Study Guide Expert System
import json, os
from typing import Dict, List, Optional
from experta import *

class StudyGuideExpert(KnowledgeEngine):
    def __init__(self, kb_path=None):
        super().__init__()
        if kb_path is None:
            kb_path = os.path.join(os.path.dirname(__file__), "study_guide_kb.json")
        try:
            with open(kb_path, "r", encoding="utf-8") as f:
                self.kb = json.load(f)
        except:
            self.kb = {}
        self.kb_path = kb_path
        self.user_profile = {}
        self.response = None
        self.fired_rules = []
        self.reasoning_trace = []
        self.inferred_facts = []
        self.confidence_scores = []
        from nlp_processor import NLPProcessor
        self.nlp = NLPProcessor()
    
    def process_query(self, query):
        self.reset()
        self.response = None
        self.fired_rules = []
        self.reasoning_trace = []
        self.inferred_facts = []
        self.confidence_scores = []
        nlp_result = self.nlp.process_query(query, self.kb)
        self.reasoning_trace.append(f"Query: {query}")
        self.reasoning_trace.append(f"Intents: {nlp_result['intents'][:2]}")
        self.declare(Fact(user_query=query.lower()))
        self.declare(Fact(processed_query=nlp_result))
        for key, val in nlp_result["entities"].items():
            self.declare(Fact(**{key: val}))
        for c in nlp_result["conditions"]:
            self.declare(Fact(condition=c))
        self.reasoning_trace.append("Running inference...")
        self.run()
        return self.response
    
    @Rule(AS.f << Fact(condition="high_stress"), salience=10)
    def infer_low_focus(self, f):
        self.declare(Fact(condition="low_focus"))
        self.inferred_facts.append("low_focus")
        self.reasoning_trace.append("Infer: stress -> low_focus")
    
    @Rule(AS.f << Fact(sleep_hours=MATCH.h & P(lambda x: x < 7)), salience=10)
    def infer_weak_memory(self, h):
        self.declare(Fact(condition="memory_weak"))
        self.inferred_facts.append("memory_weak")
        self.reasoning_trace.append(f"Infer: sleep={h}h -> weak memory")
    
    @Rule(AS.f << Fact(processed_query=MATCH.nlp), salience=5)
    def reason(self, nlp):
        intents = nlp.get("intents", [])
        if not intents:
            self.response = {"concept": "General", "explanation": "I can help with memory, stress, time management, exams, motivation, confidence, and sleep."}
            return
        topic, conf = intents[0]
        data = self.kb.get(topic, {})
        if not data:
            self.response = {"concept": "General"}
            return
        recs = []
        conds = nlp.get("conditions", [])
        for rule in data.get("rules", []):
            if rule.get("condition") in conds or rule.get("condition") == "mentions_" + topic:
                recs.append(rule["recommend"])
                self.fired_rules.append(rule["id"])
                self.confidence_scores.append(rule.get("confidence", 0.8))
        self.response = {
            "concept": data.get("concept", "Study Guide"),
            "diagnosis": data.get("diagnosis", ""),
            "explanation": data.get("explanation", ""),
            "recommendation": "\\n\\n".join([f"{i+1}. {r}" for i, r in enumerate(recs[:4])]),
            "examples": data.get("examples", []),
            "resources": data.get("resources", []),
            "confidence": max(self.confidence_scores) if self.confidence_scores else conf,
            "reasoning_trace": self.reasoning_trace.copy(),
            "fired_rules": self.fired_rules.copy(),
            "inferred_facts": self.inferred_facts.copy(),
            "topic": topic
        }
    
    def update_user_profile(self, **kwargs):
        self.user_profile.update(kwargs)
    
    def get_user_profile(self):
        return self.user_profile.copy()
    
    def get_response(self):
        return self.response
    
    def get_explanation(self):
        return "\\n".join(self.reasoning_trace)
    
    def get_confidence(self):
        return self.response.get("confidence", 0.0) if self.response else 0.0
'''

with open('study_guide_expert.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("✅ study_guide_expert.py created successfully!")
