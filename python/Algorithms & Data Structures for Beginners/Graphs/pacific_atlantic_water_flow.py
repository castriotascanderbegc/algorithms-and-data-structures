"""
Q: Pacific Atlantic Water Flow
    You are given a rectangular island heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
    The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides.
    Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height equal or lower. 
    Water can also flow into the ocean from cells adjacent to the ocean.
    
    Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. 
    Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell. 
    You may return the answer in any order.

"""
from typing import List


class Solution:
    """
        We can use Depth First Search (DFS) from the border cells of the grid. First row, first col, last row, last col.
        For the top and left borders connected to the Pacific Ocean, we can use a hash set called pacific
        For the bottom and right borders connected to the Atlantic Ocean, we can use a hash set called atlantic

        We can run DFS from each of the cells within these borders, visiting nodes recurively. 

        For the DFS, we recursively visit the neighbouring cell not visited yet with height greater than or equal to the current cell's height and add its coordinated
        to the corresponding hash set 

        The required coordinated are those cells that exist in both atlantic and pacific ocean, i.e. water can flow both to Pacific and Atlantic

    """
    # Time Complexity: T(n): O(m * n) where m, n are the dimensions of the grid
    # Space Complexity: S(n): O(m * n) where m, n are the dimensions of the grid
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # store dimensions of the grid
        ROWS, COLS = len(heights), len(heights[0])
        # use two seperate hash sets to run DFS recursively, each for each borders connected to atlantic/pacific ocean
        pacific, atlantic = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r,c) in visit or
                r < 0 or r == ROWS or 
                c < 0 or c == COLS or
                heights[r][c] < prevHeight):
                
                return
            
            visit.add((r,c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])


        # run TOP and BOTTOM borders
        for c in range(COLS):
            # run DFS in the top border connected to pacific ocean
            dfs(0, c, pacific, heights[0][c])
            # run DFS in the bottom border connected to atlantic ocean
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])
        
        # run LEFT and RIGHT borders
        for r in range(ROWS):
            # run DFS in the left border connected to pacific ocean
            dfs(r, 0, pacific, heights[r][0])
            # run DFS in the right border connected to atlantic ocean
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])
        
        res = []
        for c in range(COLS):
            for r in range(ROWS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])

        return res