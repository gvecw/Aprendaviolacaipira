import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Broad Section Paddings Resizing
html = html.replace('py-20', 'py-10 md:py-16')
html = html.replace('py-16 md:py-20', 'py-8 md:py-16')
html = html.replace('py-16', 'py-8 md:py-14')

# 2. Broad Margin Resizing (mainly for mobile, keeping some for desktop)
# Since they might be coupled (e.g. mb-12 md:mb-14, let's be careful)
# We can do regex for mb-\d+ and replace, but precise replacements are safer.

html = html.replace('mb-14', 'mb-8 md:mb-12')
html = html.replace('mb-12 md:mb-12', 'mb-6 md:mb-10')
html = html.replace('mb-12', 'mb-6 md:mb-10')
html = html.replace('mb-10 md:mb-12', 'mb-6 md:mb-10')
html = html.replace('mb-10', 'mb-6 md:mb-8')
html = html.replace('mb-8 md:mb-12', 'mb-5 md:mb-10')
html = html.replace('mt-12 mb-8', 'mt-6 mb-5 md:mt-10 md:mb-8')

# 3. Specifi modifications for "O que você vai aprender na prática"
# Title mb-4 to mb-2
html = re.sub(
    r'<h2 class="([^"]*)mb-4([^"]*)">([^<]*)O que você vai[^<]*<span[^>]*>aprender na prática</span></h2>',
    r'<h2 class="\1mb-1\2">\3O que você vai <span class="text-amber-500">aprender na prática</span></h2>',
    html, flags=re.IGNORECASE | re.DOTALL
)

# Text max-w-2xl
html = re.sub(
    r'<p class="text-gray-300 text-base md:text-lg max-w-2xl mx-auto">Mesmo começando do zero, você vai aprender passo a passo como tocar viola de forma simples e prática.</p>',
    r'<p class="text-gray-300 text-[15px] md:text-lg max-w-2xl mx-auto mt-2">Mesmo começando do zero, você vai aprender passo a passo como tocar viola de forma simples e prática.</p>',
    html
)

# Inner list margin
html = html.replace(
    '<ul class="space-y-4">',
    '<ul class="space-y-2 md:space-y-4">'
)

# Button in "Amostra" section was mt-12 mb-8 changed to mt-6 mb-5 previously.
# But let's check the new layout of "Aprender na prática" spacing.
html = html.replace(
    '<div class="mt-8 pt-5 border-t border-amber-900/30 text-center">',
    '<div class="mt-5 pt-4 border-t border-amber-900/30 text-center">'
)

# Any other huge gaps
html = html.replace('gap-8', 'gap-5 md:gap-8')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Done")
