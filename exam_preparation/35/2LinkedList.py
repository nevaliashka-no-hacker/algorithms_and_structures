'''Двусвязный список'''
'''Заглянула на сайт, в практических задачах его нет(((((('''
'''И че я делала то... Фигня какая-то...'''

class Node:
    def __init__(self, value = None):
        self.prev = None
        self.val = value
        self.next = None

class LinkedListReturn:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_to_start(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        
    def add_to_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def find(self, value):
        if not self.head:
            return False
        cur = self.head
        while cur:
            if cur.val == value:
                return True
            cur = cur.next
        return False

    def remove(self, value):
        if not self.head:
            return False
        if not self.find(value):
            return False
        cur = self.head
        while cur:
            if cur.val == value:
                if self.head == self.tail:
                    self.head = self.tail = None
                elif cur == self.head:
                    self.head = cur.next
                    self.head.prev = None
                elif cur == self.tail:
                    self.tail = cur.prev
                    self.tail.next = None
                else:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                return True
            cur = cur.next
        return False

    def translate_in_list(self):
        ordinarylist = []
        if not self.head:
            return ordinarylist
        cur = self.head
        while cur:
            ordinarylist.append(cur.val)
            cur = cur.next
        return ordinarylist

    def show(self):
        ordlist = self.translate_in_list()
        print(*ordlist, sep = '<->')
        
            

res = LinkedListReturn()
res.add_to_start(6)
res.add_to_end(7)
res.show()
print(res.find(7))
res.remove(7)
print(res.find(7))
res.show()

            
