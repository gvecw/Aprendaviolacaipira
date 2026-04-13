import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

old_pattern = r'<section id="o-que-vai-aprender".*?</section>'
match = re.search(old_pattern, html, flags=re.DOTALL)

if not match:
    print("Section not found!")
    exit()

new_section = '''<section id="o-que-vai-aprender" class="py-16 px-4 relative overflow-hidden" style="background: linear-gradient(180deg, #0d0705 0%, #130c09 50%, #0d0705 100%);">
    <!-- Glow ambiental -->
    <div style="position:absolute;top:-60px;right:-60px;width:360px;height:360px;background:radial-gradient(circle,rgba(180,83,9,0.12) 0%,transparent 70%);pointer-events:none;"></div>
    <div style="position:absolute;bottom:-60px;left:-60px;width:360px;height:360px;background:radial-gradient(circle,rgba(120,53,15,0.10) 0%,transparent 70%);pointer-events:none;"></div>

    <div class="relative z-10 max-w-4xl mx-auto">

        <!-- Título da seção -->
        <div class="text-center mb-10 md:mb-14">
            <h2 class="text-3xl md:text-4xl lg:text-5xl font-black mb-4 text-white">O que você vai <span class="text-amber-500">aprender na prática</span></h2>
            <p class="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">Mesmo começando do zero, você vai aprender passo a passo como tocar viola de forma simples e prática.</p>
        </div>

        <!-- Card Premium -->
        <div style="
            background: linear-gradient(145deg, #1e1108 0%, #271609 50%, #1a0e07 100%);
            border: 1px solid rgba(180, 110, 30, 0.35);
            border-radius: 20px;
            padding: 40px 44px 36px;
            box-shadow: 0 25px 60px rgba(0,0,0,0.55), inset 0 1px 0 rgba(245,158,11,0.08);
            max-width: 860px;
            margin: 0 auto;
        ">
            <!-- Badge Autoridade -->
            <div class="flex justify-center mb-8">
                <div style="
                    display: inline-flex;
                    align-items: center;
                    gap: 8px;
                    background: linear-gradient(90deg, rgba(180,83,9,0.25), rgba(245,158,11,0.15));
                    border: 1px solid rgba(245,158,11,0.30);
                    padding: 6px 18px;
                    border-radius: 9999px;
                ">
                    <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87L18.18 21 12 17.77 5.82 21 7 14.14l-5-4.87 6.91-1.01z"/></svg>
                    <span style="color:#f59e0b; font-size:11px; font-weight:800; letter-spacing:1.5px; text-transform:uppercase;">Método Completo para Iniciantes</span>
                </div>
            </div>

            <!-- Lista em 2 colunas -->
            <ul style="
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 16px 32px;
                list-style: none;
                padding: 0;
                margin: 0 0 32px 0;
            " class="learning-list">
                <li style="display:flex;align-items:flex-start;gap:12px;">
                    <svg xmlns="http://www.w3.org/2000/svg" style="width:20px;height:20px;flex-shrink:0;margin-top:2px;filter:drop-shadow(0 0 6px rgba(34,197,94,0.45));" fill="none" viewBox="0 0 24 24" stroke="#22c55e" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                    <span style="color:#f5f5f5;font-size:15px;font-weight:600;line-height:1.5;"><strong style="color:#fff;">Acordes Essenciais</strong> da Viola Caipira</span>
                </li>
                <li style="display:flex;align-items:flex-start;gap:12px;">
                    <svg xmlns="http://www.w3.org/2000/svg" style="width:20px;height:20px;flex-shrink:0;margin-top:2px;filter:drop-shadow(0 0 6px rgba(34,197,94,0.45));" fill="none" viewBox="0 0 24 24" stroke="#22c55e" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                    <span style="color:#f5f5f5;font-size:15px;font-weight:600;line-height:1.5;"><strong style="color:#fff;">Ritmos e Batidas</strong> Fundamentais</span>
                </li>
                <li style="display:flex;align-items:flex-start;gap:12px;">
                    <svg xmlns="http://www.w3.org/2000/svg" style="width:20px;height:20px;flex-shrink:0;margin-top:2px;filter:drop-shadow(0 0 6px rgba(34,197,94,0.45));" fill="none" viewBox="0 0 24 24" stroke="#22c55e" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                    <span style="color:#fbbf24;font-size:15px;font-weight:700;line-height:1.5;"><strong>Primeiras Músicas</strong> Passo a Passo</span>
                </li>
                <li style="display:flex;align-items:flex-start;gap:12px;">
                    <svg xmlns="http://www.w3.org/2000/svg" style="width:20px;height:20px;flex-shrink:0;margin-top:2px;filter:drop-shadow(0 0 6px rgba(34,197,94,0.45));" fill="none" viewBox="0 0 24 24" stroke="#22c55e" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                    <span style="color:#f5f5f5;font-size:15px;font-weight:600;line-height:1.5;"><strong style="color:#fff;">Exercícios Práticos</strong> para Evolução Rápida</span>
                </li>
                <li style="display:flex;align-items:flex-start;gap:12px;">
                    <svg xmlns="http://www.w3.org/2000/svg" style="width:20px;height:20px;flex-shrink:0;margin-top:2px;filter:drop-shadow(0 0 6px rgba(34,197,94,0.45));" fill="none" viewBox="0 0 24 24" stroke="#22c55e" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                    <span style="color:#f5f5f5;font-size:15px;font-weight:600;line-height:1.5;">Cifras Simplificadas dos <strong style="color:#fff;">Modões Mais Tocados</strong></span>
                </li>
                <li style="display:flex;align-items:flex-start;gap:12px;">
                    <svg xmlns="http://www.w3.org/2000/svg" style="width:20px;height:20px;flex-shrink:0;margin-top:2px;filter:drop-shadow(0 0 6px rgba(34,197,94,0.45));" fill="none" viewBox="0 0 24 24" stroke="#22c55e" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                    <span style="color:#fbbf24;font-size:15px;font-weight:700;line-height:1.5;"><strong>Repertório Sertanejo</strong> Raiz e Universitário</span>
                </li>
                <li style="display:flex;align-items:flex-start;gap:12px;grid-column:1/-1;justify-content:center;">
                    <svg xmlns="http://www.w3.org/2000/svg" style="width:20px;height:20px;flex-shrink:0;margin-top:2px;filter:drop-shadow(0 0 6px rgba(34,197,94,0.45));" fill="none" viewBox="0 0 24 24" stroke="#22c55e" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                    <span style="color:#f5f5f5;font-size:15px;font-weight:600;line-height:1.5;">Seleção de <strong style="color:#fff;">Músicas Gospel</strong> Adaptadas para Viola</span>
                </li>
            </ul>

            <!-- Mobile: lista em coluna única -->
            <style>
                @media (max-width: 640px) {
                    .learning-list { grid-template-columns: 1fr !important; }
                    .learning-list li:last-child { grid-column: unset !important; justify-content: flex-start !important; }
                    #o-que-vai-aprender .premium-card { padding: 28px 20px 24px !important; }
                }
            </style>

            <!-- Rodapé de impacto -->
            <div style="
                border-top: 1px solid rgba(180,110,30,0.25);
                margin-top: 4px;
                padding-top: 24px;
                text-align: center;
                background: linear-gradient(90deg, transparent, rgba(180,83,9,0.08), transparent);
                border-radius: 0 0 12px 12px;
                padding-left: 8px;
                padding-right: 8px;
            ">
                <p style="color:#f5f5f5; font-size:16px; font-weight:700; line-height:1.6; max-width:540px; margin:0 auto;">
                    "Tudo estruturado para você sair do zero e <span style="color:#fbbf24;">tocar com segurança</span> desde as primeiras aulas"
                </p>
            </div>
        </div>

    </div>
</section>'''

html = html[:match.start()] + new_section + html[match.end():]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Done!")
