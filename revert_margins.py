import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Reverse tweak_margins.py first
html = html.replace('<section class="relative pt-10 pb-16 md:pt-16 md:pb-20 px-4 overflow-hidden">', '<section class="relative py-20 px-4 overflow-hidden">')
html = html.replace('<div class="text-center mb-10 md:mb-14">', '<div class="text-center mb-14">')
html = html.replace('<section id="amostras-section" class="relative pt-16 pb-8 md:pt-20 md:pb-14 px-4 overflow-hidden">', '<section id="amostras-section" class="relative py-16 px-4 overflow-hidden">')
html = html.replace('mb-10 lg:mb-12', 'mb-12')

# 2. Reverse compact_spacing.py padding replacements
# Note: we need to do this carefully so we don't double replace.
html = html.replace('py-8 md:py-16', 'py-16 md:py-20')
html = html.replace('py-10 md:py-16', 'py-20')
# We need to replace standalone instances of py-8 md:py-14 back to py-16.
html = html.replace('py-8 md:py-14', 'py-16')

# Reverse margins
html = html.replace('mb-8 md:mb-12', 'mb-14')
html = html.replace('mb-6 md:mb-10', 'mb-12')
html = html.replace('mb-6 md:mb-8', 'mb-10')
html = html.replace('mb-5 md:mb-10', 'mb-8 md:mb-12')
html = html.replace('mt-6 mb-5 md:mt-10 md:mb-8', 'mt-12 mb-8')

# 3. Specific modifications for "O que você vai aprender na prática"
html = re.sub(
    r'<h2 class="([^"]*)mb-1([^"]*)">([^<]*)O que você vai <span class="text-amber-500">aprender na prática</span></h2>',
    r'<h2 class="\1mb-4\2">\3O que você vai <span class="text-amber-500">aprender na prática</span></h2>',
    html, flags=re.IGNORECASE | re.DOTALL
)

html = html.replace(
    '<p class="text-gray-300 text-[15px] md:text-lg max-w-2xl mx-auto mt-2">Mesmo começando do zero, você vai aprender passo a passo como tocar viola de forma simples e prática.</p>',
    '<p class="text-gray-300 text-base md:text-lg max-w-2xl mx-auto">Mesmo começando do zero, você vai aprender passo a passo como tocar viola de forma simples e prática.</p>'
)

# Inner list margin
html = html.replace('<ul class="space-y-2 md:space-y-4">', '<ul class="space-y-4">')

# Button area in "O que... aprender..."
html = html.replace(
    '<div class="mt-5 pt-4 border-t border-amber-900/30 text-center">',
    '<div class="mt-8 pt-5 border-t border-amber-900/30 text-center">'
)

# Any other huge gaps
html = html.replace('gap-5 md:gap-8', 'gap-8')
html = html.replace('gap-5', 'gap-8')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Done")
