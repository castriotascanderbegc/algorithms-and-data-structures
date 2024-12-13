"""
    Given an array of integers nums, calculate the pivot index of this array.
    The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
    If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
    Return the leftmost pivot index. If no such index exists, return -1.
"""

class Solution:
    # Linear Time Complexity: T(n) = O(n)
    # We make linear time to build the prefix and 
    # linear time for a single pass through the array
    def pivotIndex(self, nums: list[int]) -> int:
        prefix = self.buildPrefix(nums)     # precompute the prefix O(n)

        # pass through the array once
        for i in range(len(nums)):
            # edge case if the index is on the either edge of the array  
            if prefix[0] == prefix[len(prefix) - 1]:
                return 0
            # check whether prefix at current index is equal to entire array prefix - prefix to the left of the index
            # if so we found our pivot index as left sum == right sum
            if (i > 0 and 
            prefix[i] == prefix[len(nums) - 1] - prefix[i - 1]):
                return i
        # pivot not found
        return -1
    
    # Neetcode solution - Linear Time Complexity: T(n) = O(n)
    # We make linear time to compute the sum of the entire array
    # linear time for a single pass through the array
    def pivotIndexNeetcode(self, nums: list[int]) -> int:
        total = sum(nums)   # compute sum of the entire array
        leftSum = 0         # initialize left sum

        # pass through the array once
        for i in range(len(nums)):
            # compute current right sum
            rightSum = total - nums[i] - leftSum

            # check whether left sum and right sum are equal
            if leftSum == rightSum:
                # we found the pivot index
                return i

            # update left sum by adding current element
            leftSum += nums[i]
        
        # pivot index not found
        return -1

    # build the prefix sum of an array
    def buildPrefix(self, nums: list[int]) -> list[int]:
        prefix = []
        total = 0

        for n in nums:
            total += n
            prefix.append(total)
        
        return prefix