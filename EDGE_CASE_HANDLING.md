# Edge Case Handling - Expert System Improvements

## Overview
Enhanced the expert system to detect and handle unusual input patterns that may indicate health concerns or data entry errors.

## New Rule Added: Rule 17 - Excessive Sleep Detection

### Purpose
Detect when users report sleeping more than 10 hours per night, which is outside the normal healthy range (7-9 hours for adults).

### Implementation

**Location**: `experts/study_guide_expert.py` - Lines 336-344

```python
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
```

### Recommendation Logic

**Location**: `experts/study_guide_expert.py` - `_generate_adaptive_recommendations()` method

When excessive sleep (>10 hours) is detected, the system now provides:

1. **Warning Message**: Flags the unusual sleep pattern
2. **Possible Causes**:
   - Depression or mood disorders
   - Sleep quality issues (frequent waking, non-restorative sleep)
   - Medical conditions (thyroid issues, sleep apnea)
   - Data entry error

3. **Recommended Actions**:
   - Consult university health services or doctor
   - Track actual sleep time vs. time in bed
   - Re-enter data if error

4. **Educational Note**: Quality of sleep matters more than quantity

### Example Output

**Input**: 
- Sleep hours: 12
- Category: Stress Management
- Stress level: 6

**System Response**:
```
⚠️ **UNUSUAL SLEEP PATTERN** - You reported 12h/night, which exceeds 
the recommended 7-9 hours for adults.

**Health Check Needed**: Excessive sleep (>10h) can indicate: 
1) Depression or mood disorders, 2) Sleep quality issues (waking frequently), 
3) Medical conditions (thyroid, sleep apnea), or 4) Data entry error.

**Recommended Actions**: If this is accurate, consult university health 
services or your doctor. Quality of sleep matters more than quantity. 
Track your actual sleep vs. time in bed.

**If Data Error**: Please re-enter with actual sleep hours. Normal 
healthy range is 7-9 hours per night.
```

## Edge Cases Now Handled

### 1. ✅ Excessive Sleep (>10 hours)
- **Detection**: Rule 17 fires when sleep_hours > 10
- **Action**: Warning + health recommendations + data validation prompt
- **Salience**: 22 (high priority, fires before most other rules)

### 2. ✅ Critical Sleep Deprivation (<6 hours)
- **Detection**: Existing logic in recommendations
- **Action**: Emergency sleep recovery protocol
- **Message**: "CRITICAL: Sleep Deprivation" with immediate interventions

### 3. ✅ Suboptimal Sleep (6-7 hours)
- **Detection**: Existing logic
- **Action**: Optimization suggestions
- **Message**: Gentle recommendation to increase to 7-8 hours

### 4. ✅ Critical Burnout (high stress + high study + low sleep)
- **Detection**: Rule 12 - All three factors present
- **Action**: Immediate stop-and-rest protocol
- **Salience**: 25 (highest priority)

### 5. ✅ Exam Crisis (exam soon + low study hours)
- **Detection**: Rule 14 - upcoming_exam=True + study_hours < 3
- **Action**: Emergency triage strategies
- **Salience**: 20 (high priority)

### 6. ✅ Overpreparation (no exam + excessive study)
- **Detection**: Rule 15 - upcoming_exam=False + study_hours >= 9
- **Action**: Work-life balance recommendations
- **Salience**: 10 (moderate priority)

## Confidence Score Impact

### Excessive Sleep Pattern
- **Uncertainty Factor**: +0.05 penalty
- **Reason**: Unusual data suggests either health issue or data error, reducing confidence in normal recommendations
- **Logged**: Added to `uncertainty_factors` list for transparency

### In Reasoning Trace
Users can see in the "View Reasoning Process" section:
```
⚠️ Rule Fired: Excessive sleep (12h) → Possible health concern or 
data entry error. Normal range: 7-9h
```

## System Behavior Testing

### Test Scenario 1: Normal Sleep (7-8 hours)
- **Input**: sleep_hours = 7
- **Output**: No sleep warnings, normal recommendations
- **Confidence**: No penalty

### Test Scenario 2: Low Sleep (5 hours)
- **Input**: sleep_hours = 5
- **Output**: "CRITICAL: Sleep Deprivation" + recovery protocol
- **Confidence**: No penalty (expected behavior)

### Test Scenario 3: Excessive Sleep (12 hours)
- **Input**: sleep_hours = 12
- **Output**: "UNUSUAL SLEEP PATTERN" warning + health recommendations
- **Confidence**: -5% penalty for unusual pattern
- **Reasoning**: Shows "Rule 17 fired" in trace

### Test Scenario 4: Combined Edge Case (12h sleep + high stress)
- **Input**: sleep_hours = 12, stress_level = 8
- **Output**: 
  1. High stress interventions (breathing, grounding)
  2. Excessive sleep warning (health check needed)
  3. Combined advice addressing both concerns
- **Confidence**: Multiple factors tracked

## Medical Disclaimer

The system provides **educational guidance only** and is not a substitute for medical advice. For persistent sleep issues, depression, or other health concerns, users are directed to:

1. University health services
2. University counseling center  
3. Personal physician
4. Crisis resources (988 hotline, Crisis Text Line)

## Future Enhancements (Potential)

### Additional Edge Cases to Consider:
1. **Zero Study Hours** - Student reporting no studying despite upcoming exam
2. **Extreme Stress (10/10)** - May need crisis intervention resources
3. **Invalid Combinations** - e.g., 12h sleep + 12h study = 24h/day (impossible)
4. **Repeated Pattern** - User consistently reports extreme values across sessions
5. **Age-Based Sleep Norms** - Different recommendations for different age groups

### Validation Rules:
- Sum of sleep + study + other activities should be reasonable (<24h)
- Detect impossible patterns (all metrics at extremes)
- Track historical patterns if multi-session use

## Benefits of This Enhancement

✅ **Safety**: Identifies potential health concerns early
✅ **Accuracy**: Catches data entry errors before generating wrong recommendations
✅ **Transparency**: Explains why unusual patterns are flagged
✅ **Actionable**: Provides specific next steps (see doctor, re-enter data)
✅ **Educational**: Teaches users about healthy sleep ranges
✅ **Confidence Tracking**: Adjusts confidence score appropriately for unusual data

## Files Modified

1. **experts/study_guide_expert.py**
   - Added Rule 17: `infer_excessive_sleep()` method
   - Enhanced `_generate_adaptive_recommendations()` with excessive sleep handling
   - Total rules: 17 (up from 16)

## Testing Verification

Run the system and test:
```powershell
streamlit run .\main.py
```

**Test inputs**:
- Category: Any (e.g., "Stress Management")
- Sleep hours: 12
- Other fields: Optional

**Expected**: See warning about excessive sleep in recommendations section.

---

**Status**: ✅ Implemented and tested
**Rule Count**: 17 total inference rules
**Priority**: High (salience=22, fires early in rule execution)
