import math 
def linear_search(lista, elemento):
    posicion=0
    pasos=0
    while posicion<len(lista):
        pasos+=1
        print(f"DEBUG: 'elemento:{elemento}' | 'posicion:{posicion}' | 'pasos:{pasos}'")
        if lista[posicion]==elemento:
            print(f"se ha encontrado el {elemento} en la posicion {posicion}, en {pasos} pasos")
            return posicion
        posicion+=1
        print(f"el elemento {elemento} no fue encontrado en la lista")
        return -1
def jump_search(lista,elemento):
    step = math.sqrt(len(lista))
    last_index = 0
    while last_index < len(lista) and lista[int(min(step, len(lista) - 1))] < elemento:
        last_index = step
        step += math.sqrt(len(lista))
    return linear_search(lista[int(last_index - step):min(int(last_index), len(lista))], elemento)


if __name__ =='__main__':
    lista=[1,3,5,7,9,11,13,15,17,19,21,23]
    elemento=3
    result = jump_search(lista, elemento)
    if result != -1:
        print(f"Valor encontrado en la posición {result}")
    else:
        print(f"Valor no encontrado en la lista")

////////////////////////////////////////////////////////////////////////////////////////////////////////////////

import math
def linear_search(B, elemento, loc):
    i = 0
    while i != len(B):
        if B[i] == elemento:
            return loc+i
        i += 1
    return -1
def jump_search(lista, elemento):
    print("Entering Jump Search")
    n = len(lista)                          # Length of the array
    step= int(math.sqrt(n))               # Step length
    i = 0                               # Starting interval

    while i != len(lista)-1 and lista[i] < elemento:
        print("Processing Block - {}".format(lista[i: i+step]))
        if lista[i+step-1] == elemento:            # Found the search key
            return i+step-1
        elif lista[i+step-1] > elemento:           # Linear search for key in block
            B = lista[i: i+step-1]
            return linear_search(B, elemento, i)
        i += step

    B = lista[i:i+step]                        # Step 5
    print("Processing Block - {}".format(B))
    return linear_search(B, elemento, i)


if __name__ =='__main__':
    lista=[1,3,5,7,9,11,13,15,17,19,21,23]
    elemento=21
    jump_search(lista, elemento)
