class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
    '''Переместить первый элемент списка в конец'''
    
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
