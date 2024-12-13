"""
    Below is an example of Two Dimensional Dynamic Programming (2DP)

    We will use a Top Down approach here, using MEMOIZATION, caching. 

    Let's use the example of number of unique paths in a grid from top left corner to bottom right corner. 
    We can only move either down or right.
"""

# Time Complexity: O(2 ^ n*m)
# Space Complexity: O(N + M)
def bruteForce(r, c, rows, cols):
    if r == rows or c == cols:
        return 0
    if r == rows - 1 and c == cols - 1:
        return 1
    
    return bruteForce(r + 1, c, rows, cols) + bruteForce(r, c + 1, rows, cols)


# Use top down approach - memoization, caching
# Time and Space Complexities: O(n * m)
def memoization(r, c, rows, cols, cache):
    if r == rows or c == cols:
        return 0
    if cache[r][c] > 0:
        return cache[r][c]
    if r == rows - 1 and c == cols - 1:
        return 1
    
    cache[r][c] = memoization(r + 1, c, rows, cols, cache) + memoization(r, c + 1, rows, cols, cache)

    return cache[r][c]