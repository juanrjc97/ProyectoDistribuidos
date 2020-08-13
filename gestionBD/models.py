from __future__ import unicode_literals
from django.db import models

# Create your models here.
class usuario(models.Model):
    idUsuario = models.AutoField (primary_key = True, unique=True)
    #cedula = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    usuario = models.CharField(unique=True, max_length=25)
    contrasena = models.CharField(max_length=25)
    email = models.EmailField(max_length=200)
    def __str__(self):
        return self.usuario

class sector(models.Model):
    idSector = models.AutoField (primary_key = True, unique=True)
    nombre = models.CharField(max_length=10, unique=True)
    region = models.CharField(max_length=25)

class noticiaTip(models.Model):
    idNoticia = models.AutoField (primary_key = True, unique=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    url = models.TextField()
    tipoNoticia = models.CharField(max_length=100)
    idSector = models.ForeignKey(sector, on_delete=models.PROTECT)

class puntoRecoleccion(models.Model):
    idPunto = models.AutoField(primary_key=True, unique=True)
    latitud = models.DecimalField(max_digits=30, decimal_places=20)
    longitud = models.DecimalField(max_digits=30, decimal_places=20)
    icono = models.CharField(max_length=50)
    sumaCalificacion = models.IntegerField()
    cantidadUsuarioCal = models.IntegerField()
    idUsuario = models.ForeignKey(usuario, on_delete=models.PROTECT)
    idSector = models.ForeignKey(sector, on_delete=models.PROTECT)

class horarioRecoleccion(models.Model):
    idPuntoHorario = models.AutoField(primary_key=True, unique=True)
    dia = models.CharField(max_length=15)
    hora = models.CharField(max_length=15)
    idSector = models.ForeignKey(sector, on_delete=models.PROTECT)
