"""
    Q: Plus One
    You are given an integer array digits, where each digits[i] is the ith digit of a large integer. It is ordered from most significant to least significant digit, and it will not contain any leading zero.

    Return the digits of the given integer after incrementing it by one.
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # iterate through each num from the back 
        for i in range(len(digits) - 1, -1, -1):
            # if the current digit is at most 8, we can increment it by 1
            if digits[i] < 9:
                digits[i] += 1
                # we can immediately return here, we are done.
                return digits
            # if 9, then we can set it to zero, and continue
            digits[i] = 0
        
        # if we haven't returned yet, our digits are all 0s so we need to add a 1 in front
        return [1] + digits
        