import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# I will extract the blocks to move them.
# The block to be moved consists of:
# 1. The trust text (Liberação imediata)
# 2. The CTA button
# 3. The microcopy "Toque para ver..."

# Let's cleanly grab everything from the trust text to the end of the microcopy.
move_start_str = r'<p style="font-size:13px; color:#22c55e;'
move_end_str = r'⬇️ Toque para ver como funciona ⬇️\s*</p>'

match = re.search(f'({move_start_str}[\\s\\S]*?{move_end_str})', html)
if match:
    cta_block = match.group(1)
    # Remove it from its original spot
    html = html.replace(cta_block, '')
    
    # Now we want to insert it right after the mockup ends, but before the sub-headline.
    # The mockup wrapper ends with </div> and then <p class="sub-headline">
    
    insertion_point = r'(</div>\s*<p class="sub-headline">)'
    html = re.sub(insertion_point, cta_block + r'\n        \1', html)

# Modify button slightly for "garantir que apareça completamente na primeira dobra"
# The button already has huge padding (20px 40px), let's reduce padding on mobile to make it fit better if needed,
# but the user said "aumentar levemente tamanho, aumentar padding interno". It's already big, let's keep it big but ensure margins above and below are small.

html = re.sub(
    r'\.cta-button \{([\s\S]*?)padding: 16px 32px;',
    r'.cta-button {\1padding: 14px 28px; margin-bottom: 0.5rem;',
    html
)

html = re.sub(
    r'\.cta-button \{([\s\S]*?)padding: 20px 40px;',
    r'.cta-button {\1padding: 22px 36px; margin-bottom: 0.75rem;',
    html
)

# Shrink the mockup slightly on mobile to make SURE the button is above the fold
html = re.sub(
    r'\.mockup-wrapper \{ width: 50%; margin-bottom: 1rem; \}',
    r'.mockup-wrapper { width: 45%; margin-bottom: 0.25rem; }',
    html
)

# Shrink top padding of hero to save space for CTA
html = re.sub(
    r'\.hero-container \{([\s\S]*?)padding-top: 1\.5rem;',
    r'.hero-container {\1padding-top: 1rem;',
    html
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("done")
