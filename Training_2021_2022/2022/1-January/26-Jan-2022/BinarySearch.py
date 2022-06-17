'''
    Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity.

    

    Example 1:

    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4
    Example 2:

    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1
'''

def binary_search(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        middle = left + (right-left)//2
        if nums[middle]== target:
            return middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            right = middle -1
    return -1


def main():
    nums = [2,3,4,5]
    target = 2
    res = binary_search(nums, target)
    print(res)

main()