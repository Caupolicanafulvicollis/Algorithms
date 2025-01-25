def menu():
    print("Detector de dia juliano \n introduzca la fecha \n")
    leer_fecha()
    dia_del_mes()
    es_bisiesto()
    calcular_juliano()
    #total de dias
    print(f"El dia juliano para la fecha {dia}-{mes}-{anho} es {total}")


dia=0
mes=0
anho=0
total=0

def leer_fecha(dia,mes,anho):
    try: 
        d=int(input("introduzca el día: "))
        m=int(input("introduzca el mes (numero): "))
        a=int(input("introduzca el año: "))
        if 1>=dia>=31:
            print("debe ingresar un dia entre el 1 al 31: ")
            d=int(input("introduzca el día: "))
        elif 1>=m>=12:
            print("debe ingresar un dia entre el 1 al 12: ")
            m=int(input("introduzca el día: "))
        elif a>0:
            print("debe ser un numero entero positivo: ")
            a=int(input("introduzca el año: "))
    except ValueError:
        menu()
        raise ValueError("Debe cumplir con lo solicitado")  
    return dia_del_mes(d,m,a)



def dia_del_mes():
# Enero: 31 días
# Febrero: 28 o 29 días (si es año bisiesto)
# Marzo: 31 días
# Abril: 30 días
# Mayo: 31 días 
# Junio: 30 días 
# Julio: 31 días
# Agosto: 31 días
# Septiembre: 30 días
# Octubre: 31 días
# Noviembre: 30 días
# Diciembre: 31 días

    pass

def es_bisiesto(anho,total):
#Matemáticamente podemos saber si un año es bisiesto si este es múltiplo de 4. 
# Si además es múltiplo de 100 no será bisiesto 
# (ten en cuenta que 100 es múltiplo de 4 y 
# por tanto cualquier número que sea múltiplo de 100 también es múltiplo de 4) 
# a no ser que sea múltiplo de 400, que sí será bisiesto.
    if anho%4 != 0: #No es divisible entre 4
        print("No es bisiesto")
    elif anho%4==0 and anho%100 != 0: #divisible entre 4 y no entre 100 o 400
            print("Es bisiesto")
            total+=1
    elif anho % 4 == 0 and anho % 100 == 0 and anho % 400 != 0: #divisible entre 4 y 10 y no entre 400
	    print("No es bisiesto")
    elif anho % 4 == 0 and anho % 100 == 0 and anho % 400 == 0: #divisible entre 4, 100 y 400
	    print("Es bisiesto")
        
def calcular_juliano(anho,mes,anho,bisiesto,total):
    if bisiesto

# 365
# 366
    pass

if __name__ == "__main__":
    menu()
        
        
