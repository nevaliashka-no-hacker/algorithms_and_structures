'''Задача с монетками. Жадный алгоритм'''

def coins(nums, target):
    summ = 0
    result = []
    index = len(nums) - 1
    while summ <= target and index >= 0:
        if summ + nums[index] == target:
            result.append(nums[index])
            summ += nums[index]
            return result, len(result)
        elif summ + nums[index] > target:
            if index > 0:
                index -= 1
            else:
                return None
        else:
            summ += nums[index]
            result.append(nums[index])

nums = [1, 2, 5, 10]
target = 54
print(*coins(nums, target))
