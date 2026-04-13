import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Title
html = re.sub(
    r'Escute agora uma <span[^>]*>amostra real</span>',
    r'Veja o tipo de som que você vai <span class="text-amber-400">conseguir tocar</span>',
    html,
    flags=re.IGNORECASE | re.DOTALL | re.MULTILINE
)

# 2. Subtitle
html = re.sub(
    r'Organizado por estilos e pronto pra usar no carro ou\s*pendrive',
    r'Mesmo começando do zero, você pode chegar nesse nível',
    html,
    flags=re.IGNORECASE | re.DOTALL | re.MULTILINE
)

# 3. Badge Text
html = re.sub(
    r'Prévia\s*de áudio \(MP3\)',
    r'Exemplo real na viola',
    html,
    flags=re.IGNORECASE | re.DOTALL | re.MULTILINE
)

# 4. Playlist Sertaneja Completa (Title)
html = re.sub(
    r'Playlist Sertaneja\s*Completa',
    r'Moda de Viola (exemplo simples)',
    html,
    flags=re.IGNORECASE | re.DOTALL | re.MULTILINE
)

# 5. Badges below title
html = re.sub(
    r'Raiz • Universitário •\s*Sofrência • Hits atuais',
    r'',
    html,
    flags=re.IGNORECASE | re.DOTALL | re.MULTILINE
)

# 6. Description Text (Um dos primeiros estilos...)
html = re.sub(
    r'Seleção\s*Ouro - As Mais Tocadas',
    r'Um dos primeiros estilos que você aprende no método',
    html,
    flags=re.IGNORECASE | re.DOTALL | re.MULTILINE
)

# 7. Final text at the bottom
# The usb text looks like: 
# <p class="text-center text-gray-400 text-[10px] sm:text-xs flex items-center justify-center gap-1.5"><svg...lucide-usb...</svg>
# Text...
# Let's replace the whole <div class="mt-3 sm:mt-4 pt-2.5 sm:pt-3 border-t border-amber-900/20">...</div>
html = re.sub(
    r'<div class="mt-3 sm:mt-4 pt-2\.5 sm:pt-3 border-t border-amber-900/20">.*?</div>',
    r'<div class="mt-3 sm:mt-4 pt-2.5 sm:pt-3 border-t border-amber-900/20"><p class="text-center text-gray-400 text-[11px] font-medium flex items-center justify-center gap-1.5"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-4 h-4"><polyline points="20 6 9 17 4 12"></polyline></svg>Você começa do zero e evolui até tocar assim</p></div>',
    html,
    flags=re.DOTALL
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("done")
