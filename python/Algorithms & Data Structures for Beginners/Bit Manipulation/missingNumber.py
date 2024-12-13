"""
    Given an array nums containing n integers in the range [0, n] without any duplicates, return the single number in the range that is missing from nums.

    Follow-up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""
class Solution:
    # Below solution uses an HashSet
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def missingNumberHash(self, nums: list[int]) -> int:
        # create a set with numbers in range O - n, which is the size of the given array, O(n) time
        numSet = set([i for i in range(0, len(nums) + 1)])
        # iterate through the elements in the array, O(n) time
        for n in nums:
            # remove element in the array present in the set, O(1) time
            numSet.remove(n)
        
        # there will be one number left in the set, which is the number missing in the array
        for n in numSet:
            return n

        

    # Below solution uses Bit Manipulation
    # Time Complexity: O(n)
    # Space Complexity: O(1)

    def missingNumber(self, nums: list[int]) -> int:
        res = 0
        # compute the XOR between all the numbers in the range [0,n]
        for i in range(0, len(nums) + 1):
            res ^= i
        # compute the XOR between the result of XOR in the range [0, n] and every number in the array
        for n in nums:
            res ^= n
        
        ### note that if we do XOR of all numbers in [0, n] and all numbers in [0, n] the result should be 0. 


        # the missing number will be the result of this operation  
        return res
        

        
        

