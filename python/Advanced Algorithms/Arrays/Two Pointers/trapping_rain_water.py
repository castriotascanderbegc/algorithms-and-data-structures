"""
    Q: Trapping Rain Water

    You are given an array non-negative integers height which represent an elevation map. 
    Each value height[i] represents the height of a bar, which has a width of 1.

    Return the maximum area of water that can be trapped between the bars.

"""
from typing import List


class Solution:
    """
        The idea here is to first determine the amount of water that can be trapped at each specific position in the array.

        Uisng the image, we can see that to calculate the amount of water at each index i in the array, 
        the greater element to the left and the greater element to the right are crucial. 

        We want to use the minimum between the two maximum on either side and subtract the current elevation at index i of the array. 

        The formula to compute the trapped water is min(max(height[left]), max(height[right])) - height[i]

        For a brute force solution, we can use array slicing which take O(n) and repeat over each element in the array. The time complexity is O(n^2).

    """

    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def trapBruteForce(self, height: List[int]) -> int:
        # if the array is empty, return 0
        if not height:
            return 0

        # initialize our maximum trapped water
        result = 0

        # iterate through each element in the array
        for i in range(len(height) - 1):
            # skip the first element as we cannot trap water here
            if i == 0:
                continue

            # slice the array in two parts to find max in the left and right sides
            left = height[:i]
            right = height[i + 1:]

            # calculate the current amount of water trapped at index i
            curr_trap = min(max(left), max(right)) - height[i]

            # make sure we are not adding a negative amount of water computed
            curr_trap = max(curr_trap, 0)

            # update our maximum trapped water
            result += curr_trap
        
        # return our result
        return result

    
    """
        A better approach would be to store the prefix maximum in an array by iterating from left to right
        and the suffix maximum in another array by iterating from right to left. 

        For example, in [1, 5, 2, 3, 4], for the element 3, the prefix maximum is 5, and the suffix maximum is 4. 

        Once these arrays are built, we can iterate through the array with index i and calculate the total water trapped at each position
        using the same formula, i.e. min(prefix[i], suffix[i]) - height[i] where:
            prefix[i] has the maximum to the left side of i
            suffix[i] has the maximum to the right side of i. 

        This would bring the time complexity down to O(n), but with a space complexity of O(n)
    """

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def trap(self, height: List[int]) -> int:
        # if the array is empty, return 0
        if not height:
            return 0
        
        # initialize prefix maximum array
        leftMax = [0] * len(height)
        leftMax[0] = height[0]

        # iterate from left to right to find the maximum to the left of each element
        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i - 1], height[i])

        # initialize suffix maximum array
        rightMax = [0] * len(height)
        rightMax[-1] = height[-1]

        # iterate from right to left to find the maximum to the right of each element
        for i in range(len(height) - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        # initialize our result
        result = 0

        # iterate through the array to calculate the trapped water at each index
        for i in range(len(height)):
            res += min(leftMax[i], rightMax[i]) - height[i]
        
        return result


    """
        An optimal approach would be to use the two-pointer technique.
        This would bring the space complexity down to O(1) as we would not need to store the prefix and suffix maximums in separate arrays.
    """

    def trap_two_pointers(self, height: List[int]) -> int:
        # if array is empty, return 0
        if not height:
            return 0
        
        # initialize our left and right pointers
        l, r = 0, len(height) - 1

        # initialize our maxLeft and maxRight
        maxLeft, maxRight = height[l], height[r]

        # initialize our result
        result = 0

        # continue until pointers meet
        while l < r:
            # check which maximum is smaller
            if maxLeft < maxRight:
                # increment left pointer
                l += 1
                # update left maximum
                leftMax = max(leftMax, height[l])
                # update our result
                result += leftMax - height[l]
            else:
                # decrement right pointer
                r -= 1
                # update right maximum
                rightMax = max(rightMax, height[r])
                # update our result
                result += rightMax - height[r]
        
        # return our result
        return result