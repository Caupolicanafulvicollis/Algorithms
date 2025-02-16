def solicitar_numeros():
    lista = []
    while True:
        num = int(input("Ingrese un número (0 para finalizar): "))
        if num == 0:
            break
        lista.append(num)
    return lista

def eliminar_primera_ocurrencia(lista):
    num = int(input("Ingrese un número a eliminar de la lista: "))
    if num in lista:
        lista.remove(num)
    else:
        print("No es posible eliminar el número, no está en la lista.")

def sumar_elementos(lista):
    suma = sum(lista)
    print(f"La sumatoria de los elementos de la lista es: {suma}")

def filtrar_menores(lista):
    num = int(input("Ingrese un número para filtrar los menores: "))
    nueva_lista = [x for x in lista if x < num]
    print("Lista de elementos menores que el número dado:", nueva_lista)

def generar_tuplas(lista):
    frecuencias = {}
    for num in lista:
        frecuencias[num] = frecuencias.get(num, 0) + 1
    lista_tuplas = list(frecuencias.items())
    print("Lista de tuplas (número, frecuencia):", lista_tuplas)

def main():
    lista = solicitar_numeros()
    eliminar_primera_ocurrencia(lista)
    sumar_elementos(lista)
    filtrar_menores(lista)
    generar_tuplas(lista)

if __name__ == "__main__":
    main()