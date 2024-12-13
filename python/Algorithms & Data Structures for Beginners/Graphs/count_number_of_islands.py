"""
    Q: Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.
    An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. 
    You may assume water is surrounding the grid (i.e., all the edges are water).

"""
import collections
from typing import List


class Solution:
    ### will be using BFS on a 2D Matrix
    def numIslands(self, grid: List[List[str]]) -> int:
        # if input grid not given, return 0
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])    # store dimensions of the grid
        visited = set()                         # initialize visited HashSet
        islands = 0                             # initialize our result

        # Matrix BFS
        def bfs(r,c):

            q = collections.deque()             # initialize our queue
            q.append((r,c))                     # add r,c positions in the queue
            visited.add((r,c))                  # add r,c positions in the visited set

            # loop until we have elem in the queue
            while q:
                row, col = q.popleft()          # pop from the queue
                directions = [[1,0], [0,1], [-1, 0], [0, -1]]
                # loop through the different directions
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    # check we are within bounds and visiting a "1" cell which has not already been visited
                    if (r >= 0 and r < ROWS and
                        c >= 0 and c < COLS and
                        (r, c) not in visited and
                        grid[r][c] == "1"):
                        q.append((r,c))         # add r,c position to our queue
                        visited.add((r,c))      # add r,c, position to our visited set

        # move through the 2D grid
        for r in range(ROWS):
            for c in range(COLS):
                # make sure we run BFS on "1" cells which have not already been visited
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    # increment number of islands
                    islands += 1    

        return islands



        