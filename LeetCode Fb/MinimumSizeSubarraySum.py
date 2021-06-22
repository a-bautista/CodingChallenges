'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray
of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

'''

class SolutionON:
    def minSubArrayLen(self, s, nums):
        total = left = 0
        result = len(nums) + 1
        for right, n in enumerate(nums):
            total += n
            while total >= s:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        return result if result <= len(nums) else 0

    def solve(self, target, nums):
        total = window_start = 0
        # out of index
        result = len(nums) + 1
        for window_end in range(len(nums)):
            total += nums[window_end]
            while total >= target:
                result = min(result, window_end - window_start + 1)
                total -= nums[window_start]
                window_start +=1
        return result if result <= len(nums) else 0

class SolutionONLogN:
    def minSubArrayLen(self, target, nums):
        result = len(nums) + 1
        # Generate a cumulative sum from index 1 to the end
        # we use a cumulative sum because we want to find those values that are greater
        # than the target, so I can do a binary search only on those values that are greater
        # [2,5,6,8,12,15]
        for idx, val in enumerate(nums[1:], 1):
            nums[idx] = nums[idx - 1] + val
        left = 0

        # start doing a binary search to find the minimum values that are needed to get the target
        for right, val in enumerate(nums):
            if val >= target:
                # find the left pointer that subtracted with the right pointer will give the minimun range values
                left = self.find_left(left, right, nums, target, val)
                # right-left + 1 indicates the minimum range values that are needed to get the target
                result = min(result, right - left + 1)
        return result if result <= len(nums) else 0

    def find_left(self, left, right, nums, target, val):
        while left < right:
            mid = (left + right) // 2
            #mid = left +(right - left) // 2
            # the value is not at the left because val - nums[mid] >= target indicates our value is greater than the target
            if val - nums[mid] >= target:
                left = mid + 1
            else:
                right = mid
        return left


def main():
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    solution = SolutionONLogN()
    solution2 = SolutionON()
    res0 = solution2.solve(s, nums)
    res = solution.minSubArrayLen(s,nums)
    print(res0)

main()
'''
    Time complexity: O(Log(N))
    
'''