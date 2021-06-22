'''
Given an unsorted array of integers, find the length of the longest
consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is
[1, 2, 3, 4]. Therefore its length is 4.

# edge cases:
    []
    [0,1]
    [0,1,1,2]

# solutions to edge cases
    if not nums return 0
    max(max_count,count) if count!=1  else -1
    if nums[i]!=nums[i-1]

'''

class Solution:
    def solve(self, nums):

        # #edge case
        # if not nums:
        #     return 0
        #
        # nums.sort()
        # count = max_count = 1
        #
        # for i in range(1, len(nums)):
        #     # edge case: [0,1,1,2]
        #     if nums[i]!=nums[i-1]:
        #         # compare if the current number is equal to the previous one
        #         if nums[i]==nums[i-1]+1:
        #             count +=1
        #         else:
        #             max_count = max(max_count, count)
        #             count = 1
        # # I use the max() again to avoid the edge case [-1,0]
        # return max(max_count,count) if count!=1  else -1

        if not nums:
            return 0

        hash_set = set(nums)

        max_count = float('-inf')
        for num in hash_set:
            curr_num = num
            count = 1
            while curr_num + 1 in hash_set:
                count +=1
                curr_num +=1
            max_count = max(max_count, count)
        return max_count



def main():
    nums = [9,1,4,7,3,-1,0,5,8,-1,6]
    nums2 = [5,3,3,0,1,2,2]
    nums3 = [100, 1, 2, 3, 99]
    solution = Solution()
    res = solution.solve(nums3)
    print(res)

main()

'''
    Time complexity: n*log(N) with sorting. O(N) without sorting
    
'''