'''
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times. 
    You may assume that the majority element always exists in the array.

    Example 1:

    Input: nums = [3,2,3]
    Output: 3

    Example 2:

    Input: nums = [2,2,1,1,1,2,2]
    Output: 2
'''

from collections import Counter
class Solution:
    def majorityElement(self, nums) -> int:
        count = Counter(nums)
        keys = list(count.keys())
        values = list(count.values())
        
        max_val = float('-inf')
        for i, value in count.items():
            max_val = max(max_val, value)
        # I want to return the key based on the value of the dictionary
        # given the value of the dictionary, return the key
        #print(keys[values.index(max_val)])
        return keys[values.index(max_val)]

def main():
    nums = [2,2,1,1,1,2,2]
    solution = Solution()
    res = solution.majorityElement(nums)
    print(res)

main()