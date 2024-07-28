income=int(input('Indique su ingreso en pesos: '))
children=int(input('Indique el numero de hijos: '))
ranking=int(input('Indique los anhos de pertenencia al banco: '))
maritial_status=str(input('Indique su estado civil (S:soltero, C: casado): ')).upper()
live=str(input('Indique su zona de residencia (R:rural, U:urbano): ')).upper()

#El banco usara las siguientes reglas: solo una de ellas se aprobara el credito
#Si el cliente ha pertenecido por más de 10 años al banco y tiene dos o más hijos.
if ranking>10 and children>=2:
    print('CREDITO APROBADO')
#Si el cliente es casado y tiene más de tres hijos.
elif maritial_status=='C' and children > 3:
    print('CREDITO APROBADO')
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
elif income==2500000 and maritial_status=='S' and live=='U':
    print('CREDITO APROBADO')
#Si el cliente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años.
elif income > 3500000 and ranking > 5:
    print('CREDITO APROBADO')
elif live == 'R' and maritial_status == 'C' and children < 2:
    print('CREDITO APROBADO')
else:
    print('CREDITO RECHAZADO')