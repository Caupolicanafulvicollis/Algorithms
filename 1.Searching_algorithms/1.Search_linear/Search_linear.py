def search_linear(lista, elemento):
    posicion = 0
    encontrado = 0
    pasos = 0
    while posicion<len(lista):
        pasos+=1
        print(f"DEBUG: 'elemento:'{elemento}' | 'posicion:'{posicion}' | 'paso:'{pasos}")
        if lista[posicion] == elemento:
            encontrado = 1
            print(f"El elemento {elemento} se encuentra en la posición {posicion}. Se encontró en {pasos} pasos.")
            break
        else:
            print("El elemento no se encontró en la lista.")
        posicion += 1

if __name__ == "__main__":
    lista=[1,3,5,7,9,11,13,15,17,19,21,23]
    elemento=5
    search_linear(lista, elemento)
