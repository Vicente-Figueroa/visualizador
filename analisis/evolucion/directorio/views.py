from analisis.directorio.serializers import *
from analisis.directorio.classes import *
from analisis.evolucion.directorio.funciones import *
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
from .clases import *

data1 = pd.read_csv("analisis/data/coquimbo_2018.csv")
data2 = pd.read_csv("analisis/data/coquimbo_2019.csv")
data3 = pd.read_csv("analisis/data/coquimbo_2020.csv")
data4 = pd.read_csv("analisis/data/coquimbo_2021.csv")


class TotalView(APIView):

    def get(self, request, format=None):
        totalDirectorio = list()
        for item in evolucion_directorio(data1, data2, data3, data4):
            totalDirectorio.append(Total(total=item))

        serializer = TotalSerializer(totalDirectorio, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        lista = list()
        var = request.data['variable']
        lista.append(evolucion_por_variable(2018, data1, var))
        lista.append(evolucion_por_variable(2019, data2, var))
        lista.append(evolucion_por_variable(2020, data3, var))
        lista.append(evolucion_por_variable(2021, data4, var))

        return Response(lista)


class EstadoView(APIView):
    def get(self, request, format=None):
        lista = list()
        lista.append(evolucion_por_estado(2018, data1))
        lista.append(evolucion_por_estado(2019, data2))
        lista.append(evolucion_por_estado(2020, data3))
        lista.append(evolucion_por_estado(2021, data4))

        return Response(lista)
