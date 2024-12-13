"""
    Q: Given a square n x n matrix of integers matrix, rotate it by 90 degrees clockwise.
    You must rotate the matrix in-place. Do not allocate another 2D matrix and do the rotation.

"""


from typing import List


class Solution:
    # The idea behind rotating clockwise is to Transpose and Reverse
    def rotate(self, matrix: List[List[int]]) -> None:
        # Take size of the matrix
        ROWS, COLS = len(matrix), len(matrix[0])

        # we first want to transpose the matrix
        for r in range(ROWS):
            for c in range(r + 1, COLS):
                # swap diagonally - matrix[i][j] with matrix[j][i]
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                
        # we then want to swap the rows
        for r in range(ROWS):
            matrix[r].reverse()

        # no need to return anything as we rotated clockwise in-place 



    # Rotate by Four Cells
    def rotate_by_four_cells(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # save the topleft
                topLeft = matrix[top][l + i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1