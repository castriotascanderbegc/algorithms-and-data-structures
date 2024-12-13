"""
    Q: Given an array of intervals intervals where intervals[i] = [start_i, end_i], 
    return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

    Note: Intervals are non-overlapping even if they have a common point. For example, [1, 3] and [2, 4] are overlapping, 
    but [1, 2] and [2, 3] are non-overlapping.

"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # let's first sort the input array intervals
        intervals.sort(key=lambda pair: pair[0])

        # initialize our result
        res = 0

        # have a pointer to last visited end
        prevEnd = intervals[0][1]

        # iterate through the intervals array
        for start, end in intervals[1: ]:
            # if no overlap, simply update the prevEnd pointer to current interval
            if start >= prevEnd:
                prevEnd = end
            else:
                # we have an overlap, increment our result
                res += 1
                # keep the interval with smaller end
                prevEnd = min(prevEnd, end)
        return res

        