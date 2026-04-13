import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. NEW TOP TEXT (Replacing Badge)
html = re.sub(
    r'<span class="badge">.*?</span>',
    '<p class="pre-headline">Você sempre quis tocar viola, mas nunca soube por onde começar?</p>',
    html,
    flags=re.DOTALL
)

# Insert CSS for pre-headline and adjust top padding
html = re.sub(
    r'\.hero-container \{[\s\S]*?\}',
    '''.hero-container {
            position: relative;
            z-index: 10;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            width: 100%;
            max-width: 800px;
            margin: 0 auto;
            padding-top: 1.5rem; /* Reduced from 2rem */
        }''',
    html
)

html = re.sub(
    r'\.badge \{[\s\S]*?\}',
    '''.pre-headline {
            font-size: clamp(12px, 3.5vw, 15px);
            color: rgba(255, 255, 255, 0.75);
            font-weight: 500;
            margin-bottom: 0.5rem;
            max-width: 90%;
        }''',
    html
)

# 2. HEADLINE
html = re.sub(
    r'<h1 class="headline">[\s\S]*?</h1>',
    '''<h1 class="headline">
            <span class="headline-yellow">APRENDA VIOLA DO ZERO</span><br/>
            <span class="headline-heavy">E COMECE A TOCAR DE VERDADE</span>
        </h1>''',
    html
)

html = re.sub(
    r'\.headline \{[\s\S]*?text-shadow:.*?\}',
    '''.headline {
            font-size: clamp(28px, 6.5vw, 56px); 
            line-height: 1.0; /* Reduced from 1.05 */
            font-weight: 800; /* Less heavy for top line */
            margin-bottom: 0.75rem; /* Brought Mockup Closer */
            color: #fff;
            text-shadow: 0 4px 20px rgba(0,0,0,0.5);
        }
        .headline-heavy {
            font-weight: 900;
            font-size: clamp(30px, 7vw, 60px); /* Slightly larger */
        }''',
    html
)

# 3. MOCKUP ADJUSTMENT
html = re.sub(
    r'\.mockup-wrapper \{([\s\S]*?)width: 55%;([\s\S]*?)margin: 0 auto 2\.5rem auto;',
    r'.mockup-wrapper {\1width: 60%;\2margin: 0 auto 1.5rem auto;',
    html
)
html = re.sub(
    r'\.mockup-wrapper \{ width: 45%; margin-bottom: 1\.5rem; \}',
    r'.mockup-wrapper { width: 50%; margin-bottom: 1rem; }',
    html
)

# 4. SUB-HEADLINE
html = re.sub(
    r'<p class="sub-headline">[\s\S]*?</p>',
    '''<p class="sub-headline">
            Mesmo sem experiência, você já pode tocar suas primeiras músicas em poucos dias
        </p>''',
    html
)
html = re.sub(
    r'\.sub-headline \{([\s\S]*?)font-size: clamp\(16px, 4vw, 20px\);([\s\S]*?)margin-bottom: 2rem;',
    r'.sub-headline {\1font-size: clamp(17px, 4.5vw, 22px);\2margin-bottom: 1.5rem;',
    html
)

# 5. BENEFITS
old_benefits = '''<div class="benefits-list">
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
        </div>'''
new_benefits = '''<div class="benefits-list">
            <span class="benefit-item">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" class="benefit-icon">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M20 6L9 17l-5-5" />
                </svg>
                Método simples e direto
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
                Comece mesmo do zero
            </span>
        </div>'''
html = html.replace(old_benefits, new_benefits)

# Shrink bottom margins to make it compact
html = re.sub(
    r'\.benefits-list \{([\s\S]*?)margin-bottom: 2\.5rem;',
    r'.benefits-list {\1margin-bottom: 1.5rem;',
    html
)

# 6. CTA TEXT
html = html.replace('COMEÇAR AGORA\n        </a>', 'QUERO COMEÇAR AGORA\n        </a>')

# Global mobile padding reduction
html = re.sub(
    r'<section class="relative min-h-\[100svh\] flex flex-col justify-center items-center py-12 md:py-16 px-4 overflow-hidden">',
    '<section class="relative min-h-[100svh] flex flex-col justify-center items-center py-8 md:py-12 px-4 overflow-hidden">',
    html
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("done")
