import re
with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Background overlay and gradient opacity
text = text.replace('rgba(0,0,0,0.65)', 'rgba(0,0,0,0.80)')
text = text.replace('opacity: 0.70;', 'opacity: 0.75;')

# 2. Texto pequeno superior (badge)
text = text.replace(
    '🎁 SERTANEJO NO SEU CARRO',
    'VIOLA CAIPIRA DO ZERO'
)
# Update text-sm to include uppercase styling
text = text.replace(
    'text-white text-sm font-bold px-4 py-2 rounded-full mb-6',
    'text-white text-[11px] md:text-[13px] font-bold px-4 py-2 rounded-full mb-6 uppercase tracking-wider'
)

# 3. Headline
text = text.replace(
    '<span\n\t\t\t\t\t\tclass="text-amber-400">+3.000 CLÁSSICOS</span><br /><span class="text-white">DO\n\t\t\t\t\t\tMODÃO</span>',
    '<span class="text-amber-400">APRENDA A TOCAR</span><br /><span class="text-white">VIOLA DO ZERO</span>'
)
text = text.replace(
    '<span\n\t\t\t\t\t\tclass="text-amber-400">+3.000 CLÁSSICOS</span><br/><span class="text-white">DO\n\t\t\t\t\t\tMODÃO</span>',
    '<span class="text-amber-400">APRENDA A TOCAR</span><br/><span class="text-white">VIOLA DO ZERO</span>'
)
# Just in case whitespace is different
text = re.sub(
    r'<span[^>]*>\s*\+3\.000 CLÁSSICOS\s*</span>\s*<br\s*/?>\s*<span[^>]*>\s*DO\s*MODÃO\s*</span>',
    '<span class="text-amber-400">APRENDA A TOCAR</span><br /><span class="text-white">VIOLA DO ZERO</span>',
    text
)
# Increase headline padding
text = text.replace(
    'text-4xl md:text-6xl lg:text-7xl font-black mb-6 leading-tight',
    'text-5xl md:text-6xl lg:text-7xl font-black mb-8 leading-tight px-2'
)

# 4. Sub-headline
text = re.sub(
    r'<p class="text-xl md:text-2xl text-gray-300 mb-6 max-w-2xl mx-auto">\s*A playlist definitiva para o seu Pen Drive\. O melhor do modão raiz para ouvir na estrada ou na roça, sem depender de internet\.\s*</p>',
    '<p class="text-lg md:text-2xl text-gray-200 mb-10 max-w-lg mx-auto leading-relaxed">Mesmo sem experiência, comece a tocar suas primeiras músicas na viola com um método simples e direto.</p>',
    text
)

# 5. Lista de benefícios
# Search for the block of checks.
checks_old = r'<div class="flex flex-wrap justify-center gap-4 mb-10 text-lg">.*?Sem mensalidade</span>\s*</div>'
checks_new = """<div class="flex flex-col sm:flex-row flex-wrap justify-center items-center gap-4 sm:gap-6 mb-12 text-base sm:text-lg">
    <span class="flex items-center gap-2 text-green-400">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-check w-5 h-5 flex-shrink-0" aria-hidden="true"><path d="M20 6 9 17l-5-5"></path></svg>
        Método simples
    </span>
    <span class="flex items-center gap-2 text-green-400">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-check w-5 h-5 flex-shrink-0" aria-hidden="true"><path d="M20 6 9 17l-5-5"></path></svg>
        Sem teoria complicada
    </span>
    <span class="flex items-center gap-2 text-green-400">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-check w-5 h-5 flex-shrink-0" aria-hidden="true"><path d="M20 6 9 17l-5-5"></path></svg>
        Comece do zero
    </span>
</div>"""
text = re.sub(checks_old, checks_new, text, flags=re.DOTALL)

# 6. Botão (CTA)
text = text.replace(
    'class="inline-block bg-gradient-to-r from-amber-500 to-orange-500 text-white font-black text-xl md:text-2xl px-12 py-5 rounded-full shadow-2xl shadow-amber-500/30 transition-all duration-300 ">Garantir Meu Acesso</a>',
    'class="inline-block bg-gradient-to-r from-amber-500 to-orange-500 text-white font-black text-2xl md:text-3xl px-12 md:px-16 py-6 md:py-7 rounded-full shadow-[0_0_40px_rgba(249,115,22,0.4)] transition-all duration-300 hover:scale-105 hover:shadow-[0_0_60px_rgba(249,115,22,0.6)]">COMEÇAR AGORA</a>'
)

# 7. Texto abaixo do botão
text = text.replace(
    '<p class="text-gray-400 text-sm mt-4 flex items-center justify-center gap-2">⬇️ Toque para ver os pacotes ⬇️</p>',
    '<p class="text-gray-300 text-xs md:text-sm mt-6 flex items-center justify-center gap-2 tracking-wide opacity-90">⬇️ Toque para ver como funciona ⬇️</p>'
)

# Ensure center spacing
text = text.replace(
    '<div class="relative z-10 text-center px-4 max-w-4xl mx-auto">',
    '<div class="relative z-10 text-center px-4 max-w-4xl mx-auto flex flex-col items-center pt-8">'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)
print("done")
