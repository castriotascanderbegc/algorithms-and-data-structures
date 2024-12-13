"""
    Q: Given an array of integers nums, return the length of the longest consecutive sequence of elements.
    A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
    You must write an algorithm that runs in O(n) time.

"""
class Solution:
    """
        The brute force solution will be to sort the input array and look at the longest consecutive sequence. 
        This, however, will take O(n log n) time complexity

        The optimal solution can be built using hashing, with a set. 
        The idea is to find numbers in our input array that can be the starting point of a sequence. 
        
        In order to check if a number, say X, is the start of a sequence we can check if X - 1, its left neighbor is in the set. 
        If not in the set, that means X is the start of the sequence. 
        
        We will then count the length of this sequence by checking for subsequent number in the set keeping track of the sequence length.

    """

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def longestConsecutive(self, nums: list[int]) -> int:
        setNum = set(nums)
        longestSequence = 0
        for n in nums:
            if n - 1 not in setNum:
                length = 0
                while n + length in setNum:
                    length += 1
                longestSequence = max(longestSequence, length)
        return longestSequence