import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

###############################################
# 1. HERO – Headline
###############################################
html = html.replace(
    '<span class="headline-yellow">APRENDA VIOLA DO ZERO</span><br/>\n            <span class="headline-heavy">E TOQUE SUAS PRIMEIRAS MÚSICAS</span>',
    '<span class="headline-yellow">APRENDA VIOLA CAIPIRA DO ZERO</span><br/>\n            <span class="headline-heavy">E TOQUE SUAS PRIMEIRAS MÚSICAS EM POUCOS DIAS</span>'
)

###############################################
# 2. HERO – Subtítulo
###############################################
html = html.replace(
    'Mesmo sem experiência, você já pode tocar suas primeiras músicas em poucos dias',
    'Mesmo sem nenhuma experiência, você aprende passo a passo do jeito mais simples possível'
)

###############################################
# 3. HERO – CTA Button text
###############################################
html = html.replace(
    'QUERO COMEÇAR AGORA',
    'QUERO APRENDER VIOLA DO ZERO'
)

###############################################
# 4. HERO – Microcopy abaixo do botão
###############################################
html = html.replace(
    'Acesso imediato após a compra',
    'Acesso imediato · Sem experiência necessária'
)

###############################################
# 5. INSERT – Bloco de quebra de objeção (logo após </section> do hero)
###############################################
objection_block = '''
		<section class="relative py-10 px-4 bg-[#1a0f0a] border-y border-amber-900/20">
			<div class="absolute inset-0 bg-gradient-to-r from-amber-900/5 via-transparent to-amber-900/5"></div>
			<div class="relative z-10 max-w-3xl mx-auto text-center">
				<p class="text-base md:text-xl text-gray-200 leading-relaxed font-light">
					<span class="text-amber-400 font-bold">Você não precisa de dom, experiência ou conhecimento prévio.</span><br/>
					Este método foi criado especificamente para iniciantes absolutos que querem aprender de forma prática e sem enrolação.
				</p>
			</div>
		</section>
'''

# Insert right after the hero section closing tag
hero_end = '</section>\n\t\t<section class="relative py-20 px-4 overflow-hidden">'
html = html.replace(
    hero_end,
    '</section>\n' + objection_block + '\n\t\t<section class="relative py-20 px-4 overflow-hidden">'
)

###############################################
# 6. ADD – "Como funciona o método" section before "Como vai receber"
###############################################
method_section = '''
		<section class="relative py-14 px-4 bg-[#120a07] border-y border-amber-900/20 overflow-hidden">
			<div class="absolute top-0 left-1/2 -translate-x-1/2 w-[500px] h-[200px] bg-amber-700/10 rounded-full blur-[80px]"></div>
			<div class="relative z-10 max-w-3xl mx-auto text-center">
				<span class="text-amber-500 font-bold text-sm uppercase tracking-widest mb-3 block">🎸 Sem complicações</span>
				<h2 class="text-3xl md:text-4xl font-black mb-5 text-white">Como funciona <span class="text-amber-400">o método</span></h2>
				<p class="text-gray-300 text-base md:text-lg mb-10 leading-relaxed">
					Você não precisa de experiência. O método começa do absoluto básico e evolui rapidamente, levando você a tocar músicas simples em poucos dias — tudo de forma prática, sem teoria complicada.
				</p>
				<div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-left">
					<div class="bg-gradient-to-br from-[#2a1a12]/80 to-[#1a0f0a]/80 rounded-2xl p-5 border border-amber-900/30">
						<div class="text-2xl mb-3">🎯</div>
						<h3 class="text-white font-bold text-base mb-1">Começa do zero</h3>
						<p class="text-gray-400 text-sm leading-relaxed">Não importa se nunca tocou nada. Você começa pelo início e avança no seu ritmo.</p>
					</div>
					<div class="bg-gradient-to-br from-[#2a1a12]/80 to-[#1a0f0a]/80 rounded-2xl p-5 border border-amber-900/30">
						<div class="text-2xl mb-3">📱</div>
						<h3 class="text-white font-bold text-base mb-1">Aprende onde quiser</h3>
						<p class="text-gray-400 text-sm leading-relaxed">Acesse pelo celular ou computador, no horário que for melhor pra você.</p>
					</div>
					<div class="bg-gradient-to-br from-[#2a1a12]/80 to-[#1a0f0a]/80 rounded-2xl p-5 border border-amber-900/30">
						<div class="text-2xl mb-3">⚡</div>
						<h3 class="text-white font-bold text-base mb-1">Resultado rápido</h3>
						<p class="text-gray-400 text-sm leading-relaxed">Com prática constante, você toca suas primeiras músicas em poucos dias.</p>
					</div>
				</div>
			</div>
		</section>
'''

# Insert before the "Como você vai receber" section
delivery_anchor = '<section class="py-16 px-4 bg-[#1a0f0a]">'
html = html.replace(delivery_anchor, method_section + '\n\t\t' + delivery_anchor, 1)

###############################################
# 7. AUDIO section – Subtitle tweak (frase abaixo do player)
###############################################
html = html.replace(
    'Mesmo começando do zero, você pode chegar nesse nível',
    'Mesmo começando do zero, você pode chegar nesse nível com o método certo'
)

###############################################
# Save
###############################################
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Done!")
