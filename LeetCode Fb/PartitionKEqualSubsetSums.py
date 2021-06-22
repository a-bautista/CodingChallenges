'''
Given an array of integers nums and a positive integer k,
find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Note:

    1 <= k <= len(nums) <= 16.
    0 < nums[i] < 10000.


when k == 1, which means you already found k - 1 subsets with target sum. The remaining last group surely contains target sum.
'''


class Solution:
    def canPartitionKSubsets(self, nums, k):

        # edge cases
        if k ==1:
            return True

        if len(nums) < k:
            return False

        ASum = sum(nums)
        # reverse the nums, so you can go from left to right
        # instead of doing the right to left original approach
        nums.sort(reverse=True)
        if ASum % k != 0:
            return False

        # create the buckets that we need to fill
        # determine the target that needs to be filled in each bucket
        # [5.0,5.0,5.0, 5.0] in case k= 4 and the sum of the array is 20
        # it is possible that the buckets can have different weights, [20 30, 30]
        target = [ASum / k] * k

        # I need to fill in the k buckets with the target
        def dfs(pos):
            # when you have traversed all the numbers in the vector
            # and all the buckets then stop the recursion
            if pos == len(nums): return True
            # iterate through each bucket to check if we do not overexceed the value in the buckets
            for i in range(k):
                # if the current amount in bucket is greater than the value in A
                # then decrease the amount in the current bucket
                if target[i] >= nums[pos]:
                    # decrease the amount in the current bucket
                    target[i] -= nums[pos]
                    # move onto the next value in the A vector of values, to
                    # verify if we can continue decreasing the amounts in the buckets
                    if dfs(pos + 1):
                        return True
                    # refill the bucket in case the combination of numbers from A have not
                    # make all the buckets to become 0. The refill is made with current value in A[pos]
                    target[i] += nums[pos]
            return False
        # start with the base case 0
        return dfs(0)

def main():
    nums = [10,10,10,7,7,7,7,7,7,6,6,6]
    k = 3
    solution = Solution()
    res = solution.canPartitionKSubsets(nums, k)
    print(res)

main()