'''
622. Design Circular Queue

Реализовать класс MyCircularQueue:

MyCircularQueue(k) Инициализирует объект с размером очереди, равным k.
int Front() Получает первый элемент из очереди. Если очередь пуста, верните -1.
int Rear() Получает последний элемент из очереди. Если очередь пуста, верните -1.
boolean enQueue(int value) Вставляет элемент в циклическую очередь. Верните true, если операция прошла успешно.
boolean deQueue() Удаляет элемент из циклической очереди. Верните, true если операция прошла успешно.
boolean isEmpty() Проверяет, пуста ли циклическая очередь или нет.
boolean isFull() Проверяет, заполнена ли циклическая очередь.
'''

class MyCircularQueue:
    def __init__(self, k):
        self.queue = [None] * k
        self.max_size = k
        self.front = 0
        self.rear = -1
        self.size = 0

    def Front(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]
    
    def Rear(self):
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def enQueue(self, value):
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = value
        self.size += 1
        return True
    
    def deQueue(self):
        if self.isEmpty():
            return False
        value = self.queue[self.front]
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return True
    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.max_size


def main():
    myCircularQueue = MyCircularQueue(3)
    print(myCircularQueue.enQueue(1)) # True
    print(myCircularQueue.enQueue(2)) # True
    print(myCircularQueue.enQueue(3)) # True
    print(myCircularQueue.enQueue(4)) # False
    print(myCircularQueue.Rear()) # 3
    print(myCircularQueue.isFull()) # True
    print(myCircularQueue.deQueue()) # True
    print(myCircularQueue.enQueue(4)) # True
    print(myCircularQueue.Rear()) # 4

if __name__ == "__main__":
    main()
