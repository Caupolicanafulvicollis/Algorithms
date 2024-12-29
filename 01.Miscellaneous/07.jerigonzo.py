#despues de cada vocal, se agrega una p y se repite la vocal

def jerigonzo(string):
    vocales = 'aeiouAEIOU'
    list_string = []
    for i in string:
        if i in vocales:
            list_string.append(i + 'p' + i)
        else:
            list_string.append(i)
    return ''.join(list_string) #combina todos los indices de la lisssta y hace la frase

if __name__ == '__main__':
    print("Jerigonzo")
    while True:
        string = input("Su mensaje en jerigonzo: ")
        print(jerigonzo(string))
        op = input("Ejecutar otra vez? S/N: ").upper()
        if op != 'S':
            break