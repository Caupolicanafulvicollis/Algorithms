import unittest
from unittest.mock import patch
import unittest
from unittest.mock import patch

def solicitar_numeros():
    lista = []
    while True:
        num = int(input("Ingrese un número (0 para finalizar): "))
        if num == 0:
            break
        lista.append(num)
    return lista

def eliminar_primera_ocurrencia(lista):
    num = int(input("Ingrese un número a eliminar de la lista: "))
    if num in lista:
        lista.remove(num)
    else:
        print("No es posible eliminar el número, no está en la lista.")

def sumar_elementos(lista):
    suma = sum(lista)
    print(f"La sumatoria de los elementos de la lista es: {suma}")
    return suma  # Se devuelve para poder hacer pruebas

def filtrar_menores(lista):
    num = int(input("Ingrese un número para filtrar los menores: "))
    nueva_lista = [x for x in lista if x < num]
    print("Lista de elementos menores que el número dado:", nueva_lista)
    return nueva_lista  # Se devuelve para poder hacer pruebas

def generar_tuplas(lista):
    frecuencias = {}
    for num in lista:
        frecuencias[num] = frecuencias.get(num, 0) + 1
    lista_tuplas = list(frecuencias.items())
    print("Lista de tuplas (número, frecuencia):", lista_tuplas)
    return lista_tuplas  # Se devuelve para poder hacer pruebas

def main():
    lista = solicitar_numeros()
    eliminar_primera_ocurrencia(lista)
    sumar_elementos(lista)
    filtrar_menores(lista)
    generar_tuplas(lista)

# **Ejecutar pruebas antes de iniciar el programa**
if __name__ == "__main__":
        # Simular entrada de números [5, 10, 15, 20, 0] (cierra con 0)
    with patch("builtins.input", side_effect=["5", "10", "15", "20", "0"]):
        assert solicitar_numeros() == [5, 10, 15, 20], "Error en solicitar_numeros()"

    # Probar eliminación de un número existente
    lista = [5, 10, 15, 20]
    with patch("builtins.input", side_effect=["10"]):
        eliminar_primera_ocurrencia(lista)
        assert lista == [5, 15, 20], "Error en eliminar_primera_ocurrencia()"

    # Probar eliminación de un número que no está en la lista
    lista = [5, 15, 20]
    with patch("builtins.input", side_effect=["50"]):
        eliminar_primera_ocurrencia(lista)
        assert lista == [5, 15, 20], "Error al intentar eliminar un número inexistente"

    # Probar sumatoria de elementos
    assert sumar_elementos([5, 15, 20]) == 40, "Error en sumar_elementos()"

    # Probar filtrado de elementos menores que un número dado
    with patch("builtins.input", side_effect=["15"]):
        assert filtrar_menores([5, 10, 15, 20]) == [5, 10], "Error en filtrar_menores()"
