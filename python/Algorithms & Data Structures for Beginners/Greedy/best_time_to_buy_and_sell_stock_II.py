"""
    Q: Best Time to Buy and Sell Stock II
    You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

    On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the
    stock at any time. However, you can buy it then immediately sell it on the same day.

    Find and return the maximum profit you can achieve.
"""

from typing import List


class Solution:
    """
        We can utilize a Greedy approach where we only consider cases where pricing are stricly increasing.
        Differently, we ignore such cases were prices decrease. 

    """
    # Time Complexity: T(n) = O(n)
    # Space Complexity: S(n) = O(1)
    def maxProfit(self, prices: List[int]) -> int:
        # initialize our total profit
        profit = 0
        # move through the given prices
        for i in range(len(prices) - 1):
            # if prices are increasing, add the current profit to our total profit
            if prices[i + 1] > prices[i]:
                profit += (prices[i + 1] - prices[i])
        # return the total profit made
        return profit