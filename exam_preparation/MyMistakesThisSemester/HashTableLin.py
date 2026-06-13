class HashNode:
    def __init__(self, key = None, value = None, status = "FREE"):
        self.key = key
        self.val = value
        self.status = status

class HashTableLin:
    def __init__(self, n = 3, load_factor = 0):
        self.table = [HashNode() for _ in range(n)]
        self.n = n
        self.load_factor = load_factor

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def next_size(self, num):
        while not self.is_prime(num):
            num += 1
        return num

    def rehash(self):
        new_size = self.next_size(self.n * 2)
        print("rehash:", self.n, "=", new_size)
        print()

        new_table = [HashNode() for _ in range(new_size)]

        old_table = self.table
        old_size = self.n 

        self.n = new_size
        self.table = new_table
        self.load_factor = 0

        for i in range(old_size):
            if old_table[i].status == "BUSY":
                self.insert(old_table[i].key, old_table[i].val)
                
    def insert(self, ke, value):
        if (self.load_factor + 1) / self.n > 0.7:
            self.rehash()

        for i in range(self.n):
            index = (self.hash1(ke) + i) % self.n 
            if self.table[index].status == "FREE":
                break
            if self.table[index].status == "BUSY" and self.table[index].key == ke:
                self.table[index].val = value
                return "update"
            
        for i in range(self.n):
            index = (self.hash1(ke) + i) % self.n
            if self.table[index].status == "FREE" or self.table[index].status == "DELETED":
                self.table[index].key = ke
                self.table[index].val = value
                self.table[index].status = "BUSY"
                self.load_factor += 1
                return "GOOD INSERT"
                
    def search(self, ke):
        for i in range(self.n):
            index = (self.hash1(ke) + i) % self.n
            if self.table[index].status == "FREE":
                return "No found"
            if self.table[index].status == "BUSY" and self.table[index].key == ke:
                return self.table[index].val
        return "No found"

    def delete(self, ke):
        for i in range(self.n):
            index = (self.hash1(ke) + i) % self.n 
            if self.table[index].status == "BUSY" and self.table[index].key == ke:
                self.table[index].status = "DELETED"
                self.table[index].key = None
                self.table[index].val = None
                self.load_factor -= 1
                return "Good deleted"
        return "No deleted, no found..."

    # Хеширование строк (полиномиальное хеширование)
    def hash1(self, ke):
        h = 0
        x = 31
        for char in ke:
            h = (h * x + ord(char)) % self.n
        return h

    def show(self):
        for i in range(self.n):
            print(self.table[i].key, self.table[i].val, self.table[i].status)
        
table = HashTableLin()

table.insert("name", "tom")
table.show()
print()
table.insert("email", "tom@gmail.com")
table.show()
print()
table.insert("telephone", "+78910111213")

table.show()
print()

print(table.search("name"))

table.delete("name")
table.show()
print()

print(table.search("name"))

table.insert("company", "1C")

table.show()

    
