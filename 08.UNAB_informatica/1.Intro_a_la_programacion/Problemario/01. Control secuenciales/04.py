a=float(input("ingrese el valor de a: "))
b=float(input("ingrese el valor de b: "))
c=float(input("ingrese el valor de c: "))
d=float(input("ingrese el valor de d: "))
e=float(input("ingrese el valor de e: "))
f=float(input("ingrese el valor de f: "))
x=round((c*e-b*f)/(a*e-b*d),1)
y=round((a*f-c*d)/(a*e-b*d),1)
print(f"el valor de x es {x}")
print(f"el valor de y es {y}")