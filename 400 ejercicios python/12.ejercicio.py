"""Hacer un programa que muestre el siguiente dibujo
*
* *
* * *
* * * *
* * * * *"""

def main():
    largo=1
    alto=5
    
    for largo in range(largo,alto+1):
        print("*"*largo, end="")
        largo+1
        print()
        
if __name__=="__main__":
    main()