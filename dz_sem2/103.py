'''
Дан отсортированный по неубыванию массив целых чисел `nums`. 
Вернуть массив квадратов этих чисел, также отсортированный по неубыванию.
'''

def mergeSort(nums):
    while 1:
        flag = 0
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] > nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                flag += 1
            else:
                right -= 1

        if flag == 0:
            break
    return nums

def square(nums):
    for i in range(len(nums)):
        nums[i] *= nums[i]
    nums = mergeSort(nums)
    return nums

def main():
    #nums = input()
    nums = [-4, -1, 0, 3, 10]
    print(square(nums))

if __name__ == "__main__":
    main()
