from django.urls import path, include
from analisis.directorio.creador.views import lista_de_variables

from analisis.directorio.anio_2021.views import *

urlpatterns = [
    path('directorios/', include('analisis.evolucion.directorio.urls')),
    path('matriculas/', include('analisis.evolucion.matriculas.urls')),

]
