# Advanced Study Guide Expert System - Multi-Input Version
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
        try:
            from nlp_processor import NLPProcessor
            self.nlp = NLPProcessor()
        except ImportError:
            from experts.nlp_processor import NLPProcessor
            self.nlp = NLPProcessor()
    
    def process_query_with_inputs(self, category, question, study_hours=None, stress_level=None, 
                                   learning_style=None, has_upcoming_exam=None, sleep_hours=None):
        """
        Process query with multiple input types for personalized recommendations.
        
        Args:
            category: Topic category (Memory, Focus, Stress, etc.)
            question: User's text question
            study_hours: Hours of study per day (numeric, 0-24)
            stress_level: Stress level on scale 1-10
            learning_style: Preferred learning style (Visual/Auditory/Kinesthetic/Reading)
            has_upcoming_exam: Boolean indicating if exam is soon
            sleep_hours: Hours of sleep per night (numeric, 0-24)
        """
        self.reset()
        self.response = None
        self.fired_rules = []
        self.reasoning_trace = []
        self.inferred_facts = []
        self.confidence_scores = []
        
        # Log inputs
        self.reasoning_trace.append(f"📋 Input Analysis:")
        self.reasoning_trace.append(f"  • Category: {category}")
        self.reasoning_trace.append(f"  • Question: {question}")
        if study_hours is not None:
            self.reasoning_trace.append(f"  • Study Hours/Day: {study_hours}")
        if stress_level is not None:
            self.reasoning_trace.append(f"  • Stress Level: {stress_level}/10")
        if learning_style:
            self.reasoning_trace.append(f"  • Learning Style: {learning_style}")
        if has_upcoming_exam is not None:
            self.reasoning_trace.append(f"  • Upcoming Exam: {'Yes' if has_upcoming_exam else 'No'}")
        if sleep_hours is not None:
            self.reasoning_trace.append(f"  • Sleep Hours: {sleep_hours}")
        
        # Update user profile
        self.update_user_profile(
            category=category,
            study_hours=study_hours,
            stress_level=stress_level,
            learning_style=learning_style,
            has_upcoming_exam=has_upcoming_exam,
            sleep_hours=sleep_hours
        )
        
        # Normalize category name to match KB keys
        category_normalized = category.lower().replace(" ", "_").replace("preparation", "prep")
        
        # Declare facts
        self.declare(Fact(category=category_normalized))
        self.declare(Fact(user_query=question.lower()))
        
        if study_hours is not None:
            self.declare(Fact(study_hours=study_hours))
        if stress_level is not None:
            self.declare(Fact(stress_level=stress_level))
        if learning_style:
            self.declare(Fact(learning_style=learning_style.lower()))
        if has_upcoming_exam is not None:
            self.declare(Fact(has_upcoming_exam=has_upcoming_exam))
        if sleep_hours is not None:
            self.declare(Fact(sleep_hours=sleep_hours))
        
        # Process with NLP for additional context
        nlp_result = self.nlp.process_query(question, self.kb)
        self.declare(Fact(processed_query=nlp_result))
        
        self.reasoning_trace.append("\n🔍 Inference Engine Running...")
        self.run()
        
        return self.response
    
    def process_query(self, query):
        """Legacy method for backward compatibility"""
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
    
    # ============================================================
    # INFERENCE RULES - Multi-Input Reasoning
    # ============================================================
    
    # Rule 1: High stress + Low sleep → Poor focus and memory
    @Rule(
        AS.f1 << Fact(stress_level=MATCH.s & P(lambda x: x >= 7)),
        AS.f2 << Fact(sleep_hours=MATCH.h & P(lambda x: x < 6)),
        salience=20
    )
    def infer_high_stress_low_sleep(self, s, h):
        self.declare(Fact(condition="poor_focus"))
        self.declare(Fact(condition="memory_impaired"))
        self.inferred_facts.append("poor_focus (stress + sleep)")
        self.inferred_facts.append("memory_impaired (stress + sleep)")
        self.reasoning_trace.append(f"⚠️ Rule Fired: High stress ({s}/10) + Low sleep ({h}h) → Poor focus & memory")
    
    # Rule 2: Low study hours + Upcoming exam → Need intensive strategy
    @Rule(
        AS.f1 << Fact(study_hours=MATCH.h & P(lambda x: x < 3)),
        AS.f2 << Fact(has_upcoming_exam=True),
        salience=18
    )
    def infer_low_study_upcoming_exam(self, h):
        self.declare(Fact(condition="needs_intensive_study"))
        self.declare(Fact(condition="time_pressure"))
        self.inferred_facts.append("needs_intensive_study")
        self.inferred_facts.append("time_pressure")
        self.reasoning_trace.append(f"⚠️ Rule Fired: Low study hours ({h}h/day) + Upcoming exam → Need intensive strategy")
    
    # Rule 3: High stress alone → Focus issues
    @Rule(
        AS.f << Fact(stress_level=MATCH.s & P(lambda x: x >= 8)),
        salience=15
    )
    def infer_high_stress(self, s):
        self.declare(Fact(condition="high_stress"))
        self.declare(Fact(condition="low_focus"))
        self.inferred_facts.append("high_stress")
        self.inferred_facts.append("low_focus")
        self.reasoning_trace.append(f"⚠️ Rule Fired: High stress ({s}/10) → Low focus")
    
    # Rule 4: Low sleep → Memory weakness
    @Rule(
        AS.f << Fact(sleep_hours=MATCH.h & P(lambda x: x < 7)),
        salience=15
    )
    def infer_low_sleep(self, h):
        self.declare(Fact(condition="sleep_deprived"))
        self.declare(Fact(condition="memory_weak"))
        self.inferred_facts.append("sleep_deprived")
        self.inferred_facts.append("memory_weak")
        self.reasoning_trace.append(f"⚠️ Rule Fired: Low sleep ({h}h) → Weak memory")
    
    # Rule 5: Moderate stress + Good study hours → Optimize with learning style
    @Rule(
        AS.f1 << Fact(stress_level=MATCH.s & P(lambda x: 4 <= x <= 6)),
        AS.f2 << Fact(study_hours=MATCH.h & P(lambda x: x >= 4)),
        AS.f3 << Fact(learning_style=MATCH.ls),
        salience=12
    )
    def infer_optimize_learning_style(self, s, h, ls):
        self.declare(Fact(condition="optimize_with_learning_style"))
        self.inferred_facts.append(f"optimize_with_{ls}_learning")
        self.reasoning_trace.append(f"✅ Rule Fired: Moderate stress + Good study habits → Optimize with {ls} learning")
    
    # Rule 6: Visual learner + Memory category → Use visualization
    @Rule(
        AS.f1 << Fact(category="memory"),
        AS.f2 << Fact(learning_style="visual"),
        salience=10
    )
    def infer_visual_memory_strategy(self):
        self.declare(Fact(condition="use_visualization"))
        self.inferred_facts.append("use_visualization_techniques")
        self.reasoning_trace.append("✅ Rule Fired: Memory + Visual learning → Use visualization techniques")
    
    # Rule 7: High study hours + High stress → Risk of burnout
    @Rule(
        AS.f1 << Fact(study_hours=MATCH.h & P(lambda x: x >= 8)),
        AS.f2 << Fact(stress_level=MATCH.s & P(lambda x: x >= 7)),
        salience=18
    )
    def infer_burnout_risk(self, h, s):
        self.declare(Fact(condition="burnout_risk"))
        self.inferred_facts.append("burnout_risk")
        self.reasoning_trace.append(f"⚠️ Rule Fired: High study hours ({h}h) + High stress ({s}/10) → Burnout risk!")
    
    # Rule 8: Good sleep + Low stress → Optimal learning state
    @Rule(
        AS.f1 << Fact(sleep_hours=MATCH.h & P(lambda x: x >= 7)),
        AS.f2 << Fact(stress_level=MATCH.s & P(lambda x: x <= 3)),
        salience=10
    )
    def infer_optimal_state(self, h, s):
        self.declare(Fact(condition="optimal_learning_state"))
        self.inferred_facts.append("optimal_learning_state")
        self.reasoning_trace.append(f"✅ Rule Fired: Good sleep ({h}h) + Low stress ({s}/10) → Optimal state!")
    
    # Rule 9: Kinesthetic learner → Active learning methods
    @Rule(
        AS.f << Fact(learning_style="kinesthetic"),
        salience=8
    )
    def infer_kinesthetic_methods(self):
        self.declare(Fact(condition="use_active_learning"))
        self.inferred_facts.append("active_learning_recommended")
        self.reasoning_trace.append("✅ Rule Fired: Kinesthetic learner → Recommend active learning methods")
    
    # Rule 10: Auditory learner → Discussion and verbal methods
    @Rule(
        AS.f << Fact(learning_style="auditory"),
        salience=8
    )
    def infer_auditory_methods(self):
        self.declare(Fact(condition="use_verbal_learning"))
        self.inferred_facts.append("verbal_learning_recommended")
        self.reasoning_trace.append("✅ Rule Fired: Auditory learner → Recommend discussion/verbal methods")
    
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
    
    # Main reasoning rule - Generates personalized recommendations
    @Rule(AS.f << Fact(category=MATCH.cat), salience=5)
    def reason_with_category(self, cat):
        """Main reasoning engine that combines all inputs for personalized advice"""
        self.reasoning_trace.append(f"\n🎯 Generating Recommendations for: {cat.upper()}")
        
        # Get category data from KB
        data = self.kb.get(cat, {})
        if not data:
            self.response = {
                "concept": "General Study Guide",
                "explanation": "I can help with memory, stress, time management, exams, motivation, confidence, and sleep."
            }
            return
        
        # Collect all current facts for context-aware reasoning
        profile = self.user_profile
        recs = []
        explanations = []
        
        # Get base recommendations from KB
        for rule in data.get("rules", []):
            recs.append(rule["recommend"])
            self.fired_rules.append(rule["id"])
            self.confidence_scores.append(rule.get("confidence", 0.8))
        
        # Adaptive recommendations based on numeric/scale inputs
        adaptations = self._generate_adaptive_recommendations(cat, profile)
        recs.extend(adaptations)
        
        # Generate context-aware diagnosis
        diagnosis = self._generate_diagnosis(cat, profile, data.get("diagnosis", ""))
        
        # Generate personalized explanation
        explanation = self._generate_explanation(cat, profile, data.get("explanation", ""))
        
        # Calculate overall confidence
        base_conf = max(self.confidence_scores) if self.confidence_scores else 0.85
        adjustment = self._calculate_confidence_adjustment(profile)
        final_confidence = min(0.99, max(0.60, base_conf + adjustment))
        
        self.reasoning_trace.append(f"\n📊 Confidence: {final_confidence:.0%} (Base: {base_conf:.0%}, Adjustment: {adjustment:+.0%})")
        
        self.response = {
            "concept": data.get("concept", "Study Guide"),
            "diagnosis": diagnosis,
            "explanation": explanation,
            "recommendation": "\n\n".join([f"**{i+1}.** {r}" for i, r in enumerate(recs[:6])]),
            "examples": data.get("examples", [])[:5],
            "resources": data.get("resources", [])[:5],
            "confidence": final_confidence,
            "reasoning_trace": self.reasoning_trace.copy(),
            "fired_rules": self.fired_rules.copy(),
            "inferred_facts": self.inferred_facts.copy(),
            "topic": cat,
            "user_profile": profile
        }
    
    def _generate_adaptive_recommendations(self, category, profile):
        """Generate personalized recommendations based on user inputs"""
        recs = []
        stress = profile.get("stress_level")
        study_hrs = profile.get("study_hours")
        sleep_hrs = profile.get("sleep_hours")
        learning = profile.get("learning_style")
        upcoming_exam = profile.get("has_upcoming_exam")
        
        # High stress adaptations
        if stress and stress >= 8:
            recs.append("**PRIORITY: Stress Management** - Your stress level is very high. Practice 10-minute breathing exercises before each study session.")
            if category == "memory":
                recs.append("Use **low-stress memory methods** like gentle spaced repetition instead of intensive cramming.")
        
        # Low sleep adaptations
        if sleep_hrs and sleep_hrs < 6:
            recs.append(f"**CRITICAL: Sleep Recovery** - You're sleeping only {sleep_hrs}h/night. Aim for 7-8 hours. Memory consolidation happens during sleep!")
            if category == "memory":
                recs.append("Focus on **power naps** (20-30 min) after study sessions to boost memory retention.")
        
        # Low study hours + upcoming exam
        if study_hrs and study_hrs < 3 and upcoming_exam:
            recs.append(f"**URGENT: Time Management** - Only {study_hrs}h/day with an exam approaching. Use the **Pomodoro technique** (25min focus, 5min break) to maximize efficiency.")
        
        # Burnout risk
        if study_hrs and study_hrs >= 8 and stress and stress >= 7:
            recs.append("**⚠️ BURNOUT WARNING** - Studying 8+ hours with high stress is unsustainable. Take mandatory 1-hour breaks every 3 hours.")
        
        # Learning style adaptations
        if learning:
            if learning == "visual" and category == "memory":
                recs.append("**Visual Learning Strategy** - Use mind maps, color-coded notes, and the memory palace technique for your visual learning style.")
            elif learning == "auditory" and category == "memory":
                recs.append("**Auditory Learning Strategy** - Record yourself explaining concepts, use mnemonics, and study with discussion groups.")
            elif learning == "kinesthetic":
                recs.append(f"**Kinesthetic Learning Strategy** - Use physical flashcards, walk while reviewing, and create hands-on demonstrations for {category}.")
            elif learning == "reading":
                recs.append("**Reading/Writing Strategy** - Rewrite notes in your own words, create detailed outlines, and use written summaries.")
        
        # Optimal state encouragement
        if sleep_hrs and sleep_hrs >= 7 and stress and stress <= 3:
            recs.append("**✅ Excellent Conditions** - Your low stress and good sleep put you in an optimal learning state. Maximize this with active recall practice!")
        
        return recs
    
    def _generate_diagnosis(self, category, profile, base_diagnosis):
        """Generate personalized diagnosis based on inputs"""
        parts = [base_diagnosis] if base_diagnosis else []
        
        stress = profile.get("stress_level")
        sleep_hrs = profile.get("sleep_hours")
        study_hrs = profile.get("study_hours")
        
        if stress and stress >= 7:
            parts.append(f"High stress detected ({stress}/10) - this significantly impacts {category}.")
        if sleep_hrs and sleep_hrs < 6:
            parts.append(f"Sleep deprivation ({sleep_hrs}h) is affecting cognitive performance.")
        if study_hrs and study_hrs < 2:
            parts.append(f"Very low study time ({study_hrs}h/day) - need to increase or optimize efficiency.")
        elif study_hrs and study_hrs >= 8:
            parts.append(f"High study hours ({study_hrs}h/day) - watch for diminishing returns and burnout.")
        
        return " ".join(parts) if parts else f"Analyzing your {category} concerns..."
    
    def _generate_explanation(self, category, profile, base_explanation):
        """Generate personalized explanation with context"""
        parts = [base_explanation]
        
        learning = profile.get("learning_style")
        if learning:
            parts.append(f"\n\n**For {learning.capitalize()} Learners:** Your learning style is well-suited for {self._get_learning_style_strengths(learning)}.")
        
        if "burnout_risk" in self.inferred_facts:
            parts.append("\n\n⚠️ **Important:** Your current pattern shows burnout risk. Balance is crucial for sustainable learning.")
        
        return " ".join(parts)
    
    def _get_learning_style_strengths(self, style):
        """Get strengths for each learning style"""
        strengths = {
            "visual": "diagrams, charts, mind maps, color coding, and spatial organization",
            "auditory": "discussions, lectures, verbal explanations, podcasts, and group study",
            "kinesthetic": "hands-on practice, movement while studying, physical models, and active experimentation",
            "reading": "textbooks, written notes, detailed outlines, and written summaries"
        }
        return strengths.get(style, "various methods")
    
    def _calculate_confidence_adjustment(self, profile):
        """Calculate confidence adjustment based on data completeness"""
        adjustment = 0.0
        
        # More inputs = higher confidence
        input_count = sum(1 for v in profile.values() if v is not None)
        adjustment += input_count * 0.02  # +2% per input
        
        # Consistent patterns boost confidence
        if "optimal_learning_state" in self.inferred_facts:
            adjustment += 0.05
        
        # Warning conditions slightly reduce confidence (more uncertainty)
        if "burnout_risk" in self.inferred_facts:
            adjustment -= 0.03
        
        return adjustment
    
    
    @Rule(AS.f << Fact(processed_query=MATCH.nlp), salience=5)
    def reason(self, nlp):
        """Legacy reasoning for backward compatibility with text-only queries"""
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
            "recommendation": "\n\n".join([f"{i+1}. {r}" for i, r in enumerate(recs[:4])]),
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
        return "\n".join(self.reasoning_trace)
    
    def get_confidence(self):
        return self.response.get("confidence", 0.0) if self.response else 0.0
