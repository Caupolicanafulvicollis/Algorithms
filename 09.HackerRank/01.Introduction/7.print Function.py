def secuence(n):
    if 1<=n<=150:
        for i in range(1,n+1):
            print(i, end="")
if __name__ == '__main__':
    n = int(input())
    secuence(n)