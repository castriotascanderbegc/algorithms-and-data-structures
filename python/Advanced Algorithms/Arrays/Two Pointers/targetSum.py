"""
    Question: Given a sorted input array, return two indices of two elements which sums up to the target value. 
        Assume there's exactly one solution. 
"""

# brute force -> iterate over every single pair of integers, O(n^2) time complexity

# two pointers technique - linear time
# time complexity: T(n) = O(n) - we make a single pass on the array
def targetSum(nums: list[int], target: int) -> list[int]:
    # initialize left and right pointers 
    L, R = 0, len(nums) - 1

    # repeat until pointers cross each other 
    while L < R:
        # if sum is greater than target, decrement R 
        if nums[L] + nums[R] > target:
            R -= 1
        # if sum is smaller than targer, increment L  
        elif nums[L] + nums[R] < target:
            L += 1
        # sum is equal to targer, we found our solution
        else:
            return [L, R]
    