import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

old_pattern = r'<section id="faq".*?</section>'
match = re.search(old_pattern, html, flags=re.DOTALL)
if not match:
    print("FAQ section not found!")
    exit()

# Build the 11 FAQ items as a list of (question, answer)
faqs = [
    ("Eu nunca toquei nada, vou conseguir aprender?",
     "Sim. O método foi feito para iniciantes absolutos. Você começa do zero e evolui passo a passo, sem dificuldade."),
    ("Preciso já ter uma viola?",
     "Sim, você precisa de uma viola caipira para praticar. Qualquer modelo básico já é suficiente para começar."),
    ("Em quanto tempo vou conseguir tocar alguma coisa?",
     "Seguindo o método corretamente, você já consegue tocar suas primeiras músicas simples em poucos dias."),
    ("As aulas são difíceis?",
     "Não. O método é direto e prático, sem teoria complicada. Tudo é explicado de forma simples."),
    ("Eu preciso saber ler partitura?",
     "Não. Você não precisa de partitura. O método ensina de forma prática, fácil de entender."),
    ("O acesso é vitalício?",
     "Sim. Você paga uma única vez e pode acessar o conteúdo quando quiser."),
    ("Posso assistir pelo celular?",
     "Sim. Você pode acessar pelo celular, computador ou tablet, onde quiser."),
    ("Vou aprender músicas de verdade?",
     "Sim. Você aprende com exemplos reais, incluindo modões e estilos populares."),
    ("Tem suporte se eu tiver dúvidas?",
     "Sim. Você terá suporte para te ajudar durante o aprendizado."),
    ("E se eu não gostar?",
     "Você tem garantia de 7 dias. Se não gostar, pode pedir seu dinheiro de volta."),
]


# Generate items with 100% inline CSS
def faq_item(idx, q, a):
    return f'''
                <div class="faq-item" id="faq-{idx}" style="
                    width: 100%;
                    box-sizing: border-box;
                    background: #1c110a;
                    border: 1px solid rgba(180,110,30,0.25);
                    border-radius: 14px;
                    overflow: hidden;
                    margin-bottom: 12px;
                ">
                    <button onclick="toggleFaq({idx})" style="
                        width: 100%;
                        display: flex;
                        align-items: center;
                        justify-content: space-between;
                        gap: 16px;
                        padding: 16px 20px;
                        background: transparent;
                        border: none;
                        cursor: pointer;
                        text-align: left;
                        box-sizing: border-box;
                    ">
                        <span style="
                            color: #ffffff;
                            font-size: 15px;
                            font-weight: 600;
                            line-height: 1.5;
                            flex: 1;
                        ">{q}</span>
                        <svg id="arrow-{idx}" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;transition:transform 0.3s ease;"><path d="m6 9 6 6 6-6"/></svg>
                    </button>
                    <div id="panel-{idx}" style="
                        display: none;
                        padding: 0 20px 18px;
                        box-sizing: border-box;
                    ">
                        <p style="
                            color: #c9c9c9;
                            font-size: 14px;
                            line-height: 1.7;
                            margin: 0;
                        ">{a}</p>
                    </div>
                </div>'''

items_html = "".join(faq_item(i, q, a) for i, (q, a) in enumerate(faqs))

new_section = f'''<section id="faq" style="
    padding: 64px 16px;
    background: linear-gradient(180deg,#0d0705 0%,#130c09 100%);
    position: relative;
    overflow: hidden;
">
    <!-- Ambient glow -->
    <div style="position:absolute;top:0;left:50%;transform:translateX(-50%);width:500px;height:200px;background:radial-gradient(ellipse,rgba(180,83,9,0.09) 0%,transparent 70%);pointer-events:none;"></div>

    <div style="position:relative;z-index:10;max-width:680px;margin:0 auto;width:100%;box-sizing:border-box;">

        <!-- Heading -->
        <div style="text-align:center;margin-bottom:36px;">
            <h2 style="color:#ffffff;font-size:clamp(22px,5.5vw,32px);font-weight:900;margin:0 0 8px;">
                DÚVIDAS <span style="color:#f59e0b;">FREQUENTES</span>
            </h2>
            <p style="color:#6b7280;font-size:14px;margin:0;">Respostas rápidas para as perguntas mais comuns</p>
        </div>

        <!-- FAQ Items -->
        <div style="width:100%;box-sizing:border-box;">
{items_html}
        </div>

        <!-- Frase de reforço -->
        <div style="text-align:center;margin-top:32px;">
            <p style="color:#9ca3af;font-size:14px;line-height:1.7;margin:0;">
                Ainda com dúvida? Você pode testar sem risco.<br/>
                <strong style="color:#ffffff;">Sua compra está 100% protegida.</strong>
            </p>
        </div>

    </div>

    <script>
        function toggleFaq(idx) {{
            var panel = document.getElementById('panel-' + idx);
            var arrow = document.getElementById('arrow-' + idx);
            var item  = document.getElementById('faq-' + idx);
            var open  = panel.style.display !== 'none';

            // close all
            for (var i = 0; i < 10; i++) {{
                var p = document.getElementById('panel-' + i);
                var a = document.getElementById('arrow-' + i);
                var it = document.getElementById('faq-' + i);
                if (p) p.style.display = 'none';
                if (a) a.style.transform = 'rotate(0deg)';
                if (it) it.style.border = '1px solid rgba(180,110,30,0.25)';
            }}

            if (!open) {{
                panel.style.display = 'block';
                arrow.style.transform = 'rotate(180deg)';
                item.style.border = '1px solid rgba(245,158,11,0.55)';
                item.style.boxShadow = '0 0 20px rgba(180,83,9,0.12)';
            }}
        }}
    </script>
</section>'''

html = html[:match.start()] + new_section + html[match.end():]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Done!")
