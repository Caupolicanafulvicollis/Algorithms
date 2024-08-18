
#1. Capturar las estaturas y los pesos de las personas.
def data():
    #datos de los pacientes
    name=[]
    name_input=input('Ingrese el nombre de la persona: ')
    def create_data_name(name):
        name.append(name_input)
    age=[]
    def create_data_age(name):
        try:
            age_input=int(input(f'Ingrese la edad de {name_input}: '))
            if age_input==int():
                raise ValueError('Edad debe ser un número entero.')
            if not (1<=age_input<=100):
                print('Edad debe estar entre 1 y 100.')
                return create_data_age()
            age.append(age_input)
        except ValueError as e:
            print(f'Error: {e}. Por favor, ingrese los datos nuevamente.')
            return create_data_age()
    weight=[]
    def create_data_weight(name):
        try:
            weight_input=float(input(f'Ingrese el peso de {name_input} en kg: '))
            if weight_input==float() or weight_input==int():
                raise ValueError('Peso debe ser un número.')
            if not (0<=weight_input<=300):
                print('Peso debe estar entre 0 y 300 kg.')
                return create_data_weight()
            weight.append(weight_input)
        except ValueError as e:
            print(f'Error: {e}. Por favor, ingrese los datos nuevamente.')
            return create_data_age()
    height=[]
    def create_data_height(name):
        try:
            height_input=float(input(f'Ingrese la estatura de {name_input} en metros: '))
            if height_input==float() or height_input==int():
                raise ValueError('Altura debe ser un número.')
            if not (0.5<=height_input<=2.5):
                print('Altura debe estar entre 0.5 y 2.5 metros.')
                return create_data_height()
            height.append(height_input)
        except ValueError as e:
            print(f'Error: {e}. Por favor, ingrese los datos nuevamente.')
            return create_data_height()
    sex=[]
    def create_data_sex():
        sex_input=input(f'Ingrese el sexo de {name_input} (M/F): ')
        sex.append(sex_input)
        if not sex_input=='M' or 'F':
            print('Sexo debe ser M o F.')
            return create_data_sex()
    imc=[]
                
    age.append(age_input)
    def create_data_height():
    def create_data_weight(name,weight,height,age,sex):
    def create_data_sex():
                sex.append(input(f'Ingrese el sexo de {name_input} (M/F): '))
                weight.append(float(input(f'Ingrese el peso de {name_input} en kg: ')))
                height.append(float(input(f'Ingrese la estatura de {name_input} en metros: ')))

                if len(name) == 5:
                     break
            except ValueError as e:
                

    return 

#2. Mostrar el listado con aquellos IMC sobre el valor promedio.
def show_overweight_people():
    #codigo 
    print(f'Promedio del IMC: {mean_IMC}')
    print('Listado de IMC sobre el promedio') 

#3. Mostrar el IMC máximo y mínimo registrado.
def show_max_min_imc():
    #codigo 
    print(f'Maximo IMC registrado: {max_IMC}')
    print(f'Minimo IMC registrado: {min_IMC}')
    return
#4. Mostrar la cantidad de personas con bajo peso, peso normal, sobre peso y obesidad.
def show_weight_categories():
    #codigo 
    print(f'Cantidad de personas con bajo peso: {underweight_count}')
    print(f'Cantidad de personas con peso normal: {normal_weight_count}')
    print(f'Cantidad de personas con sobre peso: {overweight_count}')
    print(f'Cantidad de personas con obesidad: {obesity_count}')
    return


def menu(option):
    options=[1,2,3,4,5]
    try:
        option = int(option)    
        if option in options: #si option es igual a algun elemento de la lista options se cumple con esta condicion
            if option == 1:
                data()
            elif option == 2:
                show_overweight_people()
            elif option == 3:
                show_max_min_imc()
            elif option == 4:
                show_weight_categories()
            elif option == 5:
                print('Saliendo del programa.')
                exit()
            else:
                print('Opcion invalida. Intente nuevamente.')
                menu(input('Ingrese el numero de su opcion: '))
        else:
            print('Opcion invalida. Intente nuevamente.')
            menu(input('Ingrese el numero de su opcion: '))
    except ValueError:
        print('Por favor ingrese un numero entero para la opcion')
        menu(input('Ingrese el numero de su opcion: '))

if __name__ == "__main__":
    # Create a new directory named "my_directory"
    print('''
CONTROL DE INDICES DE MASA CORPORAL
          
---------------------------------------------------------------------------------------------- 

Seleccione su opcion introduciendo el numero de su opcion: 

1. Capturar las estaturas y los pesos de las personas.
2. Mostrar el listado con aquellos IMC sobre el valor promedio.
3. Mostrar el IMC máximo y mínimo registrado.
4. Mostrar la cantidad de personas con bajo peso, peso normal, sobre peso y obesidad.
5. Salir del programa.
''')
menu(input('Ingrese el numero de su opcion: '))