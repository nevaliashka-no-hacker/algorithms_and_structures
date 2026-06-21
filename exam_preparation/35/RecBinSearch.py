'''Рекурсивный бинарный поиск'''

def recursive_binary_search(arr, value, left = 0, right = None):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    middle = (left + right) // 2

    if arr[middle] == value:
        return middle
    elif value < arr[middle]:
        return recursive_binary_search(arr, value, left, middle + 1)
    elif value > arr[middle]:
        return recursive_binary_search(arr, value, middle, right)

print(recursive_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13], 11))
