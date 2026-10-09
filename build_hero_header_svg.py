import os
import base64

def generate_hero_headers():
    target_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(target_dir, 'header_hero.png')

    with open(img_path, 'rb') as f:
        img_b64 = base64.b64encode(f.read()).decode('utf-8')
        data_uri = f'data:image/png;base64,{img_b64}'

    hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 448" width="100%" height="100%">
  <defs>
    <!-- Text Gradients -->
    <linearGradient id="text-purple-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#E9D5FF"/>
      <stop offset="50%" stop-color="#C084FC"/>
      <stop offset="100%" stop-color="#A855F7"/>
    </linearGradient>

    <linearGradient id="name-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="50%" stop-color="#F3E8FF"/>
      <stop offset="100%" stop-color="#93C5FD"/>
    </linearGradient>

    <linearGradient id="aiml-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F472B6"/>
      <stop offset="50%" stop-color="#C084FC"/>
      <stop offset="100%" stop-color="#38BDF8"/>
    </linearGradient>

    <radialGradient id="avatar-aura" cx="78%" cy="48%" r="42%">
      <stop offset="0%" stop-color="#A855F7" stop-opacity="0.38"/>
      <stop offset="50%" stop-color="#38BDF8" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="octocat-aura" cx="62%" cy="80%" r="20%">
      <stop offset="0%" stop-color="#818CF8" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>

    <style>
      .sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
      .mono {{ font-family: 'Fira Code', 'Cascadia Code', 'JetBrains Mono', Consolas, monospace; }}
      .bold {{ font-weight: 800; }}

      /* Animations */
      @keyframes float-cone {{
        0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
        50% {{ transform: translateY(-12px) rotate(8deg); }}
      }}

      @keyframes float-knot-1 {{
        0%, 100% {{ transform: translateY(0px) rotate(0deg) scale(1); }}
        50% {{ transform: translateY(-10px) rotate(-10deg) scale(1.05); }}
      }}

      @keyframes float-knot-2 {{
        0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
        50% {{ transform: translateY(-8px) rotate(12deg); }}
      }}

      @keyframes rog-pulse {{
        0%, 100% {{ opacity: 0.7; transform: scale(1); filter: drop-shadow(0 0 4px #EF4444); }}
        50% {{ opacity: 1; transform: scale(1.18); filter: drop-shadow(0 0 14px #F43F5E); }}
      }}

      @keyframes keyboard-glow {{
        0%, 100% {{ opacity: 0.5; }}
        50% {{ opacity: 0.95; filter: drop-shadow(0 0 8px #38BDF8); }}
      }}

      @keyframes octocat-bounce {{
        0%, 100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-6px); }}
      }}

      @keyframes aura-pulse {{
        0%, 100% {{ opacity: 0.6; transform: scale(0.98); }}
        50% {{ opacity: 1; transform: scale(1.04); }}
      }}

      @keyframes text-shimmer {{
        0%, 100% {{ opacity: 0.92; }}
        50% {{ opacity: 1; filter: drop-shadow(0 0 8px rgba(192, 132, 252, 0.6)); }}
      }}

      @keyframes pulse-live {{
        0%, 100% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.3; transform: scale(0.85); }}
      }}

      /* Classes */
      .cone-anim {{ animation: float-cone 4s ease-in-out infinite; transform-origin: 405px 145px; }}
      .knot1-anim {{ animation: float-knot-1 5.5s ease-in-out infinite; transform-origin: 565px 60px; }}
      .knot2-anim {{ animation: float-knot-2 6.5s ease-in-out infinite 1s; transform-origin: 515px 490px; }}
      
      .rog-logo {{ animation: rog-pulse 2.2s ease-in-out infinite; transform-origin: 865px 705px; }}
      .kbd-light {{ animation: keyboard-glow 3s ease-in-out infinite; }}
      .octocat-anim {{ animation: octocat-bounce 4s ease-in-out infinite; transform-origin: 625px 840px; }}
      
      .aura-anim {{ animation: aura-pulse 4s ease-in-out infinite; transform-origin: 790px 210px; }}
      .text-anim {{ animation: text-shimmer 3s ease-in-out infinite; }}
      .live-dot {{ animation: pulse-live 2s infinite ease-in-out; transform-origin: 975px 30px; }}
    </style>
  </defs>

  <!-- Base High-Res Hero Image -->
  <image href="{data_uri}" x="0" y="0" width="1024" height="448"/>

  <!-- Background Ambient Glowing Radial Field behind Avatar -->
  <rect x="0" y="0" width="1024" height="448" fill="url(#avatar-aura)" class="aura-anim" style="mix-blend-mode: screen;"/>
  <rect x="0" y="0" width="1024" height="448" fill="url(#octocat-aura)" class="aura-anim" style="mix-blend-mode: screen;"/>

  <!-- FULL IMAGE ANIMATION OVERLAYS -->
  
  <!-- 1. Floating 3D Cone (Top Left) -->
  <g class="cone-anim">
    <circle cx="406" cy="144" r="24" fill="#A855F7" opacity="0.25" filter="blur(4px)"/>
  </g>

  <!-- 2. Floating 3D Torus Knots (Top & Mid Right) -->
  <g class="knot1-anim">
    <circle cx="580" cy="50" r="30" fill="#C084FC" opacity="0.2" filter="blur(6px)"/>
  </g>
  
  <g class="knot2-anim">
    <circle cx="516" cy="500" r="22" fill="#818CF8" opacity="0.2" filter="blur(5px)"/>
  </g>

  <!-- 3. ROG Strix Laptop Glowing Logo & Keyboard Light Bar -->
  <circle cx="865" cy="705" r="28" fill="#EF4444" opacity="0.3" class="rog-logo"/>
  <rect x="655" y="940" width="280" height="8" fill="#38BDF8" opacity="0.4" class="kbd-light" rx="4"/>

  <!-- 4. 3D Octocat Bounce Aura -->
  <g class="octocat-anim">
    <circle cx="625" cy="840" r="45" fill="#818CF8" opacity="0.15"/>
  </g>

  <!-- 5. TEXT ANIMATION ENHANCEMENT OVERLAYS -->
  <!-- Glowing Overlay for "I'm" -->
  <g class="text-anim">
    <rect x="115" y="48" width="100" height="52" fill="none"/>
  </g>

  <!-- Glowing Overlay for "Swapnil Patil." -->
  <g class="text-anim">
    <rect x="12" y="120" width="440" height="70" fill="none"/>
  </g>

  <!-- Glowing Overlay for "AI/ML Engineer" -->
  <g class="text-anim">
    <rect x="12" y="300" width="490" height="80" fill="none"/>
  </g>

  <!-- Top Right LIVE Status Tag Overlay -->
  <g transform="translate(885, 18)">
    <rect x="0" y="0" width="122" height="24" rx="12" fill="#0F172A" stroke="#334155" stroke-width="1.2" opacity="0.95"/>
    <circle cx="15" cy="12" r="4" fill="#10B981" class="live-dot"/>
    <text x="26" y="16" class="mono bold" font-size="10" fill="#10B981" letter-spacing="0.5">SYS.ACTIVE</text>
  </g>
</svg>'''

    with open(os.path.join(target_dir, 'header_hero_dark.svg'), 'w', encoding='utf-8') as f:
        f.write(hero_svg)
    with open(os.path.join(target_dir, 'header_hero_light.svg'), 'w', encoding='utf-8') as f:
        f.write(hero_svg)

    print("Header hero SVGs with full image and text animations updated successfully.")

if __name__ == '__main__':
    generate_hero_headers()
