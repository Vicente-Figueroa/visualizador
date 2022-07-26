from django.urls import path, include
from analisis.directorio.creador.views import *

urlpatterns = [
    path("prueba/", buscador, name="")
]
