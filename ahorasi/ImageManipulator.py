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






	
def turn_to_monochrome(original_image):
	'''
	Turns a picture into one in black and white.
	:param original_image: original
	:return: monochromatic image
	'''
	img = Image.open(original_image)

	imagen2 = img.convert("L")


	imagen2.save("static/imagenes/imagenBN.jpg")
	
def turn_image(original_image, side, degrees):
	'''
	Turns a picture to the right side x degree.
	:param original_image: path
	:return: none
	'''
	image1 = Image.open(original_image)


	output_path = 'static/imagenes/rotarI.jpg'
	if(side == 'L'):
		image1.rotate(degrees).save(output_path)
	elif(side == 'R'):
		image1.rotate(-degrees).save(output_path)
	else:
		image1.save(output_path)
	
def add_text(original_image, phrase, size):
    '''
    Adds text to an image
    original_image: original image path.
    phrase: text in the image.
    size: size of the text.
    '''
    im = Image.open(original_image)
		
    f = ImageFont.truetype("fonts/HelveticaNeue Medium.ttf", size)		
    draw = ImageDraw.Draw(im)		
    width, height = im.size		
    draw.text((width*0.1, height*0.1), phrase, fill = 'grey', font = f, anchor = None)				
 
   
    
    im.save("static/imagenes/textoImagen.jpg")
	
def create_pixelArt(original_image):
	'''
	Creates a pixelArt version of the picture.
	original_image: path of original image.
	'''
	im = Image.open(original_image)
	aux_image = im.resize((32,32), Image.BILINEAR)
	output_image = aux_image.resize(im.size, Image.NEAREST)


	output_image.save('static/imagenes/pixelImagen.jpg')

