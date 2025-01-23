"""
Given an integer array nums, find a subarray that has the largest product within the array and return it.

A subarray is a contiguous non-empty sequence of elements within an array.

You can assume the output will fit into a 32-bit integer.
"""

from typing import List

class Solution:
    def max_product_subarray(self, nums: List[int]) -> int:
        """
        Find the contiguous subarray within an array (containing at least one number) which has the largest product.
        """
        if not nums:
            return 0

        # Keep track of the maximum and minimum product of subarrays ending at the current index
        max_product, min_product = nums[0], nums[0]

        # Keep track of the maximum product of subarrays ending at the current index
        result = max_product
        
        # Iterate through the array
        for i in range(1, len(nums)):
            # If the current number is negative, swap the maximum and minimum product
            if nums[i] < 0:
                max_product, min_product = min_product, max_product

            # Update the maximum and minimum product of subarrays ending at the current index
            max_product = max(nums[i], max_product * nums[i])
            min_product = min(nums[i], min_product * nums[i])

            # Update the maximum product of subarrays ending at the current index
            result = max(result, max_product)

        # Return the maximum product of subarrays
        return result

    def max_product_subarray_kadanes(self, nums: List[int]) -> int:
        """
        Find the contiguous subarray within an array (containing at least one number) which has the largest product.
        """
        if not nums:
            return 0

        # Keep track of the maximum and minimum product of subarrays ending at the current index
        max_product, min_product = 1, 1

        # Keep track of the maximum product of subarrays ending at the current index
        result = nums[0]
        
        # Iterate through the array
        for num in nums:
            # Keep track of the maximum product of subarrays ending at the current index
            temp = num * max_product

            # Update the maximum and minimum product of subarrays ending at the current index
            max_product = max(max_product * num, min_product * num, num)
            # Update the maximum and minimum product of subarrays ending at the current index
            min_product = min(temp, min_product * num, num)

            # Update the maximum product of subarrays ending at the current index
            result = max(result, max_product)

        # Return the maximum product of subarrays
        return result

