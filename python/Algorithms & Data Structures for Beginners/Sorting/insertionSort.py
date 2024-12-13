# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    
    # Python implementation of Insertion Sort
    def insertionSort(self, arr: list) -> list:
	# Traverse through 1 to len(arr)
        for i in range(1, len(arr)):
            j = i - 1
            while j >= 0 and arr[j + 1] < arr[j]:
                # arr[j] and arr[j + 1] are out of order so swap them 
                tmp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = tmp
                j -= 1
        return arr
    
    def useInsertionSort(self, pairs: list[Pair]) -> list[list[Pair]]:
        # To store intermediate results
        results = []
        # Loop through the array of Pair
        for i in range(len(pairs)):
            j = i - 1
            # Keep swapping current key to the left if smaller than its left neighbor 
            while j >= 0 and pairs[j + 1].key < pairs[j].key:
                # swap
                # pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                temp = pairs[j + 1]
                pairs[j + 1] = pairs[j]
                pairs[j] = temp
                j -= 1

            # Clone and save entire state of the array at this point
            # pairs is an object that we are continously modifying  
            results.append(pairs[:])     
        return results
