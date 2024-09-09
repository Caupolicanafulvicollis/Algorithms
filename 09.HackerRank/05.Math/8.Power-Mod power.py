import math
def power(a,b,m):
    if 1<=a<=10 and 1<=b<=10 and 2<=m<=1000:
        c=a**b
        d=pow(a,b,m)
        print(c)
        print(d)
if __name__ == '__main__':
    a=int(input())
    b=int(input())
    m=int(input())
    power(a,b,m)