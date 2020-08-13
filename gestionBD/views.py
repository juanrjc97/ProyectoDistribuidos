from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import usuario, sector, noticiaTip, puntoRecoleccion, horarioRecoleccion
from .serializers import usuarioSerializer, sectorSerializer, noticiaSerializer, puntoSerializer, horarioSerializer

# Create your views Usuarios

class UsuariosList(APIView):
    def get(self, request, format=None):
        usuarios1 = usuario.objects.all()
        serializer = usuarioSerializer(usuarios1, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = usuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuariosDetalle(APIView):

    def get_object(self, pk):
        try:
            return usuario.objects.get(usuario=pk)
        except usuario.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        usuarios1 = self.get_object(pk)
        serializer = usuarioSerializer(usuarios1)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        usuarios1 = self.get_object(pk)
        serializer = usuarioSerializer(usuarios1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        usuarios1 = self.get_object(pk)
        usuarios1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views Sector

class SectorList(APIView):
    def get(self, request, format=None):
        sector1 = sector.objects.all()
        serializer = sectorSerializer(sector1, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = sectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SectorDetalle(APIView):

    def get_object(self, pk):
        try:
            return sector.objects.get(nombre=pk)
        except sector.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        sector1 = self.get_object(pk)
        serializer = sectorSerializer(sector1)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        sector1 = self.get_object(pk)
        serializer = sectorSerializer(sector1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        sector1 = self.get_object(pk)
        sector1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views Noticias

class NoticiaList(APIView):
    def get(self, request, format=None):
        noticia1 = noticiaTip.objects.all()
        serializer = noticiaSerializer(noticia1, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = noticiaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoticiaDetalle(APIView):

    def get_object(self, pk):
        try:
            return noticiaTip.objects.get(pk=pk)
        except noticiaTip.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        noticia1 = self.get_object(pk)
        serializer = noticiaSerializer(noticia1)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        noticia1 = self.get_object(pk)
        serializer = noticiaSerializer(noticia1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        noticia1 = self.get_object(pk)
        noticia1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views Punto Recoleccion

class PuntoRecoleccionList(APIView):
    def get(self, request, format=None):
        punto1 = puntoRecoleccion.objects.all()
        serializer = puntoSerializer(punto1, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = puntoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PuntoRecoleccionDetalle(APIView):

    def get_object(self, pk):
        try:
            return puntoRecoleccion.objects.get(pk=pk)
        except puntoRecoleccion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        punto1 = self.get_object(pk)
        serializer = puntoSerializer(punto1)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        punto1 = self.get_object(pk)
        serializer = puntoSerializer(punto1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        punto1 = self.get_object(pk)
        punto1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views Horario Recoleccion

class HorarioRecoleccionList(APIView):
    def get(self, request, format=None):
        horario1 = horarioRecoleccion.objects.all()
        serializer = horarioSerializer(horario1, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = horarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HorarioRecoleccionDetalle(APIView):
    def get_object(self, pk):
        try:
            return horarioRecoleccion.objects.get(pk=pk)
        except horarioRecoleccion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        horario1 = self.get_object(pk)
        serializer = horarioSerializer(horario1)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        horario1 = self.get_object(pk)
        serializer = horarioSerializer(horario1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        horario1 = self.get_object(pk)
        horario1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)