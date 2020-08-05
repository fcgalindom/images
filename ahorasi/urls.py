
from django.contrib import admin
from django.urls import path
from subir import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.imagenes ,name = 'subir'),

    path('memes/',views.memes, name = 'meme'),

]
