if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lista=sorted(set(arr),reverse=True)
    value=lista[1]
    print(value)