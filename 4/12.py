import image

img = image.Image("luther.jpg")
h = img.getHeight()
w = img.getWidth()
newimg = image.EmptyImage(w, h)
win = image.ImageWin(w, h)


def avg(x):
    return sum(x) / len(x)


# for col in range(w):
#     for row in range(h):
#         p = img.getPixel(col, row)
#         newimg.setPixel(2 * col, 2 * row, p)
#         newimg.setPixel(2 * col + 1, 2 * row, p)
#         newimg.setPixel(2 * col, 2 * row + 1, p)
#         newimg.setPixel(2 * col + 1, 2 * row + 1, p)
for col in range(1, w - 1):
    for row in range(1, h - 1):
        indexes = [0, 0], [0, 1], [1, 0], [-1, 0], [0, -1]
        r = []
        g = []
        b = []

        for pixelIndex in indexes:
            pixel = img.getPixel(col + pixelIndex[0], row + pixelIndex[1])
            r.append(pixel.getRed())
            g.append(pixel.getGreen())
            b.append(pixel.getBlue())
        newpixel = image.Pixel(avg(r), avg(g), avg(b))
        newimg.setPixel(col, row, newpixel)

newimg.draw(win)
win.exitonclick()