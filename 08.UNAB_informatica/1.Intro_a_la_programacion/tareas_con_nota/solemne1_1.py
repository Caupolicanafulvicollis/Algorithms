while True:
    try:
        income=int(input('Indique su ingreso en pesos: '))
        if income > 0:
            print('Ingreso aceptado')
            break    
        else:
            print('Por favor ingrese un numero entero para su ingreso')
    except ValueError:
        print('Por favor ingrese un numero entero para su ingreso')
while True:
    try:
        children=int(input('Indique el numero de hijos: '))
        if children >= 0:
            print('Numero de hijos aceptado')
            break
        else:
            print('Por favor ingrese un numero entero para el numero de hijos')
    except ValueError:
        print('Por favor ingrese un numero entero para el numero de hijos')
while True:
    try:
        ranking=int(input('Indique los años de pertenencia al banco: '))
        if ranking >= 0:
            print('Ranking de pertenencia aceptado')
            break
        else:
            print('Por favor ingrese un numero entero para los años de pertenencia al banco')
    except ValueError:
        print('Por favor ingrese un numero entero para los años de pertenencia al banco')
while True:
    maritial_status=str(input('Indique su estado civil (S:soltero, C: casado): ')).upper()
    if maritial_status in ['S', 'C']:
        print('Estado civil aceptado')
        break
    else:
        print('Opcion invalida. Por favor ingrese su estado civil valido (S:soltero, C: casado)')
while True:
    live=str(input('Indique su zona de residencia (R:rural, U:urbano): ')).upper()
    if live in ['R', 'U']:
        print('Zona de residencia aceptada')
        break
    else:
        print('Por favor ingrese una zona de residencia valida (R:rural, U:urbano)')
#El banco usara las siguientes reglas: solo una de ellas se aprobara el credito
#Si el cliente ha pertenecido por más de 10 años al banco y tiene dos o más hijos.
if ranking>10 and children>=2:
    print('CREDITO APROBADO')
#Si el cliente es casado y tiene más de tres hijos.
elif maritial_status=='C' and children > 3:
    print('CREDITO APROBADO')
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
elif income>2500000 and maritial_status=='S' and live=='U':
    print('CREDITO APROBADO')
#Si el cliente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años.
elif income > 3500000 and ranking > 5:
    print('CREDITO APROBADO')
elif live == 'R' and maritial_status == 'C' and children < 2:
    print('CREDITO APROBADO')
else:
    print('CREDITO RECHAZADO')