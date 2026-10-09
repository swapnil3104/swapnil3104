import os
import base64
from PIL import Image

def generate_hero_headers():
    img_path = r'C:\Users\Asus\.gemini\antigravity-ide\brain\3d7c6f29-d5d8-42a2-99cf-6eed0d6698a9\.user_uploaded\media_1791533545581.png'
    
    # Save a clean copy to repository
    target_img_path = os.path.join(os.path.dirname(__file__), 'header_hero.png')
    with open(img_path, 'rb') as src, open(target_img_path, 'wb') as dst:
        dst.write(src.read())

    # Read base64
    with open(target_img_path, 'rb') as f:
        img_b64 = base64.b64encode(f.read()).decode('utf-8')
        data_uri = f'data:image/png;base64,{img_b64}'

    # Build Animated SVG dark version
    dark_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 447" width="100%" height="100%">
  <defs>
    <!-- Gradients -->
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

    <radialGradient id="glow-aura" cx="80%" cy="50%" r="45%">
      <stop offset="0%" stop-color="#A855F7" stop-opacity="0.35"/>
      <stop offset="60%" stop-color="#38BDF8" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>

    <style>
      .sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
      .mono {{ font-family: 'Fira Code', 'Cascadia Code', 'JetBrains Mono', Consolas, monospace; }}
      .bold {{ font-weight: 800; }}
      
      @keyframes float-1 {{
        0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
        50% {{ transform: translateY(-10px) rotate(5deg); }}
      }}
      @keyframes float-2 {{
        0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
        50% {{ transform: translateY(-14px) rotate(-8deg); }}
      }}
      @keyframes pulse-rog {{
        0%, 100% {{ opacity: 0.8; transform: scale(1); filter: drop-shadow(0 0 4px #EF4444); }}
        50% {{ opacity: 1; transform: scale(1.15); filter: drop-shadow(0 0 12px #F43F5E); }}
      }}
      @keyframes shimmer-text {{
        0% {{ stop-color: #E9D5FF; }}
        50% {{ stop-color: #38BDF8; }}
        100% {{ stop-color: #E9D5FF; }}
      }}
      @keyframes pulse-dot {{
        0%, 100% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.3; transform: scale(0.9); }}
      }}

      .shape-float-1 {{ animation: float-1 4.5s ease-in-out infinite; transform-origin: 400px 70px; }}
      .shape-float-2 {{ animation: float-2 6s ease-in-out infinite; transform-origin: 510px 250px; }}
      .shape-float-3 {{ animation: float-1 5s ease-in-out infinite 1s; transform-origin: 960px 260px; }}
      
      .rog-glow {{ animation: pulse-rog 2.5s ease-in-out infinite; transform-origin: 855px 335px; }}
      .live-dot {{ animation: pulse-dot 2s infinite ease-in-out; transform-origin: 975px 32px; }}
    </style>
  </defs>

  <!-- Base High-Res Hero Image -->
  <image href="{data_uri}" x="0" y="0" width="1024" height="447"/>

  <!-- Background Ambient Glowing Radial Field -->
  <rect x="0" y="0" width="1024" height="447" fill="url(#glow-aura)" style="mix-blend-mode: screen;"/>

  <!-- Animated Vector Overlays -->
  <!-- Floating 3D Geometric Accents -->
  <!-- Floating Cone 1 -->
  <g class="shape-float-1">
    <path d="M 395 50 L 415 85 L 380 80 Z" fill="#C084FC" opacity="0.6"/>
  </g>

  <!-- Floating Torus Knot Accent 2 -->
  <g class="shape-float-2">
    <circle cx="515" cy="250" r="14" fill="none" stroke="#A855F7" stroke-width="4" opacity="0.7"/>
  </g>

  <!-- Floating Pyramid Accent 3 -->
  <g class="shape-float-3">
    <path d="M 965 255 L 980 280 L 950 278 Z" fill="#818CF8" opacity="0.7"/>
  </g>

  <!-- ROG Glowing Logo Accent Overlay -->
  <circle cx="855" cy="335" r="18" fill="#EF4444" opacity="0.25" class="rog-glow"/>

  <!-- Top Right LIVE Status Tag Overlay -->
  <g transform="translate(885, 20)">
    <rect x="0" y="0" width="120" height="24" rx="12" fill="#0F172A" stroke="#334155" stroke-width="1.2" opacity="0.9"/>
    <circle cx="15" cy="12" r="4" fill="#10B981" class="live-dot"/>
    <text x="26" y="16" class="mono bold" font-size="10" fill="#10B981" letter-spacing="0.5">SYS.ACTIVE</text>
  </g>
</svg>'''

    light_svg = dark_svg  # Both dark & light retain the sleek dark hero aesthetic

    with open(os.path.join(os.path.dirname(__file__), 'header_hero_dark.svg'), 'w', encoding='utf-8') as f:
        f.write(dark_svg)
    with open(os.path.join(os.path.dirname(__file__), 'header_hero_light.svg'), 'w', encoding='utf-8') as f:
        f.write(light_svg)

    print("Header hero SVGs generated successfully.")

if __name__ == '__main__':
    generate_hero_headers()
