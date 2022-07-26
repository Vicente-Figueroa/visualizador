# definir las funciones para obtener información

# dict items para los resultados
nombres_dependencias2 = {
    1: 'Municipal',
    2: 'P. Subvencionado',
    3: 'P. Pagado',
    4: 'Adm. Delegada',
    5: 'Servicio Local'
}
nombres_dependencias = {
    1: 'Corp. Municipal',
    2: 'Municipal DAEM',
    3: 'P. Subvencionado',
    4: 'P. Pagado',
    5: 'Adm. Delegada',
    6: 'Servicio Local'
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

# informacion sobre el total de directorio


def evolucion_directorio(data1, data2, data3, data4):
    lista_de_totales = list()

    lista_de_totales.append(data1.shape[0])
    lista_de_totales.append(data2.shape[0])
    lista_de_totales.append(data3.shape[0])
    lista_de_totales.append(data4.shape[0])

    return lista_de_totales


def evolucion_por_estado(anio, data):
    por_estado = data.groupby('ESTADO_ESTAB').count()
    por_estado['AGNO'] = anio
    por_estado[['AGNO', 'RBD']]
    variable = por_estado[['RBD']].to_dict()
    variable['AGNO'] = anio
    return variable


def evolucion_por_variable(anio, data, var):
    data['NOM_COM_RBD'] = data['NOM_COM_RBD'].str.normalize('NFKD')\
        .str.encode('ascii', errors='ignore')\
        .str.decode('utf-8')
    data = data.replace({"COD_DEPE2": nombres_dependencias2,
                        "COD_DEPE": nombres_dependencias,
                         "RURAL_RBD": nombres_urbanismo})
    por_estado = data.groupby(var).count()
    por_estado['AGNO'] = anio
    por_estado[['AGNO', 'RBD']]
    variable = por_estado[['RBD']].to_dict()
    variable['AGNO'] = anio

    return variable


def evolucion_por_urbanismo(anio, data):
    pass
