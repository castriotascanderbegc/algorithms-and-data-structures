"""
    Q: Search a 2D Matrix
    
    You are given an m x n 2-D integer array matrix and an integer target.
            Each row in matrix is sorted in non-decreasing order.
            The first integer of every row is greater than the last integer of the previous row.
    
    Return true if target exists within matrix or false otherwise.

    Can you write a solution that runs in O(log(m * n)) time?

"""
from typing import List


class Solution:
    """
        We can perform binary search on the rows to identify the row in which the target might fall.
        Once the potential round is found, we can perform a binary search on that row
    """
    # Time Complexity: T(n): O(log(m * n))
    # Space Complexity: S(n): O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # perform binary search on the rows to identify the potential row where target might exist
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        # if we have not identified a potential row, we can immediately return False
        if not (top <= bottom):
            return False
        
        # perform binary search on the identified row
        l, r = 0, len(matrix[0]) - 1
        row = (top + bottom) // 2

        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        
        return False
        
        