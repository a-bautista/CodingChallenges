from random import randrange
from copy import deepcopy

def insertion_sort(nums):
    deep_copy = deepcopy(nums)
    print(deep_copy)

    for i in range(1, len(nums)):
        current_val = nums[i]
        position = i

        while position > 0 and nums[position-1]>current_val:
            nums[position] = nums[position-1]
            position = position -1

        nums[position] = current_val

    return nums

def main():
    nums = [randrange(0,1000) for _ in range(0,6)]
    nums2 = [583, 752, 700, 713, 519, 743]
    res = insertion_sort(nums2)
    print(res)

main()