def search_linear(lista, elemento):
    posicion = 0
    encontrado = 0
    pasos = 0

    while posicion < len(lista):
        pasos += 1

        if lista[posicion] == elemento:
            encontrado = 1
            break

        posicion += 1

    if encontrado == 1:
        return f"El elemento {elemento} se encuentra en la posición {posicion}. Se encontró en {pasos} pasos."
    else:
        return "El elemento no se encontró en la lista."

# Ejemplo de uso
mi_lista =[1,3,5,7,9,11,13,15,17,19,21,23]
mi_elemento =19

resultado=search_linear(mi_lista, mi_elemento)
print(resultado)
