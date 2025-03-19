"""
   Q: You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

    [3,4,5,6,1,2] if it was rotated 4 times.
    [1,2,3,4,5,6] if it was rotated 6 times.
    Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

    Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

    A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time? 

"""
class Solution:
    # Binary Search - O(log n) time complexity
    def findMin(self, nums: list[int]) -> int:
        low, high = 0, len(nums) - 1            # initialize low and high pointers 
        currMin = float("inf")                  # initialize curr min to highest number possible

        # pass through the array until pointers cross
        while low < high:
            # calculate the mid point index
            mid = low + (high - low) // 2 
            # calculate current minimum
            currMin = min(nums[mid], currMin)

            # if current number at the middle is greater than number at the end
            # minimum will be toward the right part of mid 
            if nums[mid] > nums[high]:
                low = mid + 1           # update low pointer
            else:
                # minimum will be toward the left part of mid
                high = mid - 1          # update low pointer
        
        return int(min(nums[low], currMin)) # return the minimum number found