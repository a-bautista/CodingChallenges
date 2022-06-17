'''
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1]
'''
def solve(nums, target):
    left = 0
    right = len(nums)-1

    while left<=right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        if current_sum < target:
            left +=1
        else:
            right-=1 

def main():
    nums = [2, 7, 11, 15] 
    target = 9
    res = solve(nums, target)
    print(res)

main()