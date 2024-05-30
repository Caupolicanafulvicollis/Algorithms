def es_bisiesto(anio):
    leap = False
    if year % 4 == 0:
        leap = True
        print("Es año bisiesto")
    elif year % 100 == 0:
        leap = False
        print("No es año bisiesto")
    elif year % 100 == 0 and year % 400 == 0:
        leap = True
        print("Es año bisiesto")  

year = int(input("ingresa el anio: "))
es_bisiesto(year)
