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


def solve(nums, target):
    sol = []

    def backtrack(nextNum, combination, residual):

        # 2 conditions
        if residual == 0:
            sol.append(list(combination))
            return 

        elif residual < 0:
            return 

        for n in range(nextNum, len(nums)):
            combination.append(nums[n])
            backtrack(n, combination, residual-nums[n])
            combination.pop()

    backtrack(0, [], target)
    return sol


def main():
    nums = [1,2,3] 
    target = 5
    res = solve(nums, target)
    print(res)

main()

'''
    nums = [1,2,3]
    target = [5]

    [1,1,1,1,1] when you have a success move one level back
    [1,1,1,2]
    [1,2,2]
    [2,3]
'''