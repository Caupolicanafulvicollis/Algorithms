def div1(a,b):
    try:
        return print(a//b)
    except ZeroDivisionError:
        return 'Error: Division by zero'
def div2(a,b):
    try:
        return print(a/b)
    except ZeroDivisionError:
        return 'Error: Division by zero'

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    div1(a, b)
    div2(a, b)