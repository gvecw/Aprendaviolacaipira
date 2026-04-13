import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace padding on sections
html = re.sub(r'<section(.*?)py-20(.*?)>', r'<section\1py-10 md:py-14\2>', html)
html = re.sub(r'<section(.*?)py-16(.*?)>', r'<section\1py-10 md:py-14\2>', html)
html = re.sub(r'<section(.*?)py-12(.*?)>', r'<section\1py-8 md:py-10\2>', html)
html = html.replace('padding: 64px 16px;', 'padding: 40px 16px;')

# Reduce margin bottoms for block titles (which are usually "text-center mb-10")
html = html.replace('mb-10', 'mb-6 md:mb-8')

# Let's also look for margin-bottom 40px inline style or similar
html = html.replace('margin-bottom: 40px;', 'margin-bottom: 24px;')
html = html.replace('padding: 40px;', 'padding: 24px md:padding:32px;')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Spacings reduced!")
