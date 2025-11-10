# Bug Fix: KeyError 'study_guide_expert'

## Problem
When using the Subject Tutor tab, the application crashed with:
```
KeyError: 'study_guide_expert'
File "agents/expert_agent.py", line 623, in process_query
    expert = self.tools['study_guide_expert']
```

## Root Cause
The Study Guide expert was moved to a separate tab in the UI, removing it from the `agent.tools` dictionary in the Subject Tutor tab. However, the code in `expert_agent.py` still had special handling logic that tried to access this removed tool.

## Changes Made

### 1. Removed Special Handling Block (lines 621-667)
**Before:**
```python
if analysis['tool_name'] == 'study_guide_expert':
    print("🔧 Step 2: Activating Study Guide (Diagnostic Mode)...")
    expert = self.tools['study_guide_expert']  # KeyError!
    
    # 44 more lines of special handling...
    # Returns different response structures based on state
```

**After:**
```python
# NOTE: Study Guide is now in a separate tab and not handled by this agent
# Only Biology, Physics, and Chemistry experts are available here

# Step 2: Execute expert system tool for EACH topic
```

### 2. Updated Tool Descriptions (line 166)
**Before:**
```python
4. **study_guide_expert**: Use for study guidance and diagnostic questions
   - Topics: Study weaknesses, MCQ strategies, essay writing, exam preparation
   - Returns: Personalized diagnosis through progressive questioning
   - Usage: Progressive questioning system - responds to student's study problems
```

**After:**
```python
NOTE: Study Guide expert is now handled in a separate tab and not available through this agent.
```

### 3. Simplified `_execute_tool()` Function (line 316)
**Before:**
```python
# Handle different expert types
if tool_name == 'study_guide_expert':
    # Study guide uses diagnostic questioning
    expert.run()
    
    if expert.requires_clarification():
        return {...}
    elif expert.is_diagnosis_complete():
        return {...}
else:
    # Information experts use query_topic
    from experta import Fact
    expert.declare(Fact(query_topic=query_topic))
    expert.run()
```

**After:**
```python
# Information experts (Biology, Physics, Chemistry) use query_topic
from experta import Fact
expert.declare(Fact(query_topic=query_topic))
expert.run()
```

## Impact
- ✅ **Subject Tutor now works** without KeyError
- ✅ **Code is cleaner** - removed ~70 lines of unused special handling
- ✅ **Clear separation** - Study Guide and Subject Tutor are now properly separated
- ✅ **No functionality lost** - Study Guide still works in its own tab

## Files Modified
- `agents/expert_agent.py`: Removed study_guide_expert references and special handling

## Testing
To verify the fix works:
1. Start the Streamlit app: `.\.venv\Scripts\streamlit run main.py`
2. Go to "Subject Tutor" tab
3. Ask a biology/physics/chemistry question (e.g., "What are animal tissues?")
4. Should receive a response without any KeyError

## Status
✅ **FIXED** - Application should now start and run without errors
