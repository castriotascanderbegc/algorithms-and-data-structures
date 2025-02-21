"""
    Q: Koko Eating Bananas

    You are given an integer array piles where piles[i] is the number of bananas in the ith pile. 
    You are also given an integer h, which represents the number of hours you have to eat all the bananas.

    You may decide your bananas-per-hour eating rate of k. 
    Each hour, you may choose a pile of bananas and eats k bananas from that pile. 
    If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

    Return the minimum integer k such that you can eat all the bananas within h hours.

"""

from math import ceil
from typing import List
class Solution:
    # Time Complexity: T(n) = O(m log(n))
    # Space Complexity: S(n) = O(1)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
            Since we know h > len(piles), we first need to find an upper bound for our answer, k
            In this case, the upper bound for k, the minimum integer k such taht Koko can eat all bananas within h hours,
            is the maximum size of all the piles.

            This is true because if Koko can eat the larget pile in hour, then she can eat any other pile in one hour only.

            We can then perform binary search from 1 to this upper bound - max(piles) and find the minimum k so that Koko can eat all bananas.

        """

        # initialize lower and upper bound of our possible k
        lower, upper = 1, max(piles)
        # initialize our result
        res = upper
        # perform binary search
        while lower <= upper:
            # calculate middle value k
            k = (lower + upper) // 2
            hours = 0
            # loop over the piles
            for p in piles:
                hours += ceil(p / k)
            # check if we found our k
            if hours <= h:
                res = min(res, k)
                upper = k - 1
            else:
                lower = k + 1
        # return our result
        return res
