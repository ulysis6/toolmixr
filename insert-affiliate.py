"""
Batch insert AffiliateBanner into all toolmixr tool pages.
Inserts component just before the guide section.
"""
import os, re

pages_dir = "D:\\Project\\toolmixr\\src\\pages"
import_stmt = "import AffiliateBanner from '../components/AffiliateBanner.astro';"
component_block = '<AffiliateBanner />'
count = 0

for fname in sorted(os.listdir(pages_dir)):
    if not fname.endswith('.astro') or fname == 'index.astro':
        continue
    fpath = os.path.join(pages_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Only process pages with guide section
    if '<section class="guide"' not in content:
        continue
    
    # Skip if already has the component
    if component_block in content:
        continue
    
    changed = False
    
    # Add import
    if import_stmt not in content:
        fm_close = content.find('\n---\n', content.find('---\n') + 4)
        if fm_close > 0:
            insert_pos = content.rfind('\n', 0, fm_close) + 1
            content = content[:insert_pos] + '\n' + import_stmt + content[insert_pos:]
            changed = True
    
    # Find the guide section and insert before it
    guide_start = content.find('<section class="guide"')
    if guide_start < 0:
        continue
    
    # Find the preceding newline
    newline_before = content.rfind('\n', 0, guide_start)
    if newline_before < 0:
        continue
    
    # Get the indentation of the guide line
    indent = ''
    i = newline_before + 1
    while i < guide_start and content[i] in ' \t':
        indent += content[i]
        i += 1
    
    insert_text = '\n' + indent + component_block + '\n' + indent
    content = content[:newline_before] + insert_text + content[newline_before:]
    changed = True
    
    if changed:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"  UPDATED: {fname}")

print(f"\nDone: {count} tool pages updated")
