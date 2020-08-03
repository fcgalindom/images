from django.contrib import admin
from subir.models import Subir

# Register your models here.
@admin.register(Subir)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id','imager')




