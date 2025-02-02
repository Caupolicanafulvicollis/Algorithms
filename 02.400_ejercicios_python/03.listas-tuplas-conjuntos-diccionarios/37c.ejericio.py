def sumatoria1(list1):
    a=0
    for i in list1:
        a+=i
    return a
        

def sumatoria2(list1):
        return sum(list1)    

if __name__ == "__main__":
    # 1️⃣ Suma de una lista vacía (debe ser 0)
    assert sumatoria1([]) == 0
    assert sumatoria2([]) == 0

    # 2️⃣ Suma de una lista con un solo número
    assert sumatoria1([5]) == 5
    assert sumatoria2([5]) == 5

    # 3️⃣ Suma de una lista con múltiples números positivos
    assert sumatoria1([1, 2, 3, 4, 5]) == 15
    assert sumatoria2([1, 2, 3, 4, 5]) == 15

    # 4️⃣ Suma de una lista con números negativos
    assert sumatoria1([-1, -2, -3, -4, -5]) == -15
    assert sumatoria2([-1, -2, -3, -4, -5]) == -15

    # 5️⃣ Suma de una lista con positivos y negativos
    assert sumatoria1([10, -5, 15, -10]) == 10
    assert sumatoria2([10, -5, 15, -10]) == 10

    # 6️⃣ Suma de una lista con ceros
    assert sumatoria1([0, 0, 0, 0]) == 0
    assert sumatoria2([0, 0, 0, 0]) == 0

    # 7️⃣ Suma de una lista con números grandes
    assert sumatoria1([1000, 2000, 3000]) == 6000
    assert sumatoria2([1000, 2000, 3000]) == 6000

    # 8️⃣ Suma de una lista con números decimales
    assert sumatoria1([1.5, 2.5, 3.5]) == 7.5
    assert sumatoria2([1.5, 2.5, 3.5]) == 7.5

    # 9️⃣ Suma de una lista con números repetidos
    assert sumatoria1([5, 5, 5, 5]) == 20
    assert sumatoria2([5, 5, 5, 5]) == 20

    # 🔟 Suma de una lista de gran tamaño
    lista_grande = list(range(1, 101))  # Lista de 1 a 100
    assert sumatoria1(lista_grande) == sum(lista_grande)
    assert sumatoria2(lista_grande) == sum(lista_grande)
    print("✅ Todas las pruebas pasaron correctamente.")
