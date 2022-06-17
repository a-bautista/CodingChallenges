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

    1. This is with backtrack, create a res list to store all the numbers that will add up to the target value. 
    2. Use the target value and decrease it with the current value of the list of numbers and verify 3 conditions: 
        There are 3 conditions: 
        1. if the current target has reached 0 then add the entire combination of numbers.
        2. else if the current target has reached a value < 0 then return empty
        3. else do a dfs to add the next number
        

    def solve(nums, target):
        res = []

        def backtrack(residual, combination, nextNumber):
            if residual == 0:
                # you must use the list keyword, otherwise it will fail
                res.append(list(combination))
            elif residual < 0:
                return 
            else:
                for current in range(nextNumber, len(nums)):
                    combination.append(nums[current])
                    backtrack(residual - nums[current], combination, current)
                    #backtrack
                    combination.pop()

        dfs(target, [], 0)
        return res

    [2,2,3] target= 8

'''


def solve(nums, target):
    res = []

    def dfs(residual, combination, nextNumber):
        if residual == 0:
            res.append(list(combination))
        elif residual <0:
            return
        else:
            for current in range(nextNumber, len(nums)):
                # append the current combination
                combination.append(nums[current])
                dfs(residual-nums[current], combination, current)
                # backtrack
                del combination[-1]
    
    dfs(target, [], 0)
    return res 


def main():
    candidates = [2,3,5] # prime numbers
    target = 13
    #solution = Solution()
    res = solve(candidates, target)
    print(res)

main()
    