
#Implementar una función para calcular la potencia dado dos números enteros, el primero representa la base y segundo el exponente.
def powers(a,b):
    if a==0 and b==0:
        return ("es cero elevado a cero, el valor es indeterminado o tiene un valor de uno. depende desde donde se vea, si es desde el Cálculo es cero.")
    elif a==0:
        return 0
    elif b==0:
        return 1
    else:
        return a*powers(a,b-1)

if __name__ == "__main__": 
    base=int(input("ingrese la base de la potencia: "))
    exponent=int(input("ingrese el exponente de la potencia: "))
    print(powers(base,exponent))