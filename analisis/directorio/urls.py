from django.urls import path, include
from analisis.directorio.creador.views import lista_de_variables

from analisis.directorio.anio_2021.views import *

urlpatterns = [
    path('2021/', include('analisis.directorio.anio_2021.urls')),
    path('2020/', include('analisis.directorio.anio_2020.urls')),
    path('2019/', include('analisis.directorio.anio_2019.urls')),
    path('creador/', include('analisis.directorio.creador.urls')),
    path('columnas/', lista_de_variables),
]
