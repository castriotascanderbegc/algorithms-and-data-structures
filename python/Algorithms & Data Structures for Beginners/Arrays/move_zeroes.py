"""
    Q: Move Zeroes
    Given an integer array nums, move all 0's to the end of it while maintaining the relative
    order of the non-zero elements.
    
    Note that you must do this in-place without making a copy of the array.

"""
from typing import List


class Solution:
    """
        The idea here is to use two pointers technique. 
        
        One pointer will tell us where to place the next element and the other pointer will move through the array. 
        
        If the element is not zero, we swap the elements and move the first pointer to the next position.
    
    """
    # Time complexity: O(n)
    # Space complexity: O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pointers techinique

        # one pointer will tell us where to place the next elem
        l = 0

        # with the second pointer will move through the array
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        