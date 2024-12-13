"""
    Q: You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

    [3,4,5,6,1,2] if it was rotated 4 times.
    [1,2,3,4,5,6] if it was rotated 6 times.
    Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

    You may assume all elements in the sorted rotated array nums are unique,

    A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

"""
class Solution:
    """
        A rotated sorted array will have two sorted portions, a left and a right sorted portions. 
        Ex: [3,4,5,6,1,2] --> [3,4,5,6] [1,2]   target: 1


        We first need to understand if our mid is in the left or right portion. 
        We then need to check the case if our target is on the right/left side of mid

        We update the pointers based on above cases. 

    """
    # Binary Search - O(log n) time complexity
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1    # initialize low and high pointers 
        
        # pass through the array until pointers cross
        while low <= high:
            # calculate the mid point index
            mid = low + (high - low) // 2 

            # check if we found the target
            if nums[mid] == target: 
                return mid
            
            # check if mid is in the left sorted portion of the array
            if nums[low] <= nums[mid]:
                # is our target on the right side of mid ? 
                if target < nums[low] or target > nums[mid]:
                    low = mid + 1
                else:   # our target is on the left side of mid
                    high = mid - 1
            
            else: # mid is in the right sorted portion of the array
                # is our target on the left side of mid ? 
                if target > nums[high] or target < nums[mid]:
                    high = mid - 1
                else:   # our target is on the right side of mid
                    low = mid + 1
            
        
        return -1