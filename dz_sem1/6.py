'''
Задача 6. Sum of Subarray Minimums

Дан массив `arr`. Для каждого подмассива найти минимум.
Вернуть **сумму всех этих минимумов**.

Вход:  [3, 1, 2, 4]
Подмассивы: [3],[1],[2],[4],[3,1],[1,2],[2,4],[3,1,2],[1,2,4],[3,1,2,4]
Минимумы:    3   1   2   4    1     1     2      1       1        1
Сумма: 3+1+2+4+1+1+2+1+1+1
Выход: 17
'''

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def delete(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self) == 0

    def min(self):
        temp = self.stack.copy()
        min_num = stack[-1]
        while temp:
            if min_num < temp[-1]:
                min_num = temp[-1]
            temp.pop()
        return min_num

    def clean(self):
        while self.stack:
            self.stack.pop()

def sum_min(arr):
    result = 0
    for k in range(1, len(arr) + 1):
        
            

def main():
    arr = [3, 1, 2, 4]
    print(sum_min(arr))

if __name__ == "__main__":
    main()
