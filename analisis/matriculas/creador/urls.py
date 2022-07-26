from django.urls import path, include
from analisis.matriculas.creador.views import *

urlpatterns = [
    path("prueba/", hello_world, name="")
]
