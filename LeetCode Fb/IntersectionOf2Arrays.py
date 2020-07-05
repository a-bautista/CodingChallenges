'''
    Given two arrays, write a function to compute their intersection.

    Example 1:

    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]

    Example 2:

    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [9,4]
'''


# basic solution
# time complexity: O(M+N) where M is the length of the nums1 array and
# N is the length of the nums2 array
# space complexity: O(M+N)
# This algorithm first considers nums1 < nums2.
# We create a hashmap to count the number of times each value appears.

from collections import Counter
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        map = Counter(nums1)
        #for i in nums1:
        #    map[i] = map[i] + 1 if i in map else 1
        for j in nums2:
            if j in map and map[j] > 0:
                res.append(j)
                map[j] = 0
        return res

# Time complexity: O(N) if the arrays are sorted, else O(N*Log(N)+M*Log(M))
# Space complexity: O(1) for both cases
class Solution2:
    def intersection(self, nums1, nums2):
        res = []
        # we use the
        nums1.sort() # assume the array is sorted
        nums2.sort() # assume the array is sorted

        left = right = 0
        while left < len(nums1) and right < len(nums2):
            if nums1[left] == nums2[right]:
                res.append(nums1[left])
                left  +=1
                right +=1
            elif nums1[left] < nums2[right]:
                left +=1
            else:
                right += 1
        return res




def main():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    sol = Solution()
    ans = sol.intersection(nums1, nums2)
    print(ans)

    # second approach
    nums3 = [4,9,5,4]
    nums4 = [9,4,9,8,4,7]
    nums3.sort()
    nums4.sort()
    solution = Solution2()
    res = solution.intersection(nums3, nums4)
    print(res)


main()