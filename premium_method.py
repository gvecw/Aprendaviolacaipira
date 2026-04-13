import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Find the "Como funciona" section we inserted
old_pattern = r'<section class="relative py-14 px-4 bg-\[#120a07\] border-y border-amber-900/20 overflow-hidden">.*?</section>'
match = re.search(old_pattern, html, flags=re.DOTALL)

if not match:
    print("Section not found. Trying alternate search...")
    # Try looking for the heading text
    old_pattern2 = r'<section[^>]*>.*?Como funciona.*?</section>'
    match = re.search(old_pattern2, html, flags=re.DOTALL)

if not match:
    print("Section still not found!")
    exit()

new_section = '''<section class="relative py-16 px-4 overflow-hidden" style="background:linear-gradient(180deg,#0d0705 0%,#160d09 60%,#0d0705 100%);">
    <!-- Glow ambiental -->
    <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:600px;height:300px;background:radial-gradient(ellipse,rgba(180,83,9,0.10) 0%,transparent 70%);pointer-events:none;"></div>
    <div class="relative z-10 max-w-4xl mx-auto text-center">

        <!-- Eyebrow -->
        <span style="display:inline-block;color:#f59e0b;font-size:11px;font-weight:800;letter-spacing:2px;text-transform:uppercase;margin-bottom:14px;opacity:0.85;">&#9675; Sem enrolação</span>

        <!-- Título forte -->
        <h2 class="text-3xl md:text-4xl lg:text-5xl font-black mb-5 text-white">
            Por que esse método funciona<br class="hidden md:block"/>
            <span class="text-amber-400">mesmo pra quem nunca tocou</span>
        </h2>

        <!-- Parágrafo curto e direto -->
        <p class="text-gray-300 text-base md:text-lg mb-12 max-w-2xl mx-auto leading-relaxed">
            Simples, direto ao ponto e sem teoria complicada. Você não precisa de experiência — apenas disposição para praticar.
        </p>

        <!-- 3 Cards Premium -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-5 text-left">

            <!-- Card 1 -->
            <div style="
                background:linear-gradient(145deg,#1e1108,#271609);
                border:1px solid rgba(180,110,30,0.30);
                border-radius:16px;
                padding:32px 26px;
                box-shadow:0 20px 45px rgba(0,0,0,0.45),inset 0 1px 0 rgba(245,158,11,0.06);
                transition:border-color 0.3s;
            ">
                <!-- Ícone: Alvo/início -->
                <div style="width:52px;height:52px;border-radius:12px;background:linear-gradient(135deg,rgba(245,158,11,0.18),rgba(234,88,12,0.12));border:1px solid rgba(245,158,11,0.25);display:flex;align-items:center;justify-content:center;margin-bottom:18px;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>
                    </svg>
                </div>
                <h3 style="color:#ffffff;font-size:19px;font-weight:800;margin-bottom:10px;line-height:1.3;">Comece do Zero</h3>
                <p style="color:#a5a5a5;font-size:14px;line-height:1.65;margin:0;">Mesmo que você nunca tenha tocado nada, o método te guia desde o início com passos simples e claros.</p>
            </div>

            <!-- Card 2 -->
            <div style="
                background:linear-gradient(145deg,#1e1108,#271609);
                border:1px solid rgba(180,110,30,0.30);
                border-radius:16px;
                padding:32px 26px;
                box-shadow:0 20px 45px rgba(0,0,0,0.45),inset 0 1px 0 rgba(245,158,11,0.06);
            ">
                <!-- Ícone: Prática -->
                <div style="width:52px;height:52px;border-radius:12px;background:linear-gradient(135deg,rgba(245,158,11,0.18),rgba(234,88,12,0.12));border:1px solid rgba(245,158,11,0.25);display:flex;align-items:center;justify-content:center;margin-bottom:18px;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/>
                    </svg>
                </div>
                <h3 style="color:#ffffff;font-size:19px;font-weight:800;margin-bottom:10px;line-height:1.3;">Aprenda Praticando</h3>
                <p style="color:#a5a5a5;font-size:14px;line-height:1.65;margin:0;">Sem teoria complicada. Você aprende tocando desde as primeiras aulas, de forma direta e eficiente.</p>
            </div>

            <!-- Card 3 -->
            <div style="
                background:linear-gradient(145deg,#1e1108,#271609);
                border:1px solid rgba(180,110,30,0.30);
                border-radius:16px;
                padding:32px 26px;
                box-shadow:0 20px 45px rgba(0,0,0,0.45),inset 0 1px 0 rgba(245,158,11,0.06);
            ">
                <!-- Ícone: Progresso/seta ascendente -->
                <div style="width:52px;height:52px;border-radius:12px;background:linear-gradient(135deg,rgba(245,158,11,0.18),rgba(234,88,12,0.12));border:1px solid rgba(245,158,11,0.25);display:flex;align-items:center;justify-content:center;margin-bottom:18px;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                        <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/>
                    </svg>
                </div>
                <h3 style="color:#ffffff;font-size:19px;font-weight:800;margin-bottom:10px;line-height:1.3;">Resultados Desde o Início</h3>
                <p style="color:#a5a5a5;font-size:14px;line-height:1.65;margin:0;">Em poucos dias, você já consegue tocar suas primeiras músicas simples e sentir o progresso de verdade.</p>
            </div>

        </div>
    </div>
</section>'''

html = html[:match.start()] + new_section + html[match.end():]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Done!")
