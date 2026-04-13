'''
Реализовать систему обработки заказов в ресторане (с приоритетами).
'''

from collections import deque

class Orders:
    def __init__(self):
        self.orders = deque()
      
    def add_order(self, order):
        self.orders.append(order)
        
    def delete_order(self):
        if self.is_empty():
            return None
        return self.orders.popleft()   
        
    def is_empty(self):
        return len(self.orders) == 0

def main():
    waiter = Orders()
    waiter.add_order('23table')
    print('Заказ принят')
    waiter.add_order('1table')
    print('Заказ принят')
    waiter.add_order('5table')
    print('Заказ принят')
    print('Заказ',waiter.delete_order(), 'готов!')
    print('Заказ',waiter.delete_order(), 'готов!')
    waiter.add_order('17table')
    print('Заказ принят')
    print('Заказ',waiter.delete_order(), 'готов!')
    print('Заказ',waiter.delete_order(), 'готов!')
    
if __name__ == "__main__":
    main()    