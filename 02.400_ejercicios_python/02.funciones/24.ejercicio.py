d=0
m=0
a=0
total=0
bisiesto=False
mes_bisiesto={
        1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31
    }
mes_no_bisiesto={
        1:31,
        2:29,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31
    }

def menu():
    print("Detector de dia juliano \n introduzca la fecha \n")
    leer_fecha()
    mes()
    es_bisiesto()
    calcular_juliano()
    #total de dias
    print(f"El dia juliano para la fecha {d}-{m}-{a} es {total}")

def leer_fecha(d,m,a):
    while True:
        try: 
            d=int(input("introduzca el día: "))
            m=int(input("introduzca el mes (numero): "))
            a=int(input("introduzca el año: "))
            if not (1<=d<=31):
                print("debe ingresar un dia entre el 1 al 31: ")
                d=int(input("introduzca el día: "))
            elif not (1>=m>=12):
                print("debe ingresar un mes entre el 1 al 12: ")
                m=int(input("introduzca el mes: "))
            elif a <= 0:
                print("debe ser un numero entero positivo: ")
                a=int(input("introduzca el año: "))
            else:
                return d,m,a
            dia_del_mes(m)
            es_bisiesto(a)

        except ValueError:
            raise ValueError("Debe cumplir con lo solicitado")

def es_bisiesto(a):
    if a % 4 != 0:  # No es divisible entre 4
        print(f"El año {a} no es bisiesto")
        return False
    elif a % 100 != 0:  # Divisible entre 4 pero no entre 100
        print(f"El año {a} es bisiesto")
        return True
    elif a % 400 != 0:  # Divisible entre 100 pero no entre 400
        print(f"El año {a} no es bisiesto")
        return False
    else:  # Divisible entre 400
        print(f"El año {a} es bisiesto")
        return True
bisiesto=es_bisiesto(a)


def mes(mes_bisiesto,mes_no_bisiesto,a):
    suma=0
    if bisiesto==True:
        for clave,valor in mes_bisiesto.items():
            if clave==m:
                suma+=valor
                return suma
    
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

        
        
def calcular_juliano(a,m,d,bisiesto,total):

# 365
# 366
    pass

if __name__ == "__main__":
    menu()
        
        
