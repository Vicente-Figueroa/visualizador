import pandas as pd
from funciones import ChunkUno

import pathlib
url = pathlib.Path(__file__).parent.resolve()
print(str(url))
variable = ChunkUno("analisis/data/matriculas_2020/", 18)

print(variable["NOM_COM_RBD"].unique())
print(variable.shape)
print(variable.info())