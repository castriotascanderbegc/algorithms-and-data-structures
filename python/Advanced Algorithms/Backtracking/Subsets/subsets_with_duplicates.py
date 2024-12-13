"""
    Q: Given a list of nums, that are not necessarily distinct, return all possible distinct subsets.

"""

# input list might contain duplicates
def subsetsWithDuplicates(nums: list[int]) -> list[list[int]]:
    # first sort the input array so each duplicate is adjacent one another
    nums.sort()
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

    
    # skip duplicates
    while i + 1 < len(nums) and nums[i] == nums[i + 1]:
        i += 1
    
    # decide NOT to include element at index i
    helper(i + 1, nums, curSet, subsets)
