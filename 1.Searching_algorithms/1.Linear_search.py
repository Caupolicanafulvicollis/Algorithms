def busquedaSecuencial(lista,item):
    position=0
    encontrado=False

    while position < len(lista) and not encontrado:
        if lista[position] == item:
            encontrado=True
        else:
            position += 1
    print(encontrado,position)

lista=[1, 2, 32, 8, 17, 19, 42, 13, 0]
print(busquedaSecuencial(lista, 13))
