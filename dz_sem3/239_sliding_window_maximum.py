'''
239. Sliding Window Maximum

Вам дан массив целых чисел nums, скользящее окно размером k перемещается от левого края массива к правому. 
Вы можете видеть только k чисел в окне. 
Каждый раз скользящее окно сдвигается вправо на одну позицию.
Верните максимальное скользящее окно.

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position Max
--------------- -----
[1 3 -1] -3 5 3 6 7    3
 1 [3 -1 -3] 5 3 6 7   3
 1 3 [-1 -3 5] 3 6 7   5
 1 3 -1 [-3 5 3] 6 7   5
 1 3 -1 -3 [5 3 6] 7   6
 1 3 -1 -3 5 [3 6 7]   7
'''

from collections import deque

class Queue():
    def __init__(self, window):
        self.que = deque(window)

    def enqueue(self, value):
        self.que.append(value)

    def dequeue(self):
        if len(self.que) == 0:
            return None
        self.que.popleft()

    def max(self):
        max_num = self.que[0]
        temp = self.que.copy()
        while temp:
            if max_num < temp[0]:
                max_num = temp[0]
            temp.popleft()
        return max_num

def slidingWindow(nums, k):
    n = len(nums)
    queue = Queue(nums[:k])
    if n < k:
        return None
    result = []
    while k != n:
        result.append(queue.max())
        queue.enqueue(nums[k])
        queue.dequeue()
        k += 1
    result.append(queue.max())
    return result

def main():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(slidingWindow(nums, k))

if __name__ == "__main__":
    main()
