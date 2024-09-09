def triangle_quest(n):
    for i in range(1,n):
        print(i * ((10 ** i - 1) // 9))  # Fórmula para generar el número piramidal

if __name__ == "__main__":
    n = int(input())
    triangle_quest(n)