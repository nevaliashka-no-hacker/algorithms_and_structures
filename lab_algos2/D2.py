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
    Ответ: узел со значением 5

    1 проверка на пустой
    2 идем в концы списков, измеряем длину
    3 длина не совпадает -> несколько первых элементов
      большего списка нет в меньшем -> проходим эти элементы,
      не берем их в расчет
    4 одновременно проходимся по спискам,
      сравнивая узлы
    5 равны -> искомый узел, т.к. значение и адрес следующего
      будут равны'''

    if not headA or not headB:
        return None

    curA = headA
    lenA = 0
    curB = headB
    lenB = 0

    while curA.next:
        lenA += 1
        curA = curA.next

    while curB.next:
        lenB += 1
        curB = curB.next

    curA = headA
    curB = headB
    while lenA > lenB:
        lenA -= 1
        curA = cur.next

    while lenB > lenA:
        lenB -= 1
        curB = curB.next

    while curA.next and curB.next:
        if curA == curB:
            return curA
        curA = curA.next
        curB = curB.next
        
    
    return None


def main():
    common = build_list([5, 6])
    headA = ListNode(1, ListNode(2, common))
    headB = ListNode(3, ListNode(6, ListNode(7, common)))
    node = get_intersection(headA, headB)
    print(node.val if node else None)  # 5

if __name__ == "__main__":
    main()
