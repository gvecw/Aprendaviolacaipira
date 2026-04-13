import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Title
html = html.replace(
    'As vantagens de <span\n\n\t\t\t\t\t\t\tclass="text-amber-400">garantir seu acesso hoje</span>',
    'As vantagens de <span\n\n\t\t\t\t\t\t\tclass="text-amber-400">começar na viola hoje</span>'
)
# Case where line breaks differ
html = re.sub(
    r'As vantagens de <span[^>]*>garantir seu acesso hoje</span>',
    'As vantagens de <span class="text-amber-400">começar na viola hoje</span>',
    html
)

# 2. Subtitle
html = html.replace(
    'Tudo pronto pra você baixar, copiar pro pendrive e\n\n\t\t\t\t\t\tcurtir',
    'Um método simples pra quem nunca tocou nada'
)
html = re.sub(
    r'Tudo pronto pra você baixar, copiar pro pendrive[^<]*curtir',
    'Um método simples pra quem nunca tocou nada',
    html
)

# 3. Card 1
html = html.replace('Funciona Offline', 'Feito para iniciantes')
html = re.sub(
    r'Ouça no carro ou na\n\n\t\t\t\t\t\t\t\t\testrada sem precisar de sinal',
    r'Mesmo sem experiência, você consegue começar',
    html
)
html = re.sub(
    r'Ouça no carro ou na estrada sem precisar de sinal',
    r'Mesmo sem experiência, você consegue começar',
    html
)

# 4. Card 2
html = html.replace('Zero Propaganda', 'Método simples e direto')
html = re.sub(
    r'Nenhum anúncio\n\n\t\t\t\t\t\t\t\t\tinterrompendo suas músicas favoritas',
    r'Sem teoria complicada ou enrolação',
    html
)
html = re.sub(
    r'Nenhum anúncio interrompendo suas músicas favoritas',
    r'Sem teoria complicada ou enrolação',
    html
)

# 5. Card 3
html = html.replace('Sem Mensalidade', 'Passo a passo completo')
html = re.sub(
    r'Pague uma vez só e use pra\n\n\t\t\t\t\t\t\t\t\tsempre',
    r'Você aprende na ordem certa, sem travar',
    html
)
html = re.sub(
    r'Pague uma vez só e use pra sempre',
    r'Você aprende na ordem certa, sem travar',
    html
)

# 6. Card 4
html = html.replace('Pronto pro Pendrive', 'Aprenda no seu ritmo')
html = re.sub(
    r'Arquivos organizados, é só\n\n\t\t\t\t\t\t\t\t\tcopiar e usar',
    r'Sem pressão, no seu tempo',
    html
)
html = re.sub(
    r'Arquivos organizados, é só copiar e usar',
    r'Sem pressão, no seu tempo',
    html
)

# 7. Card 5
html = html.replace('Compatível com Tudo', 'Acesso pelo celular')
html = re.sub(
    r'Funciona no carro, TV,\n\n\t\t\t\t\t\t\t\t\tmultimídia e caixa de som',
    r'Estude de onde quiser, quando quiser',
    html
)
html = re.sub(r'Funciona no carro, TV, multimídia e caixa de som', 'Estude de onde quiser, quando quiser', html)

# 8. Card 6
html = html.replace('Acesso Imediato', 'Comece hoje mesmo')
html = re.sub(
    r'Link de download liberado\n\n\t\t\t\t\t\t\t\t\tna hora após a compra',
    r'Acesso liberado logo após a compra',
    html
)
html = re.sub(r'Link de download liberado na hora após a compra', 'Acesso liberado logo após a compra', html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Done")
