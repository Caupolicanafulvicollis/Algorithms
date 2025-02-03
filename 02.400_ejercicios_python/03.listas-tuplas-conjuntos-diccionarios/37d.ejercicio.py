def filtrar_menores(numeros, nuevo_numero):
    # Filtrar los números menores que el número ingresado
    return [num for num in numeros if num < nuevo_numero]

if __name__ == "__main__":
    # Casos de prueba con assert
    assert filtrar_menores([3, 10, 5, 8, 15, 2], 7) == [3, 5, 2]
    assert filtrar_menores([1, 4, 6, 9, 12], 5) == [1, 4]
    assert filtrar_menores([0, -1, -5, 10, 8], 0) == [-1, -5]
    assert filtrar_menores([20, 30, 40, 50], 25) == [20]
    assert filtrar_menores([2, 2, 2, 2, 2], 3) == [2, 2, 2, 2, 2]
    assert filtrar_menores([5, 10, 15], 5) == []  # Ningún número es menor a 5
    assert filtrar_menores([1, 2, 3, 4, 5], 10) == [1, 2, 3, 4, 5]  # Todos los números son menores a 10
    assert filtrar_menores([], 5) == []  # Lista vacía debe dar otra lista vacía
    assert filtrar_menores([-10, -5, 0, 5, 10], -3) == [-10, -5]  # Solo los negativos menores a -3
    assert filtrar_menores([100, 200, 300], 50) == []  # Todos los números son mayores

    print("¡Todos los tests pasaron exitosamente! 🚀")
    print("✅ Todas las pruebas pasaron correctamente.")
