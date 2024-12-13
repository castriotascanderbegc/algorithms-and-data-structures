"""
    Q: Given a distinct list of integers, return all possible distinct permutations of them
"""

def permutations(nums: list[int]) -> list[list[int]]:
    perms = [[]]

    for n in nums:
        nextPerm = []
        for p in perms:
            for i in range(len(p) + 1):
                pCopy = p.copy()
                pCopy.insert(i, n)
                nextPerm.append(pCopy)
        perms = nextPerm
    return perms