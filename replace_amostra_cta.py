import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# The button in question
old_btn_regex = r'<div class="flex justify-center mt-8 md:mt-12">\s*<a[^>]*>VER\s*OPÇÕES DE ACESSO</a>\s*</div>'

# Ensure we use exactly the correct styling requested
new_cta_html = '''<div class="flex flex-col items-center justify-center mt-6 md:mt-10">
                    <a href="#oferta-premium" onclick="document.getElementById('oferta-premium').scrollIntoView({behavior: 'smooth'}); return false;" class="inline-block bg-gradient-to-r from-[#f59e0b] to-[#ea580c] text-white font-black text-lg md:text-xl px-8 py-4 rounded-full shadow-[0_10px_25px_rgba(234,88,12,0.3)] transition-all duration-300 hover:scale-[1.02] active:scale-95 text-center">
                        QUERO APRENDER A TOCAR ASSIM
                    </a>
                    <p class="text-gray-400 text-[13px] font-medium mt-3 flex items-center justify-center gap-1">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-4 h-4"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        Mesmo começando do zero
                    </p>
                </div>'''

# Replace
if re.search(old_btn_regex, html, flags=re.IGNORECASE | re.DOTALL):
    html = re.sub(old_btn_regex, new_cta_html, html, flags=re.IGNORECASE | re.DOTALL)
else:
    print("Warning: old button not found, searching just for text")
    # Tries generalized replacement if the above fails
    html = re.sub(r'<div[^>]*>\s*<a[^>]*>VER\s*OP(Ç|&Ccedil;|&#199;)ÕES DE ACESSO</a>\s*</div>', new_cta_html, html, flags=re.IGNORECASE | re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("done")
