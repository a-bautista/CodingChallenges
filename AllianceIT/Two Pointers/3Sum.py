
"""
    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
    Find all unique triplets in the array which gives the sum of zero.

    Note:

    The solution set must not contain duplicate triplets.

    Example:

    Given array nums = [-1, 0, 1, 2, -1, -4],

    A solution set is:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]

    [-1, 0, 1, 2, -1, -4]
      ^     ^          ^

      nums.sort()
      iterate through the array
        apply a left and right pointers to find out if the sum of the
        res = []
        3 elements is equal to 0
            c_sum < 0:
                left +=1
            c_sum > 0:
                right -=1
            c_sum == target:
                store the values in an array
                # do not show the accounted values
                while l<r and array[left]==array[left+1]
                    l+=1
                while l<r and array[right]==array[right-1]
                    r-=1
                left+=1
                right-=1
"""

def solve(nums):
    nums.sort()
    res = []
    for i in range(len(nums)-2):

        # Avoid repeated values that you have accounted for
        if i >0 and nums[i]==nums[i-1]:
            continue

        left = i+1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i]+nums[left]+nums[right]
            if current_sum < 0:
                left +=1
            elif current_sum > 0:
                right -=1
            elif current_sum == 0:
                res.append((nums[i], nums[left], nums[right]))
                while left<right and nums[left]==nums[left+1]:
                    left+=1
                while left<right and nums[right]==nums[right-1]:
                    right-=1
                left +=1
                right-=1
    return res


def main():
    l = [-1, 0, 1, 2, -1, -4]
    l2 =  [2,-1,-1,2,-1,-1]
    res = solve(l2)
    print(res)

main()