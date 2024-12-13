import heapq
class Solution:
    """
    The idea here is to use a maxHeap as a utility. 

    To build the maxHeap we can heapify using the negative weights of the stones

    We then run the simulation until we have at least 2 stones in the maxHeap to smash. 
        When we smash the stones, if x == y then we do nothing, else if x < y we push x - y to the maxHeap (this is because we are using the negatives of the original weights)
    
    Once the loop completes, we are left with either 1 stone or 0 stones. 

    At this point we can return the absolute value of the weight of the last stone (if any), or simply return 0

    
    Time Complexity: T(n) = O(n log n)
        We are building the heap in O(n) using
        We are also popping/pushing in O(log n) at most n --> therfore the time complexity will be O(n log n)   
    """


    def lastStoneWeight(self, stones: list[int]) -> int:
        self.maxHeap = [-s for s in stones]
        heapq.heapify(self.maxHeap)

        while len(self.maxHeap) > 1:
            # ex. first = -8, second = -5 --> real weights first = 5, second = 8
            x = heapq.heappop(self.maxHeap)
            y = heapq.heappop(self.maxHeap)

            # second - first == 3 which is the real difference between the weights of the two stones
            # however, we still want to push the negative value of their difference, therefore we do first - second
            # so we compare first < second rather than second - first
            if x < y:
                # if stones have different weights push their difference (its negative value)
                heapq.heappush(self.maxHeap, x - y)
        
        # return the absolute value of the weight of the last stone (if any), 0 otherwise     
        return abs(self.maxHeap[0]) if len(self.maxHeap) else 0
    