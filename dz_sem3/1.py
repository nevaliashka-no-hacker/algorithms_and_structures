'''
Реализовать очередь на 2 стеках
'''

class Queue:
    def __init__(self):
        self.stackback = [] # главный
        self.stackhead = [] # помогатор

    #добавление
    def enqueue(self, item):
        self.stackback.append(item)

    #удаление
    def dequeue(self):
        temp = self.stackback.copy()
        self.clean_stackhead()
        while temp:
            self.stackhead.append(temp[-1])
            temp.pop()
        result = self.stackhead.pop()
        self.new_stacks()
        return result

    #первый элемент очереди
    def peek(self):
        if not self.stackback:
            return None
        temp = self.stackback.copy()
        self.clean_stackhead()
        while temp:
            self.stackhead.append(temp[-1])
            temp.pop()
        return self.stackhead[-1]

    #размер очереди
    def size(self):
        return len(self.stackback)

    #обновление стеков
    def new_stacks(self):
        temp = self.stackhead.copy()
        while self.stackback:
            self.stackback.pop()
        while temp:
            self.stackback.append(temp[-1])
            temp.pop()

    #чистка начала, а то мусор еще добавится с
    #прошлых заполнений этого стека
    def clean_stackhead(self):
        while self.stackhead:
            self.stackhead.pop()
    
def main():
    #тест
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())  # 1
    print(q.peek())     # 2

if __name__ == "__main__":
    main()
