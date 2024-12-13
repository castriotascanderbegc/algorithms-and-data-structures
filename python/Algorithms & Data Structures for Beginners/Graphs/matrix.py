from collections import deque
# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

class Matrix:
    """
        A typical DFS question on a Graph could be the following:
            Count the unique paths from the top left to the bottom right.
            A single path may only move along 0's and can't visit the same cell more than once
        
        We can solve above question using DFS on a matrix, a 2-dimensional array with r = rows and c = columns

        Time Complexity: T(n): O(4 ^ (n * m)) where n = # of rows, and c = # of cols
    
    """
    # Count paths (backtracking)
    def dfs(self, grid: list[list[int]], r: int, c: int, visited: set) -> int:

        # store the length of the rows and columns of the grid
        ROWS, COLS = len(grid), len(grid[0])
        # Base cases:
            # we go out of bounds
            # we visit a cell already visited
            # we visit a 1 cell
        if (min(r,c) < 0 or r == ROWS or c == COLS or 
            (r,c) in visited or grid[r][c] == 1):
            return 0
        
        # we are at bottom right corner of the grid, we found a path
        if r == ROWS - 1 and c == COLS - 1:
            return 1
        
        # add visited cell to HashSet
        visited.add((r,c))
        
        count = 0
        
        # recursively process all four directions
        count += self.dfs(grid, r + 1, c, visited)      # down
        count += self.dfs(grid, r - 1, c, visited)      # up
        count += self.dfs(grid, r, c + 1, visited)      # right
        count += self.dfs(grid, r, c - 1, visited)      # left

        # remove visited cell from HashSet --> if recursive call does not lead to a path, we want to be able to re-visit the cell
        visited.remove((r,c))

        # return number of unique paths
        return count
    

    """
        A typical BFS question on a Graph could be the following:
            Find the length of the shortest path from the top left to the bottom right of the grid.
            A single path may only move along 0's and can't visit the same cell more than once
        
        We can solve above question using BFS on a matrix, a 2-dimensional array with r = rows and c = columns

        Time Complexity: T(n) = O(n * m) where n = # of rows, and c = # of cols
    
    """
    def bfs(self) -> int:
        # initial the length of the shortest path
        length = 0
        # keep a queue
        queue = deque()
        # keep a visited cells HashSet
        visited = set()

        # store the legnth of the rows and columns of the grid
        ROWS, COLS = len(grid), len(grid[0])

        # add top left cell to the queue
        queue.append((0,0))
        # add top left cell to the visited cells HashSet
        visited.add((0,0))

        # loop until we have coordinate in the queue
        while queue:
            # take a snapshot of the length of the queue
            for i in range(len(queue)):
                # pop a cell 
                r,c = queue.popleft()

                # check we are at bottom right cell, end of the path
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                # keep a list of neighbor coordinates, i.e possible directions
                neighbors = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in neighbors:
                    # if we are out of bounds or we are at a visited cell or a cell that cannot be visited, i.e. 1 cell
                    if (min(r + dr, c + dc) < 0 or r + dr == ROWS or c + dc == COLS or 
                        (r + dr, c + dc) in visited or grid[r + dr][c + dc] == 1):
                        # continue to next iteration
                        continue
                    queue.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
            length += 1
        
        return length