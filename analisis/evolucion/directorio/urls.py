from django.urls import path, include
from analisis.evolucion.directorio.views import *

urlpatterns = [
    path('total/', TotalView.as_view()),
    path('estados/', EstadoView.as_view()),

]
