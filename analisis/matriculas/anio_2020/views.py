from analisis.directorio.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from analisis.matriculas.classes import *
from analisis.matriculas.funciones import *
import pandas as pd
from analisis.funciones import ChunkUno


nombres_dependencias = {
    1: 'Municipal',
    2: 'P. Subvencionado',
    3: 'P. pagado',
    4: 'Adm. delegada',
    5: 'Servicio local'
}
nombres_urbanismo = {
    0: 'Urbano',
    1: 'Rural'
}
nombres_generos = {
    0: 'Indefinido',
    1: 'Hombre',
    2: 'Mujer',
    3: 'Indefinido'
}
data = ChunkUno("analisis/data/matriculas_2020/", 18)

matriculas = []
urbanismo = []
comunas = []
generos = []


for numero, valor in matricula_por_urbanismo(data).items():
    urbanismo.append(Dependencias(
        cod=nombres_urbanismo[numero], total=valor))

for numero, valor in matriculas_por_dependencia(data).items():
    matriculas.append(Dependencias(
        cod=nombres_dependencias[numero], total=valor))

for nombre, valor in matricula_por_comuna(data).items():
    comunas.append(Dependencias(
        cod=nombre, total=valor))

for numero, valor in matricula_por_genero(data).items():
    generos.append(Dependencias(
        cod=nombres_generos[numero], total=valor))


class TotalView(APIView):
    def get(self, request, format=None):
        serializer = TotalSerializer(Total(total=total_de_matriculas(data)))
        return Response(serializer.data)


class NumeroEstablecimientosView(APIView):
    def get(self, request, format=None):
        serializer = TotalSerializer(
            Total(total=numero_de_establecimientos(data)))
        return Response(serializer.data)


class MatriculasMunicipalesView(APIView):
    def get(self, request, format=None):
        serializer = TotalSerializer(Total(total=matriculas_municipales(data)))
        return Response(serializer.data)


class MatriculasPorDependencia(APIView):
    def get(self, request, format=None):
        serializer = DependenciaSerializer(matriculas, many=True)
        return Response(serializer.data)


class MatriculasPorUrbanismo(APIView):
    def get(self, request, format=None):
        serializer = DependenciaSerializer(urbanismo, many=True)
        return Response(serializer.data)


class MatriculasPorComunas(APIView):
    def get(self, request, format=None):
        serializer = DependenciaSerializer(comunas, many=True)
        return Response(serializer.data)


class MatriculasPorGeneros(APIView):
    def get(self, request, format=None):
        serializer = DependenciaSerializer(generos, many=True)
        return Response(serializer.data)
