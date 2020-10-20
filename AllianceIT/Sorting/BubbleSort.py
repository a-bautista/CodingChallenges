from random import randrange

def bubble_sort(nums):
    for n in range(len(nums)-1, 0, -1):
        for k in range(n):
            if nums[k] > nums[k+1]:
                nums[k], nums[k+1] = nums[k+1], nums[k]
    return nums

def main():
    res = bubble_sort([randrange(0,10000) for _ in range(10)])
    print(res)

main()