# 🧪 Uncertainty Handling Testing Guide

## Overview
The Study Guide & Wellness tab now uses **input fields instead of sliders** to enable comprehensive testing of the expert system's uncertainty handling capabilities.

## Changes Made

### UI Changes
✅ **Replaced sliders with number input fields**
- Study hours: `st.number_input()` with `value=None` (can be left empty)
- Stress level: `st.number_input()` with `value=None` (can be left empty)
- Sleep hours: `st.number_input()` with `value=None` (can be left empty)

✅ **Replaced checkbox with tri-state radio**
- Exam status: "Not sure" / "Yes" / "No" options
- Allows explicit modeling of uncertainty

✅ **Added testing instructions**
- Prominent expander explaining how to test uncertainty
- Guidance on different scenarios to try

### Benefits
1. **Can leave fields completely empty** - Previous sliders always had a default value
2. **Tests missing data handling** - See how system behaves with 0-5 fields provided
3. **Validates uncertainty quantification** - Confidence scores adjust based on completeness
4. **Demonstrates graceful degradation** - System still provides useful advice with minimal data

## Test Scenarios

### Scenario 1: Minimal Data (Low Confidence ~70%)
**Inputs:**
- Category: Memory
- Learning Style: Not sure
- Study hours: (empty)
- Stress level: (empty)
- Sleep hours: (empty)
- Exam status: Not sure

**Expected Behavior:**
- Confidence: ~70%
- 5 missing info warnings
- General category-based recommendations
- Prominent suggestion to provide more data

### Scenario 2: Partial Data (Moderate Confidence ~80%)
**Inputs:**
- Category: Focus
- Learning Style: Visual
- Study hours: 4
- Stress level: (empty)
- Sleep hours: (empty)
- Exam status: No

**Expected Behavior:**
- Confidence: ~76-82%
- 2 missing info warnings (stress, sleep)
- Some personalized recommendations based on visual learning
- Suggestions to add stress and sleep data for better advice

### Scenario 3: Complete Data (High Confidence ~90-95%)
**Inputs:**
- Category: Memory
- Learning Style: Visual
- Study hours: 5
- Stress level: 3
- Sleep hours: 8
- Exam status: Yes

**Expected Behavior:**
- Confidence: ~90-95%
- 0 missing info warnings
- Highly personalized recommendations
- "Optimal learning state" detected
- Comprehensive category-specific advice

### Scenario 4: Critical Burnout (High Confidence + Warning)
**Inputs:**
- Category: Stress
- Learning Style: Any
- Study hours: 9
- Stress level: 9
- Sleep hours: 5
- Exam status: Yes

**Expected Behavior:**
- Confidence: ~85% (risk penalty -5%)
- "Critical burnout warning" inferred
- Emergency intervention recommendations
- Override all other advice with burnout protocol

### Scenario 5: Peak Performance (High Confidence + Bonus)
**Inputs:**
- Category: Memory
- Learning Style: Kinesthetic
- Study hours: 6
- Stress level: 2
- Sleep hours: 8
- Exam status: No

**Expected Behavior:**
- Confidence: ~93-95%
- "Optimal conditions detected" inferred
- Advanced optimization recommendations
- Encouragement to maximize current state

## What to Observe

### Confidence Score Display
- Watch how confidence changes as you add/remove fields
- Check the "Confidence Breakdown" expander for detailed calculation

### Missing Info Suggestions
- Should appear prominently when fields are empty
- Explains exactly what data would help
- Quantifies the impact of each missing field

### Recommendation Quality
- Minimal data: Generic category advice
- Partial data: Mix of generic and personalized
- Complete data: Highly specific, actionable strategies

### Uncertainty Explanation
- 🟢 Green for high confidence (90%+)
- 🟡 Yellow for good confidence (80-89%)
- 🟠 Orange for moderate confidence (70-79%)
- 🔴 Red for low confidence (<70%)

## Running Tests

1. Start the Streamlit app:
   ```powershell
   streamlit run main.py
   ```

2. Navigate to "Study Guide & Wellness" tab

3. Click "How to Test Uncertainty Handling" expander for guidance

4. Try different combinations of filled/empty fields

5. Observe:
   - Confidence score changes
   - Missing info warnings
   - Recommendation specificity
   - Inferred facts based on combinations

## Expected Output Examples

### With All Fields Empty
```
Data Completeness: 0% (0/5 fields)
Confidence: ~70%
Uncertainty: 🔴 Low Confidence - Limited information provided

Missing Info Suggestions:
• 📚 Study Hours
• 😰 Stress Level
• 🎨 Learning Style
• 📅 Exam Timeline
• 😴 Sleep Hours
```

### With All Fields Filled
```
Data Completeness: 100% (5/5 fields)
Confidence: ~93%
Uncertainty: 🟢 High Confidence - Comprehensive data provided

Inferred Facts:
• optimal_conditions_detected
• visual_learning_recommended
• room_for_optimization
```

## Technical Details

### Confidence Calculation
```python
base_confidence = 0.85  # From knowledge base
+ (provided_inputs × 0.02)  # +2% per field
- sum(uncertainty_penalties)  # Specific to each field
+ pattern_bonuses  # +5% for optimal state
- risk_penalties  # -3% for burnout, -5% for critical
= final_confidence (clamped 0.60 - 0.99)
```

### Uncertainty Penalties
- Missing stress_level: -10%
- Missing study_hours: -8%
- Missing sleep_hours: -7%
- Missing learning_style: -6%
- Missing has_upcoming_exam: -4%

---

**Test thoroughly to validate the expert system's uncertainty handling capabilities!** 🎯
