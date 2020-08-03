from django.db import models

# Create your models here.
class Subir(models.Model):
    imager= models.ImageField(upload_to="publicar/foto", blank=True , null=True)
