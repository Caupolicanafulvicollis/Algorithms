def binary_search(lista,elemento):
    izq=0
    der=len(lista)-1
    pos=-1 # Inicializo respuesta, el valor no fue encontrado
    while izq <= der:
        #valor punto medio del segmento
        medio=(izq+der)//2
        print(f"DEBUG: 'izq:'{izq}' | 'der:'{der}' | 'medio:'{medio}")
        #si el medio es igual al valor buscado, lo devuleve
        if lista[medio]==elemento:
            pos=medio
        #si el valor del punto medio es mayor que 'elemento', sigue buscando
        #en el segmento de la izquierda: [izq, medio-1], descartando la derecha
        elif lista[medio]>elemento:
            der=medio-1
        # sino, sigue buscando en el segmento de la derecha:
        # [medio+1, der], descartando la izquierda
        else:
            izq=medio+1
        # si no salió del ciclo, vuelve a iterar con el nuevo segmento
    return pos

if __name__ == '__main__':
    lista=input('Dame una listaa ordenada ([[]] para terminar): ')
    while lista !=[[]]:
        elemento= input('Valor buscado?: ')
        resultado=binary_search(lista,elemento)
        print(f"Resultado: {resultado}")
        lista=input('Dame una lista ordenada ([[]] para terminar): ')
