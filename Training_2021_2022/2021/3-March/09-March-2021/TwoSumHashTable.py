'''
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1]
'''

def solve(nums, target):
    hashTable = {}
    for i, price in enumerate(nums):
        current = target - price
        hashTable[price] = i
        if current in hashTable:
            return [hashTable[current],i]

def main():
    nums = [25, 7, 8, 10]
    target = 15
    nums = solve(nums, target)
    print(nums)

main()