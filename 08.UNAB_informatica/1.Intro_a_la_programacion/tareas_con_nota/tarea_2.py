import os

# 1. Capturar las estaturas, pesos, y otros datos de las personas.
def capture_data():
    people = []
    while True:
        try:
            name = input('Ingrese el nombre de la persona: ')
            age = int(input(f'Ingrese la edad de {name}: '))
            if not (1 <= age <= 100):
                raise ValueError('Edad debe estar entre 1 y 100.')
            
            weight = float(input(f'Ingrese el peso de {name} en kg: '))
            if not (0 <= weight <= 300):
                raise ValueError('Peso debe estar entre 0 y 300 kg.')
            
            height = float(input(f'Ingrese la estatura de {name} en metros: '))
            if not (0.5 <= height <= 2.5):
                raise ValueError('Altura debe estar entre 0.5 y 2.5 metros.')

            sex = input(f'Ingrese el sexo de {name} (M/F): ').upper()
            if sex not in ('M', 'F'):
                raise ValueError('Sexo debe ser M o F.')

            imc = round(weight / (height ** 2), 2)
            
            person = {
                'name': name,
                'age': age,
                'weight': weight,
                'height': height,
                'sex': sex,
                'imc': imc
            }
            people.append(person)

            if len(people) >= 5:  # Se detiene después de capturar 5 personas
                break

        except ValueError as e:
            print(f'Error: {e}. Por favor, ingrese los datos nuevamente.')
    
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
            file.write(f"Nombre: {person['name']}\n")
            file.write(f"Edad: {person['age']}\n")
            file.write(f"Peso: {person['weight']} kg\n")
            file.write(f"Estatura: {person['height']} m\n")
            file.write(f"Sexo: {person['sex']}\n")
            file.write(f"IMC: {person['imc']}\n")
            file.write("-" * 30 + "\n")
    print(f"Los datos han sido guardados en el archivo {filename}")

# Menú principal
def menu():
    people = []
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
6. Salir del programa.
''')
        try:
            option = int(input('Ingrese el número de su opción: '))
            if option == 1:
                people = capture_data()
            elif option == 2 and people:
                show_overweight_people(people)
            elif option == 3 and people:
                show_max_min_imc(people)
            elif option == 4 and people:
                show_weight_categories(people)
            elif option == 5 and people:
                save_data_to_file(people)
            elif option == 6:
                print('Saliendo del programa.')
                break
            else:
                print('Opción inválida o no se han capturado datos aún. Intente nuevamente.')
        except ValueError:
            print('Por favor, ingrese un número entero para la opción.')

if __name__ == "__main__":
    menu()
