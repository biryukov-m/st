from PIL import Image

im = Image.open('oxygen.png')
print(im.width)
print(im.height)
print(im.getpixel((0,0)))
pxls = [im.getpixel((x, im.height/2)) for x in range(im.width)]
pxls = pxls[::7]
print(pxls)
ords = [r for r, g, b, a in pxls if r == g == b]
print(ords)
print(''.join(list(map(chr, ords))))
back = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print(''.join(list(map(chr, back))))