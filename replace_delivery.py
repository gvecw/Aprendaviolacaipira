import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Main Title
html = re.sub(
    r'<h2 class="text-3xl md:text-4xl font-black text-center mb-4 text-white">COMO <span class="text-amber-500">VOC.*? VAI RECEBER SEU MOD.O:</span></h2>',
    r'<h2 class="text-3xl md:text-4xl font-black text-center mb-4 text-white">Como você vai <span class="text-amber-500">receber seu acesso:</span></h2>',
    html, flags=re.DOTALL
)

# 2. Main Subtitle
html = re.sub(
    r'<p class="text-gray-300 text-center mb-12 text-lg">Pr.*?tico, r.*?pido e do jeito que a gente gosta\.</p>',
    r'<p class="text-gray-300 text-center mb-12 text-lg">Rápido, simples e direto ao ponto</p>',
    html, flags=re.DOTALL
)

# 3. Step 1
html = re.sub(
    r'<h3 class="text-xl font-bold mb-2 text-amber-500">LIBERA..O IMEDIATA</h3>',
    r'<h3 class="text-xl font-bold mb-2 text-amber-500">Acesso imediato</h3>',
    html, flags=re.DOTALL
)
html = re.sub(
    r'<p class="text-gray-300 text-base">Fa.*a seu pedido com seguran.a total.*?Sem dor de cabe.a\.</p>',
    r'<p class="text-gray-300 text-base">Após a confirmação do pagamento, seu acesso é liberado automaticamente.</p>',
    html, flags=re.DOTALL
)

# 4. Step 2
html = re.sub(
    r'<h3 class="text-xl font-bold mb-2 text-amber-500">CHEGA NO ZAP E E-MAIL</h3>',
    r'<h3 class="text-xl font-bold mb-2 text-amber-500">Receba no seu e-mail</h3>',
    html, flags=re.DOTALL
)
html = re.sub(
    r'<p class="text-gray-300 text-base">Voc.* recebe o link instantaneamente por WhatsApp e e-mail.*? baixar\.</p>',
    r'<p class="text-gray-300 text-base">Você receberá o link de acesso direto para o conteúdo, pronto para começar.</p>',
    html, flags=re.DOTALL
)

# 5. Step 3
html = re.sub(
    r'<h3 class="text-xl font-bold mb-2 text-amber-500">PLUGOU, TOCOU</h3>',
    r'<h3 class="text-xl font-bold mb-2 text-amber-500">Comece a aprender</h3>',
    html, flags=re.DOTALL
)
html = re.sub(
    r'<p class="text-gray-300 text-base">Copie pro seu pendrive, plugue no r.*?dio.*?Sem mist.*?rio\.</p>',
    r'<p class="text-gray-300 text-base">Acesse pelo celular ou computador e comece suas aulas imediatamente.</p>',
    html, flags=re.DOTALL
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Done")
