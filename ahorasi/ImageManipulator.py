from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from PIL import ImageFont
from os import listdir, path
import imghdr


class ImageManipulator():

	@staticmethod
	def check_image_format(file):
		return isinstance(imghdr.what(file), str)

	@staticmethod
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
		if(not ImageManipulator.check_image_format(input_path)):
			return
		size_max = (width, height)
		im_name, im_ext = path.splitext(input_path)
		image = Image.open(input_path)
		image.thumbnail(size_max)  # We are stablishing a max size for the image
		output_path = "{}_{}x{}{}".format(im_name, width, height, im_ext)
		image.save(output_path)  # We are saving the images

	@staticmethod
	def change_many_size(input_folder, width, height):
		''' Takes a folder and changes the size of all of pictures inside.
		:param input_folder: path to a folder with pictures.
		:param width: new width
		:param height: new height
		:return: none
		'''
		size_max = (width, height)
		for i in listdir(input_folder):
			im_name, im_ext = path.splitext(i)
			if(not ImageManipulator.check_image_format(path.join(input_folder, i))):
				continue
			image = Image.open(path.join(input_folder, i))
			image.thumbnail(size_max)  # We are stablishing a max size for the image
			output_path = path.join(input_folder, "{}_{}x{}{}".format(im_name, width, height, im_ext))
			image.save(output_path)  # We are saving the images


	@staticmethod
	def turn_to_monochrome(original_image):
		'''
		Turns a picture into one in black and white.
		:param original_image: original
		:return: monochromatic image
		'''
		img = Image.open(original_image)
		#img.show()
		imagen2 = img.convert("L")
		im_name, im_ext = path.splitext(original_image)
		if (not ImageManipulator.check_image_format(original_image)):
			return
		output_path = im_name + "_result" + im_ext
		imagen2.save(output_path)
		return original_image

	@staticmethod
	def turn_image(original_image, side, degrees):
		'''
		Turns a picture to the right side x degree.
		:param original_image: path
		:return: none
		'''
		image1 = Image.open(original_image)
		im_name, im_ext = path.splitext(original_image)
		if (not ImageManipulator.check_image_format(original_image)):
			return
		output_path = im_name + "_result" + im_ext
		if(side == 'L'):
			image1.rotate(degrees).save(output_path)
		elif(side == 'R'):
			image1.rotate(-degrees).save(output_path)
		else:
			return

	@staticmethod 
	def add_text(image_path, phrase, size):
		im = Image.open(image_path)
		
		f = ImageFont.truetype("fonts/HelveticaNeue Medium.ttf", size)		
		draw = ImageDraw.Draw(im)		
		width, height = im.size		
		draw.text((width*0.1, height*0.1), phrase, fill = 'black', font = f, anchor = None)				
		im.save("tmp.png")
		

ImageManipulator.add_text("images/Buenos Aires.jpg", "HOLA A TODOS", 30)

