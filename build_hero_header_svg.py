import os
import base64
import math
import colorsys
from PIL import Image, ImageDraw, ImageFilter

def generate_hero_headers():
    target_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 1. Prepare clean background image without static left text
    clean_bg_path = os.path.join(target_dir, 'header_hero_clean_left.png')
    if not os.path.exists(clean_bg_path):
        base_img_path = os.path.join(target_dir, 'header_hero.png')
        img = Image.open(base_img_path).convert('RGBA')
        draw = ImageDraw.Draw(img)
        for y in range(448):
            r = int(12 + (19 - 12) * (y / 448.0))
            g = int(14 + (21 - 14) * (y / 448.0))
            b = int(24 + (34 - 24) * (y / 448.0))
            draw.line([(0, y), (525, y)], fill=(r, g, b, 255))
        img.save(clean_bg_path)

    # Encode base64
    with open(clean_bg_path, 'rb') as f:
        img_b64 = base64.b64encode(f.read()).decode('utf-8')
        data_uri = f'data:image/png;base64,{img_b64}'

    # Build Animated SVG dark & light versions with SVG Typing Animation
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

    <radialGradient id="rog-rgb-glow" cx="885" cy="320" r="40" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#EF4444" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#EF4444" stop-opacity="0"/>
    </radialGradient>

    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800;900&amp;family=Fira+Code:wght@600&amp;display=swap');
      
      .sans {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
      .mono {{ font-family: 'Fira Code', Consolas, monospace; }}
      .bold {{ font-weight: 800; }}
      .extrabold {{ font-weight: 900; }}

      /* Typing Animation Keyframes */
      @keyframes type-reveal-1 {{
        0%, 5% {{ clip-path: inset(0 100% 0 0); }}
        20%, 100% {{ clip-path: inset(0 0% 0 0); }}
      }}
      @keyframes type-reveal-2 {{
        0%, 22% {{ clip-path: inset(0 100% 0 0); }}
        45%, 100% {{ clip-path: inset(0 0% 0 0); }}
      }}
      @keyframes type-reveal-3 {{
        0%, 48% {{ clip-path: inset(0 100% 0 0); }}
        70%, 100% {{ clip-path: inset(0 0% 0 0); }}
      }}
      @keyframes type-reveal-4 {{
        0%, 72% {{ clip-path: inset(0 100% 0 0); }}
        92%, 100% {{ clip-path: inset(0 0% 0 0); }}
      }}

      @keyframes blink-cursor {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
      }}

      @keyframes float-cone {{
        0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
        50% {{ transform: translateY(-10px) rotate(6deg); }}
      }}

      @keyframes rog-color-shift {{
        0% {{ filter: hue-rotate(0deg); }}
        100% {{ filter: hue-rotate(360deg); }}
      }}

      .type-line-1 {{ animation: type-reveal-1 6s infinite ease-in-out; }}
      .type-line-2 {{ animation: type-reveal-2 6s infinite ease-in-out; }}
      .type-line-3 {{ animation: type-reveal-3 6s infinite ease-in-out; }}
      .type-line-4 {{ animation: type-reveal-4 6s infinite ease-in-out; }}
      
      .cursor {{ animation: blink-cursor 0.8s infinite; }}
      .cone-float {{ animation: float-cone 4.5s infinite ease-in-out; transform-origin: 405px 60px; }}
      .rog-rgb {{ animation: rog-color-shift 4s linear infinite; }}
    </style>
  </defs>

  <!-- Clean Base Hero PNG (Boy avatar stays 100% static) -->
  <image href="{data_uri}" x="0" y="0" width="1024" height="448"/>

  <!-- SVG VECTOR ANIMATED TYPING TEXT -->

  <!-- Line 1: Hi! I'm -->
  <g class="type-line-1">
    <text x="45" y="90" class="sans extrabold" font-size="46" fill="#FFFFFF" letter-spacing="-1">Hi! <tspan fill="url(#text-purple-grad)">I’m</tspan></text>
  </g>

  <!-- Line 2: Swapnil Patil. -->
  <g class="type-line-2">
    <text x="45" y="165" class="sans extrabold" font-size="56" fill="url(#name-grad)" letter-spacing="-1.5">Swapnil Patil.</text>
  </g>

  <!-- Horizontal Accent Line -->
  <g class="type-line-2">
    <line x1="45" y1="200" x2="430" y2="200" stroke="#334155" stroke-width="2.5" stroke-linecap="round"/>
  </g>

  <!-- Line 3: Aspiring AI/ML Engineer -->
  <g class="type-line-3">
    <text x="45" y="275" class="sans extrabold" font-size="38" fill="#FFFFFF" letter-spacing="-0.5">Aspiring <tspan fill="url(#aiml-grad)">AI/ML Engineer</tspan></text>
  </g>

  <!-- Line 4: Subtitle -->
  <g class="type-line-4">
    <text x="45" y="325" class="sans" font-size="15" fill="#94A3B8" letter-spacing="0">with a passion for solving problems that involve creativity and innovation</text>
    <rect x="525" y="312" width="8" height="18" fill="#22D3EE" class="cursor"/>
  </g>


  <!-- Floating 3D Cone (Top Left) -->
  <g class="cone-float">
    <circle cx="405" cy="65" r="18" fill="#C084FC" opacity="0.15"/>
  </g>

  <!-- Top Right LIVE Status Tag Overlay -->
  <g transform="translate(885, 18)">
    <rect x="0" y="0" width="122" height="24" rx="12" fill="#0F172A" stroke="#334155" stroke-width="1.2" opacity="0.95"/>
    <circle cx="15" cy="12" r="4" fill="#10B981" class="cursor"/>
    <text x="26" y="16" class="mono bold" font-size="10" fill="#10B981" letter-spacing="0.5">SYS.ACTIVE</text>
  </g>
</svg>'''

    with open(os.path.join(target_dir, 'header_hero_dark.svg'), 'w', encoding='utf-8') as f:
        f.write(hero_svg)
    with open(os.path.join(target_dir, 'header_hero_light.svg'), 'w', encoding='utf-8') as f:
        f.write(hero_svg)

    print("Header hero SVGs generated with vector typing text animation.")

if __name__ == '__main__':
    generate_hero_headers()
