class Solution:
    # Implementation of MergeSort
    def mergeSort(self, arr: list, s: int, e: int) -> list:
        # Base case: len(array) = 1
        if e - s + 1 <= 1:
            return arr
        
        # compute the middle index of the array
        m = (s + e) // 2

        # recursive call to sort left subarray
        self.mergeSort(arr, s, m)

        # recursive call to sort right subarray
        self.mergeSort(arr, m + 1, e)

        # merge sorted halfs
        self.merge(arr, s, m, e)

        return arr
    
    # Merge array in place
    def merge(self, arr: list, s: int, m: int, e: int) -> None:
        i = 0   # left sub-array pointer
        j = 0   # right sub-array pointer
        k = s   # next element to move in the array

        # temporary copy of left sub-array
        L = arr[s: m + 1]

        # temporary copy of right sub-array
        R = arr[m + 1: e + 1]

        # merge the two sorted halfs into the original array
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1

            else:
                arr[k] = R[j]
                j += 1
        
            k += 1

        # one of the two halfs will have remaining elements 

        # if remaining elements in the left sub-array
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # if remaining elements in the right sub-array 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1