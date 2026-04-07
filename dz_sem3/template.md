# Типовые шаблоны

## Очередь (Queue)

```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
```

## Очередь с приоритетом (Priority Queue)

```python
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, item, priority):
        heapq.heappush(self.heap, (-priority, item))

    def dequeue(self):
        if not self.heap:
            raise IndexError("Очередь пуста")
        return heapq.heappop(self.heap)[1]

    def is_empty(self):
        return len(self.heap) == 0
```

## Двухсторонняя очередь (Deque)

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
```
