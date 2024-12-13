"""
    Q: Given a distinct list of integers, return all possible distinct permutations of them

"""

# Time Complexity: O(n^2 * n!)
def permutations(nums: list[int]) -> list[list[int]]:
    return helper(0, nums)

def helper(i: int, nums: list[int]) -> list[list[int]]:
    if i == len(nums):
        return [[]]
    
    res = []
    perms = helper(i + 1, nums)

    # iterate through all current permutations
    for p in perms:
        # iterate through each value in the current perm
        for j in range(len(p) + 1):
            # take a copy
            pCopy = p.copy()
            # insert copy at j
            pCopy.insert(j, nums[i])
            # append to our results
            res.append(pCopy)
    return res

