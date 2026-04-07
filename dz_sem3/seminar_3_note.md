# Семинар 3: Очередь (Queue)

> [!TIP]
> Домашние задания лежат [тут](/sem_3/tasks.md). Перед выполнением стоит заглянуть в [шаблон](/sem_3/template.md), в котором есть заготовки функций.

## 1. Теория

### Что такое очередь?

**Очередь** — структура данных, работающая по принципу **FIFO** (First In, First Out) — "первым пришёл, первым ушёл".

> **Аналогия из жизни**: Очередь в магазине — кто первый встал, того первого обслужат.

**Основное отличие от стека**:
- **Стек (LIFO)**: добавление и удаление с одного конца
- **Очередь (FIFO)**: добавление в конец, удаление из начала

### Основные операции:

| Операция | Описание | Сложность |
|----------|----------|-----------|
| `enqueue(x)` | Добавить элемент в конец | O(1) |
| `dequeue()` | Удалить элемент из начала | O(1)* |
| `peek()` / `front()` | Посмотреть первый элемент | O(1) |
| `isEmpty()` | Проверка на пустоту | O(1) |
| `size()` | Размер очереди | O(1) |


## 2. Реализация

### 2.1. Очередь на основе списка

```python
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Добавить элемент в конец очереди"""
        self.items.append(item)

    def dequeue(self):
        """Удалить и вернуть первый элемент"""
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items.pop(0)  # удаление из начала - O(n)

    def peek(self):
        """Посмотреть первый элемент без удаления"""
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Пример использования
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # 1
print(q.peek())     # 2
```

> **Проблема**: `pop(0)` имеет сложность O(n), т.к. нужно сдвигать все элементы!

### 2.2. Эффективная реализация с collections.deque

```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)  # O(1)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items.popleft()  # O(1) - вот и разница!

    def peek(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
```

### 2.3. Реализация на связном списке

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None  # Указатель на начало
        self.rear = None   # Указатель на конец
        self._size = 0

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:  # Очередь пуста
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        item = self.front.data
        self.front = self.front.next
        if self.front is None:  # Очередь стала пустой
            self.rear = None
        self._size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.front.data

    def is_empty(self):
        return self.front is None

    def size(self):
        return self._size
```


## 3. Расширенные типы очередей

### 3.1. Циклическая очередь (Circular Queue)

Используется для эффективного использования памяти фиксированного размера.

```python
class CircularQueue:
    def __init__(self, k):
        self.queue = [None] * k
        self.max_size = k
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, value):
        if self.is_full():
            raise IndexError("Очередь переполнена")
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = value
        self.size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        value = self.queue[self.front]
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return value

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

# Пример
cq = CircularQueue(3)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
print(cq.dequeue())  # 1
cq.enqueue(4)        # Используем освободившееся место
```

### 3.2. Двухсторонняя очередь (Deque)

Позволяет добавлять и удалять элементы с обоих концов.

```python
from collections import deque

class Deque:
    def __init__(self):
        self.items = deque()

    def add_front(self, item):
        self.items.appendleft(item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.popleft()

    def remove_rear(self):
        return self.items.pop()

    def peek_front(self):
        return self.items[0]

    def peek_rear(self):
        return self.items[-1]

# Пример: палиндром
def is_palindrome(s):
    dq = deque(s.lower().replace(" ", ""))
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

print(is_palindrome("radar"))  # True
```


## 4. Реальные применения

### 4.1. Обход графа в ширину (BFS)

> [!NOTE]
> Разбор пропущен до последующих занятий по графам. Подробнее про обход графов можно посмотреть на сайтах [Я.Образование](https://education.yandex.ru/handbook/algorithms/article/obhody-grafa) и [Algoritmica](https://ru.algorithmica.org/cs/shortest-paths/bfs/). Пока просто знайте что такое существует.

### 4.2. Симуляция принтера

```python
from collections import deque
import time

class PrintJob:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages

class Printer:
    def __init__(self):
        self.queue = deque()

    def add_job(self, job):
        print(f"Добавлена задача: {job.name} ({job.pages} стр.)")
        self.queue.append(job)

    def process_jobs(self):
        while self.queue:
            job = self.queue.popleft()
            print(f"Печать: {job.name}...")
            time.sleep(job.pages * 0.1)  # Симуляция времени печати
            print(f"Завершено: {job.name}")

# Использование
printer = Printer()
printer.add_job(PrintJob("Документ1", 5))
printer.add_job(PrintJob("Документ2", 3))
printer.add_job(PrintJob("Документ3", 7))
printer.process_jobs()
```

### 4.3. Скользящее окно (Sliding Window)

```python
from collections import deque

def max_sliding_window(nums, k):
    """
    Найти максимум в каждом окне размера k
    Пример: [1,3,-1,-3,5,3,6,7], k=3 -> [3,3,5,5,6,7]
    """
    result = []
    dq = deque()  # Храним индексы

    for i in range(len(nums)):
        # Удаляем элементы вне окна
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Удаляем меньшие элементы (они не нужны)
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # Добавляем результат начиная с k-го элемента
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))
# [3, 3, 5, 5, 6, 7]
```

### 4.4. Обработка задач с приоритетами (Priority Queue)

```python
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, item, priority):
        # Минимальная куча, поэтому инвертируем для максимального приоритета
        heapq.heappush(self.heap, (-priority, item))

    def dequeue(self):
        if not self.heap:
            raise IndexError("Очередь пуста")
        return heapq.heappop(self.heap)[1]

    def is_empty(self):
        return len(self.heap) == 0

# Пример: система обработки заявок
pq = PriorityQueue()
pq.enqueue("Обычная заявка", 1)
pq.enqueue("Срочная заявка", 10)
pq.enqueue("Критическая заявка", 100)

while not pq.is_empty():
    print(pq.dequeue())
# Критическая заявка
# Срочная заявка
# Обычная заявка
```

## 6. Сравнительные таблицы

**Когда что стоит применять:**

| Характеристика | Стек | Очередь | Deque |
|----------------|------|---------|-------|
| Принцип работы | LIFO | FIFO | Оба конца |
| Добавление | Один конец | Конец | Оба конца |
| Удаление | Один конец | Начало | Оба конца |
| Применение | Рекурсия, отмена действий | BFS, планировщики | Скользящее окно |

**Сложность операций:**

| Реализация      | enqueue | dequeue | space |
|-----------------|---------|---------|-------|
| List (неэффект.)| O(1)    | O(n)    | O(n)  |
| deque           | O(1)    | O(1)    | O(n)  |
| Linked List     | O(1)    | O(1)    | O(n)  |
