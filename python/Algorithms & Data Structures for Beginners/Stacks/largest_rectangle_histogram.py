"""
    Q: Largest Rectangle in Histogram

    You are given an array of integers heights where heights[i] represents the height of a bar.
    The width of each bar is 1.

    Return the area of the largest rectangle that can be formed among the bars.

"""
from typing import List


class Solution:
    """
        The idea here is for a bar of height h, we can try extend it to the left and right. 
        We can't extend further when we encounter a bar with a smaller height than h. 
        The width will be the number of bars within this extended range. 

        The left and right boundaries are the positions up to which we can extend the bar at the index i.

        The area of the rectangle will be height[i] * (right - left + 1)

        These boundaries (left & right) are determined by the first smallers bars encountered to the left and right of the current bar.

        Using a stack (monotonically strictly increasing), we can store the indices and the top of the stack will represent the smaller bar that we encounter while extending the current bar. 
        We can move from left to right and vice versa, storing boundaries. 



    """
    # Time Complexity: T(n): O(n)
    # Space Complexity: S(n): O(n)
    def largestRectangleArea(self, heights: List[int]) -> int:
        # initialize our maximum area
        maxArea = 0
        # initialize our stack
        stack = []

        # iterate through the given input heights
        for i, h in enumerate(heights):
            # set the beginning of the boundary
            start = i
            # keep popping from the stack if the element is greater than the current height
            while stack and stack[-1][1] >= h:
                # pop index and height from the stack
                index, height = stack.pop()
                # compute the max area at the current bar
                maxArea = max(maxArea, height * (i - index))
                # update beginning of boundary
                start = index

            # append into the stack (beginning of boundary, height)
            stack.append((start, h))
        
        # we might still have elements left in the stack
        for i, h in stack:
            # compute the max area for these elements and update our max
            maxArea = max(maxArea, h * (len(heights) - i))
         
        return maxArea