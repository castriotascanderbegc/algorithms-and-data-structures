"""
    Q: Given a list of distinct nums (do not contain duplicates), return all possible distinct subsets.

"""

# input list does not contain any duplicates
def subsetsWithoutDuplicates(nums: list[int]) -> list[list[int]]:
    subsets, curSet = [], []
    helper(0, nums, curSet, subsets)
    
    return subsets

def helper(i: int, nums: list[int], curSet: list[int], subsets: list[list[int]]) -> None:
    # check if we are out of bounds, we traversed entire array
    if i >= len(nums):
        subsets.append(curSet.copy())
        return

    # iterate through entire array
    # append current number in the set and apply backtracking

    # decide to include element at index i
    curSet.append(nums[i])
    helper(i + 1, nums, curSet, subsets)
    curSet.pop()

    
    # decide NOT to include element at index i
    helper(i + 1, nums, curSet, subsets)

    