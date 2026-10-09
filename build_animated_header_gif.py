import os
import math
import colorsys
from PIL import Image, ImageDraw, ImageFilter

def create_animated_header():
    base_img_path = os.path.join(os.path.dirname(__file__), 'header_hero.png')
    base_img = Image.open(base_img_path).convert('RGBA')
    width, height = base_img.size

    # Pre-identify ROG logo red pixels mask in (x=840..940, y=285..350)
    rog_mask_data = []
    for y in range(280, 355):
        for x in range(835, 945):
            r, g, b, a = base_img.getpixel((x, y))
            # Detect red hue pixels of the ROG logo
            if r > 120 and r > g * 1.3 and r > b * 1.3:
                # Store relative luminance and pixel location
                intensity = r / 255.0
                rog_mask_data.append((x, y, intensity))

    frames = []
    num_frames = 36  # 36 smooth frames @ 20fps = 1.8s RGB cycle loop

    for i in range(num_frames):
        t = i / num_frames
        angle = t * 2 * math.pi

        # 1. Base frame copy (Boy avatar remains 100% static & untouched!)
        frame = base_img.copy()

        # 2. RGB Color Cycle strictly applied ONLY to the ROG logo red pixels
        hue = t  # Cycles 0.0 -> 1.0 (Red -> Yellow -> Green -> Cyan -> Blue -> Purple -> Red)
        for x, y, intensity in rog_mask_data:
            # Generate RGB color from hue
            r_c, g_c, b_c = colorsys.hsv_to_rgb(hue, 0.9, intensity)
            frame.putpixel((x, y), (int(r_c * 255), int(g_c * 255), int(b_c * 255), 255))

        # Add a subtle glowing aura around the ROG logo matching the current RGB hue
        r_glow, g_glow, b_glow = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        glow_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        glow_draw = ImageDraw.Draw(glow_layer)
        glow_draw.ellipse(
            [885 - 28, 320 - 28, 885 + 28, 320 + 28],
            fill=(int(r_glow * 255), int(g_glow * 255), int(b_glow * 255), 70)
        )
        glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(12))
        frame = Image.alpha_composite(frame, glow_layer)

        # 3. Floating 3D Cone Motion (Top Left around x=380..430, y=30..110)
        cone_offset = int(7 * math.sin(angle))
        if cone_offset != 0:
            cone_box = (380, 25, 435, 115)
            cone_crop = base_img.crop(cone_box)
            frame.paste(cone_crop, (380, 25 + cone_offset), cone_crop)

        # 4. Text Shimmer Sweep Line across left text (x: 0 -> 520)
        shimmer_x = int(-120 + t * 700)
        shimmer_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        shimmer_draw = ImageDraw.Draw(shimmer_layer)
        
        # Diagonal light sweep over text region (x < 530)
        shimmer_draw.polygon(
            [(shimmer_x, 0), (shimmer_x + 70, 0), (shimmer_x + 20, 448), (shimmer_x - 50, 448)],
            fill=(255, 255, 255, 40)
        )
        shimmer_layer = shimmer_layer.filter(ImageFilter.GaussianBlur(14))
        
        # Mask shimmer strictly to left text area (x < 530)
        text_mask = Image.new('L', (width, height), 0)
        mask_draw = ImageDraw.Draw(text_mask)
        mask_draw.rectangle([0, 0, 520, 448], fill=255)
        
        frame.paste(Image.alpha_composite(frame, shimmer_layer), (0, 0), text_mask)

        # Append frame
        frames.append(frame)

    output_gif_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'header_hero_animated.gif')
    
    # Quantize frames to 128 colors for optimal loading speed & small file size
    q_frames = [f.convert('RGB').quantize(colors=128, method=Image.Quantize.MEDIANCUT) for f in frames]
    q_frames[0].save(
        output_gif_path,
        save_all=True,
        append_images=q_frames[1:],
        duration=50,  # 50ms per frame = 20 fps
        loop=0,
        optimize=True
    )
    print(f"Animated GIF saved to {output_gif_path} ({os.path.getsize(output_gif_path)} bytes)")

if __name__ == '__main__':
    create_animated_header()
