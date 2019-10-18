# Stephen Wang

# Imports the Image portion of the PIL image library.
from PIL import Image

# Assigns the image to bear.
bear = Image.open("bear.png")

def invert( im ):
    ''' Invert the colors in the input image, im '''
    
    # Find the dimensions of the image
    (width, height) = im.size

    # Loop over the entire image
    for x in range( width ):
        for y in range( height ):
            (red, green, blue) = im.getpixel((x, y))
            im.putpixel( (x, y) , (255 - red, 255 - green, 255 - blue) )

# Calls invert function on bear.
invert(bear)

# Displays the image assigned to bear.
bear.show()

# Saves the new bear image to newbear.
bear.save("newbear", "png")

# Tests invert function with a different image.
redpanda = Image.open("redpanda.jpg")
invert(redpanda)
redpanda.show()

def invert_block( im ):
    """ Inverts the upper right quadrant of the image. """

    # Find the dimensions of the image
    (width, height) = im.size

    # Loop over the upper right quadrant of the image
    for x in range( width // 2, width ):
        for y in range( height // 2):
            (red, green, blue) = im.getpixel((x, y))
            im.putpixel( (x, y) , (255 - red, 255 - green, 255 - blue) )

invert_block(bear)
bear.show()

