import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# I will find the part from <style> hero-layout ... until the end of the hero section.
# The section starts with: <section class="relative min-h-[85vh] flex...
# Wait, my previous code replaced a div inside it.
# Let's find the entire <section class="relative min-h-[85vh] ... > until the next section.
start_str = '<section class="relative min-h-[85vh] flex items-center justify-center py-12 px-4">'
# The next section starts with: <section class="relative py-20 px-4 overflow-hidden">
try:
    start_idx = html.index(start_str)
    end_str = '<section class="relative py-20 px-4 overflow-hidden">'
    end_idx = html.index(end_str, start_idx)
    
    # We will replace the entire first fold section.
    old_hero = html[start_idx:end_idx]
    
    new_hero = """<section class="relative min-h-[100svh] flex flex-col justify-center items-center py-12 md:py-16 px-4 overflow-hidden">
    <!-- Fundo Original (MANTIDO) -->
    <div class="absolute inset-0">
        <img src="Gemini_Generated_Image_kd9ic8kd9ic8kd9i.png" class="w-full h-full object-cover" alt="" />
    </div>
    <!-- Alteração 1: Overlay um pouco mais escuro para garantir contraste na UI central -->
    <div class="absolute inset-0" style="background-color: rgba(0,0,0,0.85);"></div>
    <div class="absolute inset-0 bg-gradient-to-b from-[#2d1810] via-[#1a0f0a] to-[#0d0705]" style="opacity: 0.85;"></div>
    
    <!-- Efeitos de Luz no Fundo -->
    <div class="absolute inset-0 opacity-20 flex justify-center items-center pointer-events-none">
        <div class="w-[300px] h-[300px] bg-amber-600 rounded-full blur-[120px] absolute -top-10"></div>
        <div class="w-[400px] h-[400px] bg-orange-700 rounded-full blur-[150px] absolute bottom-0"></div>
    </div>

    <!-- Novo Estilo Inline pra garantir que o celular renderize perfeito ignorando Tailwind Ausente -->
    <style>
        .hero-container {
            position: relative;
            z-index: 10;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            width: 100%;
            max-width: 800px;
            margin: 0 auto;
            padding-top: 2rem;
        }
        
        .badge {
            display: inline-block;
            background: linear-gradient(to right, #f59e0b, #f97316);
            color: #fff;
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-weight: 700;
            padding: 6px 16px;
            border-radius: 9999px;
            margin-bottom: 1rem;
        }

        .headline {
            font-size: clamp(34px, 8vw, 64px); 
            line-height: 1.05;
            font-weight: 900;
            margin-bottom: 2rem;
            color: #fff;
            text-shadow: 0 4px 20px rgba(0,0,0,0.5);
        }
        .headline-yellow {
            color: #fbbf24;
        }

        /* Mockup */
        .mockup-wrapper {
            position: relative;
            width: 55%; /* 50% requested, added slightly more to account for max-widths */
            max-width: 320px;
            margin: 0 auto 2.5rem auto;
            animation: levitate 5s ease-in-out infinite;
        }
        .mockup-img {
            width: 100%;
            height: auto;
            display: block;
            transform: rotate(1.5deg);
            filter: drop-shadow(0 25px 25px rgba(0,0,0,0.35));
        }
        .mockup-floor-shadow {
            position: absolute;
            bottom: -15px;
            left: 50%;
            transform: translateX(-50%);
            width: 80%;
            height: 15px;
            background: rgba(0,0,0,0.5);
            filter: blur(12px);
            border-radius: 50%;
            z-index: -1;
        }

        @keyframes levitate {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-12px); }
        }

        .sub-headline {
            font-size: clamp(16px, 4vw, 20px);
            color: rgba(255, 255, 255, 0.85);
            line-height: 1.5;
            margin-bottom: 2rem;
            max-width: 480px;
        }

        .benefits-list {
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
            margin-bottom: 2.5rem;
            font-size: clamp(15px, 4vw, 18px);
            color: #fff;
            align-items: center;
        }
        .benefit-item {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .benefit-icon {
            color: #22c55e;
            width: 22px;
            height: 22px;
            flex-shrink: 0;
            stroke-width: 3px;
        }

        .cta-button {
            display: inline-block;
            background: linear-gradient(to right, #f59e0b, #ea580c);
            color: #fff;
            font-weight: 900;
            font-size: clamp(22px, 6vw, 30px);
            padding: 20px 40px;
            border-radius: 9999px;
            text-decoration: none;
            box-shadow: 0 15px 35px rgba(234, 88, 12, 0.4);
            transition: all 0.3s ease;
            width: 100%;
            max-width: 400px;
            letter-spacing: 0.5px;
        }
        .cta-button:active {
            transform: scale(0.97);
        }

        .microcopy {
            font-size: 13px;
            color: rgba(255, 255, 255, 0.6);
            margin-top: 1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }

        /* Desktop Adjustments to prevent ridiculous sizes */
        @media (min-width: 768px) {
            .hero-container { padding-top: 6rem; }
            .benefits-list { flex-direction: row; gap: 2rem; }
        }
        @media (max-height: 750px) {
            .hero-container { padding-top: 3rem; }
            .headline { margin-bottom: 1.5rem; }
            .mockup-wrapper { width: 45%; margin-bottom: 1.5rem; }
            .sub-headline { margin-bottom: 1.5rem; font-size: 15px; }
            .benefits-list { margin-bottom: 2rem; gap: 0.5rem; }
            .cta-button { padding: 16px 32px; font-size: 20px; }
        }
    </style>

    <div class="hero-container">
        <!-- BADGE superior -->
        <span class="badge">VIOLA CAIPIRA DO ZERO</span>

        <!-- HEADLINE: 2 linhas, peso extra bold, centralizada -->
        <h1 class="headline">
            <span class="headline-yellow">APRENDA VIOLA</span><br/>
            <span>DO ZERO</span>
        </h1>

        <!-- MOCKUP: Abaixo da headline, centro, 50% mobile, levitação, sombra. -->
        <div class="mockup-wrapper">
            <div class="mockup-floor-shadow"></div>
            <!-- Brilho Atrás -->
            <div style="position:absolute; inset:0; background:radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%); z-index:-1; transform:scale(1.5);"></div>
            <img src="mockup-viola.png" alt="Livro Viola Caipira do Zero" class="mockup-img" />
        </div>

        <!-- SUBHEADLINE: Branco transparente, line height alto, centrado -->
        <p class="sub-headline">
            Comece a tocar suas primeiras músicas, mesmo sem experiência
        </p>

        <!-- BENEFITS: Cor forte, espaçadas -->
        <div class="benefits-list">
            <span class="benefit-item">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" class="benefit-icon">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M20 6L9 17l-5-5" />
                </svg>
                Método simples
            </span>
            <span class="benefit-item">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" class="benefit-icon">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M20 6L9 17l-5-5" />
                </svg>
                Sem teoria complicada
            </span>
            <span class="benefit-item">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" class="benefit-icon">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M20 6L9 17l-5-5" />
                </svg>
                Comece do zero
            </span>
        </div>

        <!-- CTA: Altura e fonte maiores, sombra, bordas full rounded -->
        <a href="#oferta-premium" onclick="document.getElementById('oferta-premium').scrollIntoView({behavior: 'smooth'}); return false;" class="cta-button">
            COMEÇAR AGORA
        </a>

        <!-- MICROCOPY: -->
        <p class="microcopy">
            ⬇️ Toque para ver como funciona ⬇️
        </p>
    </div>
</section>
"""
    html = html[:start_idx] + new_hero + html[end_idx:]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Sucesso!")
except Exception as e:
    print("Erro:", e)
