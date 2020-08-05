from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from ahorasi import logica

# Create your views here.

def imagenes(request):
    if request.method == 'POST':

        darImagen = request.FILES['imagens']

        logica.logica(darImagen)





        return render(request, "memes.html")
    return render(request, "imagenes.html")
def memes (request):
    return render(request,"memes.html")
def index (request):
    render(request, "memes.html")




