import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Fix the Vantagens Section Opening tag padding
html = re.sub(
    r'<section class="relative py-10 md:py-8 md:py-14 px-4 overflow-hidden">',
    r'<section class="relative pt-10 pb-16 md:pt-16 md:pb-20 px-4 overflow-hidden">',
    html
)

# 2. Fix the Vantagens Title Margin
html = re.sub(
    r'<div class="text-center mb-8 md:mb-6 md:mb-6 md:mb-8">',
    r'<div class="text-center mb-10 md:mb-14">',
    html
)

# 3. Fix the Amostras section Opening pad
html = re.sub(
    r'<section id="amostras-section" class="relative py-8 md:py-14 px-4 overflow-hidden">',
    r'<section id="amostras-section" class="relative pt-16 pb-8 md:pt-20 md:pb-14 px-4 overflow-hidden">',
    html
)

# 4. Fix Amostras section Title margin
html = re.sub(
    r'<div class="text-center mb-6 md:mb-8 md:mb-6 md:mb-6 md:mb-8">',
    r'<div class="text-center mb-10 md:mb-14">',
    html
)

# 5. Fix remaining corrupted class stacks globally
html = re.sub(r'mb-6 md:mb-8 md:mb-6 md:mb-6 md:mb-8', r'mb-10 md:mb-14', html)
html = re.sub(r'mb-6 md:mb-8 md:mb-8 md:mb-6 md:mb-6 md:mb-8', r'mb-10 lg:mb-12', html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Done")
