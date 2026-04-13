import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Modify CTA margins and remove animations
# We want to change the .cta-button css property
html = re.sub(
    r'\.cta-button \{([\s\S]*?)margin-top: 2rem;',
    r'.cta-button {\1margin-top: 1rem;',
    html
)
html = re.sub(
    r'\.cta-button \{([\s\S]*?)margin-top: 1\.5rem;',
    r'.cta-button {\1margin-top: 1rem;',
    html
)

# Remove the active scale entirely
html = re.sub(
    r'\.cta-button:active \{([\s\S]*?)transform: scale\(0\.97\);\s*\}',
    r'',
    html
)
html = re.sub(
    r'\.cta-button:active \{([\s\S]*?)\}',
    r'',
    html
)

# Further shrink benefits bottom margin to 0
html = re.sub(
    r'\.benefits-list \{([\s\S]*?)margin-bottom: 0\.5rem;',
    r'.benefits-list {\1margin-bottom: 0;',
    html
)

html = re.sub(
    r'\.benefits-list \{([\s\S]*?)margin-bottom: 0\.75rem;',
    r'.benefits-list {\1margin-bottom: 0;',
    html
)

html = re.sub(
    r'\.benefits-list \{([\s\S]*?)margin-bottom: 1rem;',
    r'.benefits-list {\1margin-bottom: 0;',
    html
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("done")
