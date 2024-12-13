"""

    Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

    Each product is guaranteed to fit in a 32-bit integer.

    Solve the question in O(n) without using the division operator. 
"""
class Solution:

    """
        We can take an example:
            nums = [1,2,4,6]

            out[0] = out[1] * out[2] * out[3] = 48
            out[1] = out[0] * out[2] * out[3] = 24
            out[2] = out[0] * out[1] * out[3] = 12
            out[3] = out[0] * out[1] * out[2] = 8

        prefix = [1,2,8,24] where i = 0,1,2,3
        postfix = [6,24,48,48] where i = 3,2,1,0

        we know that essentially out[2] = prefix[2 - 1] * prefix[2 + 1] = 12

        Therefore, we can have a first pass on the array once calculating the prefix and storing it in our result

        Take prefix[-1] = 1

        Then, we can have a second pass on the array backward computing the postfix at the index i and multiplying by the current result at index i (containing the prefix at i - 1)
        

    """

    # Optimal Solution - Linear Time O(n)
    # No divion operator
    # Space Complexity - O(1) excluding the output array res
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)

        for i in range(1, len(nums)):
            res[i] = nums[i - 1] * res[i - 1]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
