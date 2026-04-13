import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

def replace_icon(title, new_svg):
    # Regex searches for the wrapper div that contains the flex icon circle and the title
    pattern = r'<div[^>]*class="w-12 h-12[^>]*>.*?<svg.*?</svg>.*?</div[^>]*>.*?<div[^>]*>.*?<h3[^>]*>' + title + r'</h3>'
    match = re.search(pattern, html, flags=re.DOTALL)
    if match:
        old_block = match.group(0)
        # Now replace the SVG inside old_block
        new_block = re.sub(r'<svg.*?</svg>', new_svg, old_block, flags=re.DOTALL)
        return html.replace(old_block, new_block)
    return html

html = replace_icon('Feito para iniciantes', '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="w-6 h-6 text-amber-400"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>')
html = replace_icon('Método simples e direto', '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="w-6 h-6 text-amber-400"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>')
html = replace_icon('Passo a passo completo', '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="w-6 h-6 text-amber-400"><line x1="10" y1="6" x2="21" y2="6"/><line x1="10" y1="12" x2="21" y2="12"/><line x1="10" y1="18" x2="21" y2="18"/><path d="M4 6h1v4"/><path d="M4 10h2"/><path d="M6 18H4c0-1 2-2 2-3s-1-1.5-2-1"/></svg>')
html = replace_icon('Aprenda no seu ritmo', '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="w-6 h-6 text-amber-400"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>')
html = replace_icon('Acesso pelo celular', '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="w-6 h-6 text-amber-400"><rect width="14" height="20" x="5" y="2" rx="2" ry="2"/><path d="M12 18h.01"/></svg>')
html = replace_icon('Comece hoje mesmo', '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="w-6 h-6 text-amber-400"><circle cx="12" cy="12" r="10"/><polygon points="10 8 16 12 10 16 10 8"/></svg>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Done")
