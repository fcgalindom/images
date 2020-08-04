from PIL import Image

def logica (imagen):
    img = Image.open(imagen)
    img.show()

    imagen2 = img.convert("L")
    imgen3 = img

    imagen2.save("static/imagenes/salida.png")


    return imagen
