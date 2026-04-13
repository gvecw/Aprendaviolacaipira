import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Exact original replacements mapping
html = html.replace('class="relative py-14 md:py-16 px-4 overflow-hidden"', 'class="relative py-20 px-4 overflow-hidden"') # Only the first one should be py-20, but the previous script messed that targeting. Let's fix. Wait, there was also amostras-section.

# First let's blindly revert all py-14 md:py-16 to py-16
html = html.replace('py-14 md:py-16', 'py-16')
# Then fix the specific hero section that was py-20
# It's right before "<section class="relative py-16 px-4 overflow-hidden" " wait... the hero section is `<section class="relative min-h-[100svh]` ... the one with py-20 was right after it.
html = re.sub(r'<section class="relative py-16 px-4 overflow-hidden">', r'<section class="relative py-20 px-4 overflow-hidden">', html, count=1)


html = html.replace('py-10 md:py-12', 'py-12')
html = html.replace('mb-8 md:mb-10', 'mb-10')
html = html.replace('padding: 56px 16px;', 'padding: 64px 16px;')

# There were some other leftovers from reduce_spacing.py that were missed by revert_spacing.py
html = html.replace('padding: 24px md:padding:32px;', 'padding: 40px;')
html = html.replace('mb-6 md:mb-8', 'mb-10') # in case any were left
html = html.replace('margin-bottom: 24px;', 'margin-bottom: 40px;') 
# Wait, "margin-bottom: 24px;" might revert things we didn't want. In the guarantee block we had "margin-bottom: 24px;". Let's check original. Original had 'margin-bottom: 24px;' inside the Guarantee block!
# My earlier script changed it. So I should undo ONLY what was changed incorrectly.

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Rollback total.")
