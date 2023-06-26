# Algoritmos de búsqueda

<img src="https://img.shields.io/badge/language-python-orange.svg" style="zoom:100%;" />

* **Búsqueda lineal (Linear Search)**:

Compara cada elemento de manera secuencial con el valor buscado. Es simple pero puede ser ineficiente para grandes conjuntos de datos no ordenados.
[[code](https://github.com/gnvidal/Algorithms/blob/a12091ec9b6003532a7cbdf95a22125019b69a96/1.Searching_algorithms/1.Linear_search.py)]

**Búsqueda binaria (Binary Search)**: Solo aplicable a conjuntos de datos ordenados. Divide el conjunto a la mitad en cada iteración, eliminando la mitad de los elementos en cada paso. Es más eficiente que la búsqueda lineal.

**Búsqueda por interpolación (Interpolation Search)**: Similar a la búsqueda binaria, pero utiliza una estimación interpolada para determinar la ubicación probable del elemento buscado. Es más rápida que la búsqueda binaria para conjuntos de datos uniformemente distribuidos.

**Búsqueda de salto (Jump Search)**: Funciona saltando hacia adelante en bloques fijos en lugar de comparar cada elemento. Requiere que los datos estén ordenados y es más eficiente que la búsqueda lineal.

**Búsqueda exponencial (Exponential Search)**: Comienza con un rango pequeño y lo expande exponencialmente hasta encontrar un rango que contenga el elemento buscado. Luego, realiza una búsqueda binaria en ese rango. Es eficiente para conjuntos de datos ordenados y no ordenados.

**Búsqueda de interpolación inversa (Inverse Interpolation Search)**: Una variante de la búsqueda por interpolación que se aplica cuando los datos están distribuidos de manera no uniforme y se conoce la función inversa de distribución.

**Búsqueda de Fibonacci (Fibonacci Search)**: Utiliza la secuencia de Fibonacci para dividir el conjunto de datos en segmentos. Es similar a la búsqueda binaria pero puede tener un mejor rendimiento en ciertos casos.

**Búsqueda de árbol binario (Binary Tree Search)**: Utiliza un árbol binario de búsqueda para organizar los datos de manera que la búsqueda se realice de manera eficiente en tiempo logarítmico. Requiere la construcción previa del árbol.

**Búsqueda de tabla hash (Hash Table Search)**: Utiliza una función hash para mapear las claves de búsqueda a posiciones de una tabla. Permite búsquedas rápidas en tiempo constante, pero requiere una buena
