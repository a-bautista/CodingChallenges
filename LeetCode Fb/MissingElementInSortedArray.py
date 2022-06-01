'''

the formula to calculate the missing element is = (nums[-1]-nums[0]+1)

'''

from typing import List

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        len_n = len(nums)
        missing = (nums[-1] - nums[0] + 1) - len_n
        # if k is greater than missing then we can find the missing number with the formula from below
        if k > missing:
            return nums[-1] + k - missing

        # Now the first missing number must be inside nums.
        last, left, right = 0, 0, len_n - 1
        while left <= right:
            mid = left + (right - left) // 2
            
            # you calculate the missing numbers from the internal array
            missing = nums[mid] - nums[last] + 1 - (mid - last + 1)

            # if the internal array contains less missing numbers than the kth index number
            if k > missing:
                last = mid
                # discount the missing numbers from the internal array
                k -= missing
                left = mid + 1
            else:
                right = mid - 1
        
        return nums[last] + k


def main():
    # nums = [4,6,7,8]
    nums = [2,3,4,7,11]
    k = 5
    solution = Solution()
    re = solution.missingElement(nums, k)
    print(re)

main()

'''
    Time complexity: O(Log(N))
    Space complexity: O(1)
'''