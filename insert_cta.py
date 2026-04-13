import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# We need to insert the CTA block between the mockup wrapper and the sub-headline.
search_str = '        </div>\n\n        <!-- SUBHEADLINE:'

cta_block = """        </div>

        <!-- CTA BUTTON INCORPORATED RIGHT BELOW MOCKUP -->
        <a href="#oferta-premium" onclick="document.getElementById('oferta-premium').scrollIntoView({behavior: 'smooth'}); return false;" class="cta-button">
            QUERO COMEÇAR AGORA
        </a>
        
        <!-- MICROCOPY & TRUST -->
        <div style="display:flex; flex-direction:column; gap:6px; margin-bottom:1.5rem;">
            <p style="font-size:13px; color:#22c55e; font-weight:600; display:flex; align-items:center; justify-content:center; gap:6px; margin:0;">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                Liberação imediata após a compra
            </p>
            <p class="microcopy" style="margin:0;">
                ⬇️ Toque para ver como funciona ⬇️
            </p>
        </div>

        <!-- SUBHEADLINE:"""

html = html.replace(search_str, cta_block)

# Verify the .cta-button style is still in the <style> block. (It should be, I only removed the HTML)
# Let's check .cta-button padding just to be sure it matches the new specs.
html = re.sub(
    r'\.cta-button \{([\s\S]*?)padding: 14px 28px;',
    r'.cta-button {\1padding: 18px 30px;',
    html
)
html = re.sub(
    r'\.cta-button \{([\s\S]*?)padding: 22px 36px;',
    r'.cta-button {\1padding: 24px 38px;',
    html
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Done")
