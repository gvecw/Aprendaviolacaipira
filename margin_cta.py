import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add margin-top to the CTA button CSS rule
# We search for .cta-button { ... } 
# Let's insert margin-top: 2rem; (32px for baseline) and inside the media query reduce it to 1.5rem (24px for mobile).
html = re.sub(
    r'\.cta-button \{([\s\S]*?)width: 100%;',
    r'.cta-button {\1margin-top: 2rem; width: 100%;',
    html
)

html = re.sub(
    r'\.cta-button \{([\s\S]*?)margin-bottom: 0\.5rem;',
    r'.cta-button {\1margin-top: 1.5rem; margin-bottom: 0.5rem;',
    html
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Done")
