# Recomendador de Series de Netflix

## Descripcion

Elegir que ver en Netflix puede ser en ocasiones muy complicado cuando hay tantas opciones. Este programa resuelve ese problema recomendando series segun los generos que le gustan al usuario y la calificacion minima que acepta!

La solucion usa el paradigma funcional. En este paradigma la idea principal es resolver problemas aplicando y combinando funciones puras, o sea, funciones que siempre regresan el mismo resultado para los mismos argumentos y no modifican nada externo, dare algunos ejemplos para no dejarlo en el aire: puras (Sumas, potencias, cambiar de minuscula a mayuscula), algunos ejemplos de impuras: (obtener fecha actual, modificar un dato de una lista o una lista(depende de si existe o no). Ya que en lugar de utilizar ciclos que necesitan cambian sus variables, se utilizan operaciones de `filter`, `map` y `sorted` encadenadas en un pipeline.

Ejemplos: `resultado = []` y luego `resultado.append())`, se utilizan funciones de filter , map  y sorted encadenadas en un pipeline, donde cada paso produce un nuevo resultado sin modificar los datos originales

Mi ejemplo favorito es por ejemplo en un caso hipotetico utilizar el output de un sort en una lista desordenada para facilitar un filter, ya teniendo las calificaciones ordenadas. 

En Python las expresiones lambda son la implementacion directa de este concepto. Cada transformacion del pipeline es una lambda, una funcion pequena que recibe una entrada y regresa una salida y no modifica nada 

## Modelo

La solucion es el pipeline , los datos pasan por una secuencia de transformaciones donde cada paso es una funcion lambda.

```
Todos los series
       |
       v
    por_genero              <- filter: Filtra las series por el genero escogido
       |
       v
por_calificacion          <- filter: nuevamnete filtra las series dejando unicamente las que cumplen con calificacion >= 
       |
       v
    ordenar                 <- sort: Ahora aplicamos un sort para ordenar de mayor a menor
       |
       v
   convertir                 <- map: pasa de diccionario a string leible 
       |
       v
   Recomendaciones
```
Cada paso es una lambda de orden superior, una funcion que recibe un parametro y regresa otra funcion. Estos patrones se llaman currificacion y son del calculo lambda (Church, 1941)


### Lambdas definidas

### Lambdas utilizadas

- `por_genero(generos)`: filtra las series segun los generos seleccionados
- `por_calificacion(minimo)`: filtra las series que cumplen con la calificacion minima
- `ordenar`: ordena las series de mayor a menor calificacion
- `formatear`: convierte cada serie en un formato de texto para mostrarla
- `return`: regresa el resultado final después de aplicar todos los filtros y transformaciones

### Lambdas utilizadas

- `por_genero`: filtra las series segun los generos que fueron seleccionados
- `por_calificacion`: filtra las series que cumplen con al menos la calificacion seleccionada 
- `ordenar`: ordena las series de mayor a menor calificacion
- `formatear`: convierte cada serie en un formato de texto
- `return`: regresa el resultado final despues de aplicar todos los filtros 

## Implementacion

**Archivos:**
- `series.csv` set con series en formato: (nombre, genero, calificacion, año)
- `recomendador.py` todas las lambdas y el pipeline
- `tests.py`  15 pruebas automatizadas

**Para correr el programa:**
```
python recomendador.py
```

Ejemplo de uso:
```
Escribe los generos que te gustan separados por coma y despues la calificacion minima que aceptas

Recomendaciones para: drama y horror con calificacion >= 8.5
 - The Sopranos (1999) | drama | Calificacion: 9.2
 - Dr House (2004) | drama | Calificacion: 8.7
```

**Las lambdas principales:**
```
por_genero       = lambda generos: (lambda series: list(filter(lambda s: s['genero'] in generos, series)))
por_calificacion = lambda minimo:  (lambda series: list(filter(lambda s: s['calificacion'] >= minimo, series)))
ordenar          = lambda series:  sorted(series, key=lambda s: s['calificacion'], reverse=True)
formatear        = lambda series:  list(map(lambda s: f"{s['nombre']} ({s['año']}) | {s['genero']} | Calificacion: {s['calificacion']}", series))
```

La funcion `recomendar` las encadena en orden:
```
def recomendar(series, generos, minimo):
    filtradas = por_genero(generos)(series)
    filtradas = por_calificacion(minimo)(filtradas)
    ordenadas = ordenar(filtradas)
    return formatear(ordenadas)
```

## Analisis
 
### Complejidad Temporal
 
La velocidad del programa depende de cuantas series hay
 
Cargar las series es O(n)
Filtrar por genero es O(n)
Filtrar por calificacion es O(n)
Ordenar con bubble sort es O(n^2), que es la parte mas lenta
Formatear es O(n)

El paso complicado es ordenar ya que utilizando bubble sort O(n^2), los demas son rapidos, entonces todo el programa es O(n^2),
  
## Referencias
 
- Abelson, H., y Sussman, G. J. (1996). *Structure and Interpretation of Computer Programs* (2nd ed.). MIT Press. https://mitpress.mit.edu/9780262510875/

- Bratko, I. (2012). Prolog Programming for Artificial Intelligence (4th ed.). Addison-Wesley.

- Church, A. (1941). The Calculi of Lambda Conversion. Princeton University Press.

- Python Software Foundation. (2024). Functional Programming HOWTO https://docs.python.org/3/howto/functional.html
- Sterling, L., y Shapiro, E. (1994). *The Art of Prolog* (2nd ed.). MIT Press.
 
