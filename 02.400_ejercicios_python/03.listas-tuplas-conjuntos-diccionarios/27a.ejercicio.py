def crear_lista():
    list1=[]
    while True:
        num1=int(input("Ingresar un int para agregar a la lista: "))
        while True: 
            if isinstance(num1,int):
                print(f"El dato {num1} ingresado es un int")
                if num1 != 0:
                    list1.append(num1)
                else:  
                    print("Ingresar datos en la lsita ha terminado")
            else: 
                print(f"El dato ingresado {num1} no es un int")
                return True

print("Ingresar datos en una lista")
crear_lista()