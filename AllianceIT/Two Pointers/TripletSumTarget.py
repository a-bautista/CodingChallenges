'''
    Given an array of unsorted numbers and a target number, find a triplet
    in the array whose sum is as close to the target number as possible,
    return the sum of the triplet. If there are more than one such triplet,
    return the sum of the triplet with the smallest sum.
'''

import math
# def solve(arr, target_sum):
#     arr.sort()
#     smallest_difference = math.inf
#     for i in range(len(arr) - 2):
#         left = i + 1
#         right = len(arr) - 1
#         while (left < right):
#             target_diff = target_sum - arr[i] - arr[left] - arr[right]
#             if target_diff == 0:  # we've found a triplet with an exact sum
#                 return target_sum - target_diff  # return sum of all the numbers
#
#             # the second part of the following 'if' is to handle the smallest sum when we have more than one solution
#             if abs(target_diff) < abs(smallest_difference) or \
#               (abs(target_diff) == abs(smallest_difference) and target_diff > smallest_difference):
#                 smallest_difference = target_diff  # save the closest and the biggest difference
#
#             if target_diff > 0:
#                 left += 1  # we need a triplet with a bigger sum
#             else:
#                 right -= 1  # we need a triplet with a smaller sum
#     return target_sum - smallest_difference

def solve2(nums, target):
    nums.sort()
    res = math.inf
    for i in range(len(nums)-2):
        right = len(nums)-1
        left = i+1
        while left < right:
            c_sum = nums[i]+nums[left]+nums[right]
            if c_sum == target:
                return c_sum
            if c_sum > target:
                res = min(c_sum-target, res)
                right-=1
            if c_sum < target:
                res = min(abs(c_sum-target), res)
                left+=1
    return target-res

def main():
    l = [-2, 0, 1, 2]
    res = solve2(l, 2)
    print(res)

main()