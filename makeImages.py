cellSize = 50
images = {}
im = ImageObject('custom-images/leaf.png')
im = ImageObject()
with im:
    size(cellSize, cellSize)
    font('myleaves curvepoint', cellSize*2.5)
    text('b', (0, 0))
images['b'] = im

# derive d, p, q from b
d = ImageObject()
with d:
    translate(im.size()[0], 0)
    scale(-1, 1)
    image(im, (0, 0))
images['d'] = d

p = ImageObject()
with p:
    translate(0, im.size()[1])
    scale(1, -1)
    image(im, (0, 0))
images['p'] = p

q = ImageObject()
with q:
    translate(*im.size())
    scale(-1, -1)
    image(im, (0, 0))
images['q'] = q

for char in images:
    newDrawing()
    newPage(cellSize, cellSize)
    image(images[char], (0, 0))
    saveImage(f'images/{char}.png')
    