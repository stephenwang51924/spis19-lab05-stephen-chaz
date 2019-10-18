""" If your name is Jose Falconi-Cavallini please read this docstring. Under 
    each function there are function calls that are commented out. Those are
    only there for testing purposes. """

from PIL import Image
import random

def greyScale(im):
    """ Changes the colors of the image to greyscale. """

    # Assigns the width and height of im to (width, height).
    (width, height) = im.size
    # Nested loop iterating through the entire image.
    for x in range(width):
        for y in range(height):
    # Assigns the RGB values of the pixel at (x, y) to (red, green, blue).
            (red, green, blue) = im.getpixel((x, y))
    # Calculates the luminance based on info from the lab.
            luminance = int(red * .21) + int(green * .62) + int(blue * .07)
    # Changes the RGB values of the pixel at (x, y) to the luminance value.
            im.putpixel((x, y), (luminance, luminance, luminance)) 

bear = Image.open("bear.png")
#greyScale(bear)
#bear.show()

def binarize(im, thresh, startx, starty, endx, endy):
    """ Changes the colors of the image to black and white based on a threshold
        value. """
    
    # Doesn't run and prints warning if binarize called with invalid arguments.
    if startx < 0 or starty < 0 or endx > im.size[0] or endy > im.size[1]:
        print("Box is not within the image size")
        pass
    # Nested loop iterating through box specified by function call.
    for x in range(startx, endx):
        for y in range(starty, endy):
    # Assigns the RGB values of the pixel at (x, y) to (red, green, blue).
            (red, green, blue) = im.getpixel((x, y))
    # Calculates the lumincance based on info from the lab.
            luminance = int(red * .21) + int(green * .62) + int(blue * .07)
    # Changes the pixel to black or white based on comparison with threshold.
            if luminance > thresh:
                im.putpixel((x, y), (255, 255, 255))
            else:
                im.putpixel((x, y), (0, 0, 0))


#binarize(bear, 120, 0, 0, 600, 800)
#bear.show()

def mirrorVert (im):
    """ Mirrors the image across its horizontal axis. """

    # Nested loop iterating through the top half of the image.
    for x in range (im.size[0]):
        for y in range (im.size[1] // 2):
    # Assigns the RGB values of the pixel at (x, y) to (r, g, b).
            (r, g, b) = im.getpixel ( (x, y) )
    # Changes the RGB values of the pixel opposite of (x, y) to (r, g, b).
            im.putpixel ( (x, im.size[1] - y -1), (r, g, b))

#mirrorVert(bear)
#bear.show()

def mirrorHoriz(im):
    """ Mirrors the image across its vertical axis. """

    # Nested loop iterating through the left half of the image.
    for x in range(im.size[0] // 2):
        for y in range(im.size[1]):
    # Assigns the RGB values of the pixel at (x, y) to (r, g, b).
            (r, g, b) = im.getpixel((x, y))
    # Changes the RGB values of the pixel opposite of (x, y) to (r, g, b).
            im.putpixel((im.size[0] - x - 1, y), (r, g, b))

#mirrorHoriz(bear)
#bear.show()

def flipVert(im):
    """ Flips the image upside down. """

    # Nested loop iterating through the top half of the image.
    for x in range (im.size[0]):
        for y in range (im.size[1] // 2):
    # Assigns the RGB values of the pixel at (x, y) to (r, g, b).
            (r, g, b) = im.getpixel((x, y))
    # Assigns the RGB values of the pixel opposite of (x, y) to (r2, g2, b2).
            (r2, g2, b2) = im.getpixel((x, im.size[1] - y - 1))
    # Exchanges the pixels opposite of each other to flip the image.
            im.putpixel((x, im.size[1] - y -1), (r, g, b))
            im.putpixel((x, y), (r2, g2, b2))
           

#flipVert(bear)
#bear.show()

def scale(im):
    """ Scales down the image to a smaller size. """

    # Creates a new image with half the width and height of the original image.
    (width, height) = (im.size[0] // 2, im.size[1] // 2)
    new_bear = Image.new('RGB',(width, height))
    # Nested loop iterating through every other pixel of the original image.
    for x in range(0, im.size[0], 2):
        for y in range(0, im.size[1], 2):
    # Assigns the RGB values of the pixel at (x, y) to (red, green, blue).
            (r, g, b) = im.getpixel((x, y))
    # Puts the pixel in the new image.
            new_bear.putpixel((x // 2, y // 2), (r, g, b))

    return new_bear


#new_image = scale(bear)
#new_image.show()

def blur(im):
    """ Blurs the entire image. """

    # Creates a new image with the same width and height as the original image.
    (width, height) = im.size
    newBear = Image.new('RGB', (width, height))
    # Nested for loop iterating through the bottom right corner of each 2 x 2.
    for x in range(1, width, 2):
        for y in range(1, height, 2):
    # Keeps track of each pixel by assigning their RGB values to variables.
            (r, g, b) = im.getpixel((x, y))
            (r2, g2, b2) = im.getpixel((x - 1, y - 1))
            (r3, g3, b3) = im.getpixel((x - 1, y))
            (r4, g4, b4) = im.getpixel((x, y - 1))
    # Calculates the average RGB values of the pixels in the 2 x 2 square.
            avgRed = (r + r2 + r3 + r4) // 4
            avgGreen = (g + g2 + g3 + g4) // 4
            avgBlue = (b + b2 + b3 + b4) // 4
    # Changes the RGB values in the 2 x 2 square of new image to the average RGB
            newBear.putpixel((x,y), (avgRed, avgGreen, avgBlue))
            newBear.putpixel((x - 1, y - 1), (avgRed, avgGreen, avgBlue))
            newBear.putpixel((x - 1, y), (avgRed, avgGreen, avgBlue))
            newBear.putpixel((x, y - 1), (avgRed, avgGreen, avgBlue))
    # Resets the average values for the next 2 x 2 square in the iteration.
            avgRed = 0
            avgGreen = 0
            avgBlue = 0

    return newBear

#newImage = blur(bear)
#newImage.show()
    
def randomGrid(im):
    """ Splits the image into grids and returns a scrambled version of the
        image. """

    """ The first section of this code takes the original image,
        splits it into 100 x 100 squares, and copies it into a new image. 
        Then, it adds the image object to a list. """

    # Creates a list.
    squareList = []
    (width, height) = im.size
    # Nested loop iterating through the original image with a step of 100.
    for x in range(0, width, 100):
        for y in range(0, height, 100):
    # Creates a new image with width and height of 100.
            newIm = Image.new('RGB', (100, 100))
    # Nested loop iterating through each pixel in the 100 x 100 square.
            for x2 in range(x, x + 100):
                for y2 in range(y, y + 100):
    # Assigns the RGB values at (x2, y2) of the original image to (r, g, b).
                    (r, g, b) = im.getpixel((x2, y2))
    # Changes the RGB values of the pixel of the new image to (r, g, b).
                    newIm.putpixel((x2 - x, y2 - y), (r, g, b))
    # Adds the new image to the list.
            squareList.append(newIm)
    # Randomizes the order of the list.
    random.shuffle(squareList)

    """ Once the list is shuffled,  I copy each 100 x 100 image from the list on        to a new image with the original width and height. This creates the 
        randomized squares. """


    # Creates a new image with the width and height of the original image.
    newIm2 = Image.new('RGB', (width, height))
    # Count keeps track of the index of the list.
    count = 0
    # Nested loop iterating through the new image with a step of 100.
    for x3 in range(0, width, 100):
        for y3 in range(0, height, 100):
    # Nested loop iterating through the 100 x 100 squares in the list.
                for x4 in range(100):
                    for y4 in range(100):
    # Assigns the RGB values of the pixel at (x4, y4) to (r2, g2, b2).
                        (r2, g2, b2) = squareList[count].getpixel((x4, y4))
    # Changes the RGV values of the pixel of the new image to (r2, g2, b2).
                        newIm2.putpixel((x4 + x3, y4 + y3), (r2, g2, b2))
    # Iterates the count to move on to the next 100 x 100 square in the list.
                count += 1
    # Returns the randomized image.
    return newIm2

#newImage = randomGrid(bear)
#newImage.show()
