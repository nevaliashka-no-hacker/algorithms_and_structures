'''
Реализовать очередь на 2 стеках

План реализации:
1 есть 2 стека: начало (stackhead) и конец (stackback)
2 добавление элемента в конец
3 создаем копию стека конца, добавляем в конец начального
  стека элементы и, по факту, очередь переворачивается,
  далее, обновляем конечный стек (так как он будет содержать
  старую информацию, например, с удаленным элементом
4 для первого элемента переворачиваем стек и b cмотрим последний для стека
  элемент
5 размер понятно, только основной у нас стек stackback, конечно
6 обновление конечного стека
'''

class Queue:
    def __init__(self):
        self.stackback = []
        self.stackhead = []

    #добавление
    def enqueue(self, item):
        #print(len(self.stackback))
        self.stackback.append(item)

    #удаление
    def dequeue(self):
        #print("dequeue", len(self.stackback))
        temp = self.stackback.copy()
        self.clean_stackhead()
        while temp:
            self.stackhead.append(temp[-1])
            temp.pop()
        #print("deq", len(self.stackback))
        result = self.stackhead.pop()
        self.new_stacks()
        return result

    #первый элемент очереди
    def peek(self):
        #print(len(self.stackback))
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
