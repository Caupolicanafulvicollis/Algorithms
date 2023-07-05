# Algoritmos de búsqueda
<img src="https://img.shields.io/badge/language-python-orange.svg" style="zoom:100%;" />

## ÍNDICE
* [Introducción](#introduccion)
* [Búsqueda Lineal](#búsqueda-lineal-linear-search)
  - [Código de busqueda lineal](https://github.com/gnvidal/Algorithms/blob/93dc6e423633a95cc60a16a0b3e6801b8ca24c3b/1.Searching_algorithms/1.Search_linear/Search_linear.py)
    - [Explicación del código](https://github.com/gnvidal/Algorithms/blob/efdc87170ec781c439ad154daa8cd42e776d1953/1.Searching_algorithms/1.Search_linear/Linear_search.jpg)

# Introducción

>Los algoritmos de búsqueda son algortimos que nos permite encontrar un valor dentro de un conjunto de datos.
>Para que un algoritmo de búsqueda pueda operar sobre una lista de manera efectiva, existen ciertas condiciones que deben cumplirse:
>
>Ordenación de la lista: En muchos algoritmos de búsqueda eficientes, se asume que la lista está ordenada de alguna manera. Esto permite utilizar técnicas de búsqueda más rápidas, como la búsqueda binaria, en lugar de una búsqueda lineal. Si la lista no está ordenada, es posible que sea necesario realizar una etapa de ordenamiento previa para optimizar el proceso de búsqueda.
>
>Acceso aleatorio: Los algoritmos de búsqueda eficientes suelen requerir acceso aleatorio a los elementos de la lista. Esto significa que se puede acceder directamente a cualquier elemento de la lista utilizando su posición o índice. Si la lista no permite acceso aleatorio, como ocurre en las listas enlazadas, algunos algoritmos de búsqueda pueden no ser aplicables y sería necesario adaptar el enfoque de búsqueda.
>
>Elementos comparables: En la mayoría de los algoritmos de búsqueda, se comparan los elementos de la lista para determinar si coinciden con el valor buscado. Por lo tanto, los elementos de la lista deben ser comparables, lo que implica que se pueda definir una relación de orden o igualdad entre ellos. Si los elementos no son comparables, se deben utilizar técnicas de búsqueda alternativas o se debe adaptar el algoritmo para trabajar con el tipo de datos específico.
>
>Tamaño y complejidad: El tamaño de la lista y la complejidad de los elementos también son factores importantes a tener en cuenta al seleccionar un algoritmo de búsqueda. Algunos algoritmos son más adecuados para listas pequeñas o para búsquedas en tiempo real, mientras que otros son más eficientes en listas grandes o en escenarios con requerimientos de recursos específicos.
>
>En resumen, las condiciones clave para un algoritmo de búsqueda efectivo en una lista son: ordenación (si es necesario), acceso aleatorio a los elementos, comparabilidad de los elementos y consideración del tamaño y complejidad de la lista. 

* ### **Búsqueda lineal (Linear Search)**

Compara cada elemento de manera secuencial con el valor buscado. Es simple pero puede ser ineficiente para grandes conjuntos de datos no ordenados.
[[code](https://github.com/gnvidal/Algorithms/blob/a12091ec9b6003532a7cbdf95a22125019b69a96/1.Searching_algorithms/1.Linear_search.py)]

* ### **Búsqueda binaria (Binary Search)**
Solo aplicable a conjuntos de datos ordenados. Divide el conjunto a la mitad en cada iteración, eliminando la mitad de los elementos en cada paso. Es más eficiente que la búsqueda lineal.
[[code](https://github.com/gnvidal/Algorithms/blob/76d921a4c6f78b6c2e39ba693631a83a44820bfc/1.Searching_algorithms/2.Searching_binary.py)]


* ### **Búsqueda por interpolación (Interpolation Search)**

Similar a la búsqueda binaria, pero utiliza una estimación interpolada para determinar la ubicación probable del elemento buscado. Es más rápida que la búsqueda binaria para conjuntos de datos uniformemente distribuidos.
[[code](https://github.com/gnvidal/Algorithms/blob/76d921a4c6f78b6c2e39ba693631a83a44820bfc/1.Searching_algorithms/2.Searching_binary.py)]

* ### **Búsqueda de salto (Jump Search)**

Funciona saltando hacia adelante en bloques fijos en lugar de comparar cada elemento. Requiere que los datos estén ordenados y es más eficiente que la búsqueda lineal.

**Búsqueda exponencial (Exponential Search)**: Comienza con un rango pequeño y lo expande exponencialmente hasta encontrar un rango que contenga el elemento buscado. Luego, realiza una búsqueda binaria en ese rango. Es eficiente para conjuntos de datos ordenados y no ordenados.

**Búsqueda de interpolación inversa (Inverse Interpolation Search)**: Una variante de la búsqueda por interpolación que se aplica cuando los datos están distribuidos de manera no uniforme y se conoce la función inversa de distribución.

**Búsqueda de Fibonacci (Fibonacci Search)**: Utiliza la secuencia de Fibonacci para dividir el conjunto de datos en segmentos. Es similar a la búsqueda binaria pero puede tener un mejor rendimiento en ciertos casos.

**Búsqueda de árbol binario (Binary Tree Search)**: Utiliza un árbol binario de búsqueda para organizar los datos de manera que la búsqueda se realice de manera eficiente en tiempo logarítmico. Requiere la construcción previa del árbol.

**Búsqueda de tabla hash (Hash Table Search)**: Utiliza una función hash para mapear las claves de búsqueda a posiciones de una tabla. Permite búsquedas rápidas en tiempo constante, pero requiere una buena
