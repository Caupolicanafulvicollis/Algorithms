def binary_search(lista,elemento):
    izq=0
    der=len(lista)-1
    pasos=0
    # Inicializo respuesta, el valor no fue encontrado
    while izq <= der:
        pasos+=1
        medio=(izq+der)//2
        print(f"DEBUG: 'izq:'{izq}' | 'der:'{der}' | 'medio:'{medio}")
        #si el medio es igual al valor buscado, lo devuleve
        if lista[medio]==elemento:
            print(f'Valor encontrado en {pasos} pasos, en la posicion {medio}')
            return True
        #si el valor del punto medio es mayor que 'elemento', sigue buscando
        #en el segmento de la izquierda: [izq, medio-1], descartando la derecha
        elif lista[medio]>elemento:
            der=medio-1
        # sino, sigue buscando en el segmento de la derecha:
        # [medio+1, der], descartando la izquierda
        elif lista[medio]<elemento:
            izq=medio+1
        # si no salió del ciclo, vuelve a iterar con el nuevo segmento
    print(f'Valor no encontrado')
    return False

if __name__ == '__main__':
    lista=[1,3,5,7,9,11,13,15,17,19,21,23]
    elemento=19
    posicion=binary_search(lista,elemento)
    print(posicion)
