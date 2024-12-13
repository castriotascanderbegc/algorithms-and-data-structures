"""
    Q:  You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

        Return the fewest number of coins that you need to make up the exact target amount. If it is impossible to make up the amount, return -1.

        You may assume that you have an unlimited number of each coin.

"""
from typing import List

class CoinChange:
    # Brute Force Approach: Depth First Search - Backtracking
    # Time Complexity: T(n): O(n^t) where n: length of array, t: given amount
    # Space Complexity: S(n): O(t)
    def coinChangeBruteForce(self, coins: List[int], amount: int) -> int:
        def dfs(amount):
            if amount == 0:
                return 0
            
            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            return res

        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins
    

    # Dynamic Programming - Top Down Approach: Memoization
    # Time Complexity: T(n): O(n * t) where n: length of array, t: given amount
    # Space Complexity: S(n): O(t)
    def coinChangeMemoization(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            
            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            
            memo[amount] = res
            return res

        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins


    # Dynamic Programming - Bottom Up Approach: DP
    # Time Complexity: T(n): O(n * t) where n: length of array, t: given amount
    # Space Complexity: S(n): O(t)
    def coinChangeDynamicProgramming(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1

