'''
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

    You must implement a solution with a linear runtime complexity and use only constant extra space.

    Example 1:

    Input: nums = [2,2,1]
    Output: 1
    Example 2:

    Input: nums = [4,1,2,1,2]
    Output: 4
    Example 3:

    Input: nums = [1]
    Output: 1

    Time complexity: O(N)
    Space complexity: O(N)

    -----------------------------------------------------------------------------------------------------

    Solution 2: Bit manipulation
    
    [1,2,2]
    a = 0
    i = 1
    then a 1

    a=2
    i =2
    then a =0 because xor

    a = 0
    i = 2
    then 

    
    Time complexity: O(N)
    Space complexity: O(1)

'''
from collections import Counter
def singleNumber(nums):
    count = Counter(nums)
    for _, val in enumerate(count):
        if count[val] == 1:
            return val

def bit_manipulation(nums):
    a = 0
    for i in nums:
        a ^= i
    return a

def main():
    nums = [4,1,2,1,2]
    sol = singleNumber(nums)
    sol2 = bit_manipulation(nums)
    print(sol)
    print(sol2)

main()