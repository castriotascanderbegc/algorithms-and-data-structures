import heapq
class KthLargest:

    """
        Time Complexity of the Constructor: T(n): O(n log n)

            heapify -> it is going to take O(n) to build the entire heap
            then we need to pop potentially n - k values from the heap, to have the heap of size K. 
            each pop poperation is requiring us O(log n) time

            Therefore, it will require us O(n log n) for the constructor

        Time Complexity of the add method: T(n): O(log n)

            it will take us O(log n) to push the value in the heap
            it will take us O(log n) to pop the value from the heap
            it will take us O(1) to read the minium value in the heap

            Therefore, it will require us O(log n) for each add operation

    """


    def __init__(self, k: int, nums: list[int]):
        # create a minHeap with the K largest values, i.e. Size K
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        # need to remove len(minHeap) - k smallest values in the minHeap to only have the K largest values
        # until length of the minHeap is greater than k
        while len(self.minHeap) > self.k:
            # pop the minimum value
            heapq.heappop(self.minHeap)

        # at this point our minHeap only contains the K largest values

    def add(self, val: int) -> int:
        # push the value in the minHeap 
        heapq.heappush(self.minHeap, val)
        # if we now have more than K elements in the heap
        if len(self.minHeap) > self.k:
            # pop from the heap to keep the K largest elems
            heapq.heappop(self.minHeap)
        
        # the smallest element will be at index 0, at the root of the minHeap of the K largest values
        return self.minHeap[0]