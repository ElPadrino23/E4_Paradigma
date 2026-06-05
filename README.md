# Recomendador de Series de Netflix

Autor: Luis Fernando Martinez Barragan - A01613426
Curso: TC2037 - Implementacion de Metodos Computacionales

## Descripcion

Programa que recomienda series de Netflix basado en genero y calificacion minima
Implementado en dos paradigmas: Programacion Funcional y Orientacion a Objetos

## Como ejecutar

```
python funcional.py
python orientada_objetos.py
python tests.py
```

## Paradigma Funcional

Usa funciones puras sin mutacion de estado y con pipeline de transformaciones:
- Filter por genero
- Filter por calificacion
- Ordenar (MS)
- Formatear

Funciones principales:
- `por_genero`: filtra por genero seleccionado
- `por_calificacion`: filtra por calificacion minima
- `ordenar`: ordena de mayor a menos con MS
- `formatear`: convierte a string legible
- `recomendar`: encadena todos los filtros

Complejidad: O(n log n)

## Paradigma Orientado a Objetos

Usa clases Serie y Catalogo con metodos para filtrar y ordenar.
Method chaining para composicion fluida.

Clases:
- `Serie`: representa una serie
- `Catalogo`: gestiona coleccion de series

Metodos:
- `filtrar_genero`: filtra por genero
- `filtrar_calificacion`: filtra por calificacion minima
- `ordenar`: ordena por calificacion
- `recomendar`: aplica todos los filtros

Complejidad: O(n log n)

## Datos

Base de datos: series.csv 
Campos: nombre, genero, calificacion, año

Generos disponibles: sci-fi, drama, horror, comedia, accion, guerra, misterio, animacion

## Pruebas

20 pruebas automatizadas (todas pasando):

Funcional:
- Carga de datos
- Filtros (genero, calificacion)
- Ordenamiento sin mutacion
- Formateo
- Pipeline completo
- Currying y composicion

OO:
- Creacion de objetos
- Filtrado
- Method chaining
- Equivalencia con paradigma funcional

Ejecutar: `python tests.py`

## Comparacion

### Programacion Funcional

Ventajas:
- Sin mutacion: los datos originales nunca cambian
- Predecible: misma entrada siempre da misma salida
- Facil de testear: funciones puras son aisladas
- Pipeline claro: se ve exactamente como fluyen los datos
- Currificacion: permite aplicar funciones parcialmente

Desventajas:
- Más abstracto: requiere entender lambdas y recursion
- Usa más memoria: crea nuevas listas en cada paso

Ejemplo: `por_genero(['drama'])(series)` crea una nueva lista filtrada

### Orientacion a Objetos

Ventajas:
- Intuitivo: clases representan conceptos reales
- Encapsulacion: agrupa datos y metodos juntos
- Reutilizable: facil extender con nuevas clases
- Method chaining: composicion fluida y legible

Desventajas:
- Estado mutable: los objetos pueden cambiar
- Más complejo: necesita entender clases y herencia

Ambos tienen complejidad O(n log n) y producen resultados identicos

### Complejidad

Temporal: O(n log n) en ambos
Espacial: O(n) en ambos

### Resultado

Ambos producen identicos resultados (validado en test_equivalencia).
Para este problema, Funcional es mas elegante
Para sistemas grandes, OOP es mas practico
