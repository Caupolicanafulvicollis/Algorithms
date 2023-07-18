def linear_search_recursive(lista, indice, elemento,pasos=0):
  print(f"DEBUG: 'elemento:'{elemento}' | 'indice:'{indice}' | 'paso:'{pasos}")
  if indice>=len(lista):
    print(f"El elemento {elemento} no se encontro en la lista.")
    return -1
  if lista[indice]==elemento:
    print(f"El elemento {elemento} se encuentra en la posición {indice}. Se encontró en {pasos} pasos.")
    pasos+=1
  elif lista[indice]!=elemento:
    return linear_search_recursive(lista, indice+1, elemento, pasos+1)

if __name__=="__main__":
    lista=[1,3,5,7,9,11,13,15,17,19,21,23]
    elemento=5
    linear_search_recursive(lista, 0, elemento) #se da el valor del indice 0 que va a ser el lugar donde se inicia

def binary_search(lista, elemento, medio, pasos=0):
    der=len(lista)-1
    izq=0
    print(f"DEBUG: 'derecha: {der}' | 'izquierda: {izq}' | 'pasos: {medio}' | 'elemento {elemento}'")
    if izq<=der:
        pasos+=1
        medio=(der+izq)//2
        print(f"DEBUG: 'derecha: {der}' | 'izquierda: {izq}' | 'pasos: {medio}' | 'elemento {elemento}'")
        encontrado=True
        if lista[medio]==elemento:
            print(f"elemento {elemento} se encuentra en la posicion {medio}, el algoritmo lo ubico en {pasos} pasos")
            encontrado= True
            break
        elif lista[medio]>elemento:
            der=medio-1
            print(f"DEBUG: 'derecha: {der}' | 'el valor de la izquierda se cambia a: {izq}' | 'pasos: {pasos}' | 'elemento {elemento}'")
        elif lista[medio]<elemento:
            izq=medio+1
            print(f"DEBUG: 'el valor de la derecha se cambia a: {der}' | 'izquierda: {izq}' | 'pasos: {pasos}' | 'elemento {elemento}'")
    if not encontrado:
        print(f"el elemento {elemento} no esta en la lista")  

if __name__ == "__main__":
    lista=[1,3,5,7,9,11,13,15,17,19,21,23]
    elemento=21
    binary_search(lista, elemento)
