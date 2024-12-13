"""
    Using the topDown approach as an example, here using a bottom up approach we can reduce the space complexity to O(m) where m is the number of columns
"""

from os import preadv


def dp(rows, cols):
    prevRow = [0] * cols # initialize an initial row with all 0's to calculate the bottom-most row

    for r in range(rows - 1, -1, -1): # decrement the row at each row number
        curRow = [0] * cols # initialize a row full of 0's 
        curRow[cols - 1] = 1 # set right most col to 1
        for c in range(cols - 2, -1, -1): # go through every col in the row
            curRow[c] = curRow[c + 1] + prevRow[c] 
        prevRow = curRow # set the row to the prevRow and move on 
    

    return prevRow[0]