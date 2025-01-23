"""
Q: You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:
    Each row must contain the digits 1-9 without duplicates.
    Each column must contain the digits 1-9 without duplicates.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
    Return true if the Sudoku board is valid, otherwise return false

    Note: A board does not need to be full or be solvable to be valid.

"""
from collections import defaultdict
from typing import List

class Solution:
    def isValidSudokuBruteForce(self, board: List[List[str]]) -> bool:
        # check each row is valid
        for row in range(9):
            # use a hashset to check duplicates
            seen = set()
            for i in range(9):
                # if cell is empty skip it
                if board[row][i] == ".":
                    continue
                # if cell already seen
                if board[row][i] in seen:
                    return False
                # add cell to visited set
                seen.add(board[row][i])
        
        # check each col is valid
        for col in range(9):
            # use a hashset to check duplicates
            seen = set()
            for i in range(9):
                # if empty cell, skip it
                if board[i][col] == ".":
                    continue
                # if cell already visited, return False
                if board[i][col] in seen:
                    return False
                # add cell to visited set
                seen.add(board[i][col])
        
        # check each 3 x 3 sub-boxes
        for square in range(9):
            # use a hashset to detect duplicates
            seen = set()
            # iterate over 3x3 sub-boxes
            for i in range(3):
                for j in range(3):
                    # calculate the row
                    row = (square // 3) * 3 + i
                    # calculate the col
                    col = (square % 3) * 3 + j
                    # if empty cell, skip it
                    if board[row][col] == ".":
                        continue
                    # if cell already seen, return False
                    if board[row][col] in seen:
                        return False
                    # add cell to visited set
                    seen.add(board[row][col])
        # we never returned, sudoku board is valid
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # initialize hashsets for our cols, rows, and squares
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  

        # iterate over each cell in the board
        for r in range(9):
            for c in range(9):
                # if empty cell, skip it
                if board[r][c] == ".":
                    continue
                # if we are visiting a cell already visited in either the rows, cols, or squares
                # return false
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                # add cell to our hashsets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        # we never returned, sudoku board is valid
        return True