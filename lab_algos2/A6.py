class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''    
class ListLinked:
    def __init__(self):
        self.head = None

    #вставка элемента в конец
    def push_back(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    #удаление элемента по значению
    def remove(self, val):
        dummy = ListNode(val)
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
'''


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


def move_first_to_end(head):
    '''Переместить первый элемент списка в конец:
       1 проверка на пустой или одноэлементный
       2 находим первый
       3 находим новый первый (второй в старом)
       4 идем к последнему
       5 добавляем первый после последнего
       6 в новом последнем нет указателя на следующий, поэтому None'''
    
    if not head or not head.next:
        return head

    first_node = head
    new_head = head.next

    tail = head
    while tail.next:
        tail = tail.next

    tail.next = first_node
    first_node.next = None

    return new_head

def main():
    # Тест
    head = build_list([1, 2, 3, 4])
    head = move_first_to_end(head)
    print_list(head)  # 2 → 3 → 4 → 1 → None

if __name__ == "__main__":
    main()
