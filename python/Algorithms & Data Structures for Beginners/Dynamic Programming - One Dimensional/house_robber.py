"""
    Q: You are given an integer array nums where nums[i] represents the amount of money the ith house has. 

    The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.
    You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will 
    automatically alert the police if two adjacent houses were both broken into.

    Return the maximum amount of money you can rob without alerting the police.

"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0
        # iterate through the houses in the array
        # idea is to have [rob1, rob2, n, n + 1, ...]
        for n in nums:
            tmp = max(n + rob1, rob2)               # take the max between (house[i] + house[i - 2]) and house[i - 2]
            rob1 = rob2                             # update house[i - 2]
            rob2 = tmp                              # update house[i - 1] with tmp
        return rob2

        """
        dp = [nums[0], max(nums[0], nums[1])]
        i = 2
        while i < len(nums):
            tmp = max(nums[i] + dp[0], dp[1])
            dp[0] = dp[1]
            dp[1] = tmp
        return dp[1]
        """

        
