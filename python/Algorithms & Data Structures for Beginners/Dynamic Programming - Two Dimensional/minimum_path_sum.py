"""
    Q: Minimum Path Sum
    Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
    which minimizes the sum of all numbers along its path.

    Note: You can only move either down or right at any point in time.

"""
from typing import List, Optional


class Solution:
    """
        We could solve it recurively which would take 2^(m + n) 
        in time complexity which is the height of our decision tree.

        An optimization would be to cache the work already been done and accessed it directly from the
        cache (Top-Down approach)

        A better approach is a bottom-up. So starting from the bottom right cell, calculating our
        minimum sum moving all the way up to the top left cell.

        Note: we can optimize our space by only keeping the last row our dp grid as we don't
        necessarily need the entire m * n grid
        
    """
        
    # Time Complexity: T(n) = O(n * m)
    # Space Complexity: S(n) = O(n * m)
    def minPathSum(self, grid: List[List[int]]) -> int:
        # store the dimensions of the grid
        ROWS, COLS = len(grid), len(grid[0])
        
        # intialize our dp grid
        # Note: since we want to minimize our sum we can initilize extra rows with infinity values
        dp = [[float("inf")] * (COLS + 1) for _ in range(ROWS + 1)]

        # set lasw row val to 0
        dp[ROWS - 1][COLS] = 0

        # iterate over the 2D Grid
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                dp[r][c] = grid[r][c] + min(dp[r + 1][c], dp[r][c + 1])
        
        # the value on the top left cell will be our result
        return int(dp[0][0])
