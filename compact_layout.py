import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Top spacing compression
# The body padding for the banner:
html = html.replace('body { padding-top: 40px; }', 'body { padding-top: 36px; }')

# The hero-container paddings:
html = re.sub(
    r'\.hero-container \{([\s\S]*?)padding-top: 1rem;',
    r'.hero-container {\1padding-top: 0.25rem;',
    html
)
html = re.sub(
    r'\.hero-container \{([\s\S]*?)padding-top: 6rem;',
    r'.hero-container {\1padding-top: 1.5rem;',
    html
)

# Overall Gap Compaction

# Headline bottom margin
html = re.sub(
    r'\.headline \{([\s\S]*?)margin-bottom: 0\.75rem;',
    r'.headline {\1margin-bottom: 0.5rem;',
    html
)

# Mockup width and bottom margin
html = re.sub(
    r'\.mockup-wrapper \{([\s\S]*?)margin: 0 auto 1\.5rem auto;',
    r'.mockup-wrapper {\1margin: 0 auto 0.75rem auto;',
    html
)

# CTA block gap compaction (Liberação & CTA)
html = re.sub(
    r'margin-bottom:1\.5rem;">\s*<p style="font-size:13px; color:#22c55e;',
    r'margin-bottom:0.75rem;">\n            <p style="font-size:13px; color:#22c55e;',
    html
)

# Sub headline margin
html = re.sub(
    r'\.sub-headline \{([\s\S]*?)margin-bottom: 1\.5rem;',
    r'.sub-headline {\1margin-bottom: 0.75rem;',
    html
)

# Benefits list bottom margin
html = re.sub(
    r'\.benefits-list \{([\s\S]*?)margin-bottom: 1\.5rem;',
    r'.benefits-list {\1margin-bottom: 0.5rem;',
    html
)

# Media Queries adjustments for even smaller screens
html = re.sub(
    r'@media \(max-height: 750px\) \{([\s\S]*?)\.mockup-wrapper \{ width: 45%; margin-bottom: 0\.25rem; \}([\s\S]*?)margin-bottom: 1\.5rem;',
    r'@media (max-height: 750px) {\1.mockup-wrapper { width: 45%; margin-bottom: 0.25rem; }\2margin-bottom: 0.5rem;',
    html
)

# General section padding reduction
html = html.replace('py-8 md:py-12 px-4', 'py-4 md:py-8 px-4')
html = html.replace('py-12 md:py-16 px-4', 'py-4 md:py-8 px-4') # If any other exists

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Done")
