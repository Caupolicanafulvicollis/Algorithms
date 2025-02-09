tupla = ()
personas=[]

def ingreso_datos():
    pass

def menu():
    try: 
        nombre=input("Ingrese el nombre del pasajero: ")
        dni=int(input("Ingrese el DNI del pasajero: "))
        destino=input("Ingrese ciudad de destino en codigo IATA: ").upper()
    except Exception as e:
        print(f"Ocurrio un error: ¨{e}") #Manejo del error
        print("Ingrese los datos dell pasajero de manera correcta.")
        



if __name__ == "__main__":
    pass
