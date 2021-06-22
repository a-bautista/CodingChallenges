'''
    Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

    Only numbers 1 through 9 are used.
    Each number is used at most once.

    Return a list of all possible valid combinations. The list must not contain the same combination twice, and the
    combinations may be returned in any order.

    Example 1:

    Input: k = 3, n = 7
    Output: [[1,2,4]]
    Explanation:
    1 + 2 + 4 = 7
    There are no other valid combinations.

    Example 2:

    Input: k = 3, n = 9
    Output: [[1,2,6],[1,3,5],[2,3,4]]
    Explanation:
    1 + 2 + 6 = 9
    1 + 3 + 5 = 9
    2 + 3 + 4 = 9
    There are no other valid combinations.

    Example 3:

    Input: k = 4, n = 1
    Output: []
    Explanation: There are no valid combinations. [1,2,1] is not valid because 1 is used twice.

    Solution: You need to set a remainder to indicate how far are you from the target or if the list
    of results is equal to the initial capacity. Every time you try a new number, decrease the number
    by the current number you have and -1 (to count the 0) and try if the current combination is equal
    to the len of capacity or if your target has become 0 (so this indicates you have reached the target).
'''


class Solution:
    def solve(self, capacity, target):
        results = []
        def backtrack(remain, combination, next_start):
            # if you found the combination is equal to num_values
            # or if the remainder == 0, then append the results
            if remain == 0 and len(combination)==capacity:
                results.append(list(combination))
                return

            # if you have reached the combination == to the num_values
            # or if the remainder is less than 0, then go out from the
            # backtrack
            elif remain < 0 or len(combination)==capacity:
                return

            # try the combinations of all numbers from 0 to 9
            # and do a backtrack for each of it
            for i in range(next_start, 9):
                # i+1 indicates to include the 1 because the range doesn't touch it
                combination.append(i+1)
                # i+1 indicates to add the 1
                # remain-i-1 indicates to include the 0
                backtrack(remain-i-1, combination, i+1)
                # if the combination didn't work the pop it
                combination.pop()
        backtrack(target, [], 0)
        return results

def main():
    capacity = 1
    target = 9
    solution = Solution()
    res = solution.solve(capacity,target)
    print(res)

main()


'''
    Time complexity: O! because you are adding a loop for each new number
    Space complexity: O(N)
    
'''