"""
Update Expert Systems to collect all matching rules
"""

import re

def update_expert_file(filepath):
    """Update expert system to use add_response instead of self.response."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # First, revert any previous changes
    content = content.replace('self.add_response({', 'self.response = {')
    content = content.replace('        # Allow multiple rules to fire', '        self.halt()')
    content = content.replace('    # Allow multiple rules to fire', '    self.halt()')
    
    # Now apply correct changes
    # Pattern to match entire rule methods
    # Find: self.response = { ... }
    # Replace: self.add_response({ ... })
    
    pattern = r'(self\.response\s*=\s*\{)'
    replacement = r'self.add_response({'
    
    # Count occurrences
    count = len(re.findall(pattern, content))
    
    # Do replacement
    updated_content = re.sub(pattern, replacement, content)
    
    # Remove self.halt() calls to allow multiple rules to fire
    updated_content = updated_content.replace('self.halt()', '# Multiple rules can fire')
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"✅ Updated {filepath}")
    print(f"   Changed {count} self.response assignments")
    
    return count

# Update all expert files
experts = [
    'experts/biology_expert.py',
    'experts/physics_expert.py',
    'experts/chemistry_expert.py'
]

total = 0
for expert in experts:
    count = update_expert_file(expert)
    total += count

print(f"\n✅ Total: Updated {total} rule methods across {len(experts)} experts")
print("   All experts now collect multiple matching rules!")

