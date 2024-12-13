"""
    Q: Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, 
    and return an array of the non-overlapping intervals that cover all the intervals in the input.
    
    You may return the answer in any order.
    
    Note: Intervals are non-overlapping if they have no common point. 
    For example, [1, 2] and [3, 4] are non-overlapping, but [1, 2] and [2, 3] are overlapping.

"""


from typing import List


class Solution:
    # Time Complexity: T(n) = O(n log n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()            # this takes O(n log n)
        # move through the intervals array
        for i in range(len(intervals)):
            # if our result is still empty, just append the current interval
            if not res:
                res.append(intervals[i])
            else:
                # if overlap with last appended/merged interval
                if res[-1][1] >= intervals[i][0]:
                    # merge resolving the conflict
                    start = min(res[-1][0], intervals[i][0])
                    end = max(res[-1][1], intervals[i][1])
                    # ovverride directly
                    res[-1] = [start, end]
                else:
                    # if no overlap, append the current interval to our result
                    res.append(intervals[i])         
        return res
    

        """
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output """