import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# I will find the exact bounds of the audio section bottom half.
# Look for '<!-- End Carousel -->'
start_idx = html.find('<!-- End Carousel -->')
if start_idx != -1:
    # Find the next </section> after this
    end_idx = html.find('</section>', start_idx)
    
    if end_idx != -1:
        # The new content that should sit under the carousel.
        # It should ONLY be the CTA button, as requested.
        new_bottom_html = '''<!-- End Carousel -->
                <div class="flex flex-col items-center justify-center mt-12 mb-8">
                    <a href="#oferta-premium" onclick="document.getElementById('oferta-premium').scrollIntoView({behavior: 'smooth'}); return false;" class="inline-block bg-gradient-to-r from-[#f97316] to-[#ea580c] text-white font-black text-lg px-8 py-3.5 rounded-[30px] shadow-[0_8px_20px_rgba(234,88,12,0.3)] transition-all duration-300 active:scale-95 text-center w-[90%] max-w-[350px]">
                        QUERO APRENDER A TOCAR ASSIM
                    </a>
                    <p class="text-gray-400 text-[13px] font-medium mt-3 flex items-center justify-center gap-1.5">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="w-4 h-4"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        Mesmo começando do zero
                    </p>
                </div>
            </div>
        '''
        
        # Replace the entire segment
        html = html[:start_idx] + new_bottom_html + html[end_idx:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Done")
