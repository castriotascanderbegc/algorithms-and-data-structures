"""
    Q: Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

    For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells.
    The same cell may not be used more than once in a word.
"""

from typing import List


class Solution:
    # we will be using brute force BACKTRACKING to solve the question
    # Time Complexity: T(n): O(n * m * 4^n) --> not really efficient
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])      # take the dimension of the grid
        path = set()                                # initialize a HashSet to keep track of the current path

        def dfs(r, c, index):
            # if we reached the end of the word, we know we found it
            if index == len(word):
                # we can then return True
                return True
            
            # base cases
            if (r < 0 or r >= ROWS or           # out of bounds check on ROWS
                c < 0 or c >= COLS or           # out of bounds check on COLS
                (r, c) in path or               # if we are visiting a cell already in the path
                board[r][c] != word[index]):    # if the current cell is different from the current character in the word
                # we can immediately return False
                return False
            
            # add current cell to the path
            path.add((r,c))

            # run backtracking dfs
            res = (dfs(r + 1, c, index + 1) or 
                    dfs(r - 1, c, index + 1) or
                    dfs(r, c + 1, index + 1) or
                    dfs(r, c - 1, index + 1))
            
            # backtrack, remove visited cell from path
            path.remove((r,c))
            
            # return the result
            return res

        # move over every row in the board
        for i in range(ROWS):
            # move over every col in the board
            for j in range(COLS):
                # run backtracking dfs
                if dfs(i, j, 0):
                    return True
        
        # if we haven't returned the word, return False
        return False

        