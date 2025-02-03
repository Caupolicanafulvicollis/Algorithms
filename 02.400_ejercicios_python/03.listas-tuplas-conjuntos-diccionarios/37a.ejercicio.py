def crear_lista():
    list1=[]
    while True:
        try: 
            num1 = float(input("Ingresar un numero para agregar a la lista (0 para terminar): "))
            if num1 == 0:  # Condición de salida 
                print("Ingreso de datos finalizado.")
                break
            list1.append(num1)   # Agregar el número a la lista
        except ValueError:
            print("❌ Error: Ingresa solo números.")

    return list1  # Retorna la lista completa



# Ejecutar la función y mostrar el resultado
print("Ingresar datos en una lista")
resultado = crear_lista()
print("Lista final:", resultado)