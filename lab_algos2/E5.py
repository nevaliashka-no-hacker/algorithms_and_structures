class PolyNode:
    def __init__(self, coeff, exp, next=None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

def add_polynomials(p1, p2):
    '''
    Полином представлен списком `(коэффициент, степень)` по убыванию степеней.
    Сложить два полинома.
    
    Пример:
    P1: 3x⁴ + 2x² + 1       → (3,4)→(2,2)→(1,0)
    P2: 5x³ + 2x² + 4x      → (5,3)→(2,2)→(4,1)
    Сумма: 3x⁴ + 5x³ + 4x² + 4x + 1
    '''

    if not p1 or not p2:
        return False
    
    curp1 = p1
    curp2 = p2
    max_exp = max(curp1.exp, curp2.exp)

    pres = PolyNode(0, max_exp)
    head = pres
    while max_exp > 0:
        max_exp -= 1
        new_node = PolyNode(0, max_exp)

        pres.next = new_node

        pres = pres.next

    curpres = head
    while curpres.next:
        if curpres.exp == curp1.exp:
            curpres.coeff += curp1.coeff
            curp1 = curp1.next
        if curpres.exp == curp2.exp:
            curpres.coeff += curp2.coeff
            curp2 = curp2.next
        curpres = curpres.next
        
    if curp1 and curpres.exp == curp1.exp:
        curpres.coeff += curp1.coeff
    if curp2 and curpres.exp == curp2.exp:
        curpres.coeff += curp2.coeff
        
    return head

def print_poly(head) -> None:
    cur = head
    while cur.next:
        if cur.coeff != 0:
            print(f'{cur.coeff}x^{cur.exp}', end = ' + ')
        cur = cur.next
    print(f'{cur.coeff}x^{cur.exp}')

def main():
    # Тест
    p1 = PolyNode(3,4, PolyNode(2,2, PolyNode(1,0)))
    p2 = PolyNode(5,3, PolyNode(2,2, PolyNode(4,1)))
    result = add_polynomials(p1, p2)
    print_poly(result)  # 3x^4 + 5x^3 + 4x^2 + 4x^1 + 1x^0

if __name__ == "__main__":
    main()
