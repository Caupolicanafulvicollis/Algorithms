def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    n = len(arr)
    i = 1

    while i < n and arr[i] <= target:
        i *= 2

    return binary_search(arr, target, i // 2, min(i, n - 1))

def binary_search(arr, target, left, right):
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
    target = 21
    result = exponential_search(arr, target)

    if result != -1:
        print(f'Valor encontrado en la posición {result}')
    else:
        print('Valor no encontrado')
