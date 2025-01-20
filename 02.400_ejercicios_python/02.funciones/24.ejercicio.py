def leer_fecha():
    pass

def dia_del_mes():
    pass

def es_bisiesto():
    pass

def calcular_juliano():
    pass

def menu():
    print("Detector de dia juliano \n introduzca la fecha \n")
    try: 
        dia=int(input("introduzca el día: "))
        mes=int(input("introduzca el mes (numero): "))
        anho=int(input("introduzca el año: "))
        if 1>=dia>=31:
            print("debe ingresar un dia entre el 1 al 31: ")
            dia=int(input("introduzca el día: "))
            
        elif 1>=mes>=12:
    except 