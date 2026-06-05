import csv

class Serie:
    def __init__(self, nombre, genero, calificacion, ano):
        self.nombre = nombre
        self.genero = genero
        self.calificacion = calificacion
        self.ano = ano

    def __str__(self):
        return f"{self.nombre} ({self.ano}) | {self.genero} | Calificacion: {self.calificacion}"

class Catalogo:
    def __init__(self, filepath):
        self.series = []
        with open(filepath) as f:
            for row in csv.DictReader(f):
                self.series.append(Serie(row['nombre'], row['genero'], float(row['calificacion']), int(row['ano'])))

    def filtrar_genero(self, generos):
        nuevo = Catalogo.__new__(Catalogo)
        nuevo.series = [s for s in self.series if s.genero in generos]
        return nuevo

    def filtrar_calificacion(self, minimo):
        nuevo = Catalogo.__new__(Catalogo)
        nuevo.series = [s for s in self.series if s.calificacion >= minimo]
        return nuevo

    def ordenar(self):
        nuevo = Catalogo.__new__(Catalogo)
        nuevo.series = sorted(self.series, key=lambda s: s.calificacion, reverse=True)
        return nuevo

    def recomendar(self, generos, minimo):
        return (self.filtrar_genero(generos).filtrar_calificacion(minimo).ordenar().series)
