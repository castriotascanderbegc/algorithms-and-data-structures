"""
    Let's take a look at a problem that can be solved using the two heaps approach.
    Finding the median of a continuous stream of numbers is a good example.
    
    Q: Implement a Median finder, where new values are inserted into the set, and you have to getMedian from that set.

"""

import heapq

class Median:
    def __init__(self):
        self.small, self.large = [], []
    
    def insert(self, num):
        # insert in the max heap
        heapq.heappush(self.small, -1 * num)

        # swap to minheap if needed
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # handle uneven size
        if len(self.small) > len(self.large) + 1:
           val = -1 * heapq.heappop(self.small)
           heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.small, -1 * val)

    def getMedian(self):
        # if number of elements is odd
        # MaxHeap is greater
        if len(self.small) > len(self.large): 
            return -1 * self.small[0]
        # MinHeap is greater
        elif len(self.large) > len(self.small):
            return self.large[0]
        
        # if numebr of elements is even, return averagae of min and max of respective heaps
        return (-1 * self.small[0] + self.large[0]) / 2