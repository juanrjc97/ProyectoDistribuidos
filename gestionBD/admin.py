from django.contrib import admin
from .models import usuario, sector, noticiaTip, puntoRecoleccion, horarioRecoleccion

# Register your models here.

myModels = [usuario, sector, noticiaTip, puntoRecoleccion, horarioRecoleccion]  # iterable list

admin.site.register(myModels)
# admin.site.register(Usuarios)
