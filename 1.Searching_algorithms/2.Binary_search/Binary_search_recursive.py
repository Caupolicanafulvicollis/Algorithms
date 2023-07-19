def binary_search_recursive(lista, elemento,  izq=0, der=None, pasos=0):
  if der is None:
    der=len(lista)-1
  medio=(izq+der)//2
  encontrado=False
  if izq<=der:
    pasos+=1
    print(f"DEBUG: 'derecha: {der}' | 'izquierda: {izq}' | 'pasos: {medio}' | 'elemento {elemento}'")
    if lista[medio]==elemento:
      print(f"elemento {elemento} se encuentra en la posicion {medio}, el algoritmo lo ubico en {pasos} pasos")
      encontrado=True
    elif lista[medio]>elemento:
      return binary_search_recursive(lista, elemento, izq, medio-1, pasos)
    else:
      return binary_search_recursive(lista, elemento, medio+1, der, pasos)
  if not encontrado:
    print(f"el elemento {elemento} no esta en la lista")  

if __name__ == "__main__":
  lista=[1,3,5,7,9,11,13,15,17,19,21,23]
  elemento=7
  binary_search_recursive(lista, elemento)
