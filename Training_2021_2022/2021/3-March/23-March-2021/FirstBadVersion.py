class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n - 1
        while left<=right:
            mid = left + (right - left)//2
            # if the bad version is NOT in the middle, then we need to discard
            # all the versions from the left because they contain working versions,
            # not bad versions
            if isBadVersion(mid) is False:
                left = mid + 1
            # I found the bad version in the middle but I don't know if this one is the first one, 
            # so I need to keep looking
            else: 
                right = mid - 1
        return left

"""
    Time complexity: O(log(n)) because it is binary search
    Space complexity: O(1)
"""