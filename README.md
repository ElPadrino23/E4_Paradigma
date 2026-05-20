# Recomendador de Series de Netflix

## Descripcion

Elegir que ver en Netflix puede ser en ocasiones muy complicado cuando hay tantas opciones. Este programa resuelve ese problema recomendando series segun los generos que le gustan al usuario y la calificacion minima que acepta!

La solucion usa el paradigma funcional. En este paradigma la idea principal es resolver problemas aplicando y combinando funciones puras, o sea, funciones que siempre regresan el mismo resultado para los mismos argumentos y no modifican nada externo, dare algunos ejemplos para no dejarlo en el aire: puras (Sumas, potencias, cambiar de minuscula a mayuscula), algunos ejemplos de impuras: (obtener fecha actual, modificar un dato de una lista o una lista(depende de si existe o no). Ya que en lugar de utilizar ciclos que necesitan cambian sus variables, se utilizan operaciones de `filter`, `map` y `sorted` encadenadas en un pipeline.

Ejemplos: `resultado = []` y luego `resultado.append())`, se utilizan funciones de filter , map  y sorted encadenadas en un pipeline, donde cada paso produce un nuevo resultado sin modificar los datos originales

Mi ejemplo favorito es por ejemplo en un caso hipotetico utilizar el output de un sort en una lista desordenada para facilitar un filter, ya teniendo las calificaciones ordenadas. 

En Python las expresiones lambda son la implementacion directa de este concepto. Cada transformacion del pipeline es una lambda, una funcion pequena que recibe una entrada y regresa una salida y no modifica nada 
