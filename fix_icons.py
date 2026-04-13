import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

icons = {
    'Feito para iniciantes': '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="w-6 h-6 text-amber-400"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
    'Método simples e direto': '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="w-6 h-6 text-amber-400"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>',
    'Passo a passo completo': '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="w-6 h-6 text-amber-400"><line x1="10" y1="6" x2="21" y2="6"/><line x1="10" y1="12" x2="21" y2="12"/><line x1="10" y1="18" x2="21" y2="18"/><path d="M4 6h1v4"/><path d="M4 10h2"/><path d="M6 18H4c0-1 2-2 2-3s-1-1.5-2-1"/></svg>',
    'Aprenda no seu ritmo': '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="w-6 h-6 text-amber-400"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
    'Acesso pelo celular': '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="w-6 h-6 text-amber-400"><rect width="14" height="20" x="5" y="2" rx="2" ry="2"/><path d="M12 18h.01"/></svg>',
    'Comece hoje mesmo': '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="w-6 h-6 text-amber-400"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>'
}

# The cards are inside a section. We can just iterate the keys, find them, and traverse backwards to replace the <svg...
for title, new_svg in icons.items():
    # Find title
    idx = html.find(f'<h3 class="text-lg md:text-xl font-bold text-white mb-1">{title}</h3>')
    if idx != -1:
        # Find the previous </svg>
        svg_end = html.rfind('</svg>', 0, idx)
        if svg_end != -1:
            svg_start = html.rfind('<svg', 0, svg_end)
            if svg_start != -1:
                # Replace the SVG chunk
                html = html[:svg_start] + new_svg + html[svg_end + 6:]
            else:
                print(f"Could not find <svg for {title}")
        else:
            print(f"Could not find </svg> for {title}")
    else:
        print(f"Could not find h3 for {title}")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Done")
