import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Find the section from id="ofertas" to the closing of </div> that wraps
# the old VIP block (before "Escolha sua opção de acesso")
ofertas_start = html.find('section id="ofertas"')
if ofertas_start == -1:
    print("Section not found"); exit()

# Find the inner div that wraps everything
inner_div_start = html.find('<div class="max-w-lg mx-auto lg:mx-0">', ofertas_start)
# Find the heading "Escolha sua opção de acesso" — that's where the old block ends
escolha_header = html.find('Escolha sua', ofertas_start)
# Find the closing </div> just before "Escolha sua"
end_of_bonus_block = html.rfind('</div>', inner_div_start, escolha_header) + len('</div>')

# The old bonus block is between inner_div_start and end_of_bonus_block
old_block = html[inner_div_start:end_of_bonus_block]
print(f"Old block ({len(old_block)} chars):\n{old_block[:200]}...")

new_block = '''<div class="max-w-lg mx-auto lg:mx-0">

			<div style="text-align:center; margin-bottom:28px;">
				<h4 style="color:#f59e0b; font-weight:800; font-size:15px; text-transform:uppercase; letter-spacing:1.5px; margin:0 0 10px;">
					🎁 VOCÊ NÃO RECEBE SÓ O MÉTODO…
				</h4>
				<h2 style="color:#ffffff; font-weight:900; font-size:clamp(20px,5vw,28px); margin:0; line-height:1.35;">
					Você leva um pacote completo para<br/>acelerar seu aprendizado na viola caipira
				</h2>
			</div>

			<div style="text-align:center; margin:0 auto 28px;">
				<img src="bonuses-viola.png" alt="Materiais bônus Viola Caipira"
					style="width:100%; max-width:380px; height:auto; display:block; margin:0 auto; border-radius:10px; filter:drop-shadow(0 20px 40px rgba(0,0,0,0.60)) drop-shadow(0 4px 12px rgba(180,83,9,0.30));" />
			</div>

			<div style="max-width:400px; margin:0 auto 28px;">
				<ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:13px;">
					<li style="display:flex;align-items:center;gap:12px;color:#f0f0f0;font-size:15px;font-weight:600;line-height:1.4;">
						<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><path d="M20 6 9 17l-5-5"/></svg>
						Mini dicionário de acordes da viola caipira
					</li>
					<li style="display:flex;align-items:center;gap:12px;color:#f0f0f0;font-size:15px;font-weight:600;line-height:1.4;">
						<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><path d="M20 6 9 17l-5-5"/></svg>
						Modões com cifras e tablaturas
					</li>
					<li style="display:flex;align-items:center;gap:12px;color:#f0f0f0;font-size:15px;font-weight:600;line-height:1.4;">
						<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><path d="M20 6 9 17l-5-5"/></svg>
						Repertório sertanejo raiz e universitário
					</li>
					<li style="display:flex;align-items:center;gap:12px;color:#f0f0f0;font-size:15px;font-weight:600;line-height:1.4;">
						<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><path d="M20 6 9 17l-5-5"/></svg>
						Músicas gospel adaptadas para viola
					</li>
					<li style="display:flex;align-items:center;gap:12px;color:#f0f0f0;font-size:15px;font-weight:600;line-height:1.4;">
						<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><path d="M20 6 9 17l-5-5"/></svg>
						Material organizado para estudo prático
					</li>
				</ul>
			</div>

			<div style="text-align:center; padding:16px 20px; background:linear-gradient(90deg,rgba(180,83,9,0.10),rgba(245,158,11,0.08),rgba(180,83,9,0.10)); border-radius:10px; border:1px solid rgba(245,158,11,0.18); max-width:400px; margin:0 auto 36px;">
				<p style="color:#fbbf24; font-weight:800; font-size:14px; margin:0; line-height:1.55;">
					"Tudo pronto pra você sair do zero e começar a tocar de verdade"
				</p>
			</div>'''

html = html[:inner_div_start] + new_block + html[end_of_bonus_block:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Done!")
