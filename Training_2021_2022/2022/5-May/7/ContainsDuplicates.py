'''
    Given an integer array nums, return true if any value appears at least twice in the array,
    and return false if every element is distinct.

    Example 1:

    Input: nums = [1,2,3,1]
    Output: true
    Example 2:

    Input: nums = [1,2,3,4]
    Output: false
    Example 3:

    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true
'''
from collections import Counter
def containsDuplicate(nums):
    count = Counter(nums)
    for _, val in enumerate(count):
        # print(val, count[val])
        if count[val] > 1:
            return True
    return False

def main():
    nums = [1,2,3,4]
    sol = containsDuplicate(nums)
    print(sol)

main()