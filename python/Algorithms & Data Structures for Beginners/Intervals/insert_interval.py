"""
    Q: You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] represents 
    the start and the end time of the ith interval. intervals is initially sorted in ascending order by start_i.

    You are given another interval newInterval = [start, end].
    Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i 
    and also intervals still does not have any overlapping intervals. 
    
    You may merge the overlapping intervals if needed.

    Return intervals after adding newInterval.

    Note: Intervals are non-overlapping if they have no common point. 
    For example, [1,2] and [3,4] are non-overlapping, but [1,2] and [2,3] are overlapping.

"""
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # edge case: newInterval comes before intervals[i], ex: newInterval: [2, 4], intervals[i]: [5, 6]
            # this case we can insert the newInterval to our result, and return the remaining list
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # edge case: newInterval comes after intervals[i], ex: newInterval: [7, 9], intervals[i]: [5, 6]
            # then we can append current interval to our result and continue
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # if intervals[i] and newInterval are overlapping
            # then we need to merge them
            else:
                newInterval = [
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1])
                ]

        # we can now append the newInterval
        res.append(newInterval)

        return res
