import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add the CSS for the timer
css_insertion = """
        /* Timer Styles */
        .timer-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-bottom: 2rem;
            width: 100%;
        }
        .timer-title {
            font-size: 11px;
            text-transform: uppercase;
            color: rgba(255, 255, 255, 0.7);
            letter-spacing: 2px;
            margin-bottom: 0.5rem;
            font-weight: 600;
        }
        .timer-boxes {
            display: flex;
            gap: 12px;
            align-items: center;
        }
        .timer-box {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .timer-number {
            background: rgba(0, 0, 0, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            color: #fff;
            font-size: clamp(24px, 6vw, 32px);
            font-weight: 900;
            padding: 8px 12px;
            min-width: 60px;
            text-align: center;
            box-shadow: inset 0 2px 4px rgba(255,255,255,0.05);
            font-variant-numeric: tabular-nums;
        }
        .timer-separator {
            font-size: clamp(24px, 6vw, 32px);
            font-weight: 900;
            color: #fbbf24; /* Amber yellow */
            margin-top: -5px;
        }
        .timer-label {
            font-size: 10px;
            color: rgba(255, 255, 255, 0.5);
            text-transform: uppercase;
            margin-top: 4px;
        }
        .timer-footer {
            font-size: 13px;
            color: #22c55e;
            font-weight: 600;
            margin-top: 0.75rem;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        @media (max-height: 750px) {
            .timer-container { margin-bottom: 1.5rem; }
            .timer-number { font-size: 24px; padding: 6px 10px; min-width: 50px; }
            .timer-separator { font-size: 24px; }
        }
"""
html = html.replace("</style>", css_insertion + "</style>")

# 2. Add the HTML for the timer between benefits and CTA
timer_html = """
        <div class="timer-container">
            <span class="timer-title">OFERTA POR TEMPO LIMITADO</span>
            <div class="timer-boxes">
                <!-- Horas -->
                <div class="timer-box">
                    <div class="timer-number" id="t-hours">00</div>
                </div>
                <div class="timer-separator">:</div>
                <!-- Minutos -->
                <div class="timer-box">
                    <div class="timer-number" id="t-minutes">14</div>
                </div>
                <div class="timer-separator">:</div>
                <!-- Segundos -->
                <div class="timer-box">
                    <div class="timer-number" id="t-seconds">32</div>
                </div>
            </div>
            <span class="timer-footer">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                Liberação imediata após a compra
            </span>
        </div>
"""
# Search for the spot after benefits
finding_str = '</div>\n\n        <!-- CTA:'
html = html.replace(finding_str, "</div>\n" + timer_html + "\n        <!-- CTA:")

# 3. Add Javascript to the end of the body
js_insertion = """
<script>
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
</script>
</body>
"""
html = html.replace('</body>', js_insertion)

# Since there are multiple benefits lists in the rest of the page (maybe?), the replace will only affect where "<!-- CTA:" exists.
# We also reduce margin to fit easily
html = re.sub(
    r'\.benefits-list \{([\s\S]*?)margin-bottom: 1\.5rem;',
    r'.benefits-list {\1margin-bottom: 0.75rem;',
    html
)
html = re.sub(
    r'\.benefits-list \{ margin-bottom: 2rem; gap: 0\.5rem; \}',
    r'.benefits-list { margin-bottom: 1rem; gap: 0.5rem; }',
    html
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Done")
