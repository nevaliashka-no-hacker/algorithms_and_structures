'''
Написать функцию для проверки корректности скобок с использованием очереди
'''

from collections import deque

def is_valid(parentheses: str()) -> bool:
    matching = {')': '(', ']': '[', '}': '{'}
    queue = deque()
    for ch in parentheses:
        if ch in '{[(':
            queue.append(ch)
        else:
            if not queue or queue[0] != matching[ch]:
                return False
            queue.popleft()
    return len(queue) == 0

def main():
    tests = ["([]){}", "([)]", "((()))", ")(", ""]
    for t in tests:
        print(f"{t!r:>12} -> {is_valid(t)}")

if __name__ == "__main__":
    main()
