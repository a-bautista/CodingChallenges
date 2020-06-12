"""
    Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

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
        hash_table = defaultdict(int)
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
            hash_table[running_sum] += 1
        return total

def main():
    nums = [1, 2, 1, 3]
    k = 3
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