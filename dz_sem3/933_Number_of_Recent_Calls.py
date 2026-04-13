'''
933. Number of Recent Calls

У вас есть RecentCounter класс, который подсчитывает количество недавних запросов за определенный период времени.

Реализуйте RecentCounter класс:

RecentCounter() Инициализирует счетчик нулевым количеством последних запросов.
int ping(int t) Добавляет новый запрос в момент времени t, где t — это время в миллисекундах, 
и возвращает количество запросов, поступивших за последние 3000 миллисекунд (включая новый запрос). 
В частности, возвращает количество запросов, поступивших в диапазоне [t - 3000, t].


Пример:
Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Ограничения:
1 <= t <= 109
В каждом тестовом примере будет вызываться ping с строго возрастающими значениями t.
Будет сделано не более 104 вызовов ping.
'''

from collections import deque

class RecentCounter():
    def __init__(self):
        self.pings = deque([])

    def ping(self, val):
        temp = []
        result = 0
        self.pings.append(val)
        clock = self.pings
        while clock:
            temp.append(self.pings[0])
            clock.popleft()
        temp_range = list(range(temp[0] - 3000, temp[0]))
        clock = self.pings
        while clock:
            if self.clock[0] in temp_range:
                result += 1
            clock.popleft()
        return result

def main():
    rec = RecentCounter()
    print(rec.ping(1)) # запросы = [1], диапазон равен [-2999,1], возвращает 1 
    print(rec.ping(100)) # запросы = [1, 100], диапазон равен [-2900,100], возврат 2 
    print(rec.ping(3001)) # запросы = [1, 100, 3001], диапазон равен [1,3001], возврат 3 
    print(rec.ping(3002)) # запросы = [1, 100, 3001, 3002], диапазон равен [2,3002], возврат 3

if __name__ == "__main__":
    main()