'''
Given a set of distinct integers, nums, return all possible
subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''


class Solution:
    # def subsets(self, nums):
    #     def backtrack(first=0, curr=[]):
    #         # if the combination is done
    #         if len(curr) == k:
    #             output.append(curr[:])
    #         for i in range(first, n):
    #             # add nums[i] into the current combination
    #             curr.append(nums[i])
    #             # use next integers to complete the combination
    #             backtrack(i + 1, curr)
    #             # backtrack
    #             curr.pop()
    #
    #     output = []
    #     n = len(nums)
    #     for k in range(n + 1):
    #         backtrack()
    #     return output
    def find_subsets(self, nums):
        subsets = []
        # start by adding the empty subset to the general list that holds all the subsets
        subsets.append([])
        # take the current number from the array
        for currentNumber in nums:

            n = len(subsets)
            # from the current len of the subset, add the current number to each element of the subset
            for i in range(n):
                # create a new subset from the existing subset and insert the current element to it
                set = list(subsets[i])
                set.append(currentNumber)
                # append the subset to the general list
                subsets.append(set)

        return subsets

def main():
    solution = Solution()
    res = solution.find_subsets([1,3,5])
    print(res)

main()

'''
    The solution follows a BFS approach.

    Time complexity: O(2**N) where N is the total number of elements in the input set.
    Space complexity: O(2**N) to keep all the subsets of length N, since each of NNN elements could be present or absent. 
'''