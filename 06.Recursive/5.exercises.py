#Desarrollar una función que permita convertir un número romano en un número decimal.

def roman_to_decimal(roman_number):
    roman_number = roman_number.upper()
    decimal_number = 0
    for i in range(len(roman_number)):
        if roman_number[i] == 'I':
            decimal_number += 1
            if i < len(roman_number) - 1 and roman_number[i + 1] == 'V':
                decimal_number -= 2
                i += 1
                continue
            if i < len(roman_number) - 1 and roman_number[i + 1] == 'X':
                decimal_number -= 20
                i += 1
                continue
            if i < len(roman_number) - 1 and roman_number[i + 1] == 'L':
                decimal_number -= 50
                i += 1
                continue
            if i < len(roman_number) - 1 and roman_number[i + 1] == 'C':
                decimal_number -= 100
                i += 1
                continue
            if i < len(roman_number) - 1 and roman_number[i + 1] == 'D':
                decimal_number -= 500
                i += 1
                continue
            if i < len(roman_number) - 1 and roman_number[i + 1] == 'M':
                decimal_number -= 1000
                i += 1
                continue

if __name__ == '__main__':
    #roman_number = input('Ingrese un número romano: ')
    #print(roman_to_decimal(roman_number))
    assert roman_to_decimal("XV")==15
