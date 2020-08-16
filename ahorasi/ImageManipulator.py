from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageFont
from os import listdir, path
import imghdr

def predeterminada(imagen):
	im = Image.open(imagen)
	im.save("static/imagenes/salida.jpg")
def check_image_format(file):
	return isinstance(imghdr.what(file), str)
def add_text(image_path, phrase, size):
		im = Image.open(image_path)


		f = ImageFont.truetype("fonts/HelveticaNeue Medium.ttf", size)
		draw = ImageDraw.Draw(im)
		width, height = im.size
		draw.text((width * 0.1, height * 0.1), phrase, fill='black', font=f, anchor=None)

		im.save("static/imagenes/salida2.jpg")


def change_size(input_path, width, height):

	'''Takes a pictured and returns a picture with size altered.
        Output result would be like:
            my_pic.jpg <- This is the original file
            my_pic_300X200.jpg <- The resulting image.
    :param input_path: picture path
    :param width: new width
    :param height: new height
    :return: none
    '''

	size_max = (width, height)

	image = Image.open(input_path)
	image.thumbnail(size_max)  # We are stablishing a max size for the image

	image.save("static/imagenes/tamaño.jpg")  # We are saving the images







