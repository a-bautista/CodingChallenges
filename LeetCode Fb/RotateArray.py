'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
 
Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

'''

# solution 1

#formula:
#(i+k) % n 

class Solution:
    def solve(self, nums, k):
        #(i+k) % n 
        n = len(nums)
        a = [0]*n

        for i in range(n):
            a[(i+k)%n] = nums[i]
        nums[:] = a

'''
    Time complexity: O(N)
    Space complexity: O(N)
'''


# solution 2
class Solution2:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
    
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

'''
    Time complexity: O(N)
    Space complexity: O(1)

'''
        