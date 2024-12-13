"""
    Q: Given two integers n and k, return all possible combinations of size = k, choosing from values between 1 and n

    i.e. n choose k problem
"""

# T(n): O(k * C(n, k))
def combinations(n: int, k: int) -> list[list[int]]:
    currComb, combs = [], []
    helper(1, currComb, combs, k, n)
    return combs

def helper(i: int, currComb: list[int], combs: list[list[int]], k: int, n: int) -> None:
    if len(currComb) == k:
        combs.append(currComb.copy())
        return
    if i > n:
        return 
    
    for j in range(i, n + 1):
        currComb.append(j)
        helper(j + 1, currComb, combs, k, n)
        currComb.pop()
    