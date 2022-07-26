import pandas as pd
from operator import itemgetter
from .classes import *


def total_de_matriculas(data):
    return data.shape[0]


def numero_de_establecimientos(data):
    dato = data.groupby('RBD').count()
    return dato.shape[0]


def matriculas_municipales(data):
    muni = data[data['COD_DEPE2'] == 1]
    return muni.shape[0]


def matriculas_por_dependencia(data):
    dependencia = data.groupby(['COD_DEPE2'])['RBD'].count()
    dependencia.index = dependencia.index.astype('int')
    dependencia = dependencia.to_dict()
    return dependencia


def matricula_por_urbanismo(data):
    urbanismo = data.groupby(['RURAL_RBD'])['Unnamed: 0'].count()
    urbanismo.index = urbanismo.index.astype('int')

    return urbanismo.to_dict()


def matricula_por_genero(data):
    genero = data.groupby(['GEN_ALU'])['Unnamed: 0'].count()
    genero.index = genero.index.astype('int')

    return genero.to_dict()


def matricula_por_comuna(data):
    comunas = data.groupby(['NOM_COM_RBD'])['Unnamed: 0'].count()
    return comunas.to_dict()


def creador(data, col):
    try:
        columna = data.groupby(col)['RBD'].count()
        return columna.to_dict()
    except:
        return (0, 0)


def columnas(data):
    columns= data.columns.to_list()
    columns.remove('RBD')
    columns.remove('Unnamed: 0')
    columns.remove('MRUN')



    return columns
