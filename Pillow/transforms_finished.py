# Example file for Python Essential Libraries course by Joe Marini
# demonstrates image transformations using the Pillow library
from PIL import Image, ImageFilter, ImageOps
import os


os.system('cls')
# TODO: use the crop function to crop an image
infile = "BrainHand.jpeg"

# image = Image.open(infile)
# image.show()

# with Image.open(infile) as img:
#     # calculate the middle part
#     midx = img.width / 2
#     midy = img.height / 2
#     croparea = (midy-400, midx-250, midy+400, midx+250)
#     # img.show()

#     cropimg = img.crop(croparea)
#     cropimg.show()

# TODO: perform a simple resize and rotation
# with Image.open(infile) as img:
#     newimg = img.resize((256, 256))
#     # newimg = newimg.rotate(45)
#     newimg.show()

# TODO: use the transpose function with a built-in operation
# with Image.open(infile) as img:
#     newimg = img.transpose(Image.FLIP_TOP_BOTTOM)
#     newimg.show()

# TODO: Use an ImageFilter operation
# with Image.open(infile) as img:
#     newimg = img.filter(ImageFilter.GaussianBlur(20))
#     newimg.show()

# TODO: Use ImageOps for built-in image processing
with Image.open(infile) as img:
    newimg = ImageOps.grayscale(img)
    newimg.show()
