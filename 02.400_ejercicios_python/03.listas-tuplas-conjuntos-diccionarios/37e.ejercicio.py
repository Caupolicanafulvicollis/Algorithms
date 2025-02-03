def contador_registrador(lista):
    tupla_completa=[]
    for i in lista:
        contador=0
        for j in lista:
            if j == i:
                contador +=1
        tupla=(i,j) # Crear la tupla
        tupla_completa.append(tupla) # Agregarla a la lista

