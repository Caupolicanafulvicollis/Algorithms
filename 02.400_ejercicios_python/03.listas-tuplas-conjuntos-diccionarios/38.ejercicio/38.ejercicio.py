import unittest
from unittest.mock import patch
# Base de datos de pasajeros con nombre, RUT (DNI) y código IATA del destino
db = []

# Lista de destinos con código IATA y país
destinos = []

contador_ciudad=0
contador_pais=0

def open_db(db):
    try:    
        with open('airline_db.txt') as file_object:
            lines = file_object.readlines()
        for line in lines:
            db.append(line)
        return db  # Devuelve la lista cargada
    except FileNotFoundError:
        print("El archivo no existe")
        return []  # Devuelve una lista vacía en lugar de None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return []  # Devuelve una lista vacía en caso de otros errores


def open_destinos(destinos):
    try:    
        with open('/airline_db.txt') as file_object:
                lines=file_object.readlines()
        for line in lines:
            destinos.append(line)
        return destinos
    except FileNotFoundError:
        print("El archivo no existe")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

#1. Agregar pasajeros a la lista de viajeros.
def rutas(destinos, codigos_iata, paises): #rutas(destinos,pais,ciudad)
    # Agregar los nuevos destinos a una nueva lista
    nuevos_destinos = list((codigos_iata,paises))
    destinos.extend(nuevos_destinos)
    try:
        with open('airline_destiny.txt', 'w', encoding="utgf-8") as file:
            file.writelines(nuevos_destinos)
        print("ciudad y país agregado correctamente a la base de datos")
        return destinos
    except FileNotFoundError:
        print("El archivo no existe")
    except Exception as e:
        print(f"Ocurrio un erro: {e}")

#2. Agregar ciudades a la lista de ciudades.
def base_datos(db, nombres, apellidos, dnis, destinos):    
    db = open_db(db)
    
    if db is None:  # Manejo de error adicional
        print("No se pudo cargar la base de datos.")
        return

    nuevo_pasajero = [f"{nombres} {apellidos}", dnis, destinos]
    db.extend(nuevo_pasajero)

    try:
        with open('airline_db.txt', 'w', encoding="utf-8") as file:
            file.writelines("\n".join(map(str, db)))  # Escribe los datos en líneas separadas
        print("Pasajero agregado correctamente a la base de datos")
        return db
    except FileNotFoundError:
        print("El archivo no existe")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# 3. Dado el DNI de un pasajero, ver a qué ciudad viaja.
def busqueda_dni(lista_pasajeros, dni):
    for pasajero in lista_pasajeros:
        if pasajero[1] == dni:
            print(f"El pasajero {dni} se encuentra en la base de datos")
            print(f"El pasajero {dni} viajara a {pasajero[2]}")
            return pasajero[2]
    print(f"El pasajero con DNI {dni} no está en la base de datos")
    return None

#4. Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
def flujo_destino_ciudad(lista_pasajeros, destino):
    contador_ciudad = 0
    for pasajero in lista_pasajeros:
        if pasajero[2] == destino:
            contador_ciudad += 1
    return contador_ciudad

#5. Dado un país, mostrar cuántos pasajeros viajan a ese país.
def flujo_destino_pais(lista_pasajeros, pais, destinos): 
    contador_pais = 0
    codigos_iata = []
    # Obtener los códigos IATA de las ciudades dentro del país
    for codigo, pais_destino in destinos:
        if pais_destino == pais:
            codigos_iata.append(codigo)
    # Contar pasajeros cuyo destino está en el país seleccionado
    for pasajero in lista_pasajeros:
        if pasajero[2] in codigos_iata:
            contador_pais += 1
    return contador_pais
               
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

            #1. Agregar pasajeros a la lista de viajeros.
            if option == 1: 
                while True: #Hasta que resulte las entradas    
                    try:
                        #Solicitar datos del pasajero
                        nombre=input("Ingrese el nombre del pasajero: ").title()
                        apellido=input("Ingrese el apellido del pasajero: ").title()
                        destino=input("Ingrese ciudad de destino en codigo IATA (3 letras): ").upper().strip()
                        if not nombre.isalpha() or not apellido.isalpha():
                            raise ValueError("El nombre y apellido solo pueden contener letras")
                        if not destino.isalpha() or len(destino) !=3 :
                            raise ValueError("El codigo IATA debe tener 3 letras")
                        if not nombre.replace(" ", "").isalpha() or not apellido.replace(" ", "").isalpha() or not destino.isalpha():
                            raise ValueError("El nombre, apellido y destino solo pueden contener letras")
                        if not destino: 
                            raise ValueError("El destino no puede estar vacio")
                        if len(str(destino)) != 3:
                            raise ValueError("El codigo IATA de la ciudad debe contener 3 letras.")
                        if dni <= 0 or len(str(dni)) < 7 or len(str(dni)) > 8:
                            raise ValueError("El DNI debe ser un número válido con 7 a 8 dígitos")
                        if not dni:
                            raise ValueError("El DNI no puede estar vacio")
                        break  # Salir del bucle si todo está correcto
                    except ValueError as e:
                        print(f"Ocurrió un error: {e}")
                        print("Ingrese los datos del pasajero de manera correcta.")
                    # Llamar a `base_datos()` con listas en lugar de valores individuales
                    base_datos(db,[nombre],[apellido],[dni],[destino])
            #2. Agregar ciudades a la lista de ciudades.
            elif option == 2:
                while True: 
                    try:
                        pais=input("Ingrese el pais: ").title()
                        ciudad=input("Ingrese la ciudad en codigo IATA: ").upper().strip()
                        if not ciudad.isalpha() or not pais.isalpha():
                            raise ValueError("El pais y la ciudad deben contener letras")
                        if len(str(ciudad)) == 3:
                            raise ValueError("El codigo IATA de la ciudad debe contener 3 letras.")
                        break
                    except ValueError as e:
                        print(f"Ocurrió un error: {e}")
                        print("Ingrese los datos del pasajero de manera correcta.")
                    rutas(destinos,pais,ciudad)
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
                    busqueda_dni(db, pasajero)
            #4. Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
            elif option == 4:
                while True:
                    try: 
                        ciudad=input("Ingrese la ciudad: ").upper().strip()
                        if not ciudad: 
                            raise ValueError("La ciudad no puede estar vacía")
                        if not ciudad.isalpha():
                            raise ValueError("La ciudad deben contener letras")
                        if len(str(ciudad)) == 3:
                            raise ValueError("La ciudad en código IATA debe contener 3 letras")
                        break
                    except ValueError as e:
                        print(f"Ocurrió un error: {e}")
                        print("Ingrese los datos de la ciudad de manera correcta.")
                flujo_destino_ciudad(db,ciudad)
                print(f"La cantidad de pasajeros que viajan a esa ciudad es de {contador_ciudad}")
            #5. Dado un país, mostrar cuántos pasajeros viajan a ese país.
            elif option == 5:
                while True: 
                    try: 
                        pais=input("Ingrese el país: ").tittle().strip()
                        if not pais:
                            raise ValueError("El país no puede estar vacío")
                        if not pais.isalpha():
                            raise ValueError("El páis debe contener letras.")
                        break
                    except ValueError as e: 
                        print(f"Ocurrió un error: {e}")
                        print("Ingrese el país de manera correcta.")
                flujo_destino_pais(db,pais,destinos)
                print(f"La cantidad de pasajeros que viajan a esa país es de {contador_pais}")
            elif option == 6:
                print("Saliendo del programa...")
                exit() 

            break  # Salir del bucle si todo está correcto
        
        except ValueError as e:
            print(f"Ocurrió un error: {e}")
            print("Por favor, ingrese un número válido entre 1 y 6.")                 

if __name__ == "__main__":
    menu()
#    with patch("builtins.input", side_effect=["3", "19823451", "6"]):  # Buscar un pasajero y salir
#        assert menu() is None
#
#    with patch("builtins.input", side_effect=["4", "MAD", "6"]):  # Buscar pasajeros a MAD y salir
#        assert menu() is None
#
#    with patch("builtins.input", side_effect=["5", "España", "6"]):  # Buscar pasajeros a España y salir
#        assert menu() is None
#
#    with patch("builtins.input", side_effect=["1", "Guillermo", "Vidal", "15459799", "SCL", "6"]):  # Agregar pasajero y salir
#        assert menu() is None
#
#    with patch("builtins.input", side_effect=["2", "Chile", "SCL", "6"]):  # Agregar una ciudad y salir
#        assert menu() is None
#
#    with patch("builtins.input", side_effect=["7", "6"]):  # Intentar opción inválida, luego salir
#        assert menu() is None
#    print("Todas las pruebas han pasado correctamente ✅")
