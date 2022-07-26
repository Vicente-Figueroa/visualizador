from analisis.directorio.serializers import *
from analisis.matriculas.serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response
from analisis.matriculas.classes import *
from analisis.directorio.funciones import *
import pandas as pd
from rest_framework.decorators import api_view

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
data = pd.read_csv("analisis/data/coquimbo_2020.csv")


@api_view(['GET', 'POST'])
def buscador(request):
    if request.method == 'GET':
        col = 'NOM_COM_RBD'
        variable = creador(data, col)
        comunas = []
        for nombre, valor in variable.items():
            comunas.append(Dependencias(
                cod=nombre, total=valor))

        serializer = DependenciaSerializer(comunas, many=True)
        return Response(serializer.data)

    col = request.data['col']
    col = col.replace(' ', '_')
    col = col.upper()
    variable = creador(data, col)
    comunas = []
    if col in data.columns.values:
        for nombre, valor in variable.items():
            comunas.append(Dependencias(
                cod=nombre, total=valor))

        serializer = DependenciaSerializer(comunas, many=True)
        return Response(serializer.data)
    return Response({'message': 'Aca no hay nada'})
import json
@api_view()
def lista_de_variables(request):
  
    cols= columnas(data)
    lista=list()
    # pasar a lista
    for index,dato in enumerate(cols):
        lista.append(Columnas(nombre=dato))
        pass
    serializer = ObjetoSerializer(lista, many=True)
    return Response(serializer.data)