tupla = ()
personas=[]

def rutas(pais, ciudad):
    destinos=list(map(lambda p, c: (p,c), pais, ciudad))
    return destinos

def ingreso_datos(nombre, apellido,dni,destino):
    while True: #Hasta que resulte las entradas    
        try:
    #Nombre y apellido
            nombre=input("Ingrese el nombre del pasajero: ").title()
            apellido=input("Ingrese el apellido del pasajero: ").title()
            dni=int(input("Ingrese el DNI del pasajero: ").strip())
            destino=input("Ingrese ciudad de destino en codigo IATA: ").upper().strip()
            if not nombre or not apellido:
                raise ValueError("El nombre y el apellido no pueden estar vacíos")
            if not nombre.replace(" ", "").isalpha() or not apellido.replace(" ", "").isalpha() or not destino.isalpha():
                raise ValueError("El nombre, apellido y destino solo pueden contener letras")
            if dni <= 0 or len(str(dni)) < 7 or len(str(dni)) > 9:
                raise ValueError("El DNI debe ser un número válido con 7 a 9 dígitos")
            if not dni:
                raise ValueError("El DNI no puede estar vacio")
            if not destino: 
                raise ValueError("El destino no puede estar vacio")
            break  # Salir del bucle si todo está correcto
        except ValueError as e:
            print(f"Ocurrió un error: {e}")
            print("Ingrese los datos del pasajero de manera correcta.")

    return nombre, apellido, dni, destino


def menu():
    while True: #Hasta que resulte las entradas    
        try:
        #Nombre y apellido
            print("---- BASE DE DATOS DESTINOS ----")
            print("""Elija su operación que quiera desarrollar: \n 
                  1. Agregar pasajeros a la lista de viajeros.\n 
                  2. Agregar ciudades a la lista de ciudades. \n 
                  3. Dado el DNI de un pasajero, ver a qué ciudad viaja. \n 
                  4. Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.\n 
                  5. Dado un país, mostrar cuántos pasajeros viajan a ese país. \n 
                  6. Salir del programa.""")
            option=int(input("Ingrese su opción: ").strip())
            if not option: 
                raise ValueError("La opción no puede estar vacia")
            if option >= 1 and option <= 7:
                raise ValueError("La opción debe ser un número valido entre 1 al 7.")
            if option   == 1: 
                ingreso_datos()
            elif option == 2: 
                rutas()
            elif option == 3:
                destino()
            elif option == 4:
                flujo_destino_ciudad()
            elif option == 5: 
                flujo_destino_pais()
            elif option == 6:
                exit() 
            break  # Salir del bucle si todo está correcto
        except ValueError as e:
            print(f"Ocurrió un error: {e}")
            print("Ingrese los datos del pasajero de manera correcta.")

        
                        



if __name__ == "__main__":
    menu()
