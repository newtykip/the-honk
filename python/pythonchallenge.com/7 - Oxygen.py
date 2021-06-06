import re
from PIL import Image

img = Image.open('oxygen.png')
row = [img.getpixel((x, img.height / 2)) for x in range(img.width)][::7]
ords = [r for r, g, b, a in row if r == g == b]
msg = ''.join(map(chr, ords))
nums = re.findall('\d+', msg)
nextLevel = ''.join(map(chr, map(int, nums)))

print(nextLevel)