"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from gestionBD import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', views.UsuariosList.as_view()),
    path('usuarios/<str:pk>/', views.UsuariosDetalle.as_view()),
    path('sector/', views.SectorList.as_view()),
    path('sector/<str:pk>/', views.SectorDetalle.as_view()),
    path('noticia/', views.NoticiaList.as_view()),
    path('noticia/<str:pk>/', views.NoticiaDetalle.as_view()),
    path('puntoRecoleccion/', views.PuntoRecoleccionList.as_view()),
    path('puntoRecoleccion/<str:pk>/', views.PuntoRecoleccionDetalle.as_view()),
    path('horarioRecoleccion/', views.HorarioRecoleccionList.as_view()),
    path('horarioRecoleccion/<str:pk>/', views.HorarioRecoleccionDetalle.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)