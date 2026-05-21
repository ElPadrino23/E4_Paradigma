"""
Autor: Luis Fernando Martinez Barragan - A01613426
Fecha de inicio: 16/05/2026
Fecha de fin: 18/05/2026
"""

import csv

# Obtener datos
def cargar_series(filepath):
    with open(filepath) as f:
        reader = csv.DictReader(f)

        series = []

        for row in reader:
            serie = {
                'nombre': row['nombre'],
                'genero': row['genero'],
                'calificacion': float(row['calificacion']),
                'ano': int(row['ano'])
            }

            series.append(serie)

        return series

# Lambdas

# Filtrar por genero
por_genero = lambda generos: (
    lambda series: list(filter(lambda s: s['genero'] in generos, series))
)

# Filtrar por calificacion minima
por_calificacion = lambda minimo: (
    lambda series: list(filter(lambda s: s['calificacion'] >= minimo, series))
)

# Ordenar de mayor a menor
ordenar = lambda series: sorted(series, key=lambda s: s['calificacion'], reverse=True)

# Convertir a texto
formatear = lambda series: list(map(
    lambda s: f"{s['nombre']} ({s['ano']}) | {s['genero']} | Calificacion: {s['calificacion']}",
    series
))

# Pipeline
def recomendar(series, generos, minimo):

    filtradas = por_genero(generos)(series)
    filtradas = por_calificacion(minimo)(filtradas)
    ordenadas = ordenar(filtradas)

    return formatear(ordenadas)


if __name__ == '__main__':

    series = cargar_series('series.csv')

    print("Recomendador")

    generos = input("Que generos te gustan? (sci-fi,drama,horror,comedia,accion,guerra,misterio,animacion)(Separados por ',') ")
    generos = generos.split(",")

    minimo = float(input("Cual es la calificacion minima que aceptas? "))

    resultados = recomendar(series, generos, minimo)

    print("Recomendaciones para ti:")

    if resultados:
        for r in resultados:
            print("-", r)
    else:
        print("Ninguna serie se adapta a ti jeje, btw si estas leyendo esto es por que no te gusta cualquier cosa, ve la de band of brothers, esta buena!")
