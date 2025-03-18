"""
    Q: Kth Largest Element in an Array
    
    Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.

    By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.

    Follow-up: Can you solve it without sorting?
"""
import heapq
from typing import List
class Solution:
    """
        Brute force: We could sort the array (n log n) first and then find the k-th largest
        Optimal way: 
            We can use a Min-Heap. Iterate through the give input array inserting elements in the array. 
            This will maintain the elements in sorted ascending order (smallest at the top). 
            Any time the size of the heap exceeds k we can pop from it. 

            The k-th largest element is the smallest element among the top k largest elements. 
        
    """
    # Time Complexity: T(n): O(n log k)
    # Space Complexity: S(n): O(k)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # initialize our heap
        heap = []

        # iterate over the given array
        for n in nums:
            # push the current num to the heap
            heapq.heappush(heap, n)
            # if our heap size exceeds k, then pop from it
            if len(heap) > k:
                heapq.heappop(heap)
        # the top of the heap will have the k-th largest element in the array
        return heap[0]
        