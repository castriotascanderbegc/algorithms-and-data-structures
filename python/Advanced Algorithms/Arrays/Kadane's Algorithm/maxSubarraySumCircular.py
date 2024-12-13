"""
    Question: Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
    A circular array means the end of the array connects to the beginning of the array. 
------------------------------------------------------------------------------------------------------------

    The idea here is to use Kadane's algorithm that will solve us the case if the max subarray sum lies in the middle of the array. 

    However, since the array is circular it could be possible that the max subarray sum lies at either end of the array. 
    For example, starting from the end and circling back to the beginning. 

    In order to solve this edge case we could keep track of the curMin and globMin and the entire total. 
    If the max subarray sum does not lie in the middle we can check which is greater between our global Max and total - globalMin which will give us the sub array sum at the edges
"""
class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        # keep track of both global Max and global Min 
        globMax, globMin = nums[0], nums[0]
        # keep track of the current Max and current Min 
        curMax, curMin = 0, 0

        # initialize our total to 0
        total = 0

        for n in nums:
            curMax = max(curMax + n, n)     # take the maximum between the curMax so far + number, or the number itself.
            curMin = min(curMin + n, n)     # take the minimum between the curMin so far + the number, or the number itself. 
            
            total += n                      # add n to the total 

            globMax = max(globMax, curMax)  # take the maximum between the curMax so far and the globalMax so far
            globMin = min(globMin, curMin)  # take the minimum between the curMin so far and the globalMin so far

        # at this point we take the maximum between globMax and total - globMin
        # in this way, globMax will be the max subarray sum if it lies in the middle of the array
        # total - globMin will be the max subarray sum if lies within the edges of the array
        # we need to check if there's at least a positive number in the array (i.e. globMax > 0)
        # otherwise, if there are all negative numbers the max subarray sum will just be the globMax (i.e. the greatest negative integer in the array)
        return max(globMax, total - globMin) if globMax > 0 else globMax