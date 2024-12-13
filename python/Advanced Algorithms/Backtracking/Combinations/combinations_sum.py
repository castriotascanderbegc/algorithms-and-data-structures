"""
    Q:  You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.
        The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.
        You may return the combinations in any order and the order of the numbers in each combination can be in any order.
"""

# Time Complexity: T(n) = O(2^t) where t = target

from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, currComb = [], []

        def helper(i, currComb, total):
            if total == target:
                res.append(currComb.copy())
                return

            if i >= len(nums) or total > target:
                return
            
            currComb.append(nums[i])
            helper(i, currComb, total + nums[i])
            currComb.pop()

            helper(i + 1, currComb, total)
            
        helper(0, currComb, 0)
        return res