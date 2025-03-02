"""
Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray whose sum is greater than or equal to target. 

If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""
def minimum_size_subarray(nums, target):
    L, window_sum = 0, 0
    res = float("inf")
    
    for R in range(len(nums)):
        # first we add the current num to our window_sum, expanding our window from the right
        window_sum += nums[R]
        
        # keep shrinking our window from the left if the sum is greater than target
        while window_sum >= target:
            # update our min lenght
            res = min(R - L + 1, res)
            # shring window from the left
            window_sum -= nums[L]
            L += 1
        
    return 0 if res == float("inf") else res
        

print(minimum_size_subarray([2,3,1,2,4,3], 7))
print(minimum_size_subarray([1,4,4], 4))
print(minimum_size_subarray([1,1,1,1,1,1,1,1], 11))