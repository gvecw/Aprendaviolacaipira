with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Section heading
html = html.replace(
    '<h2 class="text-2xl md:text-3xl lg:text-4xl font-black mb-3">QUEM JÁ <span\n\n\t\t\t\t\t\t\tclass="text-amber-400">COMPROU:</span></h2>',
    '<h2 class="text-2xl md:text-3xl lg:text-4xl font-black mb-3">Quem já <span class="text-amber-400">começou do zero:</span></h2>'
)

# 2. Section subtitle
html = html.replace(
    '<p class="text-gray-400 text-sm md:text-base">Veja o que estão falando da playlist</p>',
    '<p class="text-gray-400 text-sm md:text-base">Resultados reais de quem nunca tinha tocado nada</p>'
)

# 3. Slide 1 depoimento
html = html.replace(
    '&quot;Coloquei no pendrive do carro e virou uma festa! Tem TUDO, só clássico raiz.&quot;',
    '&quot;Nunca tinha tocado nada na vida e achei que não ia conseguir&hellip; mas em poucos dias já consegui tocar minha primeira música. Muito mais simples do que parece.&quot;'
)
html = html.replace(
    '<p class="font-bold text-white text-base">Carlos Silva</p>\n\n\t\t\t\t\t\t\t\t\t\t\t<p class="text-gray-500 text-sm">Goiânia - GO</p>',
    '<p class="font-bold text-white text-base">Carlos Souza</p>\n\n\t\t\t\t\t\t\t\t\t\t\t<p class="text-gray-500 text-sm">Goiânia - GO</p>'
)

# 4. Slide 2 depoimento
html = html.replace(
    '&quot;Melhor investimento! Relembrei a época que viajava com meu pai escutando Tião Carreiro. Qualidade do áudio tá impecável.&quot;',
    '&quot;Comprei sem muita expectativa e me surpreendi. O método é direto e fácil de entender, em poucos dias já tava pegando ritmo e tocando.&quot;'
)
html = html.replace(
    '<p class="font-bold text-white text-base">Marcos Almeida</p>\n\n\t\t\t\t\t\t\t\t\t\t\t<p class="text-gray-500 text-sm">Uberlândia - MG</p>',
    '<p class="font-bold text-white text-base">Marcos Ferreira</p>\n\n\t\t\t\t\t\t\t\t\t\t\t<p class="text-gray-500 text-sm">Uberlândia - MG</p>'
)

# 5. Slide 3 depoimento
html = html.replace(
    '&quot;Comprei pra colocar na caminhonete e ir pra roça. Só modão rasgado, não tem uma música ruim, bom demais.&quot;',
    '&quot;Eu sempre achei que precisava de dom pra tocar viola, mas vi que era só o método certo. Já tô conseguindo tocar músicas simples e evoluindo rápido.&quot;'
)
html = html.replace(
    '<p class="font-bold text-white text-base">João Pedro</p>\n\n\t\t\t\t\t\t\t\t\t\t\t<p class="text-gray-500 text-sm">Cuiabá - MT</p>',
    '<p class="font-bold text-white text-base">João Ribeiro</p>\n\n\t\t\t\t\t\t\t\t\t\t\t<p class="text-gray-500 text-sm">Cuiabá - MT</p>'
)

# 6. Slide 4 depoimento
html = html.replace(
    '&quot;Acabou o sofrimento sem sinal de rádio na estrada. Salva a viagem! Organizado certinho por pastas.&quot;',
    '&quot;Já tinha tentado aprender sozinho e nunca consegui sair do lugar. Aqui foi diferente, é tudo explicado passo a passo, não tem como travar.&quot;'
)
html = html.replace(
    '<p class="font-bold text-white text-base">Roberto Nunes</p>\n\n\t\t\t\t\t\t\t\t\t\t\t<p class="text-gray-500 text-sm">Londrina - PR</p>',
    '<p class="font-bold text-white text-base">Roberto Lima</p>\n\n\t\t\t\t\t\t\t\t\t\t\t<p class="text-gray-500 text-sm">Londrina - PR</p>'
)

# 7. Slide 5 depoimento
html = html.replace(
    '&quot;Minha esposa deu de presente, já tá no som do carro e não tiro mais. Lembrança boa demais.&quot;',
    '&quot;Se você tá começando do zero igual eu, pode ir sem medo. Em poucos dias já dá pra tocar e isso motiva demais a continuar.&quot;'
)
html = html.replace(
    '<p class="font-bold text-white text-base">Antônio Costa</p>\n\n\t\t\t\t\t\t\t\t\t\t\t<p class="text-gray-500 text-sm">Campo Grande - MS</p>',
    '<p class="font-bold text-white text-base">Antônio Dias</p>\n\n\t\t\t\t\t\t\t\t\t\t\t<p class="text-gray-500 text-sm">Campo Grande - MS</p>'
)

# 8. Add social proof line after the testimonial slider section closing </div></section>
# Find the closing of the testimonial section (after the dots + nav buttons)
social_proof_block = '''
\t\t\t\t<!-- Prova social - efeito manada -->
\t\t\t\t<div class="mt-10 text-center">
\t\t\t\t\t<div style="display:inline-flex;align-items:center;gap:10px;background:rgba(245,158,11,0.08);border:1px solid rgba(245,158,11,0.20);padding:10px 22px;border-radius:9999px;">
\t\t\t\t\t\t<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
\t\t\t\t\t\t<span style="color:#e5e7eb;font-size:14px;font-weight:600;">Mais de <strong style="color:#f59e0b;">1.500 iniciantes</strong> de todo o Brasil já estão tocando suas primeiras músicas</span>
\t\t\t\t\t</div>
\t\t\t\t</div>'''

# Insert before closing </div> of the max-w-2xl container wrapping the testimonials
html = html.replace(
    '\n\t\t\t\t</div>\n\n\n\n\t\t\t</div>\n\n\n\n\t\t</section>\n\n\n\n\n\n\n\n\n\n\n\n\t\t<section id="ofertas"',
    social_proof_block + '\n\t\t\t\t</div>\n\n\n\n\t\t\t</div>\n\n\n\n\t\t</section>\n\n\n\n\n\n\n\n\n\n\n\n\t\t<section id="ofertas"'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Done!")
