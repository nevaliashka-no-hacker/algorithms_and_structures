'''
Вход:  "abbaca"
Выход: "ca"
Пояснение: "abbaca" → "aaca" → "ca"
'''

def pop_duplicate(old_str: str) -> str:
    n = len(old_str)
    new_str = str()
    stack = []

    for i in range(n):
        if stack and old_str[i] == old_str[stack[-1]]:
            stack.pop()
            continue

        stack.append(i)

    while stack:
        new_str = str(old_str[stack[-1]]) + new_str
        stack.pop()
    return new_str

def main():
    s = "abbaca"
    result = pop_duplicate(s)
    print(result)

if __name__ == '__main__':
    main()
