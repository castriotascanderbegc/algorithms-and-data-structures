"""
    You are given a non-empty array of integers nums. Every integer appears twice except for one.

    Return the integer that appears only once.

    You must implement a solution with O(n) runtime complexity and use only O(1) extra space

-----------------------------------------------------------------------------------------------------------------------------------

If we didn't have O(1) extra space constraint, we could use a HashSet and going through the array, we could add each number to the HashSet 
and remove any duplicate seen in the HashSet. At the end, the HashSet will be left with the number appearing once in the array.  


However, using bit manipulation we can solve this question in O(1) extra space. 

We can make use of the XOR operation. Properties: n XOR n = 0, n XOR 0: n

We can go through the array and XOR all numbers to each other. The result of these operations will be the number appearing once in the array. 
The reason is, since n XOR n = 0, the duplicates number in the array will cancel them out when XORing. Thereore, leaving the unique number as a result of the operation. 

  
"""
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0

        for n in nums:
            res ^= n
        
        return res
    