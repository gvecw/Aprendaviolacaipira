import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Current HTML snippet to replace
old_wrapper = '''<div class="relative z-10 px-4 max-w-7xl mx-auto flex flex-col lg:flex-row items-center justify-between gap-12 lg:gap-8 pt-8">
				<!-- LADO ESQUERDO: TEXTOS -->
				<div class="w-full lg:w-[55%] flex flex-col items-center lg:items-start text-center lg:text-left">'''

new_wrapper = '''<style>
    .hero-layout {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
        gap: 2rem;
        max-width: 1280px;
        margin: 0 auto;
    }
    .hero-text-col {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    .hero-img-col {
        width: 100%;
        display: flex;
        justify-content: center;
        position: relative;
        margin-top: 2rem;
    }
    .levita-box {
        position: relative;
        width: 65%;
        max-width: 500px;
        animation: floatMockup 6s ease-in-out infinite;
    }
    @media (min-width: 1024px) {
        .hero-layout {
            flex-direction: row;
            gap: 2rem;
        }
        .hero-text-col {
            width: 55%;
            align-items: flex-start;
            text-align: left;
        }
        .hero-img-col {
            width: 40%;
            margin-top: 0;
            justify-content: center;
        }
        .levita-box {
            width: 100%;
        }
    }
    /* We need to override utility classes inside text col that force centering */
    @media (min-width: 1024px) {
        .hero-text-col > p, .hero-text-col > h1 {
            margin-left: 0 !important;
            margin-right: 0 !important;
        }
        .hero-text-col > .flex-col {
            justify-content: flex-start;
            align-items: flex-start;
        }
    }
</style>
<div class="hero-layout relative z-10 px-4 pt-8">
				<!-- LADO ESQUERDO: TEXTOS -->
				<div class="hero-text-col">'''

html = html.replace(old_wrapper, new_wrapper)

old_img_col = '''<!-- LADO DIREITO: MOCKUP -->
				<div class="w-full lg:w-[40%] flex justify-center relative mt-8 lg:mt-0">'''
new_img_col = '''<!-- LADO DIREITO: MOCKUP -->
				<div class="hero-img-col">'''

html = html.replace(old_img_col, new_img_col)

old_levita = '''<div class="relative w-[65%] sm:w-[55%] lg:w-full max-w-[500px]" style="animation: floatMockup 6s ease-in-out infinite;">'''
new_levita = '''<div class="levita-box">'''

html = html.replace(old_levita, new_levita)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
