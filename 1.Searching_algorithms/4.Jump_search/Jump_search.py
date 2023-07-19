import math
def jump_search(lista, elemento):
  pasos=math.sqrt(len(lista))

  while i != len(A)-1 and A[i] < item:
    print("Processing Block - {}".format(A[i: i+m]))
    if A[i+m-1] == item:            # Found the search key
      return i+m-1
    elif A[i+m-1] > item:           # Linear search for key in block
      B = A[i: i+m-1]
      return linear_search(B, item, i)
      i += m

    B = A[i:i+m]                        # Step 5
    print("Processing Block - {}".format(B))
    return linear_search(B, item, i)

import math
def jump_search(lista,elemento):
  left=0
  right=len(lista)-1
  pasos=math.sqrt(n)
  encontrado=False
  while :

    pasos=+1
    print(f"DEBUG: 'left:'{left}' | 'right:'{right}' | 'medio:'{mid}")
    if elemento == lista[mid]:
      print(f'Valor encontrado en {pasos} pasos, en la posicion {mid}')
      encontrado==True
      break
    elif elemento<lista[mid]:
      right=mid-1
    else:
      left=mid+1
  print(f'Valor {elemento} no encontrado')
  return encontrado

if __name__ =='__main__':
  lista=[1,3,5,7,9,11,13,15,17,19,21,23]
  elemento=21
  jump_search(lista,elemento)
