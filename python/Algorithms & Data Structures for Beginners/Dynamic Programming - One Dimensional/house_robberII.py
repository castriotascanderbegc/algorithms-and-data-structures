"""
    Q: House Robber II
    You are given an integer array nums where nums[i] represents the amount of money the ith house has. 
    The houses are arranged in a circle, i.e. the first house and the last house are neighbors.
    
    You are planning to rob money from the houses, but you cannot rob two adjacent houses 
    because the security system will automatically alert the police if two adjacent houses were both broken into.
    
    Return the maximum amount of money you can rob without alerting the police.
"""

from typing import List


class Solution:
    # Time Complexity: T(n) = O(n) where n is the length of the array
    def rob(self, nums: List[int]) -> int:

        def calculateRob(nums: List[int]) -> int:
            # these store the max amount you can rob from previous two houses
            rob1, rob2 = 0,0
            
            # iterate through every house in the given array
            # idea is to have [rob1, rob2, n, n + 1, ...], keeping track of two maximum seen so far
            for n in nums: 
                tmp = max(n + rob1, rob2)   # take the max between (house[i] + house[i - 2]) and house[i - 1]          
                rob1 = rob2                 # update house[i - 2]          
                rob2 = tmp                  # update house[i - 1] with tmp
            return rob2

        # we can re-use previous calculateRob method on two seperate arrays
        # from first house to second-to-lat house and from second house to last house
        # need to include first item in case given array has only one house
        return max(nums[0], calculateRob(nums[:-1]), calculateRob(nums[1:]))