"""
    Q: Given two strings s1 and s2, find the length of the longest common subsequence between the two strings.

"""

from typing import List


class LongestCommonSubsequence:

    # Brute Foce Solution
    # Time Complexity: T(n): O(2^(n + m))
    # Space Complexity: S(n): O(n + m)
    def dfs(self, s1: str, s2: str) -> int:
        return self.dfsHelper(s1, s2, 0, 0)

    def dfsHelper(self, s1: str, s2: str, i1: int, i2: int) -> int:
        # base case
        # if either pointer goes out of bound, we return 0
        if i1 == len(s1) or i2 == len(s2):
            return 0

        # if the characters match
        if s1[i1] == s2[i2]:
            return 1 + self.dfsHelper(s1, s2, i1 + 1, i2 + 1)

        # if the characters don't match
        else:
            return max(self.dfsHelper(s1, s2, i1 + 1, i2),
                       self.dfsHelper(s1, s2, i1, i2 + 1))
        

    # Memoization
    # Time Complexity: T(n): O(n • m)
    # Space Complexity: S(n): O(n + m)
    def memoization(self, s1: str, s2: str) -> int:
        N, M = len(s1), len(s2)
        cache = [[-1] * M for _ in range(N)]
        return self.memoHelper(s1, s2, 0, 0, cache)
    
    def memoHelper(self, s1: str, s2: str, i1: int, i2: int, cache: List[List[int]]) -> int:
        # if either pointer goes out of bound, we return 0
        if i1 == len(s1) or i2 == len(s2):
            return 0
        # if we already computed the restult at i1, i2
        # return it from cache
        if cache[i1][i2] != -1:
            return cache[i1][i2]
        
        # if the characters match
        if s1[i1] == s2[i2]: 
            cache[i1][i2] = 1 + self.memoHelper(s1, s2, i1 + 1, i2 + 1, cache)
        
        # if the characters don't match
        else:
            cache[i1][i2] = max(self.memoHelper(s1, s2, i1 + 1, i2, cache), 
                                self.memoHelper(s1, s2, i1, i2 + 1, cache))

        return cache[i1][i2]


    # Dynamic Programming Solution
    # Bottom-Up approach
    # Time Complexity: T(n): O(n • m)
    # Space Complexity: S(n): O(n + m)
    def dp(self, s1: str, s2: str) -> int:
        N, M = len(s1), len(s2)
        # initialize our grid
        # we need one extra row and column, so if we need to look diagonally up we won't go out of bounds
        dp = [[0] * (M + 1) for _ in range(N + 1)]

        # traverse the rows, i.e. chars of s1
        for i in range(N):
            # traverse the cols, i.e. chars of s2
            for j in range(M):
                # if same char
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    # if chars are different
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])


        # our result will be in bottom right corner of the grid
        return dp[N][M]


    # Optimized Dynamic Programming Solution
    # Bottom-Up approach
    # Time Complexity: T(n): O(n • m)
    # Space Complexity: S(n): O(m)

    def optimizedDp(self, s1: str, s2: str) -> int:
        N, M = len(s1), len(s2)
        dp = [0] * (M + 1)              # we don't necessarily need entire 2D grid in memory, we only really need 2 rows at a time

        for i in range(N):
            currRow = [0] * (M + 1)     # initialize row to compute the values using previous row
            for j in range(M):
                # if characters are the same
                if s1[i] == s2[j]:
                    currRow[j + 1] = 1 + dp[j]
                else:
                    # if characters are different
                    currRow[j + 1] = max(dp[j + 1], currRow[j])
            
            dp = currRow
    
        return dp[M]