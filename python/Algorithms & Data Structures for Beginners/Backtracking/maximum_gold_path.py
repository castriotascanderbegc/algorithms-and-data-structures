"""
    Q: Path with Maximum Gold

    In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

    Return the maximum amount of gold you can collect under the conditions:

        Every time you are located in a cell you will collect all the gold in that cell.
        From your position, you can walk one step to the left, right, up, or down.
        You can't visit the same cell more than once.
        Never visit a cell with 0 gold.
        You can start and stop collecting gold from any position in the grid that has some gold.

"""


from typing import List


class Solution:
    """
        The idea here is to backtrack from each cell that has gold and find the maximum gold path using DFS.
        We will use a set to keep track of the visited cells.
        We will iterate through the grid and if the cell has gold, then we will backtrack from that cell to find the maximum gold path.
        We will update the result with the maximum gold path.
        We will return the result.
    
    """
    # Time Complexity: O(N * 3^N)
    # Space Complexity: O(N)
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        # Get the number of rows and columns of the grid
        ROWS, COLS = len(grid), len(grid[0])

        # Define the directions to move
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        def dfs(r, c, visited):
            # Check if the cell is out of bounds or if the cell is empty or if the cell is already visited
            if (r < 0 or 
                    c < 0 or 
                    r >= ROWS or 
                    c >= COLS or
                    grid[r][c] == 0 or
                    (r, c) in visited):
                    return 0
            
            # Mark the cell as visited
            visited.add((r, c))
            # Initialize the result with the gold in the cell
            res = grid[r][c]

            # Iterate through the directions to move
            for dr, dc in directions:
                # Update the result with the maximum gold path
                res = max(res, grid[r][c] + dfs(r + dr, c + dc, visited))
            
            # Unmark the cell as visited
            visited.remove((r, c))

            # return the result
            return res

        # initialize the result
        res = 0

        # Iterate through the grid
        for r in range(ROWS):
            for c in range(COLS):
                # If the cell has gold, then backtrack to find the maximum gold path
                if grid[r][c] != 0:
                    # update the result with the maximum gold path
                    res = max(res, dfs(r, c, set()))
        
        # return the result
        return res