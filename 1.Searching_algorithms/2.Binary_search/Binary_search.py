def binary_search(lista, elemento):
    izq=0
    der=len(lista)-1
    encontrado=False
    pasos=0

    while izq<=der:
        pasos+=1
        medio=(der+izq)//2
        print(f"DEBUG: 'izquierda:'{izq}' | 'derecha:'{der}' | 'pasos:'{pasos} | 'medio:'{medio}")
        if lista[medio] == elemento:
            print(f"El elemento {elemento} se encuentra en la posición {medio}. Se encontró en {pasos} pasos.")
            encontrado=True
            break
        elif lista[medio]>elemento:
            der=medio-1
            print(f"DEBUG: 'izquierda: {izq} | 'cambia valor de la derecha a: {der}' | 'pasos:{pasos}'")
        elif lista[medio]<elemento:
            izq=medio+1
            print(f"DEBUG: 'cambia valor de la izquierda a: {izq} | 'derecha: {der}' | 'pasos:{pasos}'")
    if not encontrado:
        print(f"El elemento {elemento} no se encuentra en la lista.")
if __name__ == "__main__":
    lista=[1,3,5,7,9,11,13,15,17,19,21,23]
    elemento=22
    binary_search(lista, elemento)
