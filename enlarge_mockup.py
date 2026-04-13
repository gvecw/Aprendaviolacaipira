import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Headline margin (bring mockup closer)
html = re.sub(
    r'\.headline \{([\s\S]*?)margin-bottom: 0\.5rem;',
    r'.headline {\1margin-bottom: 0.2rem;',
    html
)
html = re.sub(
    r'@media \(max-height: 750px\) \{([\s\S]*?)\.headline \{ margin-bottom: 0\.75rem; \}',
    r'@media (max-height: 750px) {\1.headline { margin-bottom: 0.2rem; }',
    html
)

# 2. Mockup overall size and max-width
html = re.sub(
    r'\.mockup-wrapper \{([\s\S]*?)width: 50%;([\s\S]*?)max-width: 320px;',
    r'.mockup-wrapper {\1width: 70%;\2max-width: 420px;',
    html
)
html = re.sub(
    r'\.mockup-wrapper \{ width: 45%; margin-bottom: 0\.25rem; \}',
    r'.mockup-wrapper { width: 60%; margin-bottom: 0.25rem; }',
    html
)

# 3. Reforce shadow on the image
html = re.sub(
    r'\.mockup-img \{([\s\S]*?)filter: drop-shadow\(0 25px 25px rgba\(0,0,0,0\.35\)\);',
    r'.mockup-img {\1filter: drop-shadow(0 35px 35px rgba(0,0,0,0.25));',
    html
)

# 4. Reforce floor shadow
html = re.sub(
    r'\.mockup-floor-shadow \{([\s\S]*?)width: 80%;([\s\S]*?)height: 15px;([\s\S]*?)background: rgba\(0,0,0,0\.5\);([\s\S]*?)filter: blur\(12px\);',
    r'.mockup-floor-shadow {\1width: 85%;\2height: 18px;\3background: rgba(0,0,0,0.6);\4filter: blur(16px);',
    html
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Done")
