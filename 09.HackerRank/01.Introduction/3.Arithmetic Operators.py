def sum(a,b):
    return a + b
def rest(a,b):
    return a - b
def product(a,b):
    return a * b

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(sum(a, b))
    print(rest(a, b))
    print(product(a, b))