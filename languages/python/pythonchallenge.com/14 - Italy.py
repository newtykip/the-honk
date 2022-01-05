from PIL import Image

img = Image.open('wire.png')
print(img.size) # the real size is actually 10000x1, not 100x100

out = Image.new('RGB', (100, 100))
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)] # spiral!
x = -1
y = 0
p = 0
d = 200

while (d / 2) > 0:
    for v in delta:
        steps = d // 2
        for s in range(steps):
            x = x + v[0]
            y = y + v[1]
            out.putpixel((x, y), img.getpixel((p, 0)))
            p += 1
        d -= 1

out.save('level14.jpg')