"""
    Q: Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), 
    find the minimum number of days required to schedule all meetings without any conflicts.

    Solution uses a Two Pointers techinique
"""

# Definition of Interval:
from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    # Time Complexity: O(n log n)
    # Space Complexity: O(n)
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # we can store both start and end times, have them sorted
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        
        # initialize our count and res. res will be the max count of concurrent meetings
        res, count = 0,0
        # utilize two pointers to iterate over start and end arrays
        s = e = 0
        
        # move through the arrays until we reached the end
        while s < len(intervals):
            # if there's an overlap between meetings
            if start[s] < end[e]:
                # we move along start
                s += 1
                # we increase our count of meetings started
                count += 1
            else:
                # we move along end
                e += 1
                # we decreaed our count of meetings started, i.e. a meeting has just ended 
                count -= 1

            # keep track of the max number of concurrent meetings
            res = max(res, count)
        
        return res
