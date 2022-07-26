import pandas as pd

# Letura de chunk de archivos


def ChunkUno(url, max):
    # Header del dataframe
    header = pd.read_csv(url+"1.csv", encoding="latin-1", sep=",")
    header = header.applymap(lambda s: s.upper() if type(s) == str else s)
    # body without index
    for item in range(2, max+1):
        variable = pd.read_csv(url+str(item)+".csv",
                               encoding="latin-1",
                               names=header.columns.tolist(),
                               sep=",")
        header = pd.concat([header, variable], axis=0, ignore_index=True)
    return header[["Unnamed: 0", "AGNO",
                   "RBD",
                   "NOM_RBD", "COD_REG_RBD", "COD_PRO_RBD", "COD_COM_RBD", "NOM_COM_RBD", "COD_DEPROV_RBD", "NOM_DEPROV_RBD", "COD_DEPE", "COD_DEPE2", "RURAL_RBD", "ESTADO_ESTAB", "COD_ENSE",  "GEN_ALU", "FEC_NAC_ALU", "EDAD_ALU", "COD_REG_ALU", "COD_COM_ALU", "NOM_COM_ALU", "COD_SEC"]]
