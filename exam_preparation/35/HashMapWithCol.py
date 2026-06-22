'''HashMap с цепочками для разрешения коллизий'''

class HashMap:
    def __init__(self, n = 7):
        self.buckets = [{} for _ in range(n)]
        self.n = n

    def hash(self, key):
        h = 0
        a = 31
        for ch in key:
            h = (h * a + ord(ch)) % self.n
        return h 

    def add(self, key, value):
        index = self.hash(key) % self.n
        self.buckets[index][key] = value

    def remove(self, key):
        index = self.hash(key) % self.n
        del self.buckets[index][key]

    def show(self):
        print(self.buckets)

test = HashMap()
test.add("mouse", 3)
test.add("fish", 10)
test.add("cockroach", 100000000)
test.show()
test.remove("cockroach")
test.show()
        
        
