destinos=[]
db=[]

#Agregar ciudades a la lista de ciudades.
def rutas(pais, ciudad):
    destinos=list(map(lambda p, c: (p,c), pais, ciudad))
    return destinos

#Agregar pasajeros a la lista de viajeros.
def base_datos(nombre,apellido,dni,destino):
    bd=list(map(lambda n,a,rut,d: (f"{n} {a}",rut, d), nombre, apellido,dni,destino))
    return bd

#Dado el DNI de un pasajero, ver a qué ciudad viaja.
def destino(lista_pasajeros, dni):
    for pasajero in lista_pasajeros:
        if pasajero[1] == dni:
            if not pasajero[2]:
                print (f"El pasajero {dni} no se encuentra en la base de datos")
            else: 
                print(f"El pasajero {dni} se encuentra en la base de datos")
                print(f"El pasajero {dni} viajara a {pasajero[2]}")

def menu():
    while True:  # Hasta que se ingrese una opción válida
        try:
            # Menú de opciones
            print("---- BASE DE DATOS DESTINOS ----")
            print("""Elija la operación que desea realizar: 
                  1. Agregar pasajeros a la lista de viajeros.
                  2. Agregar ciudades a la lista de ciudades.
                  3. Dado el DNI de un pasajero, ver a qué ciudad viaja.
                  4. Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
                  5. Dado un país, mostrar cuántos pasajeros viajan a ese país.
                  6. Salir del programa.""")

            # Entrada del usuario
            option = int(input("Ingrese su opción: ").strip())

            # Validación de la opción ingresada
            if option < 1 or option > 6:
                raise ValueError("La opción debe ser un número válido entre 1 y 6.")

            # Ejecución según la opción elegida
            #1. Agregar pasajeros a la lista de viajeros.
            if option == 1: 
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
                        if dni <= 0 or len(str(dni)) < 7 or len(str(dni)) > 8:
                            raise ValueError("El DNI debe ser un número válido con 7 a 8 dígitos")
                        if not dni:
                            raise ValueError("El DNI no puede estar vacio")
                        if not destino: 
                            raise ValueError("El destino no puede estar vacio")
                        break  # Salir del bucle si todo está correcto
                    except ValueError as e:
                        print(f"Ocurrió un error: {e}")
                        print("Ingrese los datos del pasajero de manera correcta.")
                    base_datos(nombre,apellido,dni,destino)
            #2. Agregar ciudades a la lista de ciudades.
            elif option == 2:
                while True: 
                    try:
                        pais=input("Ingrese el pais: ").title()
                        ciudad=input("Ingrese la ciudad en codigo IATA: ").upper().strip()
                        if not ciudad.isalpha() or not pais.isalpha():
                            raise ValueError("El pais y la ciudad deben contener letras")
                        break
                    except ValueError as e:
                        print(f"Ocurrió un error: {e}")
                        print("Ingrese los datos del pasajero de manera correcta.")
                    rutas(pais,ciudad)
            # 3. Dado el DNI de un pasajero, ver a qué ciudad viaja.
            elif option == 3:
                while True:    
                    try:
                        pasajero=int(input("Ingrese el DNI del pasajero:" ))
                        if not pasajero:
                            raise ValueError("El DNI no puede estar vacio")
                        if pasajero <=0 or len(int(pasajero)) < 7 or len(int(pasajero))>8:
                            raise ValueError("El DNI debe ser un número válido con 7 a 8 dígitos") 
                        break
                    except ValueError as e:
                        print(f"Ocurrió un error: {e}")
                        print("Ingrese los datos del pasajero de manera correcta.")
                    destino(db, pasajero)
            #4. Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
            elif option == 4:
                flujo_destino_ciudad()
            elif option == 5: 
                flujo_destino_pais()
            elif option == 6:
                print("Saliendo del programa...")
                exit() 

            break  # Salir del bucle si todo está correcto
        
        except ValueError as e:
            print(f"Ocurrió un error: {e}")
            print("Por favor, ingrese un número válido entre 1 y 6.")


     
        
                        



if __name__ == "__main__":
    menu()
