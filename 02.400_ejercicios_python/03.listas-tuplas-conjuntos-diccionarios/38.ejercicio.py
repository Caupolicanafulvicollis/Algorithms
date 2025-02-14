tupla = ()
personas=[]

def ingreso_datos():
    pass

def menu():
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
#           if codigo not in codigos_iata_validos:
#                raise ValueError("Código IATA no reconocido. Intente nuevamente.")
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
        
                        



if __name__ == "__main__":
    pass
