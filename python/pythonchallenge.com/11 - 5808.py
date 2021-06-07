from PIL import Image

img = Image.open('cave.jpg')

even = Image.new('RGB', (img.width // 2, img.height // 2))
odd = Image.new('RGB', (img.width // 2, img.height // 2))

for i in range(img.width):
    for j in range(img.height):
        p = img.getpixel((i, j))
        if (i + j) % 2 == 1:
            odd.putpixel((i // 2, j // 2), p)
        else:
            even.putpixel((i // 2, j // 2), p)

even.save('even.jpg')
odd.save('odd.jpg') # evil