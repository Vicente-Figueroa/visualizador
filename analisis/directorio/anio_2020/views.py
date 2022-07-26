from analisis.directorio.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from analisis.directorio.classes import *
from analisis.directorio.funciones import *
import pandas as pd
import os
from backend.settings import BASE_DIR

data=pd.read_csv("analisis/data/coquimbo_2020.csv")

comment = []
dependencia=[]
dependencias_rurales=[]
estados=[]
comunas_rurales=[]
estados_rurales=[]

nombres_dependencias={
    1:'Municipal',
    2:'P. Subvencionado',
    3:'P. pagado',
    4:'Adm. delegada',
    5:'Servicio local'
}
nombres_estados={
    1:'Funcionando',
    2:'En receso',
    3:'Cerrado',
    4:' Autorizado sin matrícula',
}

for numeros,valor in ruralidad_comunas(data):
    comunas_rurales.append(ComunaRural(cod=numeros[0], total=valor, rural=numeros[1]))

for numeros,valor in estado_ruralidad(data).items():
    estados_rurales.append(EstadoRural(cod=nombres_estados[numeros[0]], total=valor, rural=numeros[1]))


for numero, valor in directorio_por_comuna(data).items():
    comment.append(Comment(label=numero, content=valor))

for numero, valor in dependencias(data).items():
    dependencia.append(Dependencia(cod=nombres_dependencias[numero], total=valor))

for numeros,valor in dependencia_rural(data):
    dependencias_rurales.append(DependenciaRural(cod=nombres_dependencias[numeros[0]], total=valor, rural=numeros[1]))

for numero,valor in estado_establecimiento(data).items():
    estados.append(Estados(cod=nombres_estados[numero], total=valor))

class Comunas(APIView):
    """
    Puedo sacar por pantalla un texto :v
    """

    def get(self, request, format=None):
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

class TotalView(APIView):
    def get(self, request, format=None):
        serializer = TotalSerializer(Total(total=total_establecimientos(data)))
        return Response(serializer.data)

class DependenciaView(APIView):
    def get(self, request, format=None):
        serializer = DependenciaSerializer(dependencia, many=True)
        return Response(serializer.data)

class DependenciaRuralView(APIView):
    def get(self, request, format=None):
        serializer = DependenciaRuralSerializer(dependencias_rurales, many=True)
        return Response(serializer.data)


class EstadosView(APIView):
    def get(self, request, format=None):
        serializer = EstadosSerializer(estados, many=True)
        return Response(serializer.data)

class ComunaRuralView(APIView):
    def get(self, request, format=None):
        serializer = DependenciaRuralSerializer(comunas_rurales, many=True)
        return Response(serializer.data)

class EstadoRuralView(APIView):
    def get(self, request, format=None):
        serializer = DependenciaRuralSerializer(estados_rurales, many=True)
        return Response(serializer.data)

class Municipales(APIView):
    def get(self, request, format=None):
        serializer = TotalSerializer(Total(total=establecimientos_municipales(data)))
        return Response(serializer.data)
