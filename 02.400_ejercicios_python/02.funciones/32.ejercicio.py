def validra_list(mensaje):
    if all(isinstance(mensaje,(int,float)) for elemento in mensaje)

def sum(lista):
    suma=0 
    for i in range(lista):
        suma+=i
        return suma
    
def multip(lista):
    multiplicacion=1
    for i in range(lista):
        multiplicacion*=i

if __name__ == "__main__":
    assert 