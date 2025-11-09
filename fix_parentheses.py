"""
Fix the closing parenthesis issue in expert systems
"""

import re

def fix_expert_file(filepath):
    """Fix add_response calls to have proper closing parentheses."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern: self.add_response({...}\n with no closing )
    # We need to add ) before the newline
    
    # Find patterns like: }  \n        # Multiple rules can fire
    # Replace with: })  \n        # Multiple rules can fire
    
    pattern = r'(\s+\'examples\':.*?\])\s*\n\s*\}\s*\n\s*# Multiple rules can fire'
    
    def add_closing_paren(match):
        return match.group(0).replace('}\n        # Multiple rules can fire', '})\n        # Multiple rules can fire')
    
    updated_content = re.sub(pattern, add_closing_paren, content, flags=re.DOTALL)
    
    # Simpler approach: replace }  \n        # Multiple with })  \n        # Multiple
    updated_content = updated_content.replace('        }\n        # Multiple rules can fire', '        })\n        # Multiple rules can fire')
    updated_content = updated_content.replace('    }\n    # Multiple rules can fire', '    })\n    # Multiple rules can fire')
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"✅ Fixed {filepath}")

# Fix all expert files
experts = [
    'experts/biology_expert.py',
    'experts/physics_expert.py',
    'experts/chemistry_expert.py'
]

for expert in experts:
    fix_expert_file(expert)

print(f"\n✅ All expert files fixed with proper closing parentheses!")
