"""
    Q: Given an integer array nums and an integer k, return the k most frequent elements within the array.

    The test cases are generated such that the answer is always unique.

    You may return the output in any order.

"""
from collections import defaultdict

class Solution:
    """
        Optimal Solution:
            Use a variation of bucket sort. 
            We first create a map to keep track of the occurrences. Then, using the map we create a bucket where each index represents
            the count/occurrence. We will store a list of values having this occurrence. 

            Once the bucket is created, we can pass through it from the back and move backwards 
            and take the elements with top K indices, i.e. count/occurrence

        Time Complexity: O(n)

    """
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = dict()
        bucket = [[] for i in range(len(nums) + 1)]
        res = []

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        for key, occurrence in count.items():
            bucket[occurrence].append(key)

        for i in range(len(bucket) - 1, 0, -1):
            for elem in bucket[i]:
                    res.append(elem)
                    if len(res) == k:
                        return res

            

    """

        Brute force idea: 
            Create a map to keep track of occurrences. Then we can sort the values of our map and take the K largest ones. 
            From these values we can build our result by searching for the keys in our map having these values.
        
        Time Complexity: O(n^2 log n)
        
        Better idea: 
            Utilize a MaxHeap and pop K times to get the largest K elements. 
            Time Complexity: O(n log n)
    """
    def topKFrequentBruteForce(self, nums: list[int], k: int) -> list[int]:
        count = dict()
        res = []
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        values = list(count.values())
        values = sorted(values, reverse=True)[:k]

        for key in count:
            if count[key] in values:
                res.append(key)
            if len(res) == k:
                break
        
        return res