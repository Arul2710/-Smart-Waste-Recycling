from PIL import Image
import os

src = Image.open('assets/icons/src-favicon.png').convert('RGBA')
print('source', src.size)

# main PNG (already 512x512)
src.save('assets/icons/favicon.png', 'PNG', optimize=True)

# multi-size ICO for legacy / default /favicon.ico requests
src.save('assets/icons/favicon.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])

# apple touch icon: iOS composites transparency on black, so flatten onto white
flat = Image.new('RGB', src.size, (255, 255, 255))
flat.paste(src, mask=src.split()[3])
flat.resize((180, 180), Image.LANCZOS).save('assets/icons/apple-touch-icon.png', 'PNG', optimize=True)

for f in ['favicon.png', 'favicon.ico', 'apple-touch-icon.png']:
    p = 'assets/icons/' + f
    im = Image.open(p)
    print('%-22s %-6s %-12s %.1f KB' % (f, im.format, str(im.size), os.path.getsize(p) / 1024))

ico = Image.open('assets/icons/favicon.ico')
print('ico embedded sizes:', sorted(ico.info.get('sizes', [])))
