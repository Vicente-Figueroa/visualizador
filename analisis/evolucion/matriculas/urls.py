from django.urls import path, include
from analisis.evolucion.matriculas.views import *

urlpatterns = [
    path('total/', TotalView.as_view()),

]
