'''

    Say you have an array for which the ith element is the price of a given stock on day i.

    If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

    Note that you cannot sell a stock before you buy one.

    Example 1:

    Input: [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                 Not 7-1 = 6, as selling price needs to be larger than buying price.

'''


class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        min_price_so_far = float('inf')

        for current_price in prices:
            # store the min price from all stocks
            min_price_so_far = min(current_price, min_price_so_far)

            # subtract the current price - lowest price that you have found
            best_possible_profit_if_sold_now = current_price - min_price_so_far

            # store the max profit if the best possible profit is greater than the current max profit
            max_profit = max(best_possible_profit_if_sold_now, max_profit)

        return max_profit


def main():
    stocks = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    res = solution.maxProfit(stocks)
    print(res)

main()