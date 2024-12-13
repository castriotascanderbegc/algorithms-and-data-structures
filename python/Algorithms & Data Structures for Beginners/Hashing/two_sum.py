class Solution:
    """
        Brute Force: For each number in the array, see if any of the remaining number adds up to the target. This is a two pass on the array. 
            It will O(n^2) time complexity and O(1) space
        
        Best implementation: Use a HashMap where we can insert and search in O(1). We can map each number in the array with its index. 
            The idea is to pass through the array once and for each number if target - num, i.e. the complement, is still not in the HashMap, 
            then we add the current number to the HashMap and continue. 

            By the time we get to the second number that adds up to the target, our HashMap will also already contain the first number that adds up to the target. 
            So, we found our solution and simply return the indices. 

                Time Complexity: T(n) = O(n)
                Space Complexity: S(n) = O(n)
    """
    def twoSum(self, nums: list[int], target: int) -> list[int]: # type: ignore
        # create a number, index pair
        indexMap = {}

        # iterate through the nums array once
        for i, n in enumerate(nums):
            # if complement, i.e. the second number that adds up to the target is already in the HashMap, we found our solution 
            if target - n in indexMap:
                # return the indices
                return [indexMap[target - n], i]
            
            # if not present yet, add the number in our HashMap
            indexMap[n] = i