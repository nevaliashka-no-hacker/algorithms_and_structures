# Лабораторная работа 2: Связные списки

## Базовая реализация связного списка

### Базовый класс узла

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### Вспомогательные функции (можно использовать в решениях)

```python
def build_list(values):
    """Создать список из массива: build_list([1,2,3]) → 1→2→3→None"""
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def print_list(head):
    """Напечатать список"""
    parts = []
    while head:
        parts.append(str(head.val))
        head = head.next
    print(" → ".join(parts) + " → None")

def list_to_array(head):
    """Список → массив (для проверки)"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
```

## Задачи для самостоятельной работы

Каждый вариант содержит **5 задач** (по одной из типов A–E). Таблица вариантов представлена после задач.

### Задачи типа A — Базовые операции


#### A1. Вставка в отсортированный список

> Дан отсортированный по возрастанию список. Вставить новое значение `val` так, чтобы список остался отсортированным.

**Пример:**
```
Вход:  1 → 3 → 5 → 7 → None,  val = 4
Выход: 1 → 3 → 4 → 5 → 7 → None
```

```python
def insert_sorted(head, val):
    pass


# Тест
head = build_list([1, 3, 5, 7])
head = insert_sorted(head, 4)
print_list(head)  # 1 → 3 → 4 → 5 → 7 → None

head = insert_sorted(None, 10)
print_list(head)  # 10 → None

head = build_list([5, 10])
head = insert_sorted(head, 1)
print_list(head)  # 1 → 5 → 10 → None
```


#### A2. Удаление всех узлов с заданным значением

> Удалить **все** узлы, значение которых равно `val`.

**Пример:**
```
Вход:  1 → 2 → 6 → 3 → 6 → None,  val = 6
Выход: 1 → 2 → 3 → None
```

```python
def remove_all(head, val):
    pass


# Тест
head = build_list([1, 2, 6, 3, 6])
head = remove_all(head, 6)
print_list(head)  # 1 → 2 → 3 → None

head = build_list([7, 7, 7])
head = remove_all(head, 7)
print_list(head)  # None
```


#### A3. Вставка после k-го элемента

> Вставить значение `val` после k-го элемента (нумерация с 1). Если k больше длины — вставить в конец.

**Пример:**
```
Вход:  10 → 20 → 30 → None,  k=2,  val=25
Выход: 10 → 20 → 25 → 30 → None
```

```python
def insert_after_k(head, k, val):
    pass


# Тест
head = build_list([10, 20, 30])
head = insert_after_k(head, 2, 25)
print_list(head)  # 10 → 20 → 25 → 30 → None

head = build_list([10, 20])
head = insert_after_k(head, 5, 99)
print_list(head)  # 10 → 20 → 99 → None
```


#### A4. Удаление каждого второго элемента

> Удалить каждый второй элемент списка (2-й, 4-й, 6-й …).

**Пример:**
```
Вход:  1 → 2 → 3 → 4 → 5 → None
Выход: 1 → 3 → 5 → None
```

```python
def remove_every_second(head):
    pass


# Тест
head = build_list([1, 2, 3, 4, 5])
head = remove_every_second(head)
print_list(head)  # 1 → 3 → 5 → None

head = build_list([1, 2, 3, 4, 5, 6])
head = remove_every_second(head)
print_list(head)  # 1 → 3 → 5 → None
```


#### A5. Перенос последнего элемента в начало

> Переместить последний элемент списка в начало.

**Пример:**
```
Вход:  1 → 2 → 3 → 4 → None
Выход: 4 → 1 → 2 → 3 → None
```

```python
def move_last_to_front(head):
    pass


# Тест
head = build_list([1, 2, 3, 4])
head = move_last_to_front(head)
print_list(head)  # 4 → 1 → 2 → 3 → None
```


#### A6. Перенос первого элемента в конец

> Переместить первый элемент списка в конец.

**Пример:**
```
Вход:  1 → 2 → 3 → 4 → None
Выход: 2 → 3 → 4 → 1 → None
```

```python
def move_first_to_end(head):
    pass


# Тест
head = build_list([1, 2, 3, 4])
head = move_first_to_end(head)
print_list(head)  # 2 → 3 → 4 → 1 → None
```


### Задачи типа B — Поиск и анализ


#### B1. Максимальный элемент и его позиция

> Найти максимальный элемент и его индекс (с 0). Вернуть кортеж `(значение, индекс)`.

**Пример:**
```
Вход:  3 → 7 → 2 → 9 → 1 → None
Выход: (9, 3)
```

```python
def find_max(head):
    pass


# Тест
head = build_list([3, 7, 2, 9, 1])
print(find_max(head))  # (9, 3)
```


#### B2. Является ли список палиндромом

> Проверить, является ли список палиндромом. **O(n) время, O(1) дополнительная память.**

**Пример:**
```
Вход:  1 → 2 → 3 → 2 → 1 → None     →  True
Вход:  1 → 2 → 3 → None             →  False
```

```python
def is_palindrome(head) -> bool:
    pass


# Тест
print(is_palindrome(build_list([1, 2, 3, 2, 1])))    # True
print(is_palindrome(build_list([1, 2, 3])))          # False
print(is_palindrome(build_list([1, 1])))             # True
```


#### B3. Найти предпоследний элемент

> Вернуть значение предпоследнего элемента. Если элементов < 2 — вернуть `None`.

**Пример:**
```
Вход:  5 → 10 → 15 → 20 → None
Выход: 15
```

```python
def second_to_last(head):
    pass


# Тест
print(second_to_last(build_list([5, 10, 15, 20])))  # 15
print(second_to_last(build_list([42])))             # None
```


#### B4. Количество элементов больше среднего арифметического

> Подсчитать, сколько элементов списка строго больше среднего арифметического всех элементов.

**Пример:**
```
Вход:  1 → 2 → 3 → 4 → 10 → None
Среднее = 4.0
Больше среднего: только 10
Выход: 1
```

```python
def count_above_average(head) -> int:
    pass


# Тест
head = build_list([1, 2, 3, 4, 10])
print(count_above_average(head))  # 1
```


#### B5. Второй по величине элемент

> Найти второй по величине элемент (второй максимум). Дубликаты считаются одним значением.

**Пример:**
```
Вход:  5 → 3 → 9 → 9 → 1 → 7 → None
Выход: 7
```

```python
def second_max(head) -> int | None:
    pass


# Тест
print(second_max(build_list([5, 3, 9, 9, 1, 7])))   # 7
print(second_max(build_list([1, 1, 1])))            # None
```


#### B6. Проверить, отсортирован ли список

> Проверить, отсортирован ли список по неубыванию.

**Пример:**
```
Вход:  1 → 3 → 5 → 5 → 8 → None    →  True
Вход:  1 → 5 → 3 → None            →  False
```

```python
def is_sorted(head) -> bool:
    pass


# Тест
print(is_sorted(build_list([1, 3, 5, 5, 8])))  # True
print(is_sorted(build_list([1, 5, 3])))        # False
print(is_sorted(build_list([])))               # True
```


### Задачи типа C — Модификация списка


#### C1. Развернуть список

> Развернуть односвязный список итеративно.

**Пример:**
```
Вход:  1 → 2 → 3 → 4 → None
Выход: 4 → 3 → 2 → 1 → None
```

```python
def reverse_list(head):
    pass


# Тест
head = build_list([1, 2, 3, 4])
head = reverse_list(head)
print_list(head)  # 4 → 3 → 2 → 1 → None
```


#### C2. Развернуть каждые k элементов

> Развернуть список группами по `k`. Если последняя группа меньше `k` — оставить как есть.

**Пример:**
```
Вход:  1 → 2 → 3 → 4 → 5 → None,  k=3
Выход: 3 → 2 → 1 → 4 → 5 → None
```

```python
def reverse_k_group(head, k):
    pass


# Тест
head = build_list([1, 2, 3, 4, 5])
head = reverse_k_group(head, 3)
print_list(head)  # 3 → 2 → 1 → 4 → 5 → None
```


#### C3. Разделить на чётные и нечётные значения

> Разделить список на два: в первом — узлы с чётными значениями, во втором — с нечётными. Вернуть оба.

**Пример:**
```
Вход:  1 → 2 → 3 → 4 → 5 → 6 → None
Чётные: 2 → 4 → 6 → None
Нечётные: 1 → 3 → 5 → None
```

```python
def split_even_odd(head):
    pass


# Тест
head = build_list([1, 2, 3, 4, 5, 6])
evens, odds = split_even_odd(head)
print_list(evens)  # 2 → 4 → 6 → None
print_list(odds)   # 1 → 3 → 5 → None
```


#### C4. Удалить n-й элемент с конца

> Удалить n-й по счёту узел с конца списка (за один проход).

**Пример:**
```
Вход:  1 → 2 → 3 → 4 → 5 → None,  n=2
Выход: 1 → 2 → 3 → 5 → None  (удалили 4)
```

```python
def remove_nth_from_end(head, n):
    pass


# Тест
head = build_list([1, 2, 3, 4, 5])
head = remove_nth_from_end(head, 2)
print_list(head)  # 1 → 2 → 3 → 5 → None
```


#### C5. Поменять местами попарно

> Поменять значения узлов попарно: (1-й и 2-й), (3-й и 4-й), и т.д.

**Пример:**
```
Вход:  1 → 2 → 3 → 4 → 5 → None
Выход: 2 → 1 → 4 → 3 → 5 → None
```

```python
def swap_pairs(head):
    pass


# Тест
head = build_list([1, 2, 3, 4, 5])
head = swap_pairs(head)
print_list(head)  # 2 → 1 → 4 → 3 → 5 → None
```


#### C6. Переместить все нули в конец

> Переместить все узлы со значением 0 в конец списка, сохранив порядок остальных.

**Пример:**
```
Вход:  0 → 1 → 0 → 3 → 0 → 5 → None
Выход: 1 → 3 → 5 → 0 → 0 → 0 → None
```

```python
def move_zeros_to_end(head):
    pass


# Тест
head = build_list([0, 1, 0, 3, 0, 5])
head = move_zeros_to_end(head)
print_list(head)  # 1 → 3 → 5 → 0 → 0 → 0 → None
```


### Задачи типа D — Алгоритмические


#### D1. Слияние двух отсортированных списков

> Слить два отсортированных списка в один отсортированный.

**Пример:**
```
l1: 1 → 3 → 5 → None
l2: 2 → 4 → 6 → None
Выход: 1 → 2 → 3 → 4 → 5 → 6 → None
```

```python
def merge_sorted(l1, l2):
    pass


# Тест
l1 = build_list([1, 3, 5])
l2 = build_list([2, 4, 6])
head = merge_sorted(l1, l2)
print_list(head)  # 1 → 2 → 3 → 4 → 5 → 6 → None
```


#### D2. Точка пересечения двух списков

> Два списка могут сливаться в один (Y-образная форма). Найти узел, где они пересекаются, или `None`.

```
A:     1 → 2 ↘
              5 → 6 → None
B: 3 → 4 → 7 ↗
Ответ: узел со значением 5
```

```python
def get_intersection(headA, headB) -> int | None:
    pass


# Тест
common = build_list([5, 6])
headA = ListNode(1, ListNode(2, common))
headB = ListNode(3, ListNode(4, ListNode(7, common)))
node = get_intersection(headA, headB)
print(node.val if node else None)  # 5
```


#### D3. Сложение двух чисел (цифры в обратном порядке)

> Два числа записаны в виде списков (цифры в обратном порядке). Вернуть их сумму в таком же формате.

**Пример:**
```
342 → список 2 → 4 → 3
465 → список 5 → 6 → 4
342 + 465 = 807 → список 7 → 0 → 8
```

```python
def add_two_numbers(l1, l2):
    pass


# Тест
l1 = build_list([2, 4, 3])  # 342
l2 = build_list([5, 6, 4])  # 465
result = add_two_numbers(l1, l2)
print_list(result)  # 7 → 0 → 8 → None (807)
```


#### D4. Обнаружение цикла и его начало

> Определить, есть ли цикл. Если да — вернуть узел, где цикл начинается.

```python
def detect_cycle(head):
    pass

# Тест
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2; n2.next = n3; n3.next = n4
n4.next = n2  # цикл: 4 → 2
print(detect_cycle(n1).val)  # 2
```


#### D5. Середина списка за один проход

> Найти средний узел. Если узлов чётное количество — вернуть второй из двух средних.

**Пример:**
```
Вход:  1 → 2 → 3 → 4 → 5 → None   →  3
Вход:  1 → 2 → 3 → 4 → None       →  3
```

```python
def find_middle(head):
    pass


# Тест
print(find_middle(build_list([1,2,3,4,5])).val)   # 3
print(find_middle(build_list([1,2,3,4])).val)     # 3
```


#### D6. Удалить дубликаты из отсортированного списка

> Удалить дубликаты, оставив по одному экземпляру каждого значения.

**Пример:**
```
Вход:  1 → 1 → 2 → 3 → 3 → 3 → 4 → None
Выход: 1 → 2 → 3 → 4 → None
```

```python
def delete_duplicates(head):
    pass


# Тест
head = build_list([1, 1, 2, 3, 3, 3, 4])
head = delete_duplicates(head)
print_list(head)  # 1 → 2 → 3 → 4 → None
```


### Задачи типа E — Прикладные


#### E1. Стек на основе связного списка

> Реализовать стек с методами `push`, `pop`, `peek`, `is_empty`.

```python
class Stack:
    def __init__(self):
        self.top_node = None
        self.size = 0

    def push(self, val):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def is_empty(self) -> bool:
        pass

    def __len__(self) -> int:
        pass


# Тест
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.peek())     # 30
print(s.pop())      # 30
print(s.pop())      # 20
print(s.is_empty()) # False
print(len(s))       # 1
```


#### E2. Очередь на основе связного списка

> Реализовать очередь с методами `enqueue`, `dequeue`, `peek`, `is_empty`.

```python
class Queue:
    def __init__(self):
        self.head = None  # откуда забираем
        self.tail = None  # куда добавляем
        self.size = 0

    def enqueue(self, val):
        pass

    def dequeue(self) -> ListNode:
        pass

    def peek(self) -> int | None:
        pass

    def is_empty(self) -> bool:
        pass


# Тест
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # 1
print(q.peek())     # 2
print(q.dequeue())  # 2
print(q.dequeue())  # 3
print(q.is_empty()) # True
```


#### E3. История браузера (назад/вперёд)

> Реализовать класс `BrowserHistory`: `visit(url)`, `back()`, `forward()`, `current()`.

```python
class BrowserNode:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:
    def __init__(self, homepage):
        self.current_page = BrowserNode(homepage)

    def visit(self, url):
        # Вперёд история стирается (как в реальном браузере)
        pass

    def back(self):
        pass

    def forward(self):
        pass

    def current(self):
        pass


# Тест
bh = BrowserHistory("google.com")
bh.visit("youtube.com")
bh.visit("github.com")
print(bh.current())   # github.com
print(bh.back())      # youtube.com
print(bh.back())      # google.com
print(bh.forward())   # youtube.com
bh.visit("reddit.com")  # стирает github.com из forward
print(bh.forward())   # reddit.com (forward нет → остаёмся)
```


#### E4. Кольцевой плейлист

> Реализовать кольцевой плейлист: `add_song`, `next_song`, `prev_song`, `current_song`, `remove_current`.

```python
class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.current = None
        self.size = 0

    def add_song(self, title: str):
        node = SongNode(title)
        pass

    def next_song(self):
        pass

    def prev_song(self):
        pass

    def current_song(self) -> str | None:
        pass

    def remove_current(self):
        pass


# Тест
pl = Playlist()
pl.add_song("Bohemian Rhapsody")
pl.add_song("Imagine")
pl.add_song("Smells Like Teen Spirit")
print(pl.current_song())  # Bohemian Rhapsody
print(pl.next_song())     # Imagine
print(pl.next_song())     # Smells Like Teen Spirit
print(pl.next_song())     # Bohemian Rhapsody  (кольцо!)
print(pl.prev_song())     # Smells Like Teen Spirit
pl.remove_current()
print(pl.current_song())  # Bohemian Rhapsody
```


#### E5. Сложение полиномов

> Полином представлен списком `(коэффициент, степень)` по убыванию степеней. Сложить два полинома.

**Пример:**
```
P1: 3x⁴ + 2x² + 1       → (3,4)→(2,2)→(1,0)
P2: 5x³ + 2x² + 4x      → (5,3)→(2,2)→(4,1)
Сумма: 3x⁴ + 5x³ + 4x² + 4x + 1
```

```python
class PolyNode:
    def __init__(self, coeff, exp, next=None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

def add_polynomials(p1, p2):
    pass

def print_poly(head) -> None:
    pass


# Тест
p1 = PolyNode(3,4, PolyNode(2,2, PolyNode(1,0)))
p2 = PolyNode(5,3, PolyNode(2,2, PolyNode(4,1)))
result = add_polynomials(p1, p2)
print_poly(result)  # 3x^4 + 5x^3 + 4x^2 + 4x^1 + 1x^0
```


#### E6. Разреженный вектор

> Разреженный вектор хранит только ненулевые элементы. Реализовать `set_val`, `get_val`, `dot_product`.

```python
class SparseNode:
    def __init__(self, index, val, next=None):
        self.index = index
        self.val = val
        self.next = next

class SparseVector:
    def __init__(self):
        self.head = None

    def set_val(self, index, val) -> None:
        pass

    def get_val(self, index) -> int:
        pass

    def dot_product(self, other) -> int:
        """Скалярное произведение двух разреженных векторов"""
        pass


# Тест: v1 = [0, 0, 3, 0, 5], v2 = [0, 1, 0, 4, 5]
# dot = 0*0 + 0*1 + 3*0 + 0*4 + 5*5 = 25
v1 = SparseVector()
v1.set_val(2, 3)
v1.set_val(4, 5)

v2 = SparseVector()
v2.set_val(1, 1)
v2.set_val(3, 4)
v2.set_val(4, 5)

print(v1.dot_product(v2))  # 25
print(v1.get_val(2))       # 3
print(v1.get_val(0))       # 0
```


## Таблица вариантов

Номер варианта должен совпадать с вашим номером в списке группы.

| Вариант | Задача A | Задача B | Задача C | Задача D | Задача E |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | A1 | B1 | C1 | D1 | E1 |
| **2** | A2 | B2 | C2 | D2 | E2 |
| **3** | A3 | B3 | C3 | D3 | E3 |
| **4** | A4 | B4 | C4 | D4 | E4 |
| **5** | A5 | B5 | C5 | D5 | E5 |
| **6** | A6 | B6 | C6 | D6 | E6 |
| **7** | A1 | B2 | C3 | D4 | E5 |
| **8** | A2 | B3 | C4 | D5 | E6 |
| **9** | A3 | B4 | C5 | D6 | E1 |
| **10** | A4 | B5 | C6 | D1 | E2 |
| **11** | A5 | B6 | C1 | D2 | E3 |
| **12** | A6 | B1 | C2 | D3 | E4 |
| **13** | A1 | B3 | C5 | D6 | E2 |
| **14** | A2 | B4 | C6 | D1 | E3 |
| **15** | A3 | B5 | C1 | D2 | E4 |
| **16** | A4 | B6 | C2 | D3 | E5 |
| **17** | A5 | B1 | C3 | D4 | E6 |
| **18** | A6 | B2 | C4 | D5 | E1 |
| **19** | A1 | B4 | C2 | D5 | E3 |
| **20** | A2 | B5 | C3 | D6 | E4 |
| **21** | A3 | B6 | C4 | D1 | E5 |
| **22** | A4 | B1 | C5 | D2 | E6 |
| **23** | A5 | B2 | C6 | D3 | E1 |
| **24** | A6 | B3 | C1 | D4 | E2 |
| **25** | A1 | B5 | C4 | D3 | E6 |
| **26** | A2 | B6 | C5 | D4 | E1 |
| **27** | A3 | B1 | C6 | D5 | E2 |
| **28** | A4 | B2 | C1 | D6 | E3 |
| **29** | A5 | B3 | C2 | D1 | E4 |
| **30** | A6 | B4 | C3 | D2 | E5 |

## Чеклист перед сдачей

-  Код запускается без ошибок
-  Пустой список обработан
-  Список из одного элемента обработан
-  Нет потерянных указателей (нарисовал на бумаге!)
-  Есть минимум 3 теста на каждую задачу
-  Указана сложность по времени и памяти
-  Код оформлен читаемо (имена, комментарии)
