''' Универсальная хеш-функция (Картер и Вегман)'''

class HashNode:
    def __init__(self):
        pass

class QuadraticHashTable:
    def __init__(self):
        pass


table = QuadraticHashTable()

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
print()

table.delete("name")
table.show()
print()

print(table.search("name"))

table.insert("company", "1C")

table.show()
