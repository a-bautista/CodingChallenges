'''
    Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations
    of candidates where the chosen numbers sum to target. You may return the combinations in any order.

    The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
    frequency of at least one of the chosen numbers is different.

    It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for
    the given input.

    Example 1:
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
    2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    7 is a candidate, and 7 = 7.
    These are the only two combinations.

    Example 2:
    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]

    Solution:
    Very similar to the CombinationSum_v3 but instead of checking if the combination is already equal to
    capacity, we just check if the remainder is equal to 0. In the backtrack, this time we don't decrease the
    number with -1 because we were provided a list of numbers, so use the current number and the current combination
    and where you should start in the next loop call.
'''


class Solution:
    def combinationSum(self, candidates, target):
        results = []

        def backtrack(remain, combination, next_start):
            # append the results when you have found a combination which is equal to the target
            if remain == 0:
                results.append(list(combination))
                return
            # the remainder <0 indicates that the current combination won't work, we need to drop the
            # current number
            elif remain < 0:
                return

            for i in range(next_start, (len(candidates))):
                # append the current number from the candidates list and use it to evaluate if
                # this is going to work
                combination.append(candidates[i])
                # evaluate if the current number will work by decreasing the remainder to see if
                # it is equal to 0 (in case it works) wit the current combination and the current number
                backtrack(remain - candidates[i], combination, i)
                # drop the number in case the number doesn't work
                combination.pop()

        backtrack(target, [], 0)
        return results

def main():
    nums = [1,2,3]
    target = 6
    solution = Solution()
    res = solution.combinationSum(nums, target)
    print(res)

main()

'''
    Time complexity: O! because you are adding a loop for each new candidate
    Space complexity: O(N)
'''