class ListNode:
    def __init__(self, val = 0, next = None):
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

def count_above_average(head) -> int:
    '''Подсчитать, сколько элементов списка строго больше
       среднего арифметического всех элементов'''

    if not head:
        return 0

    len_head = 0
    sum_head = 0
    count_el = 0
    arith_mean = 0

    cur = head
    while cur.next:
        len_head += 1
        sum_head += cur.val
        cur = cur.next
    len_head += 1
    sum_head += cur.val
    arith_mean = sum_head // len_head

    cur = head
    while cur.next:
        if cur.val > arith_mean:
            count_el += 1
        cur = cur.next

    if cur.val > arith_mean:
            count_el += 1

    return count_el

def main():
    head = build_list([1, 2, 3, 4, 10])
    print(count_above_average(head))

if __name__ == "__main__":
    main()
