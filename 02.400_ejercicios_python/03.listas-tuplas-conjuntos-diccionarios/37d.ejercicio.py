list1=[]

def crear_lista(lista): 
    while True:
        try: 
            a = float(input("Ingresar un numero para agregar a la lista (0 para terminar): "))
            if a == 0:  # Condición de salida 
                print("Ingreso de datos finalizado.")
                break
            list1.append(a)   # Agregar el número a la lista
        except ValueError:
            print("❌ Error: Ingresa solo números.")

    return lista  # Retorna la lista completa


def del_menor(list1):
    while True: 
        try:
            num2=float(input("Ingresar un numero para eliminar los datos menores a este: "))
            list1=list1.sort()
        
        except ValueError:

