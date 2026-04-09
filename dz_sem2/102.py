'''
Дан массив целых чисел `nums` и число `limit`. Найти длину наибольшего непрерывного подмассива, 
в котором разница между максимальным и минимальным элементами не превышает `limit`.
'''

def len_result(nums, limit):
    if len(nums) < 2:
        return None
    
    left = 0
    right = len(nums)
    max_res = []
    window = nums

    #1
    while left < right and left < len(nums) and right > 0 and len(window) > 1:
        window = nums[left:right]
        max_num = max(window)
        min_num = min(window)
        if max_num - min_num <= limit:
            if len(window) > len(max_res):
                max_res = window
        if nums[left] > nums[right - 1]:
            left += 1
        else:
            right -= 1

    return max_res

def main():
    #nums = input()
    #limit = int(input())
    nums = [8, 2, 4, 7]
    limit = 4
    print(len_result(nums, limit))

if __name__ == "__main__":
    main()
