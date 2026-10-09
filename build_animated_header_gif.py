import os
import math
import colorsys
from PIL import Image, ImageDraw, ImageFilter

def create_animated_header():
    target_dir = os.path.dirname(os.path.abspath(__file__))
    base_img_path = os.path.join(target_dir, 'header_hero.png')
    base_img = Image.open(base_img_path).convert('RGBA')
    width, height = base_img.size

    # 1. Identify ROG logo red pixels strictly in (x=835..945, y=280..355)
    rog_pixels = []
    for y in range(280, 355):
        for x in range(835, 945):
            r, g, b, a = base_img.getpixel((x, y))
            # Detect red hue of the ROG logo icon
            if r > 110 and r > g * 1.35 and r > b * 1.35:
                # Convert to HSV to preserve saturation and brightness shading
                h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
                rog_pixels.append((x, y, h, s, v))

    print(f"Detected {len(rog_pixels)} ROG red logo pixels.")

    # 2. Identify floating 3D elements bounding boxes
    # Top-left cone around x=380..435, y=25..110
    cone_box = (380, 25, 435, 115)
    cone_crop = base_img.crop(cone_box)

    # Top-right purple shape around x=935..990, y=10..70
    tr_box = (935, 10, 990, 70)
    tr_crop = base_img.crop(tr_box)

    # Mid-right small purple shape around x=965..1005, y=250..310
    mr_box = (965, 250, 1005, 310)
    mr_crop = base_img.crop(mr_box)

    frames = []
    num_frames = 36  # 36 smooth frames = 1.8s loop at 20fps

    for i in range(num_frames):
        t = i / num_frames
        angle = t * 2 * math.pi

        # Start with base frame (Boy avatar is 100% static & untouched)
        frame = base_img.copy()

        # A. RGB Hue Cycle strictly on ROG Logo
        for x, y, orig_h, s, v in rog_pixels:
            new_h = (orig_h + t) % 1.0
            r_c, g_c, b_c = colorsys.hsv_to_rgb(new_h, s, v)
            frame.putpixel((x, y), (int(r_c * 255), int(g_c * 255), int(b_c * 255), 255))

        # Add matching RGB glow aura strictly around the ROG logo center (885, 320)
        glow_h = t
        r_g, g_g, b_g = colorsys.hsv_to_rgb(glow_h, 1.0, 1.0)
        glow_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        glow_draw = ImageDraw.Draw(glow_layer)
        glow_draw.ellipse(
            [885 - 25, 320 - 25, 885 + 25, 320 + 25],
            fill=(int(r_g * 255), int(g_g * 255), int(b_g * 255), 75)
        )
        glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(10))
        frame = Image.alpha_composite(frame, glow_layer)

        # B. Floating 3D Elements Motion
        # Top-left cone offset
        c_off = int(7 * math.sin(angle))
        if c_off != 0:
            frame.paste(cone_crop, (380, 25 + c_off), cone_crop)

        # Top-right shape offset
        tr_off = int(5 * math.cos(angle))
        if tr_off != 0:
            frame.paste(tr_crop, (935, 10 + tr_off), tr_crop)

        # Mid-right shape offset
        mr_off = int(6 * math.sin(angle + 1))
        if mr_off != 0:
            frame.paste(mr_crop, (965, 250 + mr_off), mr_crop)

        # C. Text Animation (Neon Shimmer Light Sweep on left text)
        shimmer_x = int(-140 + t * 750)
        shimmer_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        shimmer_draw = ImageDraw.Draw(shimmer_layer)
        
        # Diagonal shimmer band across text region
        shimmer_draw.polygon(
            [(shimmer_x, 0), (shimmer_x + 80, 0), (shimmer_x + 30, 448), (shimmer_x - 50, 448)],
            fill=(255, 255, 255, 45)
        )
        shimmer_layer = shimmer_layer.filter(ImageFilter.GaussianBlur(12))
        
        # Mask shimmer strictly to text area (x < 530)
        text_mask = Image.new('L', (width, height), 0)
        mask_draw = ImageDraw.Draw(text_mask)
        mask_draw.rectangle([0, 0, 530, 448], fill=255)
        
        frame.paste(Image.alpha_composite(frame, shimmer_layer), (0, 0), text_mask)

        frames.append(frame)

    output_gif_path = os.path.join(target_dir, 'header_hero_animated.gif')
    
    # Quantize for clean, lightweight GIF animation
    q_frames = [f.convert('RGB').quantize(colors=160, method=Image.Quantize.MEDIANCUT) for f in frames]
    q_frames[0].save(
        output_gif_path,
        save_all=True,
        append_images=q_frames[1:],
        duration=50,  # 50ms = 20fps
        loop=0,
        optimize=True
    )
    print(f"Animated GIF saved to {output_gif_path} ({os.path.getsize(output_gif_path)} bytes)")

if __name__ == '__main__':
    create_animated_header()
