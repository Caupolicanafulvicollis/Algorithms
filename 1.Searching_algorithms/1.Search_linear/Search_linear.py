def linear_search(lista, elemento):
    posicion = 0
    encontrado = False
    pasos=0 
    
    while posicion < len(lista):
        pasos+=1
        print(f"DEBUG: 'elemento:'{elemento}' | 'posicion:'{posicion}' | 'paso:'{pasos}")
        if lista[posicion] == elemento:
            print(f"el elemento {elemento} se encuentra en la posicion de {posicion}, se encontro en el paso {pasos}")
            encontrado==True
            break
        else:
            posicion+=1

if __name__ == '__main__':
    lista=[1,3,5,7,9,11,13,15,17,19,21,23]
    elemento=22
    linear_search(lista, elemento)
