"""
    Q: Daily Temperatures

    You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.
    Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. 
    If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.
"""
from typing import List


class Solution:
    """
        A brute force solution would be iterating through the array with index i and checking how far is the next greater element to the right of i. 
        This would be a O(n^2) solution. 

        A better approach would be using a monotonic decreasing stack to where we pop (temperature, index) of the temperatures where values are smaller than
        the current element in the array. This way, we can use the difference between the index of the current element and the index of the element at the top of the stack just popped.
    """
    # Time Complexity: T(n) = O(n)
    # Space Complexity: S(n) = O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # first initialize our result output
        res = [0] * len(temperatures)
        # also initialize a stack, [pair(temp, idx)]
        stack = []
        # iterate through the given array of temperatures, tracking index and values
        for i, t in enumerate(temperatures):
            # keep popping from the stack until the element at the top is smaller than the current element in the array 
            while stack and stack[-1][0] < t:
                # pop temp, idx pair
                stackT, stackIndex = stack.pop()
                # use difference between index of current element and index of element popped from the stack
                res[stackIndex] = i - stackIndex
            # append current element in the stack
            stack.append((t, i))
        return res