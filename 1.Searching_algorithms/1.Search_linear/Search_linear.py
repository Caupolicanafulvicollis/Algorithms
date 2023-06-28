def linear_search(lista,elemento):
    position=0
    encontrado=False
    pasos=0
    while elemento<len(lista) and not encontrado:
        pasos+=1
        if lista[position]==elemento:
            encontrado=True
        else:
            position += 1
    print(encontrado,position)

if __name__ == '__main__':
    lista=[1,3,5,7,9,11,13,15,17,19,21,23]
    elemento=19
    linear_search(lista,elemento)
