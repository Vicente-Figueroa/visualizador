from django.urls import path, include
from analisis.matriculas.creador.views import lista_de_variables

urlpatterns = [
    path('2020/', include('analisis.matriculas.anio_2020.urls')),
    path('2019/', include('analisis.matriculas.anio_2019.urls')),
    path('creador/', include('analisis.matriculas.creador.urls')),
    path('columnas/', lista_de_variables),



]
