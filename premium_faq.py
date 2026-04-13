import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Find the FAQ section boundaries (section at line 3138)
start_marker = '\t\t<section class="py-16 px-4 bg-[#0d0705]">\n'
# The section ends at line 3476; find it after our marker
start_idx = html.find(start_marker, html.find('Como eu recebo o acesso?') - 5000)
if start_idx == -1:
    # fallback – use unique heading text
    start_idx = html.find('\t\t<section class="py-16 px-4 bg-[#0d0705]">', html.find('DÚVIDAS') - 200)
end_idx = html.find('</section>', start_idx) + len('</section>')

print(f"Replacing chars {start_idx}–{end_idx}")

NEW_FAQ = '''		<section id="faq" class="py-16 px-4 relative overflow-hidden" style="background:linear-gradient(180deg,#0d0705 0%,#130c09 100%);">
			<!-- Ambient glow -->
			<div style="position:absolute;top:0;left:50%;transform:translateX(-50%);width:500px;height:220px;background:radial-gradient(ellipse,rgba(180,83,9,0.10) 0%,transparent 70%);pointer-events:none;"></div>

			<div class="relative z-10 max-w-2xl mx-auto">

				<!-- Heading -->
				<div class="text-center mb-10">
					<h2 class="text-2xl md:text-3xl font-black text-white">DÚVIDAS <span class="text-amber-400">FREQUENTES</span></h2>
					<p class="text-gray-500 text-sm mt-2">Respostas rápidas para as perguntas mais comuns</p>
				</div>

				<!-- FAQ Items -->
				<div class="space-y-3" id="faq-list">

					<!-- Item template: question + answer -->
					<div class="faq-item rounded-2xl overflow-hidden" style="background:#1a1008;border:1px solid rgba(180,110,30,0.22);">
						<button class="faq-q w-full flex items-center justify-between px-5 py-4 text-left gap-4" onclick="toggleFaq(this)">
							<span class="text-white font-semibold text-[15px] leading-snug">Como eu recebo o acesso?</span>
							<svg class="faq-arrow flex-shrink-0 text-amber-400 transition-transform duration-300" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
						</button>
						<div class="faq-a hidden px-5 pb-5">
							<p class="text-gray-300 text-sm leading-relaxed">Assim que o pagamento é aprovado, você recebe automaticamente o link de acesso no seu e-mail (e também pode receber no WhatsApp). É só baixar e começar a usar na hora.</p>
						</div>
					</div>

					<div class="faq-item rounded-2xl overflow-hidden" style="background:#1a1008;border:1px solid rgba(180,110,30,0.22);">
						<button class="faq-q w-full flex items-center justify-between px-5 py-4 text-left gap-4" onclick="toggleFaq(this)">
							<span class="text-white font-semibold text-[15px] leading-snug">Precisa de internet pra ouvir?</span>
							<svg class="faq-arrow flex-shrink-0 text-amber-400 transition-transform duration-300" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
						</button>
						<div class="faq-a hidden px-5 pb-5">
							<p class="text-gray-300 text-sm leading-relaxed">Não. Depois de baixar, você pode ouvir tudo offline no carro, pendrive ou qualquer aparelho compatível.</p>
						</div>
					</div>

					<div class="faq-item rounded-2xl overflow-hidden" style="background:#1a1008;border:1px solid rgba(180,110,30,0.22);">
						<button class="faq-q w-full flex items-center justify-between px-5 py-4 text-left gap-4" onclick="toggleFaq(this)">
							<span class="text-white font-semibold text-[15px] leading-snug">Funciona em qualquer carro?</span>
							<svg class="faq-arrow flex-shrink-0 text-amber-400 transition-transform duration-300" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
						</button>
						<div class="faq-a hidden px-5 pb-5">
							<p class="text-gray-300 text-sm leading-relaxed">Sim. Funciona em qualquer carro que tenha entrada USB ou sistema de som que leia arquivos MP3.</p>
						</div>
					</div>

					<div class="faq-item rounded-2xl overflow-hidden" style="background:#1a1008;border:1px solid rgba(180,110,30,0.22);">
						<button class="faq-q w-full flex items-center justify-between px-5 py-4 text-left gap-4" onclick="toggleFaq(this)">
							<span class="text-white font-semibold text-[15px] leading-snug">Como coloco no pendrive?</span>
							<svg class="faq-arrow flex-shrink-0 text-amber-400 transition-transform duration-300" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
						</button>
						<div class="faq-a hidden px-5 pb-5">
							<p class="text-gray-300 text-sm leading-relaxed">Você baixa as músicas, copia para o pendrive no celular ou computador, conecta no carro e pronto. Tudo já vai organizado por pastas.</p>
						</div>
					</div>

					<div class="faq-item rounded-2xl overflow-hidden" style="background:#1a1008;border:1px solid rgba(180,110,30,0.22);">
						<button class="faq-q w-full flex items-center justify-between px-5 py-4 text-left gap-4" onclick="toggleFaq(this)">
							<span class="text-white font-semibold text-[15px] leading-snug">Eu não entendo nada disso, vou conseguir usar?</span>
							<svg class="faq-arrow flex-shrink-0 text-amber-400 transition-transform duration-300" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
						</button>
						<div class="faq-a hidden px-5 pb-5">
							<p class="text-gray-300 text-sm leading-relaxed">Sim. O processo é simples e você recebe instruções básicas para conseguir usar sem dificuldade.</p>
						</div>
					</div>

					<div class="faq-item rounded-2xl overflow-hidden" style="background:#1a1008;border:1px solid rgba(180,110,30,0.22);">
						<button class="faq-q w-full flex items-center justify-between px-5 py-4 text-left gap-4" onclick="toggleFaq(this)">
							<span class="text-white font-semibold text-[15px] leading-snug">Tem música antiga e nova?</span>
							<svg class="faq-arrow flex-shrink-0 text-amber-400 transition-transform duration-300" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
						</button>
						<div class="faq-a hidden px-5 pb-5">
							<p class="text-gray-300 text-sm leading-relaxed">Sim. Você recebe uma seleção completa com modões raiz, clássicos, universitário e hits atuais.</p>
						</div>
					</div>

					<div class="faq-item rounded-2xl overflow-hidden" style="background:#1a1008;border:1px solid rgba(180,110,30,0.22);">
						<button class="faq-q w-full flex items-center justify-between px-5 py-4 text-left gap-4" onclick="toggleFaq(this)">
							<span class="text-white font-semibold text-[15px] leading-snug">As músicas são de boa qualidade?</span>
							<svg class="faq-arrow flex-shrink-0 text-amber-400 transition-transform duration-300" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
						</button>
						<div class="faq-a hidden px-5 pb-5">
							<p class="text-gray-300 text-sm leading-relaxed">Sim. Todas as músicas são em alta qualidade de áudio, prontas pra tocar sem falhas.</p>
						</div>
					</div>

					<div class="faq-item rounded-2xl overflow-hidden" style="background:#1a1008;border:1px solid rgba(180,110,30,0.22);">
						<button class="faq-q w-full flex items-center justify-between px-5 py-4 text-left gap-4" onclick="toggleFaq(this)">
							<span class="text-white font-semibold text-[15px] leading-snug">Dá pra ouvir na TV ou caixa de som?</span>
							<svg class="faq-arrow flex-shrink-0 text-amber-400 transition-transform duration-300" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
						</button>
						<div class="faq-a hidden px-5 pb-5">
							<p class="text-gray-300 text-sm leading-relaxed">Sim. Você pode usar em TV, caixa de som, computador ou qualquer aparelho compatível com USB ou MP3.</p>
						</div>
					</div>

					<div class="faq-item rounded-2xl overflow-hidden" style="background:#1a1008;border:1px solid rgba(180,110,30,0.22);">
						<button class="faq-q w-full flex items-center justify-between px-5 py-4 text-left gap-4" onclick="toggleFaq(this)">
							<span class="text-white font-semibold text-[15px] leading-snug">É pagamento único?</span>
							<svg class="faq-arrow flex-shrink-0 text-amber-400 transition-transform duration-300" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
						</button>
						<div class="faq-a hidden px-5 pb-5">
							<p class="text-gray-300 text-sm leading-relaxed">Sim. Você paga uma vez só e o acesso é seu, sem mensalidade.</p>
						</div>
					</div>

					<div class="faq-item rounded-2xl overflow-hidden" style="background:#1a1008;border:1px solid rgba(180,110,30,0.22);">
						<button class="faq-q w-full flex items-center justify-between px-5 py-4 text-left gap-4" onclick="toggleFaq(this)">
							<span class="text-white font-semibold text-[15px] leading-snug">E se não funcionar pra mim?</span>
							<svg class="faq-arrow flex-shrink-0 text-amber-400 transition-transform duration-300" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
						</button>
						<div class="faq-a hidden px-5 pb-5">
							<p class="text-gray-300 text-sm leading-relaxed">Você tem garantia de 7 dias. Se não gostar, pode pedir seu dinheiro de volta. Sem burocracia.</p>
						</div>
					</div>

					<div class="faq-item rounded-2xl overflow-hidden" style="background:#1a1008;border:1px solid rgba(180,110,30,0.22);">
						<button class="faq-q w-full flex items-center justify-between px-5 py-4 text-left gap-4" onclick="toggleFaq(this)">
							<span class="text-white font-semibold text-[15px] leading-snug">E se eu tiver dúvidas?</span>
							<svg class="faq-arrow flex-shrink-0 text-amber-400 transition-transform duration-300" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
						</button>
						<div class="faq-a hidden px-5 pb-5">
							<p class="text-gray-300 text-sm leading-relaxed">Você recebe suporte para te ajudar no que precisar. Não vai ficar sozinho.</p>
						</div>
					</div>

				</div><!-- /faq-list -->

				<!-- Frase de reforço final -->
				<div class="mt-10 text-center">
					<p class="text-gray-400 text-sm md:text-base leading-relaxed">
						Ainda com dúvida? Você pode testar sem risco.<br/>
						<strong class="text-white">Sua compra está 100% protegida.</strong>
					</p>
				</div>

			</div><!-- /max-w -->

			<!-- FAQ JS -->
			<script>
				function toggleFaq(btn) {
					var item  = btn.closest('.faq-item');
					var panel = item.querySelector('.faq-a');
					var arrow = btn.querySelector('.faq-arrow');
					var open  = !panel.classList.contains('hidden');

					// close all
					document.querySelectorAll('.faq-a').forEach(function(p){ p.classList.add('hidden'); });
					document.querySelectorAll('.faq-arrow').forEach(function(a){ a.style.transform = 'rotate(0deg)'; });
					document.querySelectorAll('.faq-item').forEach(function(it){ it.style.border = '1px solid rgba(180,110,30,0.22)'; });

					if (!open) {
						panel.classList.remove('hidden');
						arrow.style.transform = 'rotate(180deg)';
						item.style.border = '1px solid rgba(245,158,11,0.50)';
					}
				}
			</script>
		</section>'''

html = html[:start_idx] + NEW_FAQ + html[end_idx:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Done!")
