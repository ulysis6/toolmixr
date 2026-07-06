import os, re

blog_dir = "D:\\Project\\toolmixr\\src\\pages\\blog"

fixes = 0

for fname in sorted(os.listdir(blog_dir)):
    if not fname.endswith(".astro") or fname == "index.astro":
        continue
    
    fpath = os.path.join(blog_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    changed = False
    
    # Case 1: Replace "✍️ By Lu Shen" with proper link
    old_author = '✍️ By Lu Shen'
    new_author = 'By <a href="https://lusdaily.com" target="_blank" rel="noopener" class="author-link">Lao Lu</a> · <a href="https://lusdaily.com" target="_blank" rel="noopener">lusdaily.com</a>'
    
    if old_author in content:
        content = content.replace(old_author, new_author)
        changed = True
        print(f"REPLACED: {fname}")
    
    # Case 2: Has blog-meta but no author at all (the 2 missing ones)
    if 'blog-meta' in content and old_author not in content and 'Lao Lu' not in content and 'author-link' not in content:
        # Find the line right after the last <span> in blog-meta (read time line)
        # Simple approach: replace the closing </div> of blog-meta
        meta_end = '</span>\n    </div>'
        new_meta_end = '</span>\n      <span>By <a href="https://lusdaily.com" target="_blank" rel="noopener" class="author-link">Lao Lu</a> · <a href="https://lusdaily.com" target="_blank" rel="noopener">lusdaily.com</a></span>\n    </div>'
        if meta_end in content:
            content = content.replace(meta_end, new_meta_end)
            changed = True
            print(f"ADDED author: {fname}")
    
    if changed:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        fixes += 1

print(f"\nDone: {fixes} files updated")
