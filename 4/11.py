import image

scale = 2

img = image.Image("luther.jpg")
newimg = image.EmptyImage(img.getWidth()*2, img.getHeight()*2)
win = image.ImageWin()


for col in range(img.getWidth()):
    for row in range(img.getHeight()):
        p = img.getPixel(col, row)
        newimg.setPixel(2*col, 2*row, p)
        newimg.setPixel(2*col+1, 2*row, p)
        newimg.setPixel(2*col, 2*row+1, p)
        newimg.setPixel(2*col+1, 2*row+1, p)

newimg.draw(win)
win.exitonclick()