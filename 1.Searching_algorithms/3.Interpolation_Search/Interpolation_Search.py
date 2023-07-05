def interpolation_search(lista,elemento):
  (left,right)=(0, len(lista)-1)
  pasos=0
  encontrado=False
  while lista[right]!=lista[left] and lista[left]<=elemento<=lista[right]:
    mid=left+(elemento-lista[left])*(right-left)//(lista[right]-lista[left])
    pasos=+1
    print(f"DEBUG: 'left:'{left}' | 'right:'{right}' | 'medio:'{mid}")
    if elemento == lista[mid]:
      print(f'Valor encontrado en {pasos} pasos, en la posicion {mid}')
      return encontrado==True
    elif elemento<lista[mid]:
      right=mid-1
    else:
      left=mid+1
  print(f'Valor {elemento} no encontrado')
  return encontrado

if __name__ =='__main__':
  lista=[1,3,5,7,9,11,13,15,17,19,21,23]
  elemento=21
  interpolation_search(lista,elemento)
