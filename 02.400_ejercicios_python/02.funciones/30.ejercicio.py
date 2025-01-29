def validar_vocal(mensaje):
    while True:
        try:
            letra=input(mensaje).strip() #elimina espacios en blanco
            if len(letra)==1 and letra.isalpha(): #verifica que sea una sola letra
                return letra
        except ValueError:
            print("Ingrese una letra válida")

def es_vocal(letra):
    return letra.lower() in "aeiou"

if __name__ == "__main__":
    letra=validar_vocal("Ingrese una letra: ")
    if es_vocal(letra):
        print("La letra es vocal")
    else:
        print("La letra no es vocal")