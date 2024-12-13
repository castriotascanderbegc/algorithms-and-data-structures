"""
    Q: You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

        Find two lines that together with the x-axis form a container, such that the container contains the most water.

        Return the maximum amount of water a container can store.

        Notice that you may not slant the container.

"""
class Solution:
    """
        Brute force: 
            Go through every height in the given input and use it to calculate the area at each width
            This will take O(n^2) as we need to go through each possible pair in the input
        
        Optimal solution: 
            We can use Two Pointers technique. 
            We can initialize a left pointer at the beginning of the input and a right pointer at the end (since we want to maximize the area)
            We then calculate each area and keep track of the maximum area seen. We move the pointer at the lower height since we want to maximize the height
            So if height[L] < height[R] then we increment L otherwise we decrement R. 

    """

    # Two Pointers techinique
    # Time Complexity: T(n) = O(n)
    # Space Complexity: S(n) = O(1)
    def maxArea(self, heights: list[int]) -> int:
        L, R = 0, len(heights) - 1  # initialize left and right pointers
        maxWater = 0                # keep track of the maximum area
        # repeat until pointers cross
        while L < R:
            currWater = (R - L) * min(heights[R], heights[L])   # calculate the water area
            maxWater = max(maxWater, currWater)                 # update the maximum water area

            # if height at right pointer is lower
            if heights[R] <= heights[L]:
                R -= 1  # decrement right pointer
            else: # if not
                L += 1  # increment left pointer

        return maxWater # return maximum water area


