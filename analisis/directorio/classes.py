class Label:
    def __init__(self, label):
        self.label = label


class Comment:
    def __init__(self, label, content):
        self.label = label
        self.content = content


class Total:
    def __init__(self, total):
        self.total = total


class Dependencia:
    def __init__(self, cod, total):
        self.total = total
        self.cod = cod


class DependenciaRural:
    def __init__(self, cod, rural, total):
        self.total = total
        self.cod = cod
        self.rural = rural


class Estados:
    def __init__(self, cod, total):
        self.total = total
        self.cod = cod


class ComunaRural:
    def __init__(self, cod, rural, total):
        self.total = total
        self.cod = cod
        self.rural = rural


class EstadoRural:
    def __init__(self, cod, rural, total):
        self.total = total
        self.cod = cod
        self.rural = rural


class Columnas:
    def __init__(self, nombre):
        self.nombre = nombre
