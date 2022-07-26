import pandas as pd
from operator import itemgetter


def directorio_por_comuna(data):
    agrupado_por_comuna = data.groupby('NOM_COM_RBD')['RBD'].count()
    return agrupado_por_comuna.to_dict()


def total_establecimientos(data):
    return data.shape[0]


def establecimientos_municipales(data):
    dato = data[data['COD_DEPE2'] == 1].shape[0]
    return dato


def dependencias(data):
    agrupado_por_depe2 = data.groupby('COD_DEPE2')['RBD'].count()
    return agrupado_por_depe2.to_dict()


def dependencia_rural(data):
    depe_rural = data.groupby(['COD_DEPE2', 'RURAL_RBD'])['RBD'].count()
    dic = depe_rural.to_dict()
    for a in range(1, 6):
        for b in range(2):
            if ((a, b) in dic):
                pass
            else:
                dic[(a, b)] = 0
    newlist = sorted(dic.items())
    return newlist


def estado_establecimiento(data):
    estado = data.groupby(['ESTADO_ESTAB'])['RBD'].count()
    return estado.to_dict()


def ruralidad_comunas(data):
    urbanidad_por_comuna = data.groupby(
        ['NOM_COM_RBD', 'RURAL_RBD'])['RBD'].count()
    doc = urbanidad_por_comuna.to_dict()
    doc[('RÍO HURTADO', 0)] = 0
    doc
    newlist = sorted(doc.items())
    return newlist


def estado_ruralidad(data):
    urbanidad_y_estado = data.groupby(
        ['ESTADO_ESTAB', 'RURAL_RBD'])['RBD'].count()
    return urbanidad_y_estado.to_dict()


def creador(data, col):
    try:
        columna = data.groupby(col)['RBD'].count()
        return columna.to_dict()
    except:
        return (0, 0)


def columnas(data):
    columns = data.columns.to_list()
    columns.remove('RBD')
    columns.remove('Unnamed: 0')

    return columns
