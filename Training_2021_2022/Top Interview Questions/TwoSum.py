'''
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    Example 2:

    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    Example 3:

    Input: nums = [3,3], target = 6
    Output: [0,1]
'''

def sol(nums, target):
    # x_number = target - y_number
    hash_table = dict()
    for index, value in enumerate(nums):
        missing_number = target - value
        # if the missing number is contained in the index of the hash table
        if missing_number in hash_table:
            return [index, hash_table[missing_number]]
        else:
            hash_table[value] = index
    return [-1, -1]

def main():
    nums = [3,2,4]
    nums2 = [2,7,11,15]
    target = 9
    res = sol(nums2, target)
    print(res)

main()