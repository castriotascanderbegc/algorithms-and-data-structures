class Solution:
    # Implementation of Quick Sort
    def mergeSort(self, arr: list, start: int, end: int) -> list:
        # Base case: len(array) = 1
        if end - start + 1 <= 1:
            return arr
        
        # pick the pivot element at the end of the array
        pivot = arr[end]

        # left pointer 
        left = start
        
        # Partition the array: elements smaller than pivot on the left side
        for i in range(start, end):
            if arr[i] < pivot:

                # swap 
                temp = arr[left]
                arr[left] = arr[i]
                arr[i] = temp

                # increment left pointer
                left += 1

        # Move pivot in-between left & right sides
        # left (all elements to the left are smaller)
        # right (all elements to the right are greater)
        arr[end] = arr[left]
        arr[left] = pivot

        # recursive call on the left partition
        self.mergeSort(arr, start, left - 1)

        # recursive call on the right partition
        self.mergeSort(arr, left + 1, end)
        
        return arr