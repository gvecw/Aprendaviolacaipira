import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Locate the section
old_pattern = r'<section id="o-que-vai-aprender".*?</section>'
match = re.search(old_pattern, html, flags=re.DOTALL)

if match:
    old_section = match.group(0)

    # I will construct a completely upgraded section meeting all criteria:
    new_section = '''<section id="o-que-vai-aprender" class="py-16 px-4 bg-[#0d0705] border-t border-amber-900/20 relative overflow-hidden">
            <!-- Glow Background -->
            <div class="absolute top-0 right-0 -mr-20 -mt-20 w-[300px] h-[300px] bg-amber-600/10 rounded-full blur-[100px]"></div>
            <div class="absolute bottom-0 left-0 -ml-20 -mb-20 w-[300px] h-[300px] bg-orange-600/10 rounded-full blur-[100px]"></div>

            <div class="relative z-10 max-w-4xl mx-auto">
                <div class="text-center mb-10 md:mb-14">
                    <h2 class="text-3xl md:text-4xl lg:text-5xl font-black mb-4 text-white">O que você vai <span class="text-amber-500">aprender na prática</span></h2>
                    <p class="text-gray-300 text-base md:text-lg max-w-2xl mx-auto">Mesmo começando do zero, você vai aprender passo a passo como tocar viola de forma simples e prática.</p>
                    <div class="mt-4 inline-flex items-center gap-2 bg-amber-900/30 border border-amber-500/20 px-4 py-1.5 rounded-full">
                        <span class="text-amber-400 font-bold text-xs uppercase tracking-wider">🎯 Método pensado para iniciantes absolutos</span>
                    </div>
                </div>

                <div class="bg-gradient-to-br from-[#1a0f0a] to-[#2a1a12] rounded-3xl p-6 md:p-10 border border-amber-900/40 shadow-[0_20px_50px_rgba(0,0,0,0.5)] max-w-3xl mx-auto">
                    <ul class="grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-x-8 md:gap-y-6">
                        <li class="flex items-start gap-4">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-green-500 flex-shrink-0 mt-0.5 drop-shadow-[0_0_8px_rgba(34,197,94,0.5)]" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg>
                            <span class="text-white text-[15px] md:text-[17px] font-medium leading-relaxed">acordes básicos da viola</span>
                        </li>
                        <li class="flex items-start gap-4">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-green-500 flex-shrink-0 mt-0.5 drop-shadow-[0_0_8px_rgba(34,197,94,0.5)]" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg>
                            <span class="text-white text-[15px] md:text-[17px] font-medium leading-relaxed">primeiros ritmos e batidas</span>
                        </li>
                        <li class="flex items-start gap-4">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-green-500 flex-shrink-0 mt-0.5 drop-shadow-[0_0_8px_rgba(34,197,94,0.5)]" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg>
                            <span class="text-white text-[15px] md:text-[17px] leading-relaxed"><strong class="text-amber-400 font-extrabold">como tocar suas primeiras músicas</strong></span>
                        </li>
                        <li class="flex items-start gap-4">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-green-500 flex-shrink-0 mt-0.5 drop-shadow-[0_0_8px_rgba(34,197,94,0.5)]" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg>
                            <span class="text-white text-[15px] md:text-[17px] font-medium leading-relaxed">exercícios práticos passo a passo</span>
                        </li>
                        <li class="flex items-start gap-4">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-green-500 flex-shrink-0 mt-0.5 drop-shadow-[0_0_8px_rgba(34,197,94,0.5)]" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg>
                            <span class="text-white text-[15px] md:text-[17px] font-medium leading-relaxed">cifras dos modões mais tocados</span>
                        </li>
                        <li class="flex items-start gap-4">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-green-500 flex-shrink-0 mt-0.5 drop-shadow-[0_0_8px_rgba(34,197,94,0.5)]" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg>
                            <span class="text-white text-[15px] md:text-[17px] leading-relaxed"><strong class="text-amber-400 font-extrabold">repertório sertanejo raiz e universitário</strong></span>
                        </li>
                        <li class="flex items-start gap-4">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-green-500 flex-shrink-0 mt-0.5 drop-shadow-[0_0_8px_rgba(34,197,94,0.5)]" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg>
                            <span class="text-white text-[15px] md:text-[17px] font-medium leading-relaxed">músicas gospel para tocar na viola</span>
                        </li>
                    </ul>

                    <div class="mt-8 md:mt-10 pt-6 border-t border-amber-900/30 text-center bg-gradient-to-r from-transparent via-amber-900/20 to-transparent">
                        <p class="text-amber-400 font-black text-lg md:text-xl lg:text-2xl drop-shadow-md">🚀 TUDO PRONTO PRA VOCÊ SAIR DO ZERO E COMEÇAR A TOCAR DE VERDADE</p>
                    </div>
                </div>
            </div>
        </section>'''

    html = html.replace(old_section, new_section)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Done")
else:
    print("Section not found!")
