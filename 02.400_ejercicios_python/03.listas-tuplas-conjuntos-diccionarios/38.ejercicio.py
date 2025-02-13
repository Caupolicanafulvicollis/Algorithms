tupla = ()
personas=[]

def ingreso_datos():
    pass

def menu():
    while True: #Hasta que resulte las entradas    
        try:
        #Nombre y apellido
            nombre=input("Ingrese el nombre del pasajero: ").title()
            apellido=input("Ingrese el nombre del pasajero: ").title()
            dni=int(input("Ingrese el DNI del pasajero: ").strip())
            destino=input("Ingrese ciudad de destino en codigo IATA: ").upper().strip()
            if not nombre and apellido:
                raise ValueError("El nombre del pasajero no puede estar vacio")
            if not nombre.isalpha() and apellido.isalpha() and destino.isalpha() and isinstance(dni,int):
                raise ValueError("Solo puede contener letras")
#           if codigo not in codigos_iata_validos:
#                raise ValueError("Código IATA no reconocido. Intente nuevamente.")
            if not dni:
                raise ValueError("El DNI no puede estar vacio")
            if not destino: 
                raise ValueError("El destino no puede estar vacio")
            
        except Exception as e:
            print(f"Ocurrio un error: ¨{e}") #Manejo del error
            print("Ingrese los datos del pasajero de manera correcta.")
                        



if __name__ == "__main__":
    pass
