"""
    Q: Given an m x n matrix of integers matrix, if an element is 0, set its entire row and column to 0's.
    You must update the matrix in-place.
"""

from typing import List


class Solution:
    # Time Complexity: T(n): O(m * n)
    # Space Complexity: S(n): O(m + n)    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # initialize our set with r,c coordinates with a zero value
        zeros = set()

        # iterate over the matrix to find r,c coordinates with a zero value
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    # add to the set
                    zeros.add((r,c))
        
        # loop through the set
        for r,c in zeros:
            # set the row r with all zeros
            matrix[r] = [0] * len(matrix[r])
            # iterate over all the rows to set the the cols to 0
            for row in matrix:
                row[c] = 0
        
    
    # Time Complexity: T(n): O(m * n)
    # Space Complexity: S(n): O(1)    
    def setZeroesSpaceOptimized(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # iterate over the matrix to find which rows and cols to be zeroed out
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        # based on the rows and cols to be zeroed out, change values in place
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # handle first row and first col seperately
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
        