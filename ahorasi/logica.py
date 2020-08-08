from PIL import Image
from ahorasi import ImageManipulator

def logica (imagen):
    img = Image.open(imagen)
    img.show()

    imagen2 = img.convert("L")
    imgen3 = img

    imagen2.save("static/imagenes/salida2.jpg")



    return imagen
