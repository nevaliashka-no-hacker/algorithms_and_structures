# Связные списки


## Часть 1. Что такое связный список

### Идея
Массив хранит элементы **рядом в памяти**. Связный список хранит элементы **где угодно**, а каждый элемент содержит **ссылку на следующий**.

```
Массив:     [10][20][30][40]   — непрерывный блок памяти

Список:     [10|→] → [20|→] → [30|→] → [40|∅]
             head                       tail
```

### Сравнение с массивом

| Операция | Массив | Связный список |
|---|---|---|
| Доступ по индексу | **O(1)** | O(n) |
| Вставка в начало | O(n) | **O(1)** |
| Вставка в середину | O(n) | **O(1)** * |
| Удаление из начала | O(n) | **O(1)** |
| Поиск элемента | O(n) | O(n) |
| Память | Компактно | +указатель на узел |

> \* O(1) если уже есть указатель на нужное место, иначе O(n) на поиск

### Виды списков

```
Односвязный:    [A] → [B] → [C] → None

Двусвязный:     None ← [A] ⇄ [B] ⇄ [C] → None

Кольцевой:      [A] → [B] → [C] → [A] (зацикленный)
```


## Часть 2. Реализация с нуля

### Узел (Node)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### Односвязный список — базовые операции

```python
class LinkedList:
    def __init__(self):
        self.head = None

    # Вставка в начало O(1)
    def push_front(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    # Вставка в конец O(n)
    def push_back(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    # Удаление по значению O(n)
    def remove(self, val):
        dummy = ListNode(0)      # фиктивный узел — важный приём!
        dummy.next = self.head
        prev, cur = dummy, self.head
        while cur:
            if cur.val == val:
                prev.next = cur.next
                self.head = dummy.next
                return True
            prev = cur
            cur = cur.next
        return False

    # Поиск O(n)
    def find(self, val):
        cur = self.head
        while cur:
            if cur.val == val:
                return True
            cur = cur.next
        return False

    # Печать
    def __str__(self):
        parts, cur = [], self.head
        while cur:
            parts.append(str(cur.val))
            cur = cur.next
        return " → ".join(parts) + " → None"
```

### Демонстрация

```python
ll = LinkedList()
ll.push_back(1)
ll.push_back(2)
ll.push_back(3)
ll.push_front(0)
print(ll)          # 0 → 1 → 2 → 3 → None

ll.remove(2)
print(ll)          # 0 → 1 → 3 → None
print(ll.find(3))  # True
```

## Часть 3. Ключевые приёмы и паттерны

### Приём 1: Dummy Node (фиктивная голова)

Упрощает граничные случаи (удаление головы, пустой список).

```python
def remove_all(head, val):
    """Удалить ВСЕ узлы с данным значением"""
    dummy = ListNode(0)
    dummy.next = head
    prev, cur = dummy, head
    while cur:
        if cur.val == val:
            prev.next = cur.next   # "перепрыгиваем" узел
        else:
            prev = cur
        cur = cur.next
    return dummy.next              # новая голова
```

### Приём 2: Два указателя (slow & fast)

Классика — **найти середину** или **обнаружить цикл**.

```python
def find_middle(head):
    """Медленный идёт по 1, быстрый по 2 — когда быстрый
       дойдёт до конца, медленный будет ровно посередине"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow  # это средний узел
```

```python
def has_cycle(head):
    """Алгоритм Флойда — 'черепаха и заяц'"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True     # встретились → цикл есть
    return False
```

### Приём 3: Разворот списка (in-place)

Самый частый вопрос на собеседованиях.

```python
def reverse_list(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next    # запомнили следующий
        cur.next = prev   # развернули стрелку
        prev = cur        # сдвинули prev
        cur = nxt         # сдвинули cur
    return prev           # prev — новая голова

# Визуализация:
#
# Вход:
# 1 → 2 → 3 → None
#
# Шаг 0:
#
#  prev cur
#   ↓    ↓
# None ← 1    2 → 3 → None
#
# Шаг 1:
#
#      prev cur
#        ↓   ↓
# None ← 1 ← 2    3 → None
#
# Шаг 2:
#
#          prev cur
#            ↓   ↓
# None ← 1 ← 2 ← 3
#
# Шаг 3:
#
#              prev cur
#                ↓   ↓
# None ← 1 ← 2 ← 3
#
# cur=None → СТОП
#
# Выход:
# None ← 1 ← 2 ← 3
# Что фактически можно представить в прямой записи как
# 3 → 2 → 1 → None
```

### Приём 4: Слияние двух отсортированных списков

```python
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2     # дописываем остаток
    return dummy.next
```


## Часть 4. Где это используется в реальном мире

| Применение | Почему список |
|---|---|
| **Undo/Redo** в редакторах | Каждое действие — узел; легко вставлять и удалять |
| **Навигация браузера** (назад/вперёд) | Двусвязный список страниц |
| **LRU-кэш** (Redis, ОС) | Двусвязный список + хеш-таблица → O(1) вставка/удаление |
| **Очередь / Дек** | Вставка и удаление с концов за O(1) |
| **Файловые системы** | Блоки файла разбросаны по диску, связаны указателями |
| **Музыкальный плейлист** | Кольцевой список → бесконечное воспроизведение |
| **Хеш-таблица (chaining)** | Коллизии хранятся в связном списке |
| **Malloc / аллокаторы памяти** | Свободные блоки — в связном списке |

### Мини-пример: LRU-кэш (идея)

```
Размер кэша = 4

Самый свежий     Самый старый
    ↓                 ↓
   [D] ⇄ [B] ⇄ [A] ⇄ [C]
   head                tail

Обратились к A → переносим в начало:
   [A] ⇄ [D] ⇄ [B] ⇄ [C]

Кэш полон, добавляем E → удаляем tail (C):
   [E] ⇄ [A] ⇄ [D] ⇄ [B]
```

## Часть 5. Задачи для тренировки на LeetCode

### Easy

| # | Задача | Ключевой приём |
|---|---|---|
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Разворот (итеративно + рекурсивно) |
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Dummy node, слияние |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Fast & slow pointers |
| 876 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | Fast & slow |
| 203 | [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/) | Dummy node |
| 83 | [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | Один указатель |
| 160 | [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) | Два указателя |
| 234 | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) | Середина + разворот |

### Medium

| # | Задача | Ключевой приём |
|---|---|---|
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Dummy node, carry |
| 19 | [Remove Nth Node From End](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Два указателя с зазором |
| 24 | [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) | Перестановка указателей |
| 142 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | Флойд — найти начало цикла |
| 148 | [Sort List](https://leetcode.com/problems/sort-list/) | Merge sort на списке |
| 146 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | Двусвязный список + хеш |
| 138 | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | Хеш-таблица / interleaving |
| 92 | [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) | Частичный разворот |

### Hard

| # | Задача | Ключевой приём |
|---|---|---|
| 25 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | Разворот блоками |
| 23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Heap / divide & conquer |


## Советы

1. Всегда задавайте вопрос: "Нужен ли dummy node?".
2. Сохраняйте next ПЕРЕД тем, как менять следующий элемент.
3. Slow/Fast - середина, цикл, n-й с конца.
4. Разворот = prev/cur/next + цикл.
5. Лучше всего расписать каждый шаг на бумаге.
