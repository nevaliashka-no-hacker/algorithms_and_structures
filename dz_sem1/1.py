'''
Используем монотонный стек, т.к. ищем ближайший меньший элемент правее оптимальным способом.
Решаем задачу через значения, слева направо.
'''

def next_smaller_element(old: list([int])) -> list([int]):
    stack = []
    n = len(old)
    result = [-1] * n

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] >= old[i]:
            stack.pop()

        if stack:
           result[i] = stack[-1]

        stack.append(old[i])

    return result

def test():
    a = [4, 5, 2, 10, 8]
    print(f"Массив:       {a}")
    print(f"Next smaller: {next_smaller_element(a)}")

def main():
    test()

if __name__ == "__main__":
    main()
