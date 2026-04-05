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

def get_intersection(headA, headB) -> int | None:
    '''Два списка могут сливаться в один (Y-образная форма).
       Найти узел, где они пересекаются, или `None`.

    A:     1 → 2 ↘
                    5 → 6 → None
    B: 3 → 4 → 7 ↗
    Ответ: узел со значением 5 '''

    if not headA or not headB:
        return None
    
    curA = headA
    curB = headB
    while curA:
        while curB:
            if curA.val == curB.val:
                if curA.next and curB and curA.next == curB:
                    return curA.val
            curB = curB.next
        curA = curA.next

    if curA and curB:
        if curA.val == curB.val:
            return curA.val
    
    return None


def main():
    common = build_list([5, 6])
    headA = ListNode(1, ListNode(2, common))
    headB = ListNode(3, ListNode(4, ListNode(7, common)))
    node = get_intersection(headA, headB)
    print(node.val if node else None)  # 5

if __name__ == "__main__":
    main()
