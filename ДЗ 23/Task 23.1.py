from PIL import Image, ImageFilter, ImageDraw


path = '/home/nikolay/cute.png'

image = Image.open(path)

def greyer(img):
   draw = ImageDraw.Draw(img)
   width = image.size[0]
   height = image.size[1]
   pix = image.load()

   for x in range(width):
       for y in range(height):
          red = pix[x, y][0]
          green = pix[x, y][1]
          blue = pix[x, y][2]
          sr = (red + green + blue) // 3
          draw.point((x, y), (sr, sr, sr))

   image.save('/home/nikolay/all_grey.png', 'PNG')


def inverser(img):
   draw = ImageDraw.Draw(img)
   width = image.size[0]
   height = image.size[1]
   pix = image.load()

   for x in range(width):
       for y in range(height):
           red = pix[x, y][0]
           green = pix[x, y][1]
           blue = pix[x, y][2]
           sr = (red + green + blue) // 3
           draw.point((x, y), (255 - sr, 255 - sr, 255 - sr))

   image.save('/home/nikolay/inverse.png', 'PNG')


def negativer(img):
   draw = ImageDraw.Draw(img)
   width = image.size[0]
   height = image.size[1]
   pix = image.load()

   for x in range(width):
      for y in range(height):
         red = pix[x, y][0]
         green = pix[x, y][1]
         blue = pix[x, y][2]
         draw.point((x, y), (255 - red, 255 - green, 255 - blue))

   image.save('/home/nikolay/negative.png', 'PNG')


def bluer(img):
   draw = ImageDraw.Draw(img)
   width = image.size[0]
   height = image.size[1]
   pix = image.load()

   for x in range(width):
       for y in range(height):
           red = pix[x, y][0]
           green = pix[x, y][1]
           blue = pix[x, y][2]
           sr = (red + green + blue) // 3
           draw.point((x, y), (255 - sr, 255 - sr, 255))

   image.show()
   image.save('/home/nikolay/all_blue.png', 'PNG')


def somth(img):
   draw = ImageDraw.Draw(img)
   width = image.size[0]
   height = image.size[1]
   pix = image.load()

   km = (0, 0, 0,
         0, 1, 0,
         0, 0, 0)

   k = ImageFilter.Kernel(
       size=(3, 3),
       kernel=km,
       scale=sum(km),
       offset=0)

   for x in range(width):
       for y in range(height):
           red = pix[x, y][0] // 4
           green = pix[x, y][1] // 4
           blue = pix[x, y][2] * 2
           draw.point((x, y), (255 - red, 255 - green, 255 - blue))

   img.filter(k)

   image.show()
   image.save('/home/nikolay/somth.png', 'PNG')


somth(image)
