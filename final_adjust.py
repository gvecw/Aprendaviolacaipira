import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 3. Change Headline text
html = html.replace('E COMECE A TOCAR DE VERDADE', 'E TOQUE SUAS PRIMEIRAS MÚSICAS')

# 1. MOVEMENT of CTA Block
cta_search = re.search(r'(<!-- CTA BUTTON INCORPORATED RIGHT BELOW MOCKUP -->.*?</div>)', html, re.DOTALL)
if cta_search:
    cta_block_complete = cta_search.group(1)
    
    # Remove from original position
    html = html.replace(cta_block_complete, '')
    
    # Create the new microcopy
    new_microcopy = '''
        <p style="font-size:13px; color:rgba(255, 255, 255, 0.7); font-weight:500; display:flex; align-items:center; justify-content:center; gap:6px; margin-top:0.5rem; margin-bottom: 1rem;">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>
            Acesso imediato após a compra
        </p>'''
    
    # Replace the old microcopy/trust wrapper with the new one
    cta_only = re.sub(r'<!-- MICROCOPY & TRUST -->[\s\S]*?</div>', '<!-- MICROCOPY -->\n' + new_microcopy, cta_block_complete)
    
    # Put the CTA block right after the benefits list
    benefits_search = re.search(r'(<div class="benefits-list">.*?</div>)', html, re.DOTALL)
    if benefits_search:
        benefits_block = benefits_search.group(1)
        html = html.replace(benefits_block, benefits_block + '\n\n' + cta_only)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Done")
