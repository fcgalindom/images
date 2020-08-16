from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from ahorasi import logica
from ahorasi import ImageManipulator

# Create your views here.

def imagenes(request):
    if request.method == 'POST':

        darImagen = request.FILES['imagens']

        ImageManipulator.change_size(darImagen,40,40)
        ImageManipulator.predeterminada(darImagen)

        textoMeme = None
        if'checkTexto' in  request.POST :
             textoMeme = request.POST['textoMeme']
             textoNumero = request.POST['numeroMeme']
             textoNumero = int(textoNumero)

             ImageManipulator.add_text(darImagen, textoMeme, textoNumero)
        if  'ceckTamaño' in request.POST :
            cambiarAlto = request.POST['cambiarAlto']
            cambiarAncho = request.POST['cambiarAncho']
            cambiarAncho = int (cambiarAncho)
            cambiarAlto = int (cambiarAlto)
            ImageManipulator.change_size(darImagen,cambiarAncho,cambiarAlto)










        return render(request, "memes.html",{'textoMeme': textoMeme ,
        'cambiarAlto': cambiarAlto , 'cambiarAncho' : cambiarAncho
                                             })
    return render(request, "imagenes.html")
def memes (request):
    return render(request,"memes.html")





