from django.urls import path, include
from analisis.matriculas.anio_2019.views import *

urlpatterns = [
    path('total/', TotalView.as_view()),
    path('numero-de-establecimientos/', NumeroEstablecimientosView.as_view()),
    path('matriculas-municipales/', MatriculasMunicipalesView.as_view()),
    path('matriculas-por-dependencias/', MatriculasPorDependencia.as_view()),
    path('matriculas-por-urbanismo/', MatriculasPorUrbanismo.as_view()),
    path('matriculas-por-comunas/', MatriculasPorComunas.as_view()),
    path('matriculas-por-generos/', MatriculasPorGeneros.as_view()),

    
]
