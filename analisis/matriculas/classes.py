class Total:
    def __init__(self, total):
        self.total = total


class Dependencias:
    def __init__(self, cod, total):
        self.total = total
        self.cod = cod


class Objeto:
    def __init__(self, cod, cod2, val):
        self.cod = cod
        self.val = val
        self.cod2 = cod2


class Columnas:
    def __init__(self, nombre):
        self.nombre = nombre
