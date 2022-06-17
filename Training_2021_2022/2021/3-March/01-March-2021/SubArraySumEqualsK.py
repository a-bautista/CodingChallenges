# def solve(nums, target):
#     count = 0
#     start_window = 0
#     running_sum = 0
#
#     for end_window in range(len(nums)):
#         if start_window!=0:
#             running_sum+= nums[start_window] + nums[end_window]
#         else:
#             running_sum += nums[end_window]
#         if running_sum == target or nums[end_window]==target:
#             count+=1
#             start_window = end_window
#             running_sum =0
#     return count if count!=0 else 0
#
# def main():
#     nums1 = [1,1,1,1]
#     target1 = 2
#     nums2 = [1,2,3,5]
#     target2 = 11
#     nums3 = [-1,-1,1]
#     target3= 0
#     #res1 = solve(nums1, target1)
#     #res2 = solve(nums2, target2)
#     res3 = solve(nums3, target3)
#     print(res3)
#
# main()

"""
    Given an array of integers and an integer k, you need to find the total number of continuous subarrays
    whose sum equals to k.

    Example 1:
    Input:nums = [1,1,1], k = 2
    Output: 2

    The length of the array is in range [1, 20,000].
    The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

"""
        The get() method takes maximum of two parameters:

        key - key to be searched in the dictionary
        value (optional) - Value to be returned if the key is not found. The default value is None.
"""

from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        running_sum = 0
        #hash_table = defaultdict(int)
        hash_table = dict()
        total = 0
        for x in nums:
            running_sum += x
            # k is the target to find, so verify if the running_sum - k
            # is a value already stored in our hash table and if so, then we find our next value
            sum = running_sum - k
            if sum in hash_table:
                total += hash_table[sum]
            if running_sum == k:
                total += 1
            if running_sum not in hash_table:
                hash_table[running_sum] =0
            hash_table[running_sum] += 1
        return total


def main():
    nums = [1, 1, 1, 1]
    k = 2
    solution = Solution()
    res = solution.subarraySum(nums, k)
    print(res)


main()

"""
    You can visualize the problem as:

                    - target sum -
                    |             |
                    |             |
    -------------------------------
    s               x             y


    ------- running sum y --------

    - running sum x - target sum -
    |               |             |
    |               |             |
    -------------------------------
    s               x             y


    Time complexity: O(N)
    Space complexity: 
"""