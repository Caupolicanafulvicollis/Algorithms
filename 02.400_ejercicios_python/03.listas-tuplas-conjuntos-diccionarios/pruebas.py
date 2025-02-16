def buscar_pasajeros(lista_pasajeros,nombre):
    for pasajero in lista_pasajeros:
        if pasajero[0]==nombre:
            return pasajero[1],pasajero[2]
    return None, None

pasajeros=[
    ("Manuel Juarez", 19823451,"Liverpool"), 
    ("Silvana Paredes", 22709128, "Buenos Aires"), 
    ("Rosa Ortiz", 15123978,"Glasgow"), 
    ("Luciana Hernandez", 38981374, "Lisboa")
    ] 

paises=[
    ("Buenos Aires","Argentina"), 
    ("Glasgow","Escocia"), 
    ("Lisboa", "Portugal"), 
    ("Liverpool","Inglaterra"),
    ("Madrid","España")
    ]

nombre_buscado="Rosa Ortiz"
rut,destino=buscar_pasajeros(pasajeros,nombre_buscado)

if rut and destino:
    print(f"El RUT de {nombre_buscado} es {rut} y su desitno es {destino}.")
else:
    print(f"No se encontro al pasajero {nombre_buscado}")