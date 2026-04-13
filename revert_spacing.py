import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Reverter paddings para algo intermediário, não tão colado
html = html.replace('py-10 md:py-14', 'py-14 md:py-16')
html = html.replace('py-8 md:py-10', 'py-10 md:py-12')
html = html.replace('mb-6 md:mb-8', 'mb-8 md:mb-10')
html = html.replace('padding: 40px 16px;', 'padding: 56px 16px;')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Rollback parcial feito")
