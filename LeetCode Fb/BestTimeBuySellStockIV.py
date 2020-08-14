'''

Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

'''

class Solution:
    def maxProfit(self, k: int, prices) -> int:

        # solve special cases
        if not prices or k == 0:
            return 0

        n = len(prices)

        # first case: we can trade as much as we can because k>=n//2
        # so if we have 10 items then the max number of transactions I can do is 5
        # buy and sell
        if k >= n // 2:  # problem 122. Best Time to Buy and Sell Stock II
            max_profit = 0
            for i in range(n - 1):
                max_profit += max(prices[i + 1] - prices[i], 0)
            return max_profit

        globalMax = [[0] * n for _ in range(k + 1)]
        for i in range(1, k + 1):
            # The max profit with i transations and selling stock on day j.
            localMax = [0] * n
            for j in range(1, n):
                profit = prices[j] - prices[j - 1]
                localMax[j] = max(
                    # We have made max profit with (i - 1) transations in
                    # (j - 1) days.
                    # For the last transation, we buy stock on day (j - 1)
                    # and sell it on day j.
                    globalMax[i - 1][j - 1] + profit,
                    # We have made max profit with (i - 1) transations in
                    # (j - 1) days.
                    # For the last transation, we buy stock on day j and
                    # sell it on the same day, so we have 0 profit, apparently
                    # we do not have to add it.
                    globalMax[i - 1][j - 1],  # + 0,
                    # We have made profit in (j - 1) days.
                    # We want to cancel the day (j - 1) sale and sell it on
                    # day j.
                    localMax[j - 1] + profit)
                globalMax[i][j] = max(globalMax[i][j - 1], localMax[j])
        return globalMax[k][-1]

        # second case: we cannot trade that much so create the following structure for storing the results
        # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        # dp = [[0 for _ in range(k + 1)] for _ in range(n)]
        # # for number of transactions starting from 1 to k+1, i.e., k=2 then k1 = 1 and stop in k=3
        # for k1 in range(1, k + 1):
        #     # take the first price in the transactions
        #     local_max = -prices[0]
        #
        #     for i in range(1, n):
        #         # dp[i - 1][k1] means the value in the previous array,
        #         # prices[i] + local_max takes the current price[i] and add it to the local_max
        #         # assign to dp[i][k1] the current max val between the previous and the current price + local max
        #         # buy the previous value
        #         dp[i][k1] = max(dp[i - 1][k1], prices[i] + local_max)
        #         # local max is used to get the result which will be stored at the very end of the list structure
        #         local_max = max(local_max, dp[i - 1][k1 - 1] - prices[i])
        #
        # # return the last element from the last list because we store the result on it
        # return dp[n - 1][k]


def main():
    nums =  [3, 2, 6, 5, 0, 3]
    k = 2
    solution = Solution()
    res = solution.maxProfit(k, nums)
    print(res)


main()
'''
    Time complexity: O(kn).
    Space Complexity: O(kn) 
'''