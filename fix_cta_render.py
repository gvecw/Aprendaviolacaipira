import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the previous "button" HTML with one that does not depend on arbitrary uncompiled Tailwind classes
old_button_regex = r'<a href="#oferta-premium"?[^>]*>(\s*)QUERO APRENDER A TOCAR ASSIM(\s*)</a>'

new_button_html = '''
                    <a href="#oferta-premium" onclick="document.getElementById('oferta-premium').scrollIntoView({behavior: 'smooth'}); return false;" style="display:block; width:100%; max-width:320px; background:linear-gradient(to right, #f59e0b, #ea580c); color:#fff; font-weight:900; font-size:1.1rem; padding:16px 24px; border-radius:9999px; text-decoration:none; box-shadow:0 10px 25px rgba(234,88,12,0.3); transition:all 0.3s ease; text-align:center; margin:0 auto;">
                        QUERO APRENDER A TOCAR ASSIM
                    </a>
'''

if re.search(old_button_regex, html, flags=re.DOTALL):
    html = re.sub(old_button_regex, new_button_html, html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Done")
