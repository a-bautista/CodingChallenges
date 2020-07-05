from typing import List

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        len_n = len(nums)
        missing = (nums[-1] - nums[0] + 1) - len_n
        if k > missing:
            return nums[-1] + k - missing

        # Now the first missing number must be inside nums.
        last, left, right = 0, 0, len_n - 1
        while left <= right:
            mid = left + (right - left) // 2
            missing = nums[mid] - nums[last] + 1 - (mid - last + 1)
            if k > missing:
                last = mid
                k -= missing
                left = mid + 1
            else:
                right = mid - 1
        return nums[last] + k

'''
    Time complexity: O(Log(N))
    Space complexity: O(1)
'''