
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        map = {}
        for i in nums1:
            map[i] = map[i] + 1 if i in map else 1
        for j in nums2:
            if j in map and map[j] > 0:
                res.append(j)
                map[j] = 0
        return res


def main():
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    solution = Solution()
    res = solution.intersection(nums1, nums2)
    print(res)


main()