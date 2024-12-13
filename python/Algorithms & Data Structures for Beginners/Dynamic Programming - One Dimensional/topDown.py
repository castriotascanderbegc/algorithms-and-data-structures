"""
    Below is an example of One Dimensional Dynamic Programming (1DP)

    We will use a Top Down approach - Recursion with MEMOIZATION

"""

# Calculate the Nth Fibonacci number
# Time Complexity: T(2^n)
def bruteForce(n: int) -> int:
    if n <= 1:
        return n
    return bruteForce(n - 1) + bruteForce(n - 2)

"""
    Using memoization, also known as caching. We can store each computation of nth fib number in the cache for O(1) retrieval. 

    Time Complexity: O(n)
    Space Complexity: O(n)
"""
def memoization(n: int, cache: dict) -> int:
    if n <= 1:
        return n
    if n in cache:
        return cache[n]
    
    cache[n] = memoization(n - 1, cache) + memoization(n - 2, cache)

    return cache[n]



