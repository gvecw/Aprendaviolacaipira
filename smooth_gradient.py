import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix the stacked classes from the previous global string replace
html = re.sub(r'py-8 md:py-14 md:py-10 md:py-8 md:py-14', r'py-8 md:py-14', html)
html = re.sub(r'mb-6 md:mb-8 md:mb-6 md:mb-6 md:mb-8', r'mb-6 md:mb-8', html)
html = re.sub(r'mb-6 md:mb-8 md:mb-8 md:mb-6 md:mb-6 md:mb-8', r'mb-6 md:mb-8', html)

# Smoothen the Amostras Section Background Drop
# We will replace its absolute background div to ensure a flawless gradient flow
# We want it to just fade seamlessly down from the previous section without clipping
old_bg = r'<div class="absolute inset-0"\s*style="background:radial-gradient\(ellipse at top, rgba\(42, 26, 18, 0\.5\) 0%, transparent 50%\), radial-gradient\(ellipse at bottom, rgba\(42, 26, 18, 0\.5\) 0%, transparent 50%\), linear-gradient\(180deg, #1a0f0a 0%, #0d0705 100%\)">\s*</div>'

# We'll put a smooth top-bottom overlay and remove the sharp ellipse top.
new_bg = '''<div class="absolute inset-0"
				style="background:radial-gradient(ellipse at bottom, rgba(42, 26, 18, 0.3) 0%, transparent 50%), linear-gradient(180deg, #1a0f0a 0%, #0d0705 30%, #0d0705 100%)">
			</div>
            <div class="absolute top-0 left-0 w-full h-32 bg-gradient-to-b from-[#1a0f0a] to-transparent z-0"></div>'''

if re.search(old_bg, html, flags=re.DOTALL):
    html = re.sub(old_bg, new_bg, html, flags=re.DOTALL)
else:
    print("Warning: old background string not strictly matched.")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Done")
