class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class ListLinked:
    def __init__(self):
        self.head = None
    
    def push_back(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node


def build_list(values):
    """Создать список из массива: build_list([1,2,3]) → 1→2→3→None"""
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def print_list(List):
    """Напечатать список"""
    parts = []
    cur = List.head
    while cur:
        parts.append(str(cur.val))
        cur = cur.next
    print(" → ".join(parts) + " → None")

def split_even_odd(head):
    '''Разделить список на два: в первом — узлы с чётными значениями, 
       во втором — с нечётными. Вернуть оба:
       1 + класс уже целого списка
       2 + нужный метод класса целого списка
       3 в самой функции фильтра
         а) проверка
         б) два объекта списка
         в) проход по всему старому и отдельно по последнему элементу
            и добавление в списки по нужным условиям
       4 вывод'''
    
    if not head:
        return False
    
    evens = ListLinked()
    odds = ListLinked()

    cur = head
    while cur.next:
        if cur.val % 2 == 0:
            evens.push_back(cur.val)
        else:
            odds.push_back(cur.val)
        cur = cur.next

    if cur.val % 2 == 0:
        evens.push_back(cur.val)
    else:
        odds.push_back(cur.val)

    return evens, odds


def main():
    head = build_list([1, 2, 3, 4, 5, 6])
    evens, odds = split_even_odd(head)
    print_list(evens)  # 2 → 4 → 6 → None
    print_list(odds)   # 1 → 3 → 5 → None

if __name__ == "__main__":
    main()
