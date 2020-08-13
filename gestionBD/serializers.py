from .models import usuario, sector, noticiaTip, puntoRecoleccion, horarioRecoleccion
from rest_framework import serializers

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = ('idUsuario', 'nombre', 'apellido', 'usuario', 'contrasena','email')

class sectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = sector
        fields = ('idSector', 'nombre', 'region')

class noticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = noticiaTip
        fields = ('idNoticia', 'titulo', 'descripcion', 'url', 'tipoNoticia', 'idSector')

class puntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = puntoRecoleccion
        fields = ('idPunto', 'latitud', 'longitud', 'icono', 'sumaCalificacion', 'cantidadUsuarioCal', 'idUsuario', 'idSector')

class horarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = horarioRecoleccion
        fields = ('idPuntoHorario','dia','hora', 'idSector')