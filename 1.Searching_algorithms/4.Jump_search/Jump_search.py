import math 
def jump_search(lista,elemento):
    step=math.sqrt(len(lista))
    last_index=0
    while lista[int(min(step,len(lista)-1))]<elemento:
       last_index=step
       step+=math.sqrt(len(lista))
       if last_index>=len(lista):
          return -1
    
    while lista[int(last_index)]<elemento:
       last_index+=1
       if last_index==min(step,len(lista)):
            return-1
    if lista[int(last_index)]==elemento:
       return last_index
    return-1
    print(f'Valor encontrado en {elemento}')

if __name__ =='__main__':
  lista=[1,3,5,7,9,11,13,15,17,19,21,23]
  elemento=21
  jump_search(lista,elemento)
////////////////////////////
import math 
def jump_search(lista,elemento):
    step=math.sqrt(len(lista))
    step=0
    while lista[int(min(step,len(lista)-1))]<elemento:
       step+=math.sqrt(len(lista))
       if step>=len(lista):
        print(f"DEBUG: 'step:'{step}' | 'right:'{right}' | 'medio:'{mid}")
        return -1
    while lista[int(step)]<elemento:
        step+=1
        if step==min(step,len(lista)):
            return-1
    if lista[int(step)]==elemento:
        print(f'Valor encontrado {elemento} fue encontrado en {step} pasos, en la poscion ')
        return step
    

if __name__ =='__main__':
  lista=[1,3,5,7,9,11,13,15,17,19,21,23]
  elemento=21
  jump_search(lista,elemento)
