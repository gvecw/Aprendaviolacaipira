import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# We need to insert the new section exactly after the <section id="amostras-section"> ... </section> closes.
# We can find where 'amostras-section' is defined.
start_idx = html.find('id="amostras-section"')
if start_idx != -1:
    # Find the next </section> after start_idx
    end_idx = html.find('</section>', start_idx)
    
    if end_idx != -1:
        # The exact text to insert after the end_idx + len("</section>")
        insertion_idx = end_idx + len('</section>')
        
        new_section = """\n
        <section id="o-que-vai-aprender" class="py-16 px-4 bg-[#0d0705] border-t border-amber-900/20 relative overflow-hidden">
            <!-- Glow Background -->
            <div class="absolute top-0 right-0 -mr-20 -mt-20 w-64 h-64 bg-amber-600/10 rounded-full blur-[80px]"></div>
            <div class="absolute bottom-0 left-0 -ml-20 -mb-20 w-64 h-64 bg-orange-600/10 rounded-full blur-[80px]"></div>

            <div class="relative z-10 max-w-3xl mx-auto">
                <div class="text-center mb-8 md:mb-12">
                    <h2 class="text-3xl md:text-4xl font-black mb-4 text-white">O que você vai <span class="text-amber-500">aprender na prática</span></h2>
                    <p class="text-gray-300 text-base md:text-lg max-w-2xl mx-auto">Mesmo começando do zero, você vai aprender passo a passo como tocar viola de forma simples e prática.</p>
                </div>

                <div class="bg-gradient-to-br from-[#1a0f0a] to-[#2a1a12] rounded-2xl p-6 md:p-8 border border-amber-900/30 shadow-xl shadow-black/40">
                    <ul class="space-y-4">
                        <li class="flex items-start gap-4">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-green-500 flex-shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg>
                            <span class="text-white text-base md:text-lg font-medium leading-relaxed">acordes básicos da viola</span>
                        </li>
                        <li class="flex items-start gap-4">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-green-500 flex-shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg>
                            <span class="text-white text-base md:text-lg font-medium leading-relaxed">primeiros ritmos e batidas</span>
                        </li>
                        <li class="flex items-start gap-4">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-green-500 flex-shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg>
                            <span class="text-white text-base md:text-lg font-medium leading-relaxed">como tocar suas primeiras músicas</span>
                        </li>
                        <li class="flex items-start gap-4">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-green-500 flex-shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg>
                            <span class="text-white text-base md:text-lg font-medium leading-relaxed">exercícios práticos passo a passo</span>
                        </li>
                        <li class="flex items-start gap-4">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-green-500 flex-shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg>
                            <span class="text-white text-base md:text-lg font-medium leading-relaxed">cifras dos modões mais tocados</span>
                        </li>
                        <li class="flex items-start gap-4">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-green-500 flex-shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg>
                            <span class="text-white text-base md:text-lg font-medium leading-relaxed">repertório sertanejo raiz e universitário</span>
                        </li>
                        <li class="flex items-start gap-4">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-green-500 flex-shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg>
                            <span class="text-white text-base md:text-lg font-medium leading-relaxed">músicas gospel para tocar na viola</span>
                        </li>
                    </ul>

                    <div class="mt-8 pt-5 border-t border-amber-900/30 text-center">
                        <p class="text-amber-400 font-bold text-base md:text-lg italic">" Tudo pronto pra você sair do zero e começar a tocar de verdade "</p>
                    </div>
                </div>
            </div>
        </section>\n"""

        # Perform the insertion
        html = html[:insertion_idx] + new_section + html[insertion_idx:]
        
        # Save back
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Done! Section added.")
    else:
        print("Error: Could not find closing section of amostras-section.")
else:
    print("Error: Could not find amostras-section ID.")
