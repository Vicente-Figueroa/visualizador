from django.urls import path, include
from analisis.directorio.urls import *

urlpatterns = [
    path('directorio/', include('analisis.directorio.urls')),
    path('matriculas/', include('analisis.matriculas.urls')),
    path('evolucion/', include('analisis.evolucion.urls')),

]
