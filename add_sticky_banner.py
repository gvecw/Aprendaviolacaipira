import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. REMOVE PRE-HEADLINE
html = re.sub(
    r'<p class="pre-headline">Você sempre quis.*?<\/p>',
    '',
    html,
    flags=re.DOTALL
)
# Remove the pre-headline CSS
html = re.sub(
    r'\.pre-headline \{[\s\S]*?\}',
    '',
    html
)

# 2. REMOVE PREVIOUS TIMER CONTAINER
html = re.sub(
    r'<div class="timer-container">[\s\S]*?Liberação imediata após a compra[\s\S]*?<\/div>',
    '',
    html
)

# Replace the previous JS snippet with the new one for the sticky timer targeting id "sticky-timer"
old_js = '''<script>
    // Timer Countdown Logic
    document.addEventListener("DOMContentLoaded", function() {
        var duration = 14 * 60 + 32; // 14 minutes and 32 seconds
        var displayHours = document.getElementById('t-hours');
        var displayMinutes = document.getElementById('t-minutes');
        var displaySeconds = document.getElementById('t-seconds');
        
        // Optional: Save start time in localStorage to persist across refreshes
        var startTime = localStorage.getItem('timer_start');
        var now = Math.floor(Date.now() / 1000);
        
        if (!startTime || (now - startTime) > duration) {
            startTime = now;
            localStorage.setItem('timer_start', startTime);
        }
        
        function updateTimer() {
            var currentNow = Math.floor(Date.now() / 1000);
            var passedText = currentNow - startTime;
            var remaining = duration - passedText;
            
            if (remaining <= 0) {
                // Restart
                startTime = currentNow;
                localStorage.setItem('timer_start', startTime);
                remaining = duration;
            }
            
            var h = Math.floor(remaining / 3600);
            var m = Math.floor((remaining % 3600) / 60);
            var s = remaining % 60;
            
            displayHours.textContent = h < 10 ? "0" + h : h;
            displayMinutes.textContent = m < 10 ? "0" + m : m;
            displaySeconds.textContent = s < 10 ? "0" + s : s;
        }
        
        updateTimer();
        setInterval(updateTimer, 1000);
    });
</script>'''

new_js = '''<script>
    document.addEventListener("DOMContentLoaded", function() {
        var duration = 14 * 60 + 32;
        var displayTimer = document.getElementById('sticky-timer');
        
        var startTime = localStorage.getItem('timer_start');
        var now = Math.floor(Date.now() / 1000);
        
        if (!startTime || (now - startTime) > duration) {
            startTime = now;
            localStorage.setItem('timer_start', startTime);
        }
        
        function updateTimer() {
            if(!displayTimer) return;
            var currentNow = Math.floor(Date.now() / 1000);
            var passedText = currentNow - startTime;
            var remaining = duration - passedText;
            
            if (remaining <= 0) {
                startTime = currentNow;
                localStorage.setItem('timer_start', startTime);
                remaining = duration;
            }
            
            var h = Math.floor(remaining / 3600);
            var m = Math.floor((remaining % 3600) / 60);
            var s = remaining % 60;
            
            var sh = h < 10 ? "0" + h : h;
            var sm = m < 10 ? "0" + m : m;
            var ss = s < 10 ? "0" + s : s;
            
            displayTimer.textContent = sh + ":" + sm + ":" + ss;
        }
        
        updateTimer();
        setInterval(updateTimer, 1000);
    });
</script>'''
html = html.replace(old_js, new_js)

# We also still want the "Liberação imediata" text just before the CTA? 
# Wait, the user said "Substituindo o texto atual superior... remover completamente o texto antigo do topo". 
# The user doesn't say to remove the "Liberação imediata após a compra", but that was inside my timer div.
# Let's add it back right above the CTA.
liberacao_html = '''
        <p style="font-size:13px; color:#22c55e; font-weight:600; display:flex; align-items:center; justify-content:center; gap:6px; margin-bottom:1rem;">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            Liberação imediata após a compra
        </p>
'''

html = re.sub(
    r'<!-- CTA: Altura e fonte maiores, sombra, bordas full rounded -->',
    liberacao_html + '<!-- CTA: Altura e fonte maiores, sombra, bordas full rounded -->',
    html
)


# 3. ADD INITIAL CSS AND HTML FOR STICKY BANNER
sticky_css = '''
    <style>
        .sticky-urgency-bar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #f97316; /* Laranja do botão */
            color: #ffffff;
            z-index: 100000;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 8px 12px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
            font-size: clamp(13px, 3.5vw, 16px);
            font-weight: 600;
            gap: 6px;
        }
        .sticky-urgency-bar span strong {
            font-weight: 800;
            font-variant-numeric: tabular-nums;
            letter-spacing: 0.5px;
        }
        /* Mobile padding fix to avoid hiding top of hero */
        body { padding-top: 40px; }
    </style>
'''
html = html.replace('</head>', sticky_css + '</head>')


sticky_html = '''
    <div class="sticky-urgency-bar">
        OFERTA TERMINA EM: <strong id="sticky-timer">00:14:32</strong>
    </div>
'''
html = html.replace('<body class="antialiased">', '<body class="antialiased">' + sticky_html)

# Let's remove the .timer-container CSS just to maintain the file clean
html = re.sub(r'/\* Timer Styles \*/[\s\S]*?\.timer-separator \{ font-size: 24px; \}\s*\}', '', html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Done")
