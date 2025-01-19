def mcd_euclides():
    a=150//39
    b=150%39
    # 150 = 39*3 + 33
    # 39 = 33*1 + 6
    # 33 = 6*5 + 3 el mcd es el 3
    # 6 = 3*2 + 0

    return 0 

if __name__ == "__main__":
    num1=int(input("Introduce el primer numero: "))
    num2=int(input("Introduce el segundo numero: "))
    if num1>num2:
        mcd_euclides(num1,num2)
    else:
        mcd_euclides(num2,num1)
    
    print(a)
    print(b)