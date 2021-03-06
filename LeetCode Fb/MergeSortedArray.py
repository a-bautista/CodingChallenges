"""
    Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

    Note:

        The number of elements initialized in nums1 and nums2 are m and n respectively.
        You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

    Example:

    Input:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6],       n = 3

    Output: [1,2,2,3,5,6]

"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # Make a copy of nums1.
        nums1_copy = nums1[:m]
        nums1[:] = []

        # Two get pointers for nums1_copy and nums2.
        p1 = 0
        p2 = 0

        # Compare elements from nums1_copy and nums2
        # and add the smallest one into nums1.
        while p1 < m and p2 < n:
            # if elements of nums1_copy are less than elements of nums2,
            # then add each element of nums1_copy to nums1.
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            # if an element of nums2 is greater than an element of nums1
            # then add it to nums1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        # if there are still elements to add
        if p1 < m:
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]
        return nums1


def main():

    nums1 = [0, 1]
    nums2 = [0, 0, 0]
    p = 2
    q = 3

    solution = Solution()
    res = solution.merge(nums1, p, nums2, q)
    print(res)

main()


"""
    Complexity Analysis
        Time complexity : O(n+m).
        Space complexity : O(m). 
"""