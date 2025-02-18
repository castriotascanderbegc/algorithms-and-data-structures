"""
    Q: Car Fleet
    There are n cars traveling to the same destination on a one-lane highway.

    You are given two arrays of integers position and speed, both of length n.

    position[i] is the position of the ith car (in miles)
    speed[i] is the speed of the ith car (in miles per hour)
    The destination is at position target miles.

    A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

    A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

    If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

    Return the number of different car fleets that will arrive at the destination.
"""
from typing import List


class Solution:
    """
        Since a car can only form a fleet with another car that is ahead of it, we can sort the array of pairs (pos, speed) in descending order of position. 
        Two cars will form a fleet if and only if the car ahead has a time that is greater than or equal to the time of the car behind it.

        Iterating through the array in reverse sorted order (descending order), we can calculate the time for the current car to reach the target --> time = (target - position) / speed
        
        We can use a stack to maintain the times of the fleets. If the current's car time is less than or equal than the top of the stack, it will form a fleet. 
        Otherwise, it will form a new fleet so we can push its time onto the stack. 

        At the end, the length of the stack will represent the number of total fleets formed. 

    """
    # Time Complexity: T(n) = O(n log n)
    # Space Complexity: S(n) = O(n)
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # create a list of (pos, speed) pairs
        items = list(zip(position, speed))
        # sort in descending order of positions
        sortedItems = sorted(items, key=lambda x: x[0], reverse=True)
        # initialize a stack to keep track of the times of the fleets
        stack = []

        # iterate through the array
        for pos, speed in sortedItems:
            # if stack is empty, initialize it
            if not stack:
                time = float((target - sortedItems[0][0]) / sortedItems[0][1])
                stack.append(time)
            # calcualte the time for the current car to reach the target destination
            time = float((target - pos) / speed)
            # check if the current car will join the same fleet or form a new one
            if time > stack[-1]:
                stack.append(time)
        
        # the length of the stack represents the total number of fleets formed
        return len(stack)