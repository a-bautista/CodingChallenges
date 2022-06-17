'''
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    time complexity = O(n)
    space complexity = O(n)

    hash_table = dict()
    for index, value in enumerate(nums):
        complement = target - value
        if complement in hash_table:
            return [hash_table[complement], index]
        else:
            hash_table[value] = index

'''

def twoSum(nums, target):
    hash_table = dict()
    for index, value in enumerate(nums):
        complement = target - value
        if complement in hash_table:
            return [hash_table[complement], index]
        else:
            hash_table[value] = index

def main():
    nums = [2,7,11,15]
    target = 9
    sol = twoSum(nums, target)
    print(sol)

main()