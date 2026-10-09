import os

def create_dark_svg():
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 460" width="100%" height="100%">
  <defs>
    <linearGradient id="bg-grad-dark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A101F"/>
      <stop offset="100%" stop-color="#070B14"/>
    </linearGradient>
    <linearGradient id="border-grad-dark" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#22D3EE" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#A78BFA" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#10B981" stop-opacity="0.8"/>
    </linearGradient>
    <linearGradient id="portrait-glow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#A78BFA" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#7C3AED" stop-opacity="0.05"/>
    </linearGradient>
    <linearGradient id="text-highlight" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#22D3EE"/>
      <stop offset="100%" stop-color="#A78BFA"/>
    </linearGradient>
    <radialGradient id="cyber-grid-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#22D3EE" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#0A101F" stop-opacity="0"/>
    </radialGradient>
    
    <style>
      .mono { font-family: 'Fira Code', 'Cascadia Code', 'JetBrains Mono', Consolas, monospace; }
      .sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
      .bold { font-weight: 700; }
      .dim { fill: #64748B; }
      .cyan { fill: #22D3EE; }
      .purple { fill: #A78BFA; }
      .green { fill: #10B981; }
      .white { fill: #F8FAFC; }
      .dotted { stroke: #334155; stroke-width: 1.5; stroke-dasharray: 2 6; }
      
      @keyframes pulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.4; transform: scale(0.95); }
      }
      @keyframes radar-sweep {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
      }
      @keyframes logo-morph {
        0%, 30% { opacity: 1; transform: scale(1); }
        33%, 63% { opacity: 0; transform: scale(0.8); }
        66%, 96% { opacity: 0; transform: scale(0.8); }
      }
      @keyframes logo-morph-2 {
        0%, 30% { opacity: 0; transform: scale(0.8); }
        33%, 63% { opacity: 1; transform: scale(1); }
        66%, 96% { opacity: 0; transform: scale(0.8); }
      }
      @keyframes logo-morph-3 {
        0%, 63% { opacity: 0; transform: scale(0.8); }
        66%, 96% { opacity: 1; transform: scale(1); }
        100% { opacity: 0; transform: scale(0.8); }
      }
      @keyframes scanline {
        0% { transform: translateY(0); }
        100% { transform: translateY(320px); }
      }
      .live-dot { animation: pulse 2s infinite ease-in-out; transform-origin: 1115px 33px; }
      .radar { animation: radar-sweep 12s linear infinite; transform-origin: 240px 240px; }
      .morph-1 { animation: logo-morph 9s infinite ease-in-out; transform-origin: 240px 240px; }
      .morph-2 { animation: logo-morph-2 9s infinite ease-in-out; transform-origin: 240px 240px; }
      .morph-3 { animation: logo-morph-3 9s infinite ease-in-out; transform-origin: 240px 240px; }
    </style>
  </defs>

  <!-- Main Background Container -->
  <rect x="2" y="2" width="1176" height="456" rx="12" fill="url(#bg-grad-dark)" stroke="url(#border-grad-dark)" stroke-width="2"/>

  <!-- Terminal Window Header -->
  <path d="M 2 14 C 2 7 7 2 14 2 L 1166 2 C 1173 2 1178 7 1178 14 L 1178 48 L 2 48 Z" fill="#0F172A"/>
  <line x1="2" y1="48" x2="1178" y2="48" stroke="#1E293B" stroke-width="1.5"/>

  <!-- Window Control Buttons -->
  <circle cx="24" cy="25" r="6" fill="#EF4444"/>
  <circle cx="44" cy="25" r="6" fill="#F59E0B"/>
  <circle cx="64" cy="25" r="6" fill="#10B981"/>

  <!-- Window Title -->
  <text x="590" y="30" text-anchor="middle" class="mono bold" font-size="13" fill="#94A3B8" letter-spacing="1">profile.sh --live</text>

  <!-- LIVE Badge & User Pill -->
  <rect x="1000" y="15" width="162" height="22" rx="11" fill="#1E293B" stroke="#334155" stroke-width="1"/>
  <circle cx="1015" cy="26" r="4" fill="#EF4444" class="live-dot"/>
  <text x="1025" y="30" class="mono bold" font-size="10" fill="#EF4444" letter-spacing="0.5">LIVE</text>
  <text x="1060" y="30" class="mono" font-size="11" fill="#22D3EE">@swapnil3104</text>

  <!-- LEFT PANEL: VISUAL.MAP (Portrait Frame & Cyber Matrix) -->
  <g transform="translate(30, 70)">
    <!-- Frame Box -->
    <rect x="0" y="0" width="380" height="360" rx="8" fill="#0D1527" stroke="#1E293B" stroke-width="1.5"/>
    
    <!-- Visual Map Label -->
    <rect x="15" y="12" width="100" height="20" rx="4" fill="#1E293B"/>
    <text x="65" y="26" text-anchor="middle" class="mono bold" font-size="10" fill="#A78BFA" letter-spacing="1">VISUAL.MAP</text>
    <text x="365" y="26" text-anchor="end" class="mono" font-size="10" fill="#475569">SYS.ID // 3104</text>

    <!-- Radar / Dither Grid Effect -->
    <circle cx="190" cy="185" r="130" fill="url(#cyber-grid-glow)"/>
    <circle cx="190" cy="185" r="130" fill="none" stroke="#1E293B" stroke-width="1" stroke-dasharray="4 4"/>
    <circle cx="190" cy="185" r="95" fill="none" stroke="#1E293B" stroke-width="1"/>
    <circle cx="190" cy="185" r="60" fill="none" stroke="#1E293B" stroke-width="1" stroke-dasharray="2 2"/>
    
    <!-- Crosshairs -->
    <line x1="190" y1="45" x2="190" y2="325" stroke="#1E293B" stroke-width="1"/>
    <line x1="50" y1="185" x2="330" y2="185" stroke="#1E293B" stroke-width="1"/>

    <!-- Rotating Radar Line -->
    <g class="radar">
      <line x1="190" y1="185" x2="320" y2="185" stroke="#22D3EE" stroke-width="1.5" opacity="0.6"/>
    </g>

    <!-- Center Morphing Tech Logos / Dither Core -->
    <!-- Logo 1: AI / Brain / Code Glyph -->
    <g class="morph-1" transform="translate(145, 140)">
      <rect x="0" y="0" width="90" height="90" rx="16" fill="#1E1B4B" stroke="#7C3AED" stroke-width="2"/>
      <path d="M 25 30 L 40 45 L 25 60 M 65 30 L 50 45 L 65 60 M 40 65 L 50 25" stroke="#A78BFA" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
      <text x="45" y="82" text-anchor="middle" class="mono bold" font-size="9" fill="#A78BFA">AI / CORE</text>
    </g>

    <!-- Logo 2: Python / ML -->
    <g class="morph-2" transform="translate(145, 140)">
      <rect x="0" y="0" width="90" height="90" rx="16" fill="#062C43" stroke="#22D3EE" stroke-width="2"/>
      <path d="M 43 20 C 32 20 28 24 28 31 L 28 37 L 43 37 L 43 39 L 23 39 C 17 39 15 44 15 53 C 15 62 18 67 25 67 L 30 67 L 30 60 C 30 52 35 48 44 48 L 56 48 C 61 48 65 44 65 39 L 65 31 C 65 24 60 20 43 20 Z" fill="#22D3EE"/>
      <circle cx="34" cy="27" r="2.5" fill="#062C43"/>
      <path d="M 47 70 C 58 70 62 66 62 59 L 62 53 L 47 53 L 47 51 L 67 51 C 73 51 75 46 75 37 C 75 28 72 23 65 23 L 60 23 L 60 30 C 60 38 55 42 46 42 L 34 42 C 29 42 25 46 25 51 L 25 59 C 25 66 30 70 47 70 Z" fill="#10B981"/>
      <circle cx="56" cy="63" r="2.5" fill="#062C43"/>
      <text x="45" y="82" text-anchor="middle" class="mono bold" font-size="9" fill="#22D3EE">PYTHON / ML</text>
    </g>

    <!-- Logo 3: React / UI-UX -->
    <g class="morph-3" transform="translate(145, 140)">
      <rect x="0" y="0" width="90" height="90" rx="16" fill="#064E3B" stroke="#10B981" stroke-width="2"/>
      <ellipse cx="45" cy="45" rx="28" ry="10" fill="none" stroke="#10B981" stroke-width="2.5" transform="rotate(30 45 45)"/>
      <ellipse cx="45" cy="45" rx="28" ry="10" fill="none" stroke="#10B981" stroke-width="2.5" transform="rotate(90 45 45)"/>
      <ellipse cx="45" cy="45" rx="28" ry="10" fill="none" stroke="#10B981" stroke-width="2.5" transform="rotate(150 45 45)"/>
      <circle cx="45" cy="45" r="5" fill="#10B981"/>
      <text x="45" y="82" text-anchor="middle" class="mono bold" font-size="9" fill="#10B981">DEV / STACK</text>
    </g>

    <!-- Bottom Status Bar -->
    <rect x="15" y="325" width="350" height="22" rx="4" fill="#1E293B"/>
    <text x="25" y="340" class="mono" font-size="10" fill="#10B981">STATUS: ONLINE</text>
    <text x="355" y="340" text-anchor="end" class="mono" font-size="10" fill="#A78BFA">DITHER MATRIX v2.4</text>
  </g>

  <!-- RIGHT PANEL: SYSTEM.INFO Readout -->
  <g transform="translate(440, 70)">
    <!-- Header Box -->
    <rect x="0" y="0" width="710" height="360" rx="8" fill="#0D1527" stroke="#1E293B" stroke-width="1.5"/>

    <text x="25" y="32" class="mono bold" font-size="12" fill="#22D3EE" letter-spacing="1.5">SYSTEM.INFO // DEVELOPER SPECIFICATION</text>
    <line x1="25" y1="42" x2="685" y2="42" stroke="#1E293B" stroke-width="1.5"/>

    <!-- Data Rows with Dotted Leaders -->
    
    <!-- Row 1: Subject -->
    <g transform="translate(25, 70)">
      <text x="0" y="0" class="mono bold" font-size="13" fill="#94A3B8">Subject</text>
      <line x1="75" y1="-4" x2="270" y2="-4" class="dotted"/>
      <text x="280" y="0" class="mono bold" font-size="14" fill="#F8FAFC">Swapnil Sanjay Patil</text>
    </g>

    <!-- Row 2: Role -->
    <g transform="translate(25, 100)">
      <text x="0" y="0" class="mono bold" font-size="13" fill="#94A3B8">Role</text>
      <line x1="50" y1="-4" x2="270" y2="-4" class="dotted"/>
      <text x="280" y="0" class="mono bold" font-size="13" fill="#22D3EE">Computer Science Engineer</text>
    </g>

    <!-- Row 3: Focus -->
    <g transform="translate(25, 130)">
      <text x="0" y="0" class="mono bold" font-size="13" fill="#94A3B8">Focus</text>
      <line x1="60" y1="-4" x2="270" y2="-4" class="dotted"/>
      <text x="280" y="0" class="mono" font-size="13" fill="#A78BFA">AI / ML · Data Analytics · UI/UX</text>
    </g>

    <!-- Row 4: Status -->
    <g transform="translate(25, 160)">
      <text x="0" y="0" class="mono bold" font-size="13" fill="#94A3B8">Status</text>
      <line x1="65" y1="-4" x2="270" y2="-4" class="dotted"/>
      <rect x="280" y="-14" width="220" height="20" rx="4" fill="#064E3B"/>
      <text x="290" y="0" class="mono bold" font-size="11" fill="#10B981">Building + Learning + Shipping 🚀</text>
    </g>

    <!-- Row 5: Core.Lang -->
    <g transform="translate(25, 195)">
      <text x="0" y="0" class="mono bold" font-size="13" fill="#94A3B8">Core.Lang</text>
      <line x1="95" y1="-4" x2="270" y2="-4" class="dotted"/>
      <text x="280" y="0" class="mono" font-size="12" fill="#CBD5E1">Python · C++ · JavaScript · C · PHP</text>
    </g>

    <!-- Row 6: Core.AI_ML -->
    <g transform="translate(25, 225)">
      <text x="0" y="0" class="mono bold" font-size="13" fill="#94A3B8">Core.AI_ML</text>
      <line x1="100" y1="-4" x2="270" y2="-4" class="dotted"/>
      <text x="280" y="0" class="mono" font-size="12" fill="#22D3EE">PyTorch · TensorFlow · OpenCV · Scikit-Learn</text>
    </g>

    <!-- Row 7: Core.WebUI -->
    <g transform="translate(25, 255)">
      <text x="0" y="0" class="mono bold" font-size="13" fill="#94A3B8">Core.WebUI</text>
      <line x1="100" y1="-4" x2="270" y2="-4" class="dotted"/>
      <text x="280" y="0" class="mono" font-size="12" fill="#A78BFA">React · React Native · Three.js · Vite · Node.js</text>
    </g>

    <!-- Row 8: Core.Tools -->
    <g transform="translate(25, 285)">
      <text x="0" y="0" class="mono bold" font-size="13" fill="#94A3B8">Core.Tools</text>
      <line x1="100" y1="-4" x2="270" y2="-4" class="dotted"/>
      <text x="280" y="0" class="mono" font-size="12" fill="#CBD5E1">Figma · Blender · Adobe Photoshop · Git</text>
    </g>

    <!-- Bottom Info Grid Badges -->
    <line x1="25" y1="308" x2="685" y2="308" stroke="#1E293B" stroke-width="1.5"/>
    <g transform="translate(25, 335)">
      <text x="0" y="0" class="mono" font-size="11" fill="#64748B">MAIL: <tspan fill="#22D3EE">swapnilp3104@gmail.com</tspan></text>
      <text x="310" y="0" class="mono" font-size="11" fill="#64748B">LOC: <tspan fill="#10B981">India 🇮🇳</tspan></text>
      <text x="520" y="0" class="mono" font-size="11" fill="#64748B">GITHUB: <tspan fill="#A78BFA">@swapnil3104</tspan></text>
    </g>
  </g>
</svg>'''
    return svg_content

def create_light_svg():
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 460" width="100%" height="100%">
  <defs>
    <linearGradient id="bg-grad-light" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F8FAFC"/>
      <stop offset="100%" stop-color="#F1F5F9"/>
    </linearGradient>
    <linearGradient id="border-grad-light" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0891B2" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#7C3AED" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#059669" stop-opacity="0.8"/>
    </linearGradient>
    
    <style>
      .mono { font-family: 'Fira Code', 'Cascadia Code', 'JetBrains Mono', Consolas, monospace; }
      .bold { font-weight: 700; }
      .dotted { stroke: #CBD5E1; stroke-width: 1.5; stroke-dasharray: 2 6; }
      
      @keyframes pulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.4; transform: scale(0.95); }
      }
      @keyframes radar-sweep {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
      }
      @keyframes logo-morph {
        0%, 30% { opacity: 1; transform: scale(1); }
        33%, 63% { opacity: 0; transform: scale(0.8); }
        66%, 96% { opacity: 0; transform: scale(0.8); }
      }
      @keyframes logo-morph-2 {
        0%, 30% { opacity: 0; transform: scale(0.8); }
        33%, 63% { opacity: 1; transform: scale(1); }
        66%, 96% { opacity: 0; transform: scale(0.8); }
      }
      @keyframes logo-morph-3 {
        0%, 63% { opacity: 0; transform: scale(0.8); }
        66%, 96% { opacity: 1; transform: scale(1); }
        100% { opacity: 0; transform: scale(0.8); }
      }
      .live-dot { animation: pulse 2s infinite ease-in-out; transform-origin: 1115px 33px; }
      .radar { animation: radar-sweep 12s linear infinite; transform-origin: 240px 240px; }
      .morph-1 { animation: logo-morph 9s infinite ease-in-out; transform-origin: 240px 240px; }
      .morph-2 { animation: logo-morph-2 9s infinite ease-in-out; transform-origin: 240px 240px; }
      .morph-3 { animation: logo-morph-3 9s infinite ease-in-out; transform-origin: 240px 240px; }
    </style>
  </defs>

  <!-- Main Background Container -->
  <rect x="2" y="2" width="1176" height="456" rx="12" fill="url(#bg-grad-light)" stroke="url(#border-grad-light)" stroke-width="2"/>

  <!-- Terminal Window Header -->
  <path d="M 2 14 C 2 7 7 2 14 2 L 1166 2 C 1173 2 1178 7 1178 14 L 1178 48 L 2 48 Z" fill="#E2E8F0"/>
  <line x1="2" y1="48" x2="1178" y2="48" stroke="#CBD5E1" stroke-width="1.5"/>

  <!-- Window Control Buttons -->
  <circle cx="24" cy="25" r="6" fill="#EF4444"/>
  <circle cx="44" cy="25" r="6" fill="#F59E0B"/>
  <circle cx="64" cy="25" r="6" fill="#10B981"/>

  <!-- Window Title -->
  <text x="590" y="30" text-anchor="middle" class="mono bold" font-size="13" fill="#475569" letter-spacing="1">profile.sh --live</text>

  <!-- LIVE Badge & User Pill -->
  <rect x="1000" y="15" width="162" height="22" rx="11" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <circle cx="1015" cy="26" r="4" fill="#DC2626" class="live-dot"/>
  <text x="1025" y="30" class="mono bold" font-size="10" fill="#DC2626" letter-spacing="0.5">LIVE</text>
  <text x="1060" y="30" class="mono" font-size="11" fill="#0891B2">@swapnil3104</text>

  <!-- LEFT PANEL: VISUAL.MAP (Portrait Frame & Cyber Matrix) -->
  <g transform="translate(30, 70)">
    <!-- Frame Box -->
    <rect x="0" y="0" width="380" height="360" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
    
    <!-- Visual Map Label -->
    <rect x="15" y="12" width="100" height="20" rx="4" fill="#F1F5F9"/>
    <text x="65" y="26" text-anchor="middle" class="mono bold" font-size="10" fill="#7C3AED" letter-spacing="1">VISUAL.MAP</text>
    <text x="365" y="26" text-anchor="end" class="mono" font-size="10" fill="#94A3B8">SYS.ID // 3104</text>

    <!-- Radar Grid Effect -->
    <circle cx="190" cy="185" r="130" fill="none" stroke="#E2E8F0" stroke-width="1" stroke-dasharray="4 4"/>
    <circle cx="190" cy="185" r="95" fill="none" stroke="#E2E8F0" stroke-width="1"/>
    <circle cx="190" cy="185" r="60" fill="none" stroke="#E2E8F0" stroke-width="1" stroke-dasharray="2 2"/>
    
    <!-- Crosshairs -->
    <line x1="190" y1="45" x2="190" y2="325" stroke="#E2E8F0" stroke-width="1"/>
    <line x1="50" y1="185" x2="330" y2="185" stroke="#E2E8F0" stroke-width="1"/>

    <!-- Rotating Radar Line -->
    <g class="radar">
      <line x1="190" y1="185" x2="320" y2="185" stroke="#0891B2" stroke-width="1.5" opacity="0.6"/>
    </g>

    <!-- Center Morphing Tech Logos -->
    <g class="morph-1" transform="translate(145, 140)">
      <rect x="0" y="0" width="90" height="90" rx="16" fill="#F3E8FF" stroke="#7C3AED" stroke-width="2"/>
      <path d="M 25 30 L 40 45 L 25 60 M 65 30 L 50 45 L 65 60 M 40 65 L 50 25" stroke="#6D28D9" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
      <text x="45" y="82" text-anchor="middle" class="mono bold" font-size="9" fill="#6D28D9">AI / CORE</text>
    </g>

    <g class="morph-2" transform="translate(145, 140)">
      <rect x="0" y="0" width="90" height="90" rx="16" fill="#CFFAFE" stroke="#0891B2" stroke-width="2"/>
      <path d="M 43 20 C 32 20 28 24 28 31 L 28 37 L 43 37 L 43 39 L 23 39 C 17 39 15 44 15 53 C 15 62 18 67 25 67 L 30 67 L 30 60 C 30 52 35 48 44 48 L 56 48 C 61 48 65 44 65 39 L 65 31 C 65 24 60 20 43 20 Z" fill="#0891B2"/>
      <circle cx="34" cy="27" r="2.5" fill="#CFFAFE"/>
      <path d="M 47 70 C 58 70 62 66 62 59 L 62 53 L 47 53 L 47 51 L 67 51 C 73 51 75 46 75 37 C 75 28 72 23 65 23 L 60 23 L 60 30 C 60 38 55 42 46 42 L 34 42 C 29 42 25 46 25 51 L 25 59 C 25 66 30 70 47 70 Z" fill="#059669"/>
      <circle cx="56" cy="63" r="2.5" fill="#CFFAFE"/>
      <text x="45" y="82" text-anchor="middle" class="mono bold" font-size="9" fill="#0891B2">PYTHON / ML</text>
    </g>

    <g class="morph-3" transform="translate(145, 140)">
      <rect x="0" y="0" width="90" height="90" rx="16" fill="#D1FAE5" stroke="#059669" stroke-width="2"/>
      <ellipse cx="45" cy="45" rx="28" ry="10" fill="none" stroke="#059669" stroke-width="2.5" transform="rotate(30 45 45)"/>
      <ellipse cx="45" cy="45" rx="28" ry="10" fill="none" stroke="#059669" stroke-width="2.5" transform="rotate(90 45 45)"/>
      <ellipse cx="45" cy="45" rx="28" ry="10" fill="none" stroke="#059669" stroke-width="2.5" transform="rotate(150 45 45)"/>
      <circle cx="45" cy="45" r="5" fill="#059669"/>
      <text x="45" y="82" text-anchor="middle" class="mono bold" font-size="9" fill="#059669">DEV / STACK</text>
    </g>

    <!-- Bottom Status Bar -->
    <rect x="15" y="325" width="350" height="22" rx="4" fill="#F1F5F9"/>
    <text x="25" y="340" class="mono" font-size="10" fill="#059669">STATUS: ONLINE</text>
    <text x="355" y="340" text-anchor="end" class="mono" font-size="10" fill="#7C3AED">DITHER MATRIX v2.4</text>
  </g>

  <!-- RIGHT PANEL: SYSTEM.INFO Readout -->
  <g transform="translate(440, 70)">
    <!-- Header Box -->
    <rect x="0" y="0" width="710" height="360" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>

    <text x="25" y="32" class="mono bold" font-size="12" fill="#0891B2" letter-spacing="1.5">SYSTEM.INFO // DEVELOPER SPECIFICATION</text>
    <line x1="25" y1="42" x2="685" y2="42" stroke="#E2E8F0" stroke-width="1.5"/>

    <!-- Data Rows -->
    <g transform="translate(25, 70)">
      <text x="0" y="0" class="mono bold" font-size="13" fill="#64748B">Subject</text>
      <line x1="75" y1="-4" x2="270" y2="-4" class="dotted"/>
      <text x="280" y="0" class="mono bold" font-size="14" fill="#0F172A">Swapnil Sanjay Patil</text>
    </g>

    <g transform="translate(25, 100)">
      <text x="0" y="0" class="mono bold" font-size="13" fill="#64748B">Role</text>
      <line x1="50" y1="-4" x2="270" y2="-4" class="dotted"/>
      <text x="280" y="0" class="mono bold" font-size="13" fill="#0891B2">Computer Science Engineer</text>
    </g>

    <g transform="translate(25, 130)">
      <text x="0" y="0" class="mono bold" font-size="13" fill="#64748B">Focus</text>
      <line x1="60" y1="-4" x2="270" y2="-4" class="dotted"/>
      <text x="280" y="0" class="mono" font-size="13" fill="#7C3AED">AI / ML · Data Analytics · UI/UX</text>
    </g>

    <g transform="translate(25, 160)">
      <text x="0" y="0" class="mono bold" font-size="13" fill="#64748B">Status</text>
      <line x1="65" y1="-4" x2="270" y2="-4" class="dotted"/>
      <rect x="280" y="-14" width="220" height="20" rx="4" fill="#D1FAE5"/>
      <text x="290" y="0" class="mono bold" font-size="11" fill="#059669">Building + Learning + Shipping 🚀</text>
    </g>

    <g transform="translate(25, 195)">
      <text x="0" y="0" class="mono bold" font-size="13" fill="#64748B">Core.Lang</text>
      <line x1="95" y1="-4" x2="270" y2="-4" class="dotted"/>
      <text x="280" y="0" class="mono" font-size="12" fill="#334155">Python · C++ · JavaScript · C · PHP</text>
    </g>

    <g transform="translate(25, 225)">
      <text x="0" y="0" class="mono bold" font-size="13" fill="#64748B">Core.AI_ML</text>
      <line x1="100" y1="-4" x2="270" y2="-4" class="dotted"/>
      <text x="280" y="0" class="mono" font-size="12" fill="#0891B2">PyTorch · TensorFlow · OpenCV · Scikit-Learn</text>
    </g>

    <g transform="translate(25, 255)">
      <text x="0" y="0" class="mono bold" font-size="13" fill="#64748B">Core.WebUI</text>
      <line x1="100" y1="-4" x2="270" y2="-4" class="dotted"/>
      <text x="280" y="0" class="mono" font-size="12" fill="#7C3AED">React · React Native · Three.js · Vite · Node.js</text>
    </g>

    <g transform="translate(25, 285)">
      <text x="0" y="0" class="mono bold" font-size="13" fill="#64748B">Core.Tools</text>
      <line x1="100" y1="-4" x2="270" y2="-4" class="dotted"/>
      <text x="280" y="0" class="mono" font-size="12" fill="#334155">Figma · Blender · Adobe Photoshop · Git</text>
    </g>

    <!-- Bottom Info Grid Badges -->
    <line x1="25" y1="308" x2="685" y2="308" stroke="#E2E8F0" stroke-width="1.5"/>
    <g transform="translate(25, 335)">
      <text x="0" y="0" class="mono" font-size="11" fill="#94A3B8">MAIL: <tspan fill="#0891B2">swapnilp3104@gmail.com</tspan></text>
      <text x="310" y="0" class="mono" font-size="11" fill="#94A3B8">LOC: <tspan fill="#059669">India 🇮🇳</tspan></text>
      <text x="520" y="0" class="mono" font-size="11" fill="#94A3B8">GITHUB: <tspan fill="#7C3AED">@swapnil3104</tspan></text>
    </g>
  </g>
</svg>'''
    return svg_content

if __name__ == '__main__':
    target_dir = r'd:\Downloads\Github Profile'
    with open(os.path.join(target_dir, 'dark.svg'), 'w', encoding='utf-8') as f:
        f.write(create_dark_svg())
    with open(os.path.join(target_dir, 'light.svg'), 'w', encoding='utf-8') as f:
        f.write(create_light_svg())
    print("SVGs generated successfully.")
