class Solution:
    def rob(self, nums):
        prev_max = 0
        curr_max = 0
        for x in nums:
            temp = curr_max
            curr_max = max(prev_max+x, curr_max)
            prev_max = temp
        return curr_max