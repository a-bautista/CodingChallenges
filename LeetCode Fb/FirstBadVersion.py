class Solution:
    def solve(self, n):

        # set the 2 pointers to create the window for binary search
        right = n - 1
        left  = 0

        # start the binary search
        while (left <= right):

            # use the following formula to avoid overflow
            mid = left + (right - left)//2

            # if the bad version is NOT in the middle, then we need to discard
            # all the versions from the left because they contain working versions,
            # not bad versions
            if self.isBadVersion(mid) == False:
                left = mid +1
            # if the bad version is in the middle then we might have the first bad version
            # or maybe it is located before, so discard all the bad versions from the right
            else:
                right = mid -1
        return left

    def isBadVersion(self, mid):
        pass


"""
    Time complexity: O(log(n)) because it is binary search
    Space complexity: O(1)
"""