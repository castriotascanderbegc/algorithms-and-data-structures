"""
    Q: Subarray Sum Equals K

    Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

    A subarray is a contiguous non-empty sequence of elements within an array.

"""

from typing import List

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
            The idea here is to keep a dictionary to store the prefix sum and the number of times it has occured.
            We will iterate through the array and keep adding the elements to the prefix sum.
            If the difference between the current prefix sum and k is present in the dictionary, we will increment the result by its value in the prefix dictionary.
            We will also increment the value of the prefix sum in the dictionary.
        """

        # Initialize the result, current sum and the prefix dictionary
        res, curSum = 0, 0
        prefix = {0: 1}
        
        # Iterate through the array
        for n in nums:
            
            # Add the current element to the current sum
            curSum += n

            # If the difference between the current sum and k is present in the prefix dictionary, increment the result by its value
            if curSum - k in prefix:
                res += prefix[curSum - k]
            
            # Increment the value of the current sum in the prefix dictionary
            prefix[curSum] = 1 + prefix.get(curSum, 0)
        
        # Return the result
        return res