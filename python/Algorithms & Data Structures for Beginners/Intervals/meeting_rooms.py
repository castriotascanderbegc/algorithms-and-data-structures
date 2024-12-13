"""
    Q: Given an array of meeting time interval objects consisting of start and end times 
    [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

"""


# Definition of Interval:
from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    # T(n): O(n log n) since we are sorting the input array
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort the input array of intervals based on the start time
        intervals.sort(key = lambda i: i.start)

        # loop through the intervals and 
        # compare intervals[i].end with intervals[i + 1].start to check if they overlap
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                # if they overlap, immediately return False
                return False
        return True


