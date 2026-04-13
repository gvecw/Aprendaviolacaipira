import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# We need to extract the contents of the wrapper and wrap it in the new layout.
# Let's find the start of the wrapper:
wrapper_start = '<div class="relative z-10 text-center px-4 max-w-4xl mx-auto flex flex-col items-center pt-8">'

if wrapper_start in html:
    # Everything inside until the end of the section
    # Let's do a replace of the wrapper start
    new_wrapper_start = '''<div class="relative z-10 px-4 max-w-7xl mx-auto flex flex-col lg:flex-row items-center justify-between gap-12 lg:gap-8 pt-8">
				<!-- LADO ESQUERDO: TEXTOS -->
				<div class="w-full lg:w-[55%] flex flex-col items-center lg:items-start text-center lg:text-left">'''
    
    html = html.replace(wrapper_start, new_wrapper_start)
    
    # Now we need to modify the internal elements that were centered to be responsive (center on mobile, left on desktop)
    html = html.replace('max-w-lg mx-auto', 'max-w-lg mx-auto lg:mx-0')
    html = html.replace('max-w-[90vw] mx-auto', 'max-w-[90vw] mx-auto lg:mx-0')
    html = html.replace('justify-center items-center', 'justify-center lg:justify-start items-center lg:items-start')
    
    # We need to find the specific ending of the text block to insert the image right after.
    # The text block ends with 
    # <p class="text-gray-300 text-xs md:text-sm mt-6 flex items-center justify-center gap-2 tracking-wide opacity-90">⬇️ Toque para ver como funciona ⬇️</p>
    # </div>
    
    end_text = '<p class="text-gray-300 text-xs md:text-sm mt-6 flex items-center justify-center gap-2 tracking-wide opacity-90">⬇️ Toque para ver como funciona ⬇️</p>\n\n\n\n\t\t\t</div>'
    
    image_block = '''<p class="text-gray-300 text-xs md:text-sm mt-6 flex items-center justify-center lg:justify-start gap-2 tracking-wide opacity-90">⬇️ Toque para ver como funciona ⬇️</p>
				</div>
				<!-- LADO DIREITO: MOCKUP -->
				<div class="w-full lg:w-[40%] flex justify-center relative mt-8 lg:mt-0">
					<style>
						@keyframes floatMockup {
							0%, 100% { transform: translateY(0px) rotate(1.5deg); }
							50% { transform: translateY(-15px) rotate(0.5deg); }
						}
					</style>
					
					<div class="relative w-[65%] sm:w-[55%] lg:w-full max-w-[500px]" style="animation: floatMockup 6s ease-in-out infinite;">
						
						<!-- Efeito de profundidade/brilho no fundo (Backdrop Blur e Glow) -->
						<div class="absolute inset-0 bg-gradient-to-r from-amber-500/20 to-orange-500/10 blur-[80px] rounded-full scale-110 -z-10"></div>
						
						<!-- Sombra na base para dar peso e realismo -->
						<div class="absolute -bottom-8 left-1/2 -translate-x-1/2 w-[80%] h-[20px] bg-black/40 blur-[20px] rounded-[100%] -z-10"></div>
						
						<!-- Highlight lateral simulando luz da esquerda -->
						<div class="absolute inset-0 rounded-2xl bg-gradient-to-tr from-white/10 to-transparent opacity-50 mix-blend-overlay z-20 pointer-events-none"></div>
						
						<!-- Imagem do Mockup -->
						<img src="mockup-viola.png" alt="Livro Viola Caipira" class="relative z-10 w-full h-auto drop-shadow-[0_20px_40px_rgba(0,0,0,0.35)]" style="filter: contrast(1.05) saturate(1.05);" />
					</div>
				</div>
			</div>'''
    
    html = html.replace(end_text, image_block)
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated index.html successfully.")
else:
    print("Wrapper start not found! The HTML might be formatted differently.")
