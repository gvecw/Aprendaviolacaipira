import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Negative margin on headline to bring mockup up
html = re.sub(
    r'\.headline \{([\s\S]*?)margin-bottom: 0\.2rem;',
    r'.headline {\1margin-bottom: -5px;',
    html
)
html = re.sub(
    r'\.headline \{ margin-bottom: 0\.2rem; \}',
    r'.headline { margin-bottom: -8px; }',
    html
)

# 2. Increase mockup size up to 75% baseline and 70% mobile
html = re.sub(
    r'\.mockup-wrapper \{([\s\S]*?)width: 70%;([\s\S]*?)max-width: 420px;',
    r'.mockup-wrapper {\1width: 75%;\2max-width: 480px;',
    html
)
html = re.sub(
    r'\.mockup-wrapper \{ width: 60%; margin-bottom: 0\.25rem; \}',
    r'.mockup-wrapper { width: 70%; margin-bottom: -5px; }',
    html
)

# 3. Increase rotation to 2.5deg
html = re.sub(
    r'transform: rotate\(1\.5deg\);',
    r'transform: rotate(2.5deg);',
    html
)

# 4. Reforce the floor shadow again (more blur, wider spread)
html = re.sub(
    r'\.mockup-floor-shadow \{([\s\S]*?)filter: blur\(16px\);',
    r'.mockup-floor-shadow {\1filter: blur(22px);',
    html
)

# 5. Fix keyframes to match rotation properly (if I didn't change rotation in keyframes it will look weird)
# Wait, my keyframes levitate ONLY do translateY, except the first one I did had rotate. Let's check!
# The current keyframes in my code:
# @keyframes levitate {
#     0%, 100% { transform: translateY(0); }
#     50% { transform: translateY(-12px); }
# }
# Since rotation is on the img tag, the wrapper translates. That separates concerns! No need to change keyframes.

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Done")
