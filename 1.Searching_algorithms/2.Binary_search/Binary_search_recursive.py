def binary_search_recursive(lista, elemento,  left=0, right=None, pasos=0):
  if right is None:
    right=len(lista)-1
  medio=(left+right)//2
  encontrado=False
  if left<=right:
    pasos+=1
    print(f"DEBUG: 'derecha: {right}' | 'izquierda: {left}' | 'pasos: {medio}' | 'elemento {elemento}'")
    if lista[medio]==elemento:
      print(f"elemento {elemento} se encuentra en la posicion {medio}, el algoritmo lo ubico en {pasos} pasos")
      encontrado=True
    elif lista[medio]>elemento:
        print(f"DEBUG2: 'izquierda: {left}' | 'el valor de la derecha se cambia a: {right}' | 'pasos: {pasos}' | 'elemento {elemento}'")
        return binary_search_recursive(lista, elemento, left, medio-1, pasos)
    elif lista[medio]<elemento:
      return binary_search_recursive(lista, elemento, medio+1, right, pasos)
  if not encontrado:
    print(f"el elemento {elemento} no esta en la lista")  

if __name__ == "__main__":
  lista=[1,3,5,7,9,11,13,15,17,19,21,23]
  elemento=2
  binary_search_recursive(lista, elemento)
