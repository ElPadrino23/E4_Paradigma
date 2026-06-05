"""
Autor: Luis Fernando Martinez Barragan - A01613426
Fecha de inicio: 16/05/2026
Fecha de fin: 18/05/2026
Update: 04/06/2026
"""

import csv
from functools import reduce


def cargar_series(filepath):
    with open(filepath) as archivo:

        def agregar_serie(acumulador, fila):
            acumulador.append({
                'nombre': fila['nombre'],
                'genero': fila['genero'],
                'calificacion': float(fila['calificacion']),
                'ano': int(fila['ano'])
            })
            return acumulador

        return reduce(
            agregar_serie,
            csv.DictReader(archivo),
            []
        )


def por_genero(generos):

    def filtrar(series):
        return list(
            filter(
                lambda serie: serie['genero'] in generos,
                series
            )
        )

    return filtrar


def por_calificacion(minimo):

    def filtrar(series):
        return list(
            filter(
                lambda serie: serie['calificacion'] >= minimo,
                series
            )
        )

    return filtrar


def merge_sort(series):

    if len(series) <= 1:
        return series

    mitad = len(series) // 2

    izquierda = merge_sort(series[:mitad])
    derecha = merge_sort(series[mitad:])

    return merge(izquierda, derecha)


def merge(izquierda, derecha):

    if not izquierda:
        return derecha

    if not derecha:
        return izquierda

    if izquierda[0]['calificacion'] >= derecha[0]['calificacion']:
        return [izquierda[0]] + merge(
            izquierda[1:],
            derecha
        )

    return [derecha[0]] + merge(
        izquierda,
        derecha[1:]
    )


def ordenar(series):
    return merge_sort(series)


def formatear(series):

    return list(
        map(
            lambda serie:
            f"{serie['nombre']} ({serie['ano']}) | "
            f"{serie['genero']} | "
            f"Calificacion: {serie['calificacion']}",
            series
        )
    )


def recomendar(series, generos, minimo):

    filtrar_genero = por_genero(generos)
    filtrar_calificacion = por_calificacion(minimo)

    return formatear(
        ordenar(
            filtrar_calificacion(
                filtrar_genero(series)
            )
        )
    )


if __name__ == '__main__':

    series = cargar_series('series.csv')

    print("Recomendador de Series")

    generos = input(
        "Generos (separados por coma): "
    ).split(",")

    generos = [g.strip() for g in generos]

    minimo = float(
        input("Calificacion minima: ")
    )

    resultados = recomendar(
        series,
        generos,
        minimo
    )

    print("\nRecomendaciones:\n")

    for resultado in resultados:
        print(f"  - {resultado}")

    if not resultados:
        print("Ninguna serie se adapta a ti jeje, btw si estas leyendo esto es por que no te gusta cualquier cosa, ve la de band of brothers, esta buena!")
