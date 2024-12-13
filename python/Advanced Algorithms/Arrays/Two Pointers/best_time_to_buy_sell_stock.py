"""
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


class Solution:
    # Two Pointers - Linear Time Solution - O(n)
    # make a single pass on the array with 2 pointers
    def maxProfit(self, prices: list[int]) -> int:
        # L = buy, R = sell

        L = 0           # initialize our left pointer
        maxProfit = 0   # initialize max profit

        # move through the array of prices with both pointers
        # make a single pass through the array once
        for R in range(1, len(prices)):
            # check if the transaction is profitable 
            if prices[L] < prices[R]:
                # calculate current profit
                currProfit = prices[R] - prices[L]
                # update maximun profit so far
                maxProfit = max(maxProfit, currProfit)
            else:
                # shift L pointer directly to where R currently is
                L = R

        # return maximum profit if any
        return maxProfit
