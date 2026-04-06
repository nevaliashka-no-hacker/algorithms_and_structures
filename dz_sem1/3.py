'''
Эту задачу решаем с использованием стека, только в данном случае массив
pushed выступает стеком. Сохранено по значениям.
'''

def valid(pushed, popped) -> bool:
    if not pushed or not popped or len(pushed) != len(popped):
        return False

    n = len(pushed)
    new = [0] * n

    for i in range(n):
        new[i] = pushed.pop()

    if new == popped:
        return True
    return False
    

def test1():
    pushed = [1, 2, 3, 4, 5]
    popped = [5, 4, 3, 2, 1]
    print(valid(pushed, popped))

def test2():
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]
    print(valid(pushed, popped))

def test3():
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]
    print(valid(pushed, popped))

def main():
    test1()
    test2()
    test3()

if __name__ == "__main__":
    main()
