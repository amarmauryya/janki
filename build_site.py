import os

head = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Janki's Garden - A Fanpage</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        bloom: { bg: '#F8F3EC', pink: '#D78492', green: '#748A7A', text: '#6A615D', btnBg: '#FCEBEA', btnText: '#CD6F80' }
                    }
                }
            }
        }
        
    </script>
    <style type="text/tailwindcss">
        @layer utilities {
            body { @apply bg-bloom-bg text-bloom-text dark:bg-slate-900 dark:text-slate-200 transition-colors duration-700; font-family: 'Montserrat', sans-serif; overflow-x: hidden; }
            h1, h2, h3, h4, .font-serif { font-family: 'Playfair Display', serif; }
            .header-divider { display: flex; align-items: center; gap: 12px; margin-top: 1.5rem; margin-bottom: 2rem; }
            .header-divider::before, .header-divider::after { content: ''; height: 1px; width: 40px; @apply bg-bloom-pink/40 dark:bg-bloom-pink/30; }
            .image-container { border-radius: 2rem; }
            .glass-card { @apply bg-white/40 dark:bg-slate-800/40 backdrop-blur-md border border-bloom-pink/20 dark:border-white/10 shadow-sm transition-all duration-300; }
            .glass-card:hover { transform: translateY(-5px); @apply shadow-[0_10px_25px_-5px_rgba(215,132,146,0.3)] dark:shadow-[0_10px_25px_-5px_rgba(215,132,146,0.1)]; }
            .reveal { opacity: 0; transform: translateY(40px); transition: opacity 1.2s ease, transform 1.2s ease; }
            .reveal.active { opacity: 1; transform: translateY(0); }
            #mobile-menu.hidden-menu { opacity: 0; visibility: hidden; pointer-events: none; }
            #mobile-menu { transition: opacity 0.3s ease, visibility 0.3s ease; }
            
            /* Chat Widget Styles */
            #chat-widget { transition: all 0.4s cubic-bezier(0.22, 1, 0.36, 1); transform-origin: bottom right; }
            #chat-widget.hidden-chat { opacity: 0; transform: scale(0.8) translateY(20px); pointer-events: none; }
            .envelope-btn { animation: float 3s ease-in-out infinite; }
            
            /* Falling Petals */
            .petal { position: fixed; top: -10%; z-index: 10; pointer-events: none; user-select: none; animation: fall linear infinite; opacity: 0.7; }
            .dark .petal { opacity: 0.4; filter: brightness(1.2); }
            
            /* Animations */
            @keyframes float { 0% { transform: translateY(0px); } 50% { transform: translateY(-8px); } 100% { transform: translateY(0px); } }
            @keyframes fall {
                0% { transform: translate(0, 0) rotate(0deg); }
                100% { transform: translate(100px, 120vh) rotate(360deg); }
            }
            @keyframes spin-slow { 100% { transform: rotate(360deg); } }
            .music-playing #music-icon { animation: spin-slow 4s linear infinite; }
        }
    </style>
</head>
<body class="min-h-screen relative flex flex-col pt-24">
"""

def get_navbar(active_page):
    def a(p):
        return "text-bloom-pink border-b border-bloom-pink pb-1" if p == active_page else "text-bloom-text dark:text-slate-300 hover:text-bloom-pink dark:hover:text-bloom-pink"
    
    return f"""
    <!-- Decorative Watermark Flowers -->
    <div class="fixed top-20 -left-20 text-bloom-pink opacity-[0.03] dark:opacity-5 transform -rotate-12 pointer-events-none z-0">
        <span class="material-symbols-outlined" style="font-size: 45vh;">local_florist</span>
    </div>
    <div class="fixed -bottom-10 -right-10 text-bloom-pink opacity-[0.03] dark:opacity-5 transform rotate-12 pointer-events-none z-0">
        <span class="material-symbols-outlined" style="font-size: 55vh;">spa</span>
    </div>

    <!-- Falling Petals Container -->
    <div id="petal-container" class="fixed inset-0 overflow-hidden pointer-events-none z-0"></div>

    <nav class="fixed top-0 left-0 right-0 z-50 flex items-center justify-between px-6 lg:px-10 py-4 lg:py-5 max-w-[1600px] mx-auto w-full bg-[#F8F3EC]/90 dark:bg-slate-900/90 backdrop-blur-md shadow-sm transition-colors duration-700">
        <a href="index.html" class="flex items-center gap-2 group cursor-pointer" id="secret-trigger">
            <h1 class="font-serif text-2xl lg:text-3xl font-medium text-bloom-pink">Janki's Garden</h1>
            <span class="material-symbols-outlined text-bloom-pink group-hover:rotate-12 transition-transform" style="font-size: 26px;">spa</span>
        </a>
        <div class="hidden md:flex items-center gap-10">
            <a href="index.html" class="text-sm font-medium transition-colors {a('home')}">Home</a>
            <a href="about.html" class="text-sm font-medium transition-colors {a('about')}">About</a>
            <a href="gallery.html" class="text-sm font-medium transition-colors {a('gallery')}">Gallery</a>
            <a href="memories.html" class="text-sm font-medium transition-colors {a('memories')}">Memories</a>
            <a href="fanwall.html" class="text-sm font-medium transition-colors {a('fanwall')}">Fan Wall</a>
            <a href="littlethings.html" class="text-sm font-medium transition-colors {a('little')}">Little Things</a>
        </div>
        <div class="flex items-center gap-4">
            <button id="menu-btn" class="md:hidden text-bloom-pink p-2"><span class="material-symbols-outlined text-[28px]">menu</span></button>
        </div>
    </nav>
    <div id="mobile-menu" class="hidden-menu fixed inset-0 bg-[#F8F3EC]/95 dark:bg-slate-900/95 backdrop-blur-xl z-[45] flex flex-col items-center justify-center gap-8 md:hidden transition-colors duration-700">
        <a href="index.html" class="mobile-link text-2xl font-serif text-bloom-text dark:text-slate-200 hover:text-bloom-pink transition-colors">Home</a>
        <a href="about.html" class="mobile-link text-2xl font-serif text-bloom-text dark:text-slate-200 hover:text-bloom-pink transition-colors">About</a>
        <a href="gallery.html" class="mobile-link text-2xl font-serif text-bloom-text dark:text-slate-200 hover:text-bloom-pink transition-colors">Gallery</a>
        <a href="memories.html" class="mobile-link text-2xl font-serif text-bloom-text dark:text-slate-200 hover:text-bloom-pink transition-colors">Memories</a>
        <a href="fanwall.html" class="mobile-link text-2xl font-serif text-bloom-text dark:text-slate-200 hover:text-bloom-pink transition-colors">Fan Wall</a>
        <a href="littlethings.html" class="mobile-link text-2xl font-serif text-bloom-text dark:text-slate-200 hover:text-bloom-pink transition-colors">Little Things</a>
    </div>
"""

footer = """
    <!-- Background Music -->
    <button id="music-toggle" class="fixed bottom-8 left-8 z-40 w-14 h-14 rounded-full bg-white/80 dark:bg-slate-800/80 backdrop-blur shadow-lg flex items-center justify-center text-bloom-pink border border-bloom-pink/20 transition-all hover:scale-110">
        <span class="material-symbols-outlined text-2xl" id="music-icon">music_off</span>
    </button>
    <audio id="bg-audio" loop src="audio.mp3"></audio>

    <!-- Secret Letter Modal -->
    <div id="secret-modal" class="fixed inset-0 z-[100] bg-black/60 backdrop-blur-sm hidden flex items-center justify-center p-6 opacity-0 transition-opacity duration-500">
        <div class="bg-[#F8F3EC] dark:bg-slate-800 w-full max-w-lg rounded-[2rem] p-10 relative shadow-2xl transform scale-95 transition-transform duration-500" id="secret-content">
            <button id="close-secret" class="absolute top-6 right-6 text-bloom-text/50 dark:text-slate-400 hover:text-bloom-pink transition-colors">
                <span class="material-symbols-outlined">close</span>
            </button>
            <span class="material-symbols-outlined text-bloom-pink text-5xl mb-6 block text-center opacity-80">favorite</span>
            <h2 class="font-serif text-3xl text-bloom-pink mb-6 text-center">A Secret Note Just For You</h2>
            <p class="text-bloom-text dark:text-slate-300 leading-relaxed text-center font-medium opacity-90 mb-6 italic">
                "Some people make the world a little brighter just by being in it. <br><br>
                Thank you for being such an amazing friend, for your radiant smile, and for the joy you bring everywhere you go. Keep shining, Janki!"
            </p>
            <div class="text-center text-sm font-semibold text-bloom-pink">With love, forever. ✨</div>
        </div>
    </div>

    <footer class="w-full py-12 lg:py-16 px-6 lg:px-24 flex flex-col items-center gap-6 bg-[#F8F3EC] dark:bg-slate-900/50 relative z-10 border-t border-bloom-pink/10 mt-auto transition-colors duration-700">
        <div class="font-serif text-2xl text-bloom-pink">Janki's Garden</div>
        <p class="text-sm text-bloom-text dark:text-slate-400 opacity-60 text-center">© 2024 Botanical Bloom. Created with love for my favorite person.</p>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // Mobile Menu
            const menuBtn = document.getElementById('menu-btn');
            const mobileMenu = document.getElementById('mobile-menu');
            let menuOpen = false;
            menuBtn.addEventListener('click', () => {
                menuOpen = !menuOpen;
                if(menuOpen) {
                    mobileMenu.classList.remove('hidden-menu');
                    menuBtn.innerHTML = '<span class="material-symbols-outlined text-[28px]">close</span>';
                } else {
                    mobileMenu.classList.add('hidden-menu');
                    menuBtn.innerHTML = '<span class="material-symbols-outlined text-[28px]">menu</span>';
                }
            });

            // Scroll Reveal
            const reveals = document.querySelectorAll('.reveal');
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(e => { if(e.isIntersecting) e.target.classList.add('active'); });
            }, { threshold: 0.1 });
            reveals.forEach(r => observer.observe(r));
            setTimeout(() => reveals.forEach(r => { if(r.getBoundingClientRect().top < window.innerHeight) r.classList.add('active'); }), 100);


            // Background Music
            const musicBtn = document.getElementById('music-toggle');
            const musicIcon = document.getElementById('music-icon');
            const audio = document.getElementById('bg-audio');
            let isPlaying = false;
            
            musicBtn.addEventListener('click', () => {
                if (isPlaying) {
                    audio.pause();
                    musicIcon.textContent = 'music_off';
                    musicBtn.classList.remove('music-playing');
                } else {
                    audio.play().catch(e => console.log('Audio play failed:', e));
                    musicIcon.textContent = 'music_note';
                    musicBtn.classList.add('music-playing');
                }
                isPlaying = !isPlaying;
            });

            // Secret Letter Logic (3 clicks)
            const secretTrigger = document.getElementById('secret-trigger');
            const secretModal = document.getElementById('secret-modal');
            const secretContent = document.getElementById('secret-content');
            const closeSecret = document.getElementById('close-secret');
            let clickCount = 0;
            let clickTimer;

            secretTrigger.addEventListener('click', (e) => {
                e.preventDefault(); // Prevent navigating home immediately if they are clicking fast
                clickCount++;
                clearTimeout(clickTimer);
                
                if (clickCount >= 3) {
                    // Open Secret Letter
                    secretModal.classList.remove('hidden');
                    // small delay for transition
                    setTimeout(() => {
                        secretModal.classList.remove('opacity-0');
                        secretContent.classList.remove('scale-95');
                    }, 50);
                    clickCount = 0;
                } else {
                    // If not 3 clicks, just act as a normal link after a short delay
                    clickTimer = setTimeout(() => {
                        if (clickCount === 1) window.location.href = 'index.html';
                        clickCount = 0;
                    }, 400);
                }
            });

            closeSecret.addEventListener('click', () => {
                secretModal.classList.add('opacity-0');
                secretContent.classList.add('scale-95');
                setTimeout(() => secretModal.classList.add('hidden'), 500);
            });

            // Falling Petals Logic
            const petalContainer = document.getElementById('petal-container');
            const petalsCount = 15;
            const colors = ['#D78492', '#FCEBEA', '#FFB7B2'];
            
            for (let i = 0; i < petalsCount; i++) {
                createPetal();
            }

            function createPetal() {
                const petal = document.createElement('div');
                petal.classList.add('petal');
                
                // Random properties
                const size = Math.random() * 15 + 10; // 10px to 25px
                const left = Math.random() * 100; // 0% to 100%
                const animationDuration = Math.random() * 10 + 10; // 10s to 20s
                const animationDelay = Math.random() * 15; // 0s to 15s delay
                
                // SVG Path for a petal
                petal.innerHTML = `<svg width="${size}" height="${size}" viewBox="0 0 24 24" fill="${colors[Math.floor(Math.random() * colors.length)]}"><path d="M12 2C8 2 4 6 4 10C4 14.5 12 22 12 22C12 22 20 14.5 20 10C20 6 16 2 12 2Z"/></svg>`;
                
                petal.style.left = `${left}vw`;
                petal.style.animationDuration = `${animationDuration}s`;
                petal.style.animationDelay = `${animationDelay}s`;
                
                petalContainer.appendChild(petal);
            }
        });
    </script>
</body>
</html>
"""

# ----------------- PAGES CONTENT -----------------

pages = {}

# HOME PAGE
pages['index.html'] = ("home", """
    <section class="relative min-h-[80dvh] flex items-center pb-24">
        <div class="max-w-[1400px] mx-auto w-full grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12 px-6 lg:px-10 items-center relative z-10">
            <div class="reveal relative z-30 pt-4 lg:pt-0 pl-2 lg:pl-16">
                <h2 class="font-serif text-[55px] md:text-[75px] leading-tight text-bloom-pink mb-4">Dearest Janki</h2>
                <div class="flex items-end gap-3 max-w-[450px]">
                    <p class="font-serif text-[24px] md:text-[34px] leading-tight text-bloom-green dark:text-green-200/80">A little corner dedicated to Janki</p>
                    <span class="material-symbols-outlined text-bloom-pink opacity-80 pb-1 hidden sm:inline-block text-[36px]">spa</span>
                </div>
                <div class="header-divider"><span class="material-symbols-outlined text-bloom-pink opacity-60 text-[20px]">local_florist</span></div>
                <p class="text-bloom-text dark:text-slate-300 text-[15px] leading-relaxed max-w-sm mb-10 font-medium opacity-80">
                    A wonderful friend with an endless love for Rasmalai. Some people don't need a reason to be appreciated. They simply are.
                </p>
                <a href="about.html" class="inline-flex bg-bloom-pink text-white px-8 py-3.5 rounded-full font-medium text-[15px] items-center gap-2 hover:bg-opacity-90 transition-colors shadow-lg">
                    Explore <span class="material-symbols-outlined text-lg">arrow_forward</span>
                </a>
            </div>
            <div class="reveal flex justify-center lg:justify-end pr-0 lg:pr-16 relative z-10 mt-8 lg:mt-0">
                <div class="w-full max-w-[360px] md:max-w-[460px] aspect-[4/5] image-container overflow-hidden shadow-xl relative ring-4 ring-white/30 dark:ring-white/10">
                    <img src="janki_photo.jpeg" alt="Janki" class="w-full h-full object-cover object-top" />
                </div>
            </div>
        </div>
    </section>
    
    <!-- Envelope Chat Widget -->
    <div class="fixed bottom-8 right-8 z-50 flex items-center gap-4">
        <!-- Attention grabber tooltip -->
        <div id="chat-tooltip" class="hidden sm:block relative bg-white dark:bg-slate-800 text-bloom-pink dark:text-pink-300 px-4 py-3 rounded-2xl shadow-lg border border-bloom-pink/20 dark:border-white/10 animate-bounce">
            <p class="text-sm font-medium font-sans">Psst... Janki, check this! ✨</p>
            <div class="absolute -right-[6px] top-1/2 -translate-y-1/2 w-3 h-3 bg-white dark:bg-slate-800 border-t border-r border-bloom-pink/20 dark:border-white/10 rotate-45"></div>
        </div>
        
        <div class="relative envelope-btn">
            <button id="envelope-toggle" class="w-16 h-16 rounded-full bg-bloom-pink text-white flex items-center justify-center shadow-xl hover:bg-opacity-90 transition-all border-2 border-white/50 cursor-pointer">
                <span class="material-symbols-outlined text-[32px]">mail</span>
            </button>
            <span id="chat-notif-dot" class="absolute -top-1 -right-1 flex h-5 w-5">
              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-red-400 opacity-75"></span>
              <span class="relative inline-flex rounded-full h-5 w-5 bg-red-500 border-2 border-white"></span>
            </span>
        </div>
    </div>

    <div id="chat-widget" class="hidden-chat fixed bottom-28 right-8 z-50 w-[350px] sm:w-[400px] h-[550px] max-h-[70vh] bg-[#F8F3EC]/95 dark:bg-slate-900/95 backdrop-blur-xl rounded-[2rem] shadow-2xl border border-bloom-pink/20 dark:border-white/10 flex flex-col overflow-hidden">
        <div class="bg-bloom-pink text-white p-5 flex justify-between items-center rounded-t-[2rem]">
            <div class="flex items-center gap-3"><span class="material-symbols-outlined text-2xl">spa</span>
                <div><h3 class="font-serif text-lg font-medium">Lotus Bot</h3><p class="text-xs opacity-80 font-sans">Always here to listen 🌸</p></div>
            </div>
            <button id="close-chat" class="hover:text-white/70"><span class="material-symbols-outlined">close</span></button>
        </div>
        <div id="chat-messages" class="flex-grow p-5 overflow-y-auto flex flex-col gap-4 text-sm">
            <div class="flex flex-col gap-1 items-start"><div class="p-3.5 shadow-sm max-w-[85%] leading-relaxed bg-white dark:bg-slate-800 text-bloom-text dark:text-slate-200 border border-bloom-pink/20 dark:border-white/10 rounded-[18px_18px_18px_0px]">Namaste Janki ji! 🌸 I hope your day is as sweet as Rasmalai! How are you feeling today?</div></div>
        </div>
        <div class="p-4 bg-white/50 dark:bg-slate-800/50 border-t border-bloom-pink/10 dark:border-white/10">
            <form id="chat-form" class="flex items-center gap-2">
                <input type="text" id="chat-input" placeholder="Say something magical..." class="flex-grow bg-white dark:bg-slate-700 border border-bloom-pink/20 dark:border-transparent rounded-full px-4 py-3 text-sm focus:outline-none focus:ring-1 focus:ring-bloom-pink text-bloom-text dark:text-white placeholder-bloom-text/50 dark:placeholder-slate-400">
                <button type="submit" class="w-11 h-11 rounded-full bg-bloom-pink text-white flex items-center justify-center shadow-md flex-shrink-0"><span class="material-symbols-outlined text-xl ml-1">send</span></button>
            </form>
        </div>
    </div>
    <script>
        document.getElementById('envelope-toggle').addEventListener('click', () => {
            document.getElementById('chat-widget').classList.remove('hidden-chat');
            const tooltip = document.getElementById('chat-tooltip');
            const notifDot = document.getElementById('chat-notif-dot');
            if(tooltip) tooltip.style.display = 'none';
            if(notifDot) notifDot.style.display = 'none';
        });
        document.getElementById('close-chat').addEventListener('click', () => document.getElementById('chat-widget').classList.add('hidden-chat'));
        
        function appendMessage(text, sender) {
            const chatMessages = document.getElementById('chat-messages');
            const wrapper = document.createElement('div');
            wrapper.className = `flex flex-col gap-1 ${sender === 'user' ? 'items-end' : 'items-start'}`;
            const userClasses = 'bg-bloom-pink text-white rounded-[18px_18px_0px_18px]';
            const botClasses = 'bg-white dark:bg-slate-800 text-bloom-text dark:text-slate-200 border border-bloom-pink/20 dark:border-white/10 rounded-[18px_18px_18px_0px]';
            wrapper.innerHTML = `<div class="p-3.5 shadow-sm max-w-[85%] leading-relaxed ${sender === 'user' ? userClasses : botClasses}">${text.replace(/\\n/g, '<br>')}</div>`;
            chatMessages.appendChild(wrapper);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }

        document.getElementById('chat-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const input = document.getElementById('chat-input');
            const text = input.value.trim();
            if (!text) return;
            appendMessage(text, 'user');
            input.value = '';
            
            const typingId = 'typing-' + Date.now();
            const chatMessages = document.getElementById('chat-messages');
            chatMessages.insertAdjacentHTML('beforeend', `<div id="${typingId}" class="flex flex-col gap-1 items-start"><div class="bg-white dark:bg-slate-800 text-bloom-pink dark:text-pink-300 border border-bloom-pink/20 dark:border-white/10 rounded-[18px_18px_18px_0px] p-3.5 shadow-sm italic">Typing magically... ✨</div></div>`);
            chatMessages.scrollTop = chatMessages.scrollHeight;

            try {
                const API_KEY = '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';
                const systemPrompt = "You are 'Lotus Bot', a magical digital garden assistant created by Amar for his dear friend Janki. Talk to Janki with extreme sweetness, warmth, and poetry. You know she loves Rasmalai, is from Jodhpur, and was born on March 7, 2002, but ONLY mention these facts if it perfectly fits the conversation naturally. Do NOT mention them in every reply. Always use cute emojis like 🌸✨🌷. Keep your replies very short (1-2 sentences max) and highly conversational. Janki says: " + text;
                
                const res = await fetch('https://api.groq.com/openai/v1/chat/completions', {
                    method: 'POST',
                    headers: { 
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${API_KEY}`
                    },
                    body: JSON.stringify({
                        model: "llama-3.1-8b-instant",
                        messages: [
                            { role: "system", content: systemPrompt },
                            { role: "user", content: text }
                        ]
                    })
                });
                
                const data = await res.json();
                const indicator = document.getElementById(typingId);
                if (indicator) indicator.remove();
                
                if (!res.ok || data.error) {
                    throw new Error(data.error?.message || "Invalid Groq API Key");
                }
                
                if (data.choices && data.choices[0] && data.choices[0].message) {
                    appendMessage(data.choices[0].message.content, 'bot');
                } else {
                    throw new Error("No response generated.");
                }
            } catch (err) {
                const indicator = document.getElementById(typingId);
                if (indicator) indicator.remove();
                appendMessage("Oops! My magical connection faded. 🌸", 'bot');
            }
        });
    </script>
""")

pages['about.html'] = ("about", """
    <section class="py-20 px-6 lg:px-24 max-w-4xl mx-auto">
        <div class="reveal text-center space-y-8">
            <span class="material-symbols-outlined text-bloom-green dark:text-green-300/50 text-5xl opacity-50">spa</span>
            <h2 class="font-serif text-5xl md:text-6xl text-bloom-pink font-semibold">The Essence of Janki</h2>
            <div class="header-divider justify-center"><span class="material-symbols-outlined text-bloom-pink opacity-60 text-[20px]">local_florist</span></div>
            <p class="text-lg md:text-xl text-bloom-text dark:text-slate-300 leading-relaxed opacity-90 font-medium">
                Some things are simply known without explanation. The quiet strength she carries, the subtle grace in her steps, the way light seems to catch differently in her presence. <br><br>
                This space is a reflection of that vibrant energy—a digital garden cultivated with memories and admiration for an amazing friend hailing all the way from the beautiful blue city of Jodhpur.
            </p>
            <div class="inline-flex items-center gap-3 bg-white/60 dark:bg-slate-800/60 backdrop-blur px-8 py-4 rounded-full border border-bloom-pink/30 dark:border-white/10 shadow-sm mt-8">
                <span class="material-symbols-outlined text-bloom-pink">cake</span>
                <span class="font-serif text-xl text-bloom-pink font-medium">March 7, 2002</span>
            </div>
            <div class="inline-flex items-center gap-3 bg-white/60 dark:bg-slate-800/60 backdrop-blur px-8 py-4 rounded-full border border-bloom-pink/30 dark:border-white/10 shadow-sm mt-4 ml-4">
                <span class="material-symbols-outlined text-bloom-pink">location_on</span>
                <span class="font-serif text-xl text-bloom-pink font-medium">Jodhpur, Rajasthan</span>
            </div>
        </div>
    </section>
""")

pages['gallery.html'] = ("gallery", """
    <section class="py-20 px-6 lg:px-24 max-w-6xl mx-auto min-h-screen">
        <div class="reveal text-center mb-16">
            <h2 class="font-serif text-4xl md:text-5xl text-bloom-pink font-semibold mb-4">Picture Garden</h2>
            <p class="text-bloom-text dark:text-slate-400 font-medium opacity-80">Moments frozen in time, bright and blooming. (Click to zoom)</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div class="reveal image-container overflow-hidden shadow-lg border border-white/50 dark:border-white/10 h-[400px] cursor-pointer hover:scale-105 transition-transform duration-300" onclick="openLightbox('janki_photo.jpeg')">
                <img src="janki_photo.jpeg" class="w-full h-full object-cover" />
            </div>
            <div class="reveal glass-card rounded-[2rem] flex flex-col items-center justify-center h-[400px] cursor-pointer hover:bg-bloom-pink/10" onclick="openLightbox('https://images.unsplash.com/photo-1490750967868-88aa4486c946?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80')">
                <span class="material-symbols-outlined text-bloom-pink text-4xl mb-2 opacity-50">image</span>
                <p class="text-bloom-text dark:text-slate-400 opacity-50 font-medium">Sample Bloom</p>
            </div>
            <div class="reveal glass-card rounded-[2rem] flex flex-col items-center justify-center h-[400px] cursor-pointer hover:bg-bloom-pink/10" onclick="openLightbox('https://images.unsplash.com/photo-1518895949257-7621c3c786d7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80')">
                 <span class="material-symbols-outlined text-bloom-pink text-4xl mb-2 opacity-50">image</span>
                 <p class="text-bloom-text dark:text-slate-400 opacity-50 font-medium">Sample Petal</p>
            </div>
        </div>
    </section>
    
    <!-- Lightbox Modal -->
    <div id="lightbox-modal" class="fixed inset-0 z-[100] bg-black/90 backdrop-blur-sm hidden flex items-center justify-center p-4 opacity-0 transition-opacity duration-300" onclick="closeLightbox()">
        <button class="absolute top-8 right-8 text-white hover:text-bloom-pink transition-colors z-50">
            <span class="material-symbols-outlined text-4xl">close</span>
        </button>
        <img id="lightbox-img" src="" class="max-w-full max-h-[90vh] rounded-xl shadow-2xl object-contain transform scale-95 transition-transform duration-300" onclick="event.stopPropagation();">
    </div>

    <script>
        const lightbox = document.getElementById('lightbox-modal');
        const lightboxImg = document.getElementById('lightbox-img');
        function openLightbox(src) {
            lightboxImg.src = src;
            lightbox.classList.remove('hidden');
            setTimeout(() => {
                lightbox.classList.remove('opacity-0');
                lightboxImg.classList.remove('scale-95');
            }, 10);
        }
        function closeLightbox() {
            lightbox.classList.add('opacity-0');
            lightboxImg.classList.add('scale-95');
            setTimeout(() => {
                lightbox.classList.add('hidden');
            }, 300);
        }
    </script>
""")

pages['memories.html'] = ("memories", """
    <section class="py-20 px-6 lg:px-24 max-w-3xl mx-auto min-h-screen">
        <div class="reveal text-center mb-16">
            <h2 class="font-serif text-4xl md:text-5xl text-bloom-pink font-semibold mb-4">Beautiful Memories</h2>
            <p class="text-bloom-text dark:text-slate-400 font-medium opacity-80">The timeline of a wonderful friendship.</p>
        </div>
        <div class="space-y-12 relative before:absolute before:inset-0 before:ml-5 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-transparent before:via-bloom-pink/50 before:to-transparent">
            
            <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                <div class="flex items-center justify-center w-10 h-10 rounded-full border border-white dark:border-slate-800 bg-bloom-pink text-white shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 z-10">
                    <span class="material-symbols-outlined text-sm">stars</span>
                </div>
                <div class="reveal glass-card w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] p-6 rounded-2xl shadow-sm">
                    <time class="font-serif text-bloom-pink font-semibold mb-1">March 7, 2002</time>
                    <div class="text-bloom-text dark:text-slate-300 font-medium">A flower bloomed in Jodhpur. Happy Birthday Janki!</div>
                </div>
            </div>

            <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                <div class="flex items-center justify-center w-10 h-10 rounded-full border border-white dark:border-slate-800 bg-bloom-pink text-white shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 z-10">
                    <span class="material-symbols-outlined text-sm">auto_awesome</span>
                </div>
                <div class="reveal glass-card w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] p-6 rounded-2xl shadow-sm">
                    <time class="font-serif text-bloom-pink font-semibold mb-1">Present Day</time>
                    <div class="text-bloom-text dark:text-slate-300 font-medium">Making new memories every single day.</div>
                </div>
            </div>

        </div>
    </section>
""")

pages['fanwall.html'] = ("fanwall", """
    <section class="py-20 px-6 lg:px-24 max-w-6xl mx-auto min-h-screen">
        <div class="reveal text-center mb-16">
            <h2 class="font-serif text-4xl md:text-5xl text-bloom-pink font-semibold mb-4">The Fan Wall</h2>
            <p class="text-bloom-text dark:text-slate-400 font-medium opacity-80">Sweet messages dedicated to you.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div class="reveal glass-card p-8 rounded-3xl relative overflow-hidden group">
                <div class="absolute -right-4 -top-4 w-24 h-24 bg-bloom-pink/10 rounded-full blur-2xl group-hover:bg-bloom-pink/20 transition-all duration-500"></div>
                <span class="material-symbols-outlined absolute top-6 right-6 text-bloom-pink/30 text-4xl">format_quote</span>
                <p class="text-bloom-text dark:text-slate-300 font-medium italic mb-6 leading-relaxed relative z-10">"Janki, you light up every room you walk into! Never stop being your amazing self. The world needs your Jodhpur charm!"</p>
                <div class="font-serif text-bloom-pink font-semibold">- Your Friend</div>
            </div>
            <div class="reveal glass-card p-8 rounded-3xl relative overflow-hidden group">
                <div class="absolute -right-4 -top-4 w-24 h-24 bg-bloom-pink/10 rounded-full blur-2xl group-hover:bg-bloom-pink/20 transition-all duration-500"></div>
                <span class="material-symbols-outlined absolute top-6 right-6 text-bloom-pink/30 text-4xl">format_quote</span>
                <p class="text-bloom-text dark:text-slate-300 font-medium italic mb-6 leading-relaxed relative z-10">"To the most wonderful person. Keep smiling always, it suits you best!"</p>
                <div class="font-serif text-bloom-pink font-semibold">- Well Wisher</div>
            </div>
        </div>
    </section>
""")

pages['littlethings.html'] = ("little", """
    <section class="py-20 px-6 lg:px-24 max-w-6xl mx-auto min-h-screen">
        <div class="reveal text-center mb-16">
            <h2 class="font-serif text-4xl md:text-5xl text-bloom-pink font-semibold mb-4">The Little Things</h2>
            <p class="text-bloom-text dark:text-slate-400 font-medium opacity-80">All the petals that make you, you.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div class="reveal glass-card rounded-3xl p-8 flex flex-col items-center text-center gap-4 hover:border-bloom-pink/40">
                <div class="w-16 h-16 rounded-full bg-bloom-pink text-white flex items-center justify-center shadow-lg transform transition-transform hover:rotate-12"><span class="material-symbols-outlined text-2xl">favorite</span></div>
                <h3 class="font-serif text-2xl text-bloom-pink font-semibold">Personality</h3>
                <p class="text-bloom-text dark:text-slate-300 font-medium opacity-90">Warm, caring, and full of radiant life.</p>
            </div>
            <div class="reveal glass-card rounded-3xl p-8 flex flex-col items-center text-center gap-4 hover:border-bloom-pink/40">
                <div class="w-16 h-16 rounded-full bg-bloom-pink text-white flex items-center justify-center shadow-lg transform transition-transform hover:-rotate-12"><span class="material-symbols-outlined text-2xl">thumb_up</span></div>
                <h3 class="font-serif text-2xl text-bloom-pink font-semibold">Likes</h3>
                <p class="text-bloom-text dark:text-slate-300 font-medium opacity-90">Can never say no to Rasmalai, loves beautiful places, and great company.</p>
            </div>
            <div class="reveal glass-card rounded-3xl p-8 flex flex-col items-center text-center gap-4 hover:border-bloom-pink/40">
                <div class="w-16 h-16 rounded-full bg-bloom-pink text-white flex items-center justify-center shadow-lg transform transition-transform hover:rotate-12"><span class="material-symbols-outlined text-2xl">location_city</span></div>
                <h3 class="font-serif text-2xl text-bloom-pink font-semibold">Jodhpur</h3>
                <p class="text-bloom-text dark:text-slate-300 font-medium opacity-90">Proudly hailing from the beautiful Blue City.</p>
            </div>
        </div>
    </section>
""")

for filename, (active, content) in pages.items():
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(head + get_navbar(active) + content + footer)

print("Site built successfully with Magical Features.")
