from django.urls import path, include
from analisis.directorio.anio_2020.views import *

urlpatterns = [
    path('total/', TotalView.as_view()),
    path('municipales/', Municipales.as_view()),
    path('comunas/', Comunas.as_view()),
    path('dependencia/', DependenciaView.as_view()),
    path('estados/',EstadosView.as_view()),

    path('dependencia-rural/',DependenciaRuralView.as_view()),
    path('ruralidad-comuna/',ComunaRuralView.as_view()),
    path('ruralidad-estado/', EstadoRuralView.as_view())

]
