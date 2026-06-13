'''Так, стоп! Время на подготовку очень огрничено, 
а я переписываю просто хеш таблицу с линейнфм пробированием и 
лишб чуток меняю строчки (где высчитывается index и применчеося
функция хеширования. В общем, здесь нужно только функцию 
хеширования прописать и все...'''


class QuadraticHashTable:
    def __init__(self, n = 3, cnt = 0):
        self.table = [(None, None, "free") for _ in range(n)]
        self.n = n
        self.cnt = cnt
        
    def insert(self, key, value):
        if (cnt + 1) % self.n >= 0.7:
            self.rehash()
            
        for i in range(self.n):
            index = (hashed(key) + i * i) % self.n
            if self.table[index][2] == "free":
                break
                             


