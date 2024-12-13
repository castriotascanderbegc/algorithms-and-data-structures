"""
    Q: Given an m x n matrix of integers matrix, return a list of all elements within the matrix in spiral order.

""" 

from typing import List


class Solution:
    # Time Complexity: T(n): O(n * m)
    # Space Complexity: S(n): O(1)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # edge case: empty or no matrix
        if not matrix or len(matrix) == 0: 
            return


        # initialize count and total number of elements in the 2d grid
        count, total = 0, sum(len(row) for row in matrix)

        # initialize our pointers: TOP, BOTTOM, LEFT, RIGHT
        startingRow, endingRow = 0, len(matrix)
        startingCol, endingCol = 0, len(matrix[0])
        
        # initialize our result
        res = []

        # move until we haven't seen all numbers in the 2d grid
        while count < total:

            # print first row -- move left to right
            for i in range(startingCol, endingCol):
                res.append(matrix[startingRow][i])
                count += 1

            # increment top
            startingRow += 1

            # print last col -- move top to bottom
            for i in range(startingRow, endingRow):
                res.append(matrix[i][endingCol - 1])
                count += 1
            
            # decrement right
            endingCol -= 1

            # if we completed, break the loop
            if not (count < total):
                break

            # print last row -- move right to left
            for i in range(endingCol - 1, startingCol - 1, -1):
                res.append(matrix[endingRow - 1][i])
                count += 1

            # decrement bottom
            endingRow -= 1

            # print first col -- move bottom to top
            for i in range(endingRow - 1, startingRow - 1, -1):
                res.append(matrix[i][startingCol])
                count += 1
            
            # increment left
            startingCol += 1

        return res
