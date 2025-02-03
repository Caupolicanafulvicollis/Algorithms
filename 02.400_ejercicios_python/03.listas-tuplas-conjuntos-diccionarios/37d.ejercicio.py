list1=[]

def crear_lista(num1,lista): 
    while True:
        try: 
            num1 = float(input("Ingresar un int para agregar a la lista (0 para terminar): "))
            if num1 == 0:  # Condición de salida 
                print("Ingreso de datos finalizado.")
                break
            list1.append(num1)   # Agregar el número a la lista
        except ValueError:
            print("❌ Error: Ingresa solo números enteros.")

    return lista  # Retorna la lista completa


def del_menor(a,list1)