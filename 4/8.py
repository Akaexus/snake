
import image

img = image.Image("luther.jpg")
newimg = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin()

for col in range(img.getWidth()):
    for row in range(img.getHeight()):
        p = img.getPixel(col, row)
        x = (p.getRed()+p.getBlue()+p.getGreen())/3

        newpixel = image.Pixel(x, x, x)

        newimg.setPixel(col, row, newpixel)

newimg.draw(win)
win.exitonclick()