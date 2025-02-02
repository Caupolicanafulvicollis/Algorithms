def detectar(a,list1):
    list2=[]
    list1=sorted(list1)
    for i in list1:
        if i ==a:
            return True    
    return False
    

if __name__ == "__main__":



# def buscar(a, list1):
#     try:
#         return list1.index(a) #Retorna la poscion del elemento
#     except ValueError:
#         return -1 #Si el elemento no esta, devuleve -1