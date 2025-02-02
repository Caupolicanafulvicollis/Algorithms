def menu(a):
    print("Agregar listas")
    validar_numero(a)
    crear_lista(a)

def validar_numero(a):
    if isinstance(a,int):
        

def crear_lista(a):
    list1=[]
    try:
        while True:
            if isinstance(a,int):
                print(f"El dato {a} ingresado es un int")
                if a != 0:
                    list1.append(a)
                else: 
                    return False
                return False
            else: 
                print(f"El dato ingresado {a} no es un int")
            return True
    except Exception as e:
        print(f"Error: {e}")
        

    pass
        

if __name__ == "__main__":
    num1=int(input("Ingresar un int para agregar a la lista: "))
    menu(num1)