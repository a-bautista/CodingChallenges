

'''
    Given non-decreasing array and a value k return the number of occurences of k in the array

    Your algorithm's runtime complexity must be in the order of O(log n).

    array: [1, 2, 3, 3, 8]
    k: 3
    output: 2


'''
class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, lookLeftIndex):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > target or (lookLeftIndex and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1

        return lo


    def searchRange(self, nums, target):
        # first look for the left index
        left_idx = self.extreme_insertion_index(nums, target, True)

        # If the left index didn't find the target value then just return -1
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1]

        # look for the right index and when found, don't forget to subtract -1 to stay
        # in the bounds of the array
        res = [left_idx, self.extreme_insertion_index(nums, target, False)-1]
        # count the number of elements in the result, so that's going to indicate the number of times the target appeared
        return len(set(res))

def main():
    nums = [[1, 2, 3, 3, 8]]
    target = 3
    nums2 = [1,2,5,5,5,9]
    target2 = 9
    solution = Solution()
    res = solution.searchRange(nums2, target2)
    print(res)

main()

'''
    Time complexity: O(Log(N))
    Space complexity: O(1)
'''