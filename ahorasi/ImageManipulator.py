from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageFont
from os import listdir, path
import imghdr



def add_text(image_path, phrase, size):
		im = Image.open(image_path)
		im.save("static/imagenes/salida.jpg")

		f = ImageFont.truetype("fonts/HelveticaNeue Medium.ttf", size)
		draw = ImageDraw.Draw(im)
		width, height = im.size
		draw.text((width * 0.1, height * 0.1), phrase, fill='black', font=f, anchor=None)

		im.save("static/imagenes/salida2.jpg")




