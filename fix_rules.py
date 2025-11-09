import re

with open('experts/study_guide_expert.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove Fact(action='provide_study_guidance'), from all @Rule definitions
content = re.sub(
    r"    @Rule\(\n        Fact\(action='provide_study_guidance'\),\n        Fact\(user_query=",
    "    @Rule(\n        Fact(user_query=",
    content
)

with open('experts/study_guide_expert.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed all rules!")
