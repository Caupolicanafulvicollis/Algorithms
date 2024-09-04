import os

# 1. Capturar las estaturas, pesos, y otros datos de las personas.
def capture_data(num_people):
    people = load_data_from_file()  # Cargar los datos previos si existen
    for i in range(num_people):
        try:
            name = input(f'Ingrese el nombre de la persona {i + 1}: ')
            
            weight = float(input(f'Ingrese el peso de {name} en kg: '))
            if not (0 <= weight <= 300):
                raise ValueError('Peso debe estar entre 0 y 300 kg.')
            
            height = float(input(f'Ingrese la estatura de {name} en metros: '))
            if not (0.5 <= height <= 2.5):
                raise ValueError('Altura debe estar entre 0.5 y 2.5 metros.')

            imc = round(weight / (height ** 2), 2)
            
            person = {
                'name': name,
                'weight': weight,
                'height': height,
                'imc': imc
            }
            people.append(person)

        except ValueError as e:
            print(f'Error: {e}. Por favor, ingrese los datos nuevamente.')
    
    save_data_to_file(people)  # Guardar los datos al finalizar la captura
    return people

# 2. Mostrar el listado con aquellos IMC sobre el valor promedio.
def show_overweight_people(people):
    imc_values = [p['imc'] for p in people]
    mean_imc = sum(imc_values) / len(imc_values)
    print(f'Promedio del IMC: {mean_imc:.2f}')
    print('Listado de personas con IMC sobre el promedio:')
    for person in people:
        if person['imc'] > mean_imc:
            print(f"{person['name']} - IMC: {person['imc']}")

# 3. Mostrar el IMC máximo y mínimo registrado.
def show_max_min_imc(people):
    imc_values = [p['imc'] for p in people]
    max_imc = max(imc_values)
    min_imc = min(imc_values)
    print(f'Máximo IMC registrado: {max_imc}')
    print(f'Mínimo IMC registrado: {min_imc}')

# 4. Mostrar la cantidad de personas con bajo peso, peso normal, sobre peso y obesidad.
def show_weight_categories(people):
    underweight_count = sum(1 for p in people if p['imc'] < 18.5)
    normal_weight_count = sum(1 for p in people if 18.5 <= p['imc'] < 24.9)
    overweight_count = sum(1 for p in people if 25 <= p['imc'] < 29.9)
    obesity_count = sum(1 for p in people if p['imc'] >= 30)

    print(f'Cantidad de personas con bajo peso: {underweight_count}')
    print(f'Cantidad de personas con peso normal: {normal_weight_count}')
    print(f'Cantidad de personas con sobrepeso: {overweight_count}')
    print(f'Cantidad de personas con obesidad: {obesity_count}')

# 5. Guardar los registros de los pacientes en un archivo .txt.
def save_data_to_file(people, filename="registros_pacientes.txt"):
    with open(filename, 'w') as file:
        for person in people:
            file.write(f"{person['name']},{person['weight']},{person['height']}\n")
    print(f"Los datos han sido guardados en el archivo {filename}")

# 6. Cargar los datos de estaturas y pesos desde el archivo .txt.
def load_data_from_file(filename="registros_pacientes.txt"):
    people = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                name, weight, height = line.strip().split(',')
                imc = round(float(weight) / (float(height) ** 2), 2)
                people.append({
                    'name': name,
                    'weight': float(weight),
                    'height': float(height),
                    'imc': imc
                })
        print(f"Datos cargados desde {filename}")
    return people

# 7. Borrar los datos del archivo .txt.
def delete_data_file(filename="registros_pacientes.txt"):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"El archivo {filename} ha sido borrado.")
    else:
        print(f"No se encontró el archivo {filename}.")

# 8. Mostrar los datos cargados desde el archivo.
def show_loaded_data(people):
    if people:
        print("Datos cargados:")
        for person in people:
            print(f"Nombre: {person['name']}, Peso: {person['weight']} kg, Estatura: {person['height']} m, IMC: {person['imc']}")
    else:
        print("No hay datos cargados para mostrar.")

# Menú principal
def menu():
    people = load_data_from_file()  # Cargar datos respaldados al inicio
    while True:
        print('''
CONTROL DE ÍNDICES DE MASA CORPORAL
          
---------------------------------------------------------------------------------------------- 

Seleccione su opción introduciendo el número de su opción: 

1. Capturar las estaturas y los pesos de las personas.
2. Mostrar el listado con aquellos IMC sobre el valor promedio.
3. Mostrar el IMC máximo y mínimo registrado.
4. Mostrar la cantidad de personas con bajo peso, peso normal, sobre peso y obesidad.
5. Guardar los registros en un archivo.
6. Borrar los datos del archivo.
7. Mostrar los datos cargados desde el archivo.
8. Salir del programa.
''')
        try:
            option = int(input('Ingrese el número de su opción: '))
            if option == 1:
                num_people = int(input("¿Cuántas personas desea registrar? "))
                people = capture_data(num_people)
                save_data_to_file(people)  # Hacer respaldo al terminar de capturar datos
            elif option == 2 and people:
                show_overweight_people(people)
            elif option == 3 and people:
                show_max_min_imc(people)
            elif option == 4 and people:
                show_weight_categories(people)
            elif option == 5 and people:
                save_data_to_file(people)
            elif option == 6:
                delete_data_file()  # Borrar los datos del archivo
                people = []  # Vaciar la lista de personas en memoria
            elif option == 7:
                show_loaded_data(people)  # Mostrar los datos cargados desde el archivo
            elif option == 8:
                print('Saliendo del programa.')
                break
            else:
                print('Opción inválida o no se han capturado datos aún. Intente nuevamente.')
        except ValueError:
            print('Por favor, ingrese un número entero para la opción.')

if __name__ == "__main__":
    menu()