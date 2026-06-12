class PrioretyQueue:
    def __init__(self, iteams = []):
        self._iteams = iteams

    def enqueue(self, priorety, element):
        return self._iteams.append((priorety, element))

    def dequeue(self):
        if len(self._iteams) == 0:
            return "Where elements?"

        min_idx = 0
        for i in range(len(self._iteams)):
            if (self._iteams[i][0] < self._iteams[min_idx][0]):
                min_idx = i

        return self._iteams.pop(min_idx)

    def find(self, element):
        for i in range(len(self._iteams)):
            if (self._iteams[i][1] == element):
                return i

        return "No element"

    def show(self):
        for i in range(len(self._iteams)):
            print(self._iteams[i])

iteams = PrioretyQueue()
iteams.enqueue(3, "soup")
iteams.enqueue(4, "meat")
iteams.enqueue(1, "macaron")
iteams.enqueue(5, "egg")
iteams.enqueue(2, "lime")

iteams.show()
print()

iteams.dequeue()
iteams.dequeue()
iteams.dequeue()

iteams.show()
print()

print(iteams.find("meat"))
print(iteams.find("macaron"))
