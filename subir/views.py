from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from ahorasi import logica
from ahorasi import ImageManipulator

# Create your views here.

def imagenes(request):
    if request.method == 'POST':

        darImagen = request.FILES['imagens']

        textoMeme = None
        if'checkTexto' in  request.POST :
             textoMeme = request.POST['textoMeme']

             ImageManipulator.add_text(darImagen, textoMeme, 30)






        return render(request, "memes.html",{'textoMeme': textoMeme})
    return render(request, "imagenes.html")
def memes (request):
    return render(request,"memes.html")





