"""
Insert AffiliateBanner into all toolmixr blog posts after the first H2 paragraph.
"""
import os

blog_dir = "D:\\Project\\toolmixr\\src\\pages\\blog"
import_stmt = "import AffiliateBanner from '../../components/AffiliateBanner.astro';"
component_tag = '<AffiliateBanner variant="compact" />'

count = 0
for fname in sorted(os.listdir(blog_dir)):
    if not fname.endswith('.astro') or fname == 'index.astro':
        continue
    fpath = os.path.join(blog_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if component_tag in content:
        continue
    
    changed = False
    
    # Add import
    if import_stmt not in content:
        fm_close = content.find('\n---\n', content.find('---\n') + 4)
        if fm_close > 0:
            insert_pos = content.rfind('\n', 0, fm_close) + 1
            content = content[:insert_pos] + '\n' + import_stmt + content[insert_pos:]
            changed = True
    
    # Find first </h2> and insert after its following paragraph
    first_h2 = content.find('</h2>')
    if first_h2 > 0:
        after_h2 = content[first_h2:]
        next_p_end = after_h2.find('</p>')
        if next_p_end > 0:
            insert_at = first_h2 + next_p_end + 4
            content = content[:insert_at] + '\n\n  ' + component_tag + '\n\n' + content[insert_at:]
            changed = True
    
    if changed:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"  UPDATED: {fname}")

print(f"\nDone: {count} blog posts updated")
