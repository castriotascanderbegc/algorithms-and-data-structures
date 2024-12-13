"""
    Q: You are given an integer array nums where each element nums[i] indicates your maximum jump length at that position.

    Return true if you can reach the last index starting from index 0, or false otherwise.
"""

from typing import List


class Solution:
    # Greedy Approach
    # Time Complexity: T(n) = O(n)
    def canJump(self, nums: List[int]) -> bool:
        """
            The idea here is to set a goal post to the end, and work our way backward. 
            If we can reach the goal post using the value at the current index, i.e. i + nums[i] >= goal
            Then we can shift left the goal and continue. By the end of our input array, we either.
                1. Have our goal = 0 -> We were able to reach the end
                2. Have our goal > 0 -> We were not able to reach the end
        """
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            # if we can reach the goal from the current index, shift the goal
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0

        