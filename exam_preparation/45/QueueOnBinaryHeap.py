'''Приоритетная очередь на бинарной куче'''

class PriorQueueOnBinHeapMin:
    def __init__(self):
        self.heap = []

    def len(self):
        return len(self.heap)

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def sift_up(self, i):
        parent = self.parent(i)
        while i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            i = parent
            parent = self.parent(i)

    def sift_down(self, i):
        size = self.len(self.heap)
        while True:
            smallest = i
            left = self.left(i)
            right = self.right(i)
            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == i:
                break
            self.swap(i, smallest)
            i = smallest

    def push(self, item):
        self.heap.append(item)
        self.sift_up(self.len(self.heap) - 1)

    def pop(self):
        '''извлечение минимального элемента'''
        if not self.heap:
            raise IndexError("pop from empty priority queue")
        min_item = self.heap[0]
        last_item = self.heap.pop()
        if self.heap:
            self.heap[0] = last_item
            self.sift_down(0)
        return min_item

    def peek(self):
        '''минимальный элемент'''
        if not self.heap:
            raise IndexError("peek form empty priority queue")
        return self.heap[0]


class PriorQueueOnBinHeapMax:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return i * 2 + 1

    def right(self, i):
        return i * 2 + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def sift_up(self, i):
        parent = self.parent(i)
        while i > 0 and self.heap[i] > self.heap[parent]:
            self.swap(i, parent)
            i = parent
            parent = (i - 1) // 2

    def sift_down(self, i):
        size = len(self.heap)
        while True:
            maximus = i
            left = self.left(i)
            right = sel.right(i)
            if left < size and self.heap[left] > self.heap[maximus]:
                maximus = left
            if right < size and self.heap[right] > self.heap[maximus]:
                maximus = right
            if maximus == i:
                break
            self.swap(i, maximus)
            i = maximus

    def push(self, i):
        self.heap.append(i)
        self.sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            raise IndexError("no priority queue")
        max_item = self.heap[0]
        last_item = self.heap.pop()
        if self.heap:
            self.heap[0] = last_item
            self.sift_down(0)
        return max_item

    def peek(self):
        if not self.heap:
            raise IndexError("no priority queue")
        return self.heap[0]
