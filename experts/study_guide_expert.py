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
        self.uncertainty_factors = []
        self.missing_info_warnings = []
        self.confidence_breakdown = {}
    
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
        self.uncertainty_factors = []
        self.missing_info_warnings = []
        self.confidence_breakdown = {}
        
        # Analyze data completeness
        total_inputs = 5  # study_hours, stress_level, learning_style, has_upcoming_exam, sleep_hours
        provided_inputs = sum([
            study_hours is not None,
            stress_level is not None,
            learning_style is not None,
            has_upcoming_exam is not None,
            sleep_hours is not None
        ])
        
        data_completeness = (provided_inputs / total_inputs) * 100
        
        # Log inputs
        self.reasoning_trace.append("📋 Input Analysis:")
        self.reasoning_trace.append(f"  • Category: {category}")
        self.reasoning_trace.append(f"  • Question: {question}")
        self.reasoning_trace.append(f"  • Data Completeness: {data_completeness:.0f}% ({provided_inputs}/{total_inputs} fields)")
        
        if study_hours is not None:
            self.reasoning_trace.append(f"  • Study Hours/Day: {study_hours}")
        else:
            self.missing_info_warnings.append("study_hours")
            self.uncertainty_factors.append(("missing_study_hours", 0.08))
            
        if stress_level is not None:
            self.reasoning_trace.append(f"  • Stress Level: {stress_level}/10")
        else:
            self.missing_info_warnings.append("stress_level")
            self.uncertainty_factors.append(("missing_stress_level", 0.10))
            
        if learning_style:
            self.reasoning_trace.append(f"  • Learning Style: {learning_style}")
        else:
            self.missing_info_warnings.append("learning_style")
            self.uncertainty_factors.append(("missing_learning_style", 0.06))
            
        if has_upcoming_exam is not None:
            self.reasoning_trace.append(f"  • Upcoming Exam: {'Yes' if has_upcoming_exam else 'No'}")
        else:
            self.missing_info_warnings.append("has_upcoming_exam")
            self.uncertainty_factors.append(("missing_exam_info", 0.04))
            
        if sleep_hours is not None:
            self.reasoning_trace.append(f"  • Sleep Hours: {sleep_hours}")
        else:
            self.missing_info_warnings.append("sleep_hours")
            self.uncertainty_factors.append(("missing_sleep_hours", 0.07))
        
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
        
        self.reasoning_trace.append("\n🔍 Inference Engine Running...")
        self.run()
        
        return self.response
    
    def process_query(self, query):
        """Legacy method for backward compatibility - simplified version without NLP"""
        self.reset()
        self.response = None
        self.fired_rules = []
        self.reasoning_trace = []
        self.inferred_facts = []
        self.confidence_scores = []
        
        self.reasoning_trace.append(f"Query: {query}")
        self.declare(Fact(user_query=query.lower()))
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
    
    # Rule 11: Reading/Writing learner → Text-based methods
    @Rule(
        AS.f << Fact(learning_style="reading writing"),
        salience=8
    )
    def infer_reading_writing_methods(self):
        self.declare(Fact(condition="use_text_based_learning"))
        self.inferred_facts.append("text_based_learning_recommended")
        self.reasoning_trace.append("✅ Rule Fired: Reading/Writing learner → Recommend note-taking and written summaries")
    
    # Rule 12: High stress + High study hours + Low sleep → Critical burnout
    @Rule(
        AS.f1 << Fact(stress_level=MATCH.s & P(lambda x: x >= 7)),
        AS.f2 << Fact(study_hours=MATCH.h & P(lambda x: x >= 7)),
        AS.f3 << Fact(sleep_hours=MATCH.sl & P(lambda x: x < 7)),
        salience=25
    )
    def infer_critical_burnout(self, s, h, sl):
        self.declare(Fact(condition="critical_burnout_imminent"))
        self.inferred_facts.append("critical_burnout_warning")
        self.reasoning_trace.append(f"🚨 Rule Fired: High stress ({s}/10) + High study ({h}h) + Low sleep ({sl}h) → CRITICAL BURNOUT RISK!")
        self.uncertainty_factors.append(("high_risk_detected", -0.05))
    
    # Rule 13: Low stress + High study hours + Good sleep → Optimal performance zone
    @Rule(
        AS.f1 << Fact(stress_level=MATCH.s & P(lambda x: x <= 4)),
        AS.f2 << Fact(study_hours=MATCH.h & P(lambda x: x >= 5)),
        AS.f3 << Fact(sleep_hours=MATCH.sl & P(lambda x: x >= 7)),
        salience=15
    )
    def infer_optimal_performance(self, s, h, sl):
        self.declare(Fact(condition="peak_performance_zone"))
        self.inferred_facts.append("optimal_conditions_detected")
        self.reasoning_trace.append(f"⭐ Rule Fired: Low stress ({s}/10) + Good study ({h}h) + Good sleep ({sl}h) → PEAK PERFORMANCE!")
    
    # Rule 14: Upcoming exam + Low study hours → Urgent intervention needed
    @Rule(
        AS.f1 << Fact(has_upcoming_exam=True),
        AS.f2 << Fact(study_hours=MATCH.h & P(lambda x: x < 3)),
        salience=20
    )
    def infer_urgent_exam_crisis(self, h):
        self.declare(Fact(condition="exam_crisis"))
        self.inferred_facts.append("urgent_exam_preparation_needed")
        self.reasoning_trace.append(f"⚠️ Rule Fired: Upcoming exam + Low study ({h}h/day) → URGENT ACTION REQUIRED!")
    
    # Rule 15: No upcoming exam + High study hours → Potential overpreparation
    @Rule(
        AS.f1 << Fact(has_upcoming_exam=False),
        AS.f2 << Fact(study_hours=MATCH.h & P(lambda x: x >= 9)),
        salience=10
    )
    def infer_overpreparation(self, h):
        self.declare(Fact(condition="possible_overpreparation"))
        self.inferred_facts.append("balance_needed")
        self.reasoning_trace.append(f"💡 Rule Fired: No immediate exam + High study ({h}h/day) → Consider work-life balance")
    
    # Rule 16: Moderate values across all metrics → Stable but improvable
    @Rule(
        AS.f1 << Fact(stress_level=MATCH.s & P(lambda x: 4 <= x <= 6)),
        AS.f2 << Fact(study_hours=MATCH.h & P(lambda x: 3 <= x <= 6)),
        AS.f3 << Fact(sleep_hours=MATCH.sl & P(lambda x: 6 <= x <= 8)),
        salience=8
    )
    def infer_stable_baseline(self, s, h, sl):
        self.declare(Fact(condition="stable_baseline"))
        self.inferred_facts.append("room_for_optimization")
        self.reasoning_trace.append(f"✓ Rule Fired: Balanced metrics → Good foundation, room for optimization")
    
    # Rule 17: Excessive sleep (>10 hours) → Health concern or data error
    @Rule(
        AS.f << Fact(sleep_hours=MATCH.h & P(lambda x: x > 10)),
        salience=22
    )
    def infer_excessive_sleep(self, h):
        self.declare(Fact(condition="excessive_sleep_detected"))
        self.inferred_facts.append("excessive_sleep_warning")
        self.reasoning_trace.append(f"⚠️ Rule Fired: Excessive sleep ({h}h) → Possible health concern or data entry error. Normal range: 7-9h")
        self.uncertainty_factors.append(("unusual_sleep_pattern", 0.05))
    
    # Rule 18: Severe sleep deprivation (1-2 hours) → Emergency crisis intervention
    @Rule(
        AS.f << Fact(sleep_hours=MATCH.h & P(lambda x: 1 <= x <= 2)),
        salience=30  # Highest priority - critical health risk
    )
    def infer_severe_sleep_deprivation(self, h):
        self.declare(Fact(condition="severe_sleep_deprivation"))
        self.inferred_facts.append("critical_sleep_crisis")
        self.reasoning_trace.append(f"🚨 CRITICAL Rule Fired: Severe sleep deprivation ({h}h) → Immediate health risk. Cognitive function severely impaired.")
        self.uncertainty_factors.append(("critical_health_risk", 0.15))
    
    # Rule 19: Critical sleep deficit (3-4 hours) → Immediate recovery protocol
    @Rule(
        AS.f << Fact(sleep_hours=MATCH.h & P(lambda x: 3 <= x <= 4)),
        salience=28
    )
    def infer_critical_sleep_deficit(self, h):
        self.declare(Fact(condition="critical_sleep_deficit"))
        self.inferred_facts.append("severe_sleep_debt")
        self.reasoning_trace.append(f"🚨 Rule Fired: Critical sleep deficit ({h}h) → Immediate recovery needed. Performance degraded by 40-60%.")
        self.uncertainty_factors.append(("severe_sleep_debt", 0.12))
    
    # Rule 20: Suboptimal sleep (5-6 hours) → Optimization strategies
    @Rule(
        AS.f << Fact(sleep_hours=MATCH.h & P(lambda x: 5 <= x <= 6)),
        salience=20
    )
    def infer_suboptimal_sleep(self, h):
        self.declare(Fact(condition="suboptimal_sleep"))
        self.inferred_facts.append("sleep_optimization_needed")
        self.reasoning_trace.append(f"⚠️ Rule Fired: Suboptimal sleep ({h}h) → Below recommended 7-9h. Performance degraded by 20-30%.")
        self.uncertainty_factors.append(("sleep_deficit", 0.08))
    
    # Rule 21: Optimal sleep (7-9 hours) → Maintenance recommendations
    @Rule(
        AS.f << Fact(sleep_hours=MATCH.h & P(lambda x: 7 <= x <= 9)),
        salience=15
    )
    def infer_optimal_sleep(self, h):
        self.declare(Fact(condition="optimal_sleep"))
        self.inferred_facts.append("sleep_quality_good")
        self.reasoning_trace.append(f"✓ Rule Fired: Optimal sleep ({h}h) → Within healthy range. Focus on sleep quality maintenance.")
    
    # Rule 22: Minimal stress (1-2) → Peak performance optimization
    @Rule(
        AS.f << Fact(stress=MATCH.s & P(lambda x: 1 <= x <= 2)),
        salience=18
    )
    def infer_minimal_stress(self, s):
        self.declare(Fact(condition="minimal_stress"))
        self.inferred_facts.append("peak_performance_state")
        self.reasoning_trace.append(f"✓ Rule Fired: Minimal stress ({s}/10) → Excellent baseline. Focus on maximizing this advantage.")
    
    # Rule 23: Low stress (3-4) → Proactive stress management
    @Rule(
        AS.f << Fact(stress=MATCH.s & P(lambda x: 3 <= x <= 4)),
        salience=16
    )
    def infer_low_stress(self, s):
        self.declare(Fact(condition="low_stress"))
        self.inferred_facts.append("proactive_management_zone")
        self.reasoning_trace.append(f"✓ Rule Fired: Low stress ({s}/10) → Good baseline. Proactive management can prevent escalation.")
    
    # Rule 24: Moderate-high stress (6-7) → Active intervention needed
    @Rule(
        AS.f << Fact(stress=MATCH.s & P(lambda x: 6 <= x <= 7)),
        salience=22
    )
    def infer_moderate_high_stress(self, s):
        self.declare(Fact(condition="moderate_high_stress"))
        self.inferred_facts.append("intervention_needed")
        self.reasoning_trace.append(f"⚠️ Rule Fired: Moderate-high stress ({s}/10) → Active intervention needed to prevent burnout.")
        self.uncertainty_factors.append(("elevated_stress", 0.08))
    
    # Rule 25: Extreme stress (9-10) → Crisis mode + mental health resources
    @Rule(
        AS.f << Fact(stress=MATCH.s & P(lambda x: 9 <= x <= 10)),
        salience=29
    )
    def infer_extreme_stress(self, s):
        self.declare(Fact(condition="extreme_stress"))
        self.inferred_facts.append("mental_health_crisis")
        self.reasoning_trace.append(f"🚨 CRITICAL Rule Fired: Extreme stress ({s}/10) → Crisis level. Professional mental health support recommended.")
        self.uncertainty_factors.append(("crisis_stress", 0.15))
    
    # Rule 26: Minimal study (0-1 hours) → Motivation + time management crisis
    @Rule(
        AS.f << Fact(study_hours=MATCH.h & P(lambda x: 0 <= x <= 1)),
        salience=24
    )
    def infer_minimal_study(self, h):
        self.declare(Fact(condition="minimal_study"))
        self.inferred_facts.append("motivation_crisis")
        self.reasoning_trace.append(f"⚠️ Rule Fired: Minimal study ({h}h) → Possible motivation or time management issue. Academic risk.")
        self.uncertainty_factors.append(("academic_engagement_low", 0.10))
    
    # Rule 27: Low study (2-3 hours) → Efficiency and technique focus
    @Rule(
        AS.f << Fact(study_hours=MATCH.h & P(lambda x: 2 <= x <= 3)),
        salience=18
    )
    def infer_low_study(self, h):
        self.declare(Fact(condition="low_study"))
        self.inferred_facts.append("efficiency_focus_needed")
        self.reasoning_trace.append(f"⚠️ Rule Fired: Low study ({h}h) → Focus on study efficiency and effective techniques to maximize limited time.")
    
    # Rule 28: Optimal study (4-6 hours) → Quality over quantity emphasis
    @Rule(
        AS.f << Fact(study_hours=MATCH.h & P(lambda x: 4 <= x <= 6)),
        salience=15
    )
    def infer_optimal_study(self, h):
        self.declare(Fact(condition="optimal_study"))
        self.inferred_facts.append("sustainable_study_pattern")
        self.reasoning_trace.append(f"✓ Rule Fired: Optimal study ({h}h) → Sustainable range. Focus on quality and active learning techniques.")
    
    # Rule 29: Excessive study (9-10 hours) → Diminishing returns warning
    @Rule(
        AS.f << Fact(study_hours=MATCH.h & P(lambda x: 9 <= x <= 10)),
        salience=21
    )
    def infer_excessive_study(self, h):
        self.declare(Fact(condition="excessive_study"))
        self.inferred_facts.append("diminishing_returns")
        self.reasoning_trace.append(f"⚠️ Rule Fired: Excessive study ({h}h) → Diminishing returns zone. Risk of burnout and reduced effectiveness.")
        self.uncertainty_factors.append(("overwork_risk", 0.08))
    
    # Rule 30: Extreme study (11-12 hours) → Burnout prevention mandate
    @Rule(
        AS.f << Fact(study_hours=MATCH.h & P(lambda x: 11 <= x <= 12)),
        salience=26
    )
    def infer_extreme_study(self, h):
        self.declare(Fact(condition="extreme_study"))
        self.inferred_facts.append("burnout_imminent")
        self.reasoning_trace.append(f"🚨 Rule Fired: Extreme study ({h}h) → Burnout risk critical. Immediate schedule reduction needed.")
        self.uncertainty_factors.append(("critical_burnout_risk", 0.12))
    
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
        
        # Generate missing information suggestions
        missing_info_suggestions = self._generate_missing_info_suggestions()
        
        # Generate uncertainty explanation
        uncertainty_explanation = self._generate_uncertainty_explanation(final_confidence)
        
        self.response = {
            "concept": data.get("concept", "Study Guide"),
            "diagnosis": diagnosis,
            "explanation": explanation,
            "recommendation": "\n\n".join([f"**{i+1}.** {r}" for i, r in enumerate(recs[:6])]),
            "examples": data.get("examples", [])[:5],
            "resources": data.get("resources", [])[:5],
            "confidence": final_confidence,
            "confidence_breakdown": self.confidence_breakdown,
            "uncertainty_explanation": uncertainty_explanation,
            "missing_info_warnings": self.missing_info_warnings,
            "missing_info_suggestions": missing_info_suggestions,
            "reasoning_trace": self.reasoning_trace.copy(),
            "fired_rules": self.fired_rules.copy(),
            "inferred_facts": self.inferred_facts.copy(),
            "topic": cat,
            "user_profile": profile
        }
    
    def _generate_adaptive_recommendations(self, category, profile):
        """Generate personalized recommendations based on user inputs and inferred conditions"""
        recs = []
        stress = profile.get("stress_level")
        study_hrs = profile.get("study_hours")
        sleep_hrs = profile.get("sleep_hours")
        learning = profile.get("learning_style")
        upcoming_exam = profile.get("has_upcoming_exam")
        
        # Critical burnout state (highest priority)
        if "critical_burnout_warning" in self.inferred_facts:
            recs.append("🚨 **CRITICAL: IMMEDIATE ACTION REQUIRED** - Your combination of high stress, excessive study hours, and insufficient sleep puts you at severe burnout risk. STOP studying for 24 hours and prioritize rest.")
            recs.append("**Emergency Recovery Plan**: Sleep 8+ hours tonight, take tomorrow off completely, schedule urgent meeting with academic counselor or therapist.")
            recs.append("**Long-term Intervention**: Your current approach is unsustainable. Shift to quality over quantity - study 4-5 hours max with proper breaks.")
            return recs  # Return immediately - this overrides everything else
        
        # Peak performance zone (encourage optimization)
        if "optimal_conditions_detected" in self.inferred_facts:
            recs.append("⭐ **OPTIMAL STATE DETECTED** - You're in peak learning conditions! Your balanced stress, good sleep, and sufficient study hours create ideal cognitive performance.")
            if category == "memory":
                recs.append("**Maximize This Window**: Use advanced memory techniques like the method of loci, interleaving practice, and elaborative interrogation.")
            elif category == "focus":
                recs.append("**Deep Work Potential**: Your conditions are perfect for 90-minute deep work sessions. Tackle your most challenging material now.")
            else:
                recs.append("**Compound Your Advantage**: This is the time to learn new, complex material. Your brain is primed for deep understanding.")
            recs.append("**Maintain Excellence**: Keep this routine - track what's working and replicate it daily.")
        
        # Urgent exam crisis
        if "urgent_exam_preparation_needed" in self.inferred_facts:
            recs.append(f"⏰ **EXAM CRISIS MODE** - With only {study_hrs}h/day and an exam approaching, you need emergency triage strategies.")
            recs.append("**Priority Triage**: Focus ONLY on high-weightage topics (use 80/20 rule). Skip minor details completely.")
            recs.append("**Intensive Study Protocol**: 3 x 90-min sessions daily with Pomodoro breaks. Use active recall and past papers only - no passive reading.")
            recs.append("**Night-Before Strategy**: Light review only, 8 hours sleep mandatory (sacrificing sleep for cramming reduces performance 40%).")
        
        # Overpreparation warning
        if "balance_needed" in self.inferred_facts:
            recs.append(f"⚖️ **BALANCE CHECK** - You're studying {study_hrs}h/day without an immediate exam. This intensity may lead to diminishing returns.")
            recs.append("**Optimization Advice**: Reduce to 5-6 hours of focused study. Quality > Quantity. Your brain needs rest for consolidation.")
            recs.append("**Schedule Downtime**: Add deliberate breaks for hobbies, exercise, socializing. Burnout prevention is key for long-term success.")
        
        # Stable baseline (room for optimization)
        if "room_for_optimization" in self.inferred_facts:
            recs.append("✓ **SOLID FOUNDATION** - Your metrics show balance, but there's room for improvement to reach peak performance.")
            if stress and 4 <= stress <= 6:
                recs.append("**Stress Optimization**: You're in the moderate zone. Try meditation (10 min/day) to drop to optimal range (2-4).")
            if study_hrs and 3 <= study_hrs <= 6:
                recs.append("**Study Optimization**: Consider adding 1-2 hours of focused study using proven techniques (spaced repetition, active recall).")
        
        # High stress specific interventions
        if stress and stress >= 8:
            recs.append("**PRIORITY: Stress Management** - Your stress level is critically high. Start with 4-7-8 breathing: Inhale 4s, Hold 7s, Exhale 8s (repeat 3x).")
            if category == "memory":
                recs.append("**Low-Stress Memory Protocol**: Avoid intense cramming - it spikes cortisol which impairs hippocampus function. Use gentle spaced repetition (10 min sessions).")
        elif stress and stress >= 5:
            recs.append("**Stress Reduction**: Moderate stress detected. Daily 20-min walk + 10-min meditation can significantly improve focus and retention.")
        
        # Sleep-specific interventions
        if "critical_sleep_crisis" in self.inferred_facts:
            # Severe sleep deprivation (1-2 hours) - Rule 18
            recs.append(f"🚨 **EMERGENCY: SEVERE SLEEP DEPRIVATION** - {sleep_hrs}h is a critical health risk. Normal cognitive function is impossible at this level.")
            recs.append("**IMMEDIATE ACTION REQUIRED**: 1) Cancel all non-essential activities today, 2) Take a 90-minute nap NOW if possible, 3) Go to bed at least 2 hours earlier tonight, 4) Seek medical attention if this is chronic.")
            recs.append("**Health Warning**: Sleep deprivation at this level impairs judgment worse than alcohol intoxication. Academic performance will be near zero. Recovery must be your only priority.")
            recs.append("**Crisis Resources**: Contact university health services immediately. This level indicates possible crisis situation requiring professional support.")
        elif "severe_sleep_debt" in self.inferred_facts:
            # Critical sleep deficit (3-4 hours) - Rule 19
            recs.append(f"🚨 **CRITICAL SLEEP DEFICIT** - {sleep_hrs}h/night causes 40-60% performance degradation. You're operating in crisis mode.")
            recs.append("**Recovery Protocol**: Tonight: Sleep 8+ hours (set hard bedtime). This week: Build back to 7h minimum. Cancel non-essential commitments.")
            recs.append("**Performance Reality Check**: Your current study efforts are 50% less effective than they would be with proper sleep. Sleeping IS studying.")
            if category == "memory":
                recs.append("**Memory Impact**: Memory consolidation requires REM sleep - you're getting almost none. Information studied now won't stick.")
        elif "sleep_optimization_needed" in self.inferred_facts:
            # Suboptimal sleep (5-6 hours) - Rule 20
            recs.append(f"⚠️ **SUBOPTIMAL SLEEP** - {sleep_hrs}h reduces performance by 20-30%. Aiming for 7-8h will significantly boost results.")
            recs.append("**Sleep Extension Plan**: Move bedtime 30 min earlier this week, then another 30 min next week. Use the 10-3-2-1-0 rule: No caffeine 10h before bed, no food 3h before, no work 2h before, no screens 1h before, 0 times hitting snooze.")
            if category == "focus":
                recs.append("**Focus Impact**: That afternoon brain fog you feel? It's directly from insufficient sleep. Add 1-2h sleep to regain sharp focus.")
        elif "sleep_quality_good" in self.inferred_facts:
            # Optimal sleep (7-9 hours) - Rule 21
            recs.append(f"✓ **OPTIMAL SLEEP** - {sleep_hrs}h is excellent! Your cognitive performance is at maximum capacity.")
            recs.append("**Maintain Excellence**: Keep consistent sleep/wake times (even weekends). Monitor sleep quality using apps like Sleep Cycle. Focus on REM and deep sleep optimization.")
            if category == "memory":
                recs.append("**Memory Advantage**: Your sleep is perfect for memory consolidation. Review important material before bed to maximize overnight processing.")
        elif sleep_hrs and sleep_hrs > 10:
            # Excessive sleep warning (Rule 17 triggered)
            recs.append(f"⚠️ **UNUSUAL SLEEP PATTERN** - You reported {sleep_hrs}h/night, which exceeds the recommended 7-9 hours for adults.")
            recs.append("**Health Check Needed**: Excessive sleep (>10h) can indicate: 1) Depression or mood disorders, 2) Sleep quality issues (waking frequently), 3) Medical conditions (thyroid, sleep apnea), or 4) Data entry error.")
            recs.append("**Recommended Actions**: If this is accurate, consult university health services or your doctor. Quality of sleep matters more than quantity. Track your actual sleep vs. time in bed.")
            recs.append("**If Data Error**: Please re-enter with actual sleep hours. Normal healthy range is 7-9 hours per night.")
        
        # Stress-specific interventions by level
        if "mental_health_crisis" in self.inferred_facts:
            # Extreme stress (9-10) - Rule 25
            recs.append(f"🚨 **CRISIS-LEVEL STRESS** - {stress}/10 stress indicates severe distress. Your wellbeing is more important than any deadline.")
            recs.append("**URGENT: Seek Support Immediately**: 1) University Counseling Center (same-day appointments), 2) Crisis hotline: 988 (USA) / 116 123 (UK), 3) Trusted friend/family member, 4) Academic advisor for deadline extensions.")
            recs.append("**Emergency Stress Relief**: 4-7-8 breathing (Inhale 4s, Hold 7s, Exhale 8s) x 4 rounds. Cold water on face. Progressive muscle relaxation. These activate parasympathetic nervous system.")
            recs.append("**Academic Pause Needed**: Consider requesting incomplete grade or medical withdrawal. Your mental health must come first.")
        elif "intervention_needed" in self.inferred_facts:
            # Moderate-high stress (6-7) - Rule 24
            recs.append(f"⚠️ **ELEVATED STRESS** - {stress}/10 is approaching burnout territory. Active intervention needed now to prevent crisis.")
            recs.append("**Intervention Plan**: 1) Daily 20-min walk outside (proven stress reducer), 2) Box breathing 3x daily (4s in, 4s hold, 4s out, 4s hold), 3) Reduce study hours by 25% to prevent escalation.")
            recs.append("**Schedule Relief Activities**: Block calendar time for stress management - it's not optional. Consider yoga, exercise, hobbies, social connection.")
            if category == "focus":
                recs.append("**Focus Recovery**: High stress kills concentration. Take frequent breaks (Pomodoro). Meditate 10 min before study sessions.")
        elif "proactive_management_zone" in self.inferred_facts:
            # Low stress (3-4) - Rule 23
            recs.append(f"✓ **LOW STRESS** - {stress}/10 is a healthy baseline. Proactive management will keep you here.")
            recs.append("**Maintain This State**: Daily stress check-ins. Keep stress diary to identify triggers. Continue current wellness practices.")
            recs.append("**Stress Prevention**: Build buffer time in schedule. Practice saying 'no' to overcommitment. Weekly stress-relief activities.")
        elif "peak_performance_state" in self.inferred_facts:
            # Minimal stress (1-2) - Rule 22
            recs.append(f"⭐ **PEAK MENTAL STATE** - {stress}/10 stress is optimal! You're in the zone for maximum learning and creativity.")
            recs.append("**Maximize This Advantage**: Tackle your hardest, most complex material now. Your brain is primed for deep understanding and problem-solving.")
            recs.append("**Maintain Peak Performance**: Track what's keeping stress low (sleep, exercise, social support). Replicate these conditions daily.")
        
        # Study hours interventions by level
        if "burnout_imminent" in self.inferred_facts:
            # Extreme study (11-12 hours) - Rule 30
            recs.append(f"🚨 **BURNOUT IMMINENT** - {study_hrs}h/day is unsustainable and counterproductive. You're past the point of diminishing returns.")
            recs.append("**MANDATORY REDUCTION**: Cut to 6h max tomorrow. Your brain needs recovery time to consolidate learning. More hours = less retention at this point.")
            recs.append("**Quality Over Quantity**: 4 hours of focused, strategic study beats 12 hours of exhausted cramming. Prioritize sleep and breaks.")
            recs.append("**Schedule Intervention**: Meet with academic advisor about workload. Consider dropping a course if possible. Your health matters more than grades.")
        elif "diminishing_returns" in self.inferred_facts:
            # Excessive study (9-10 hours) - Rule 29
            recs.append(f"⚠️ **DIMINISHING RETURNS ZONE** - {study_hrs}h/day approaches the limit of productive study. Efficiency is dropping.")
            recs.append("**Optimization Advice**: Research shows 6-8h is the sweet spot. Beyond that, fatigue reduces retention significantly. Consider reducing by 2-3 hours.")
            recs.append("**Quality Focus**: Instead of longer hours, improve technique: Active recall testing, spaced repetition, teaching concepts to others.")
        elif "sustainable_study_pattern" in self.inferred_facts:
            # Optimal study (4-6 hours) - Rule 28
            recs.append(f"✓ **OPTIMAL STUDY VOLUME** - {study_hrs}h/day is sustainable and effective. Focus on study quality now.")
            recs.append("**Maximize Effectiveness**: Use proven techniques: Pomodoro (25 min work, 5 min break), active recall, elaborative interrogation, spaced repetition.")
            recs.append("**Quality Indicators**: If you're staying in this range, focus on deep work vs. shallow work. Minimize distractions, use time-blocking.")
        elif "efficiency_focus_needed" in self.inferred_facts:
            # Low study (2-3 hours) - Rule 27
            recs.append(f"⚠️ **LIMITED STUDY TIME** - {study_hrs}h/day may be insufficient depending on your goals. Focus on maximum efficiency.")
            recs.append("**Efficiency Protocol**: Use Pareto principle (80/20 rule) - focus on high-yield material. Eliminate passive reading. Use active recall exclusively.")
            recs.append("**Time Expansion**: If possible, find 1-2 more hours. Morning slots are most effective. Audit time-wasters (social media, TV).")
            if category == "time_management":
                recs.append("**Time Management**: Use time-blocking. Schedule study sessions like appointments. Track where time goes with app like RescueTime.")
        elif "motivation_crisis" in self.inferred_facts:
            # Minimal study (0-1 hours) - Rule 26
            recs.append(f"🚨 **ACADEMIC ENGAGEMENT CRISIS** - {study_hrs}h/day indicates possible motivation or time management breakdown.")
            recs.append("**Root Cause Analysis**: Is this: 1) Motivation issue (don't want to), 2) Time issue (don't have time), or 3) Mental health (can't focus)? Each needs different solution.")
            recs.append("**Immediate Steps**: Start tiny - commit to just 15 minutes today. Use Pomodoro timer. Pick easiest/most interesting subject. Build momentum slowly.")
            recs.append("**Support Resources**: Meet with academic advisor. Consider tutoring or study skills workshop. Join study group for accountability.")
            if category == "motivation":
                recs.append("**Motivation Recovery**: Set tiny, achievable goals. Use reward systems. Find study buddy. Connect material to personal interests.")
        
        # Learning style specific recommendations
        if learning:
            learning_lower = learning.lower()
            if "visual" in learning_lower:
                if category == "memory":
                    recs.append("**Visual Memory Mastery**: Create mind maps with colors. Use memory palace technique. Draw diagrams. Watch educational videos.")
                elif category == "focus":
                    recs.append("**Visual Focus Strategy**: Remove visual distractions. Use visual timers (Pomodoro). Study in organized, visually calm spaces.")
                else:
                    recs.append(f"**Visual Learning for {category}**: Use charts, diagrams, color-coding, and visual metaphors to understand concepts.")
            
            elif "auditory" in learning_lower:
                if category == "memory":
                    recs.append("**Auditory Memory Techniques**: Record lectures and replay. Teach concepts aloud. Create verbal mnemonics. Join study groups for discussion.")
                elif category == "focus":
                    recs.append("**Auditory Focus**: Use white noise or binaural beats. Explain concepts aloud while studying. Minimize auditory distractions.")
                else:
                    recs.append(f"**Auditory Learning for {category}**: Use podcasts, lectures, verbal explanations, and discussion-based learning.")
            
            elif "kinesthetic" in learning_lower:
                if category == "memory":
                    recs.append("**Kinesthetic Memory Methods**: Walk while reviewing flashcards. Use physical objects as memory aids. Act out concepts. Write by hand (not typing).")
                elif category == "focus":
                    recs.append("**Kinesthetic Focus**: Take movement breaks every 25 min. Use standing desk. Fidget tools for hands. Active note-taking.")
                else:
                    recs.append(f"**Kinesthetic Learning for {category}**: Use hands-on activities, physical models, role-playing, and movement-based learning.")
            
            elif "reading" in learning_lower or "writing" in learning_lower:
                if category == "memory":
                    recs.append("**Reading/Writing Memory**: Rewrite notes multiple times. Create detailed written summaries. Use Cornell note-taking method.")
                elif category == "focus":
                    recs.append("**Reading/Writing Focus**: Annotate heavily while reading. Take detailed written notes. Use bullet journaling for task management.")
                else:
                    recs.append(f"**Reading/Writing for {category}**: Use textbooks, written guides, detailed note-taking, and written self-explanations.")
        
        return recs
    
    def _generate_diagnosis(self, category, profile, base_diagnosis):
        """Generate personalized diagnosis based on inputs"""
        parts = [base_diagnosis] if base_diagnosis else []
        
        stress = profile.get("stress_level")
        sleep_hrs = profile.get("sleep_hours")
        study_hrs = profile.get("study_hours")
        
        # Critical patterns (highest priority)
        if "critical_sleep_crisis" in self.inferred_facts:
            parts.append(f"🚨 EMERGENCY: Severe sleep deprivation ({sleep_hrs}h) - immediate health risk.")
        elif "mental_health_crisis" in self.inferred_facts:
            parts.append(f"🚨 CRISIS: Extreme stress ({stress}/10) - urgent professional support needed.")
        elif "burnout_imminent" in self.inferred_facts:
            parts.append(f"🚨 CRITICAL: Burnout imminent with {study_hrs}h/day study - immediate reduction required.")
        
        # Sleep patterns
        elif "severe_sleep_debt" in self.inferred_facts:
            parts.append(f"Critical sleep deficit ({sleep_hrs}h) causing 40-60% performance loss.")
        elif "sleep_optimization_needed" in self.inferred_facts:
            parts.append(f"Suboptimal sleep ({sleep_hrs}h) reducing {category} performance by 20-30%.")
        elif "sleep_quality_good" in self.inferred_facts:
            parts.append(f"Optimal sleep ({sleep_hrs}h) supporting peak cognitive function.")
        elif sleep_hrs and sleep_hrs > 10:
            parts.append(f"Unusual sleep pattern ({sleep_hrs}h) - health check recommended.")
        
        # Stress patterns
        if "intervention_needed" in self.inferred_facts:
            parts.append(f"Elevated stress ({stress}/10) approaching burnout zone - active intervention needed.")
        elif "proactive_management_zone" in self.inferred_facts:
            parts.append(f"Low-moderate stress ({stress}/10) - good baseline with room for prevention.")
        elif "peak_performance_state" in self.inferred_facts:
            parts.append(f"Minimal stress ({stress}/10) - optimal state for peak {category}.")
        
        # Study hours patterns
        if "motivation_crisis" in self.inferred_facts:
            parts.append(f"Minimal study engagement ({study_hrs}h/day) - motivation/time management concern.")
        elif "efficiency_focus_needed" in self.inferred_facts:
            parts.append(f"Limited study time ({study_hrs}h/day) - efficiency optimization critical.")
        elif "sustainable_study_pattern" in self.inferred_facts:
            parts.append(f"Optimal study volume ({study_hrs}h/day) - focus on quality techniques.")
        elif "diminishing_returns" in self.inferred_facts:
            parts.append(f"Excessive study ({study_hrs}h/day) entering diminishing returns zone.")
        
        # Compound patterns
        if "critical_burnout_warning" in self.inferred_facts:
            parts.append("CRITICAL BURNOUT: High stress + excessive study + insufficient sleep.")
        elif "optimal_conditions_detected" in self.inferred_facts:
            parts.append("OPTIMAL STATE: Balanced stress, good sleep, and adequate study creating peak conditions.")
        
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
        """Calculate confidence adjustment based on data completeness and uncertainty"""
        adjustment = 0.0
        
        # More inputs = higher confidence
        input_count = sum(1 for v in profile.values() if v is not None)
        adjustment += input_count * 0.02  # +2% per input
        
        # Deduct for missing information
        for _, penalty in self.uncertainty_factors:
            adjustment -= penalty
        
        # Consistent patterns boost confidence
        if "optimal_learning_state" in self.inferred_facts:
            adjustment += 0.05
        
        # Warning conditions slightly reduce confidence (more uncertainty)
        if "burnout_risk" in self.inferred_facts:
            adjustment -= 0.03
        
        # Track confidence breakdown for transparency
        self.confidence_breakdown = {
            "base_inputs": input_count * 0.02,
            "missing_data_penalty": -sum(p for _, p in self.uncertainty_factors),
            "pattern_bonus": 0.05 if "optimal_learning_state" in self.inferred_facts else 0.0,
            "risk_penalty": -0.03 if "burnout_risk" in self.inferred_facts else 0.0
        }
        
        return adjustment
    
    def _generate_missing_info_suggestions(self):
        """Generate suggestions for what additional information would improve recommendations"""
        if not self.missing_info_warnings:
            return []
        
        suggestions = []
        missing_map = {
            "study_hours": "📚 **Study Hours**: Knowing your daily study time would help tailor time management strategies.",
            "stress_level": "😰 **Stress Level**: Your stress level would help identify mental health interventions needed.",
            "learning_style": "🎨 **Learning Style**: Knowing your preferred learning style would enable personalized study techniques.",
            "has_upcoming_exam": "📅 **Exam Timeline**: Whether you have an upcoming exam would adjust urgency of recommendations.",
            "sleep_hours": "😴 **Sleep Hours**: Your sleep duration would help assess cognitive readiness and recovery needs."
        }
        
        for missing in self.missing_info_warnings:
            if missing in missing_map:
                suggestions.append(missing_map[missing])
        
        return suggestions
    
    def _generate_uncertainty_explanation(self, confidence):
        """Generate human-readable explanation of uncertainty level"""
        if confidence >= 0.90:
            return "🟢 **High Confidence**: Comprehensive data provided. Recommendations are highly personalized and reliable."
        elif confidence >= 0.80:
            return "🟡 **Good Confidence**: Most key information provided. Recommendations are well-tailored but could be more precise with additional data."
        elif confidence >= 0.70:
            return "🟠 **Moderate Confidence**: Some key information missing. Recommendations are general and could be significantly improved with more data."
        else:
            return "🔴 **Low Confidence**: Limited information provided. Recommendations are based on category defaults. Please provide more details for personalized advice."
    
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
