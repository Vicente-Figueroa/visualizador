from analisis.directorio.serializers import *
from analisis.directorio.classes import *
from analisis.evolucion.matriculas.funciones import *
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
from analisis.funciones import ChunkUno

data1 = ChunkUno("analisis/data/matriculas_2017/", 17)
data2 = ChunkUno("analisis/data/matriculas_2018/", 17)
data3 = ChunkUno("analisis/data/matriculas_2019/", 18)
data4 = ChunkUno("analisis/data/matriculas_2020/", 18)


class TotalView(APIView):

    def get(self, request, format=None):

        return Response("get")

    def post(self, request, format=None):
        lista = list()
        var = request.data['variable']
        lista.append(evolucion_por_variable(2017, data1, var))
        lista.append(evolucion_por_variable(2018, data2, var))
        lista.append(evolucion_por_variable(2019, data3, var))
        lista.append(evolucion_por_variable(2020, data4, var))

        return Response(lista)
