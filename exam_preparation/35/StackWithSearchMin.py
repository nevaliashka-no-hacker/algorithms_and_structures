'''Стек с поиском минимума/максимума/67 за О(1)'''

class StackWithMinMax67:
    def __init__(self):
        self.stack = []
        self.minstack = []
        self.maxstack = []
        self.if67 = False

    def push(self, value):
        self.stack.append(value)
        if self.minstack == [] or self.minstack[-1] > value:
            self.minstack.append(value)
        if self.maxstack == [] or self.maxstack[-1] < value:
            self.maxstack.append(value)
        if value == 67:
            self.if67 = True

    def remove(self):
        if self.minstack != [] and self.minstack[-1] == self.stack[-1]:
            self.minstack.pop()
        if self.maxstack != [] and self.maxstack[-1] == self.stack[-1]:
            self.maxstack.pop()
        if self.stack[-1] == 67:
            self.if67 = False
        self.stack.pop()

    def question67(self):
        return self.if67

    def get_min(self):
        return self.minstack[-1]

    def get_max(self):
        return self.maxstack[-1]

stack = StackWithMinMax67()
stack.push(67)
stack.push(54)
stack.push(45)
stack.push(100)

print(stack.question67())
print(stack.get_min())
print(stack.get_max())

stack.remove()

print(stack.get_min())
print(stack.get_max())
