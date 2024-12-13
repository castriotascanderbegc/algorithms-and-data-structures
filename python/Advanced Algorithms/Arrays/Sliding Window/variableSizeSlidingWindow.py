"""
    The variable size sliding window is useful when we don't have a fixed size window and 
    we need to keep expanding our window as long as our window meets a certain constraint. 

    Ex. Question: Find the length of the longest subarray with the same value in each position. 
"""

# Time Complexity: O(n) - using two pointers we make a single pass on the array
def longestSubarray(nums: list[int]) -> int:
    maxLength = 0           # initialize length of longest subarray 
    L = 0                   # initialize left pointer

    # make a single pass through the array using a right pointer
    for R in range(len(nums)):
        # if we encounter a new value, stop expanding the window
        if nums[L] != nums[R]:
            L = R   # bring left pointer to our right pointer. we know each value before was a duplicate
        
        maxLength = max(maxLength, R - L + 1)   # take the max lenght between current length (R - L + 1) and maximum length so far
    
    return maxLength



"""

    A more classic and complex example of variable size sliding window is the following. 

    Ex: Question: Find the minimum length subarray, where the sum is greater or equal to the target. Assume all values are positive. 
"""


# Time Complexity: O(n) - using two pointers we make a single pass on the array
# The inner loop does not necessarily run n times at each iteration. 
# In this case, we look at the amortised run, i.e. the total number of iterations of the inner loop is n times. 
# Therefore, both pointers move at most n times, making the time complexity linear

def shortestSubarray(nums: list[int], target: int) -> int:
    L, total = 0, 0             # initialize left pointer and current subarray sum
    length = float("inf")       # initialize length of the subarray to positive infinity

    # make a single pass through the array with the right pointer 
    for R in range(len(nums)):
        total += nums[R]        # update current subarray sum with current element
        # keep shrinking the current window if the current total is greater or equal to the targer
        # i.e. keep shrinking the current window if the window meets the constaint
        # we do this by incrementing the left pointer, and reducing the current subarray sum
        while total >= target:
            length = min(R - L + 1, length)         # find the minimum length between the current length of the window and the minimum length so far
            total -= nums[L]                        # reduce the current subarray sum when shrinking current window
            L += 1                                  # shrink current window by incrementing left pointer
    
    return 0 if length == float("inf") else length
        


"""
    Q: Given a string s, find the length of the longest substring without duplicate characters.

    A substring is a contiguous sequence of characters within a string.
"""
class Solution:
    """
        Here we can use a variable size sliding window technique with 2 pointers. 
        The idea is to use a window, and in our case since we need to track duplicates we can use a set. 
        We keep removing duplicates from the window-set and shrinking the window from the left by incrementing the left pointer. 
        Once we don't see the duplicates, we can add the element in the window-set and update our max substring length.
    """

    # Sliding Window Technique - Linear Time O(n)
    # Space Complexity: O(n) since we allocate extra space for the set. Potentially we could have all unique chars in the input string
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()      # initialize our window-set
        maxLength = 0       # initialize our max substring length
        L = 0               # initialize left pointer

        # pass through the array once with the right pointer
        for R in range(len(s)):
            # keep shrinking the window until we see a duplicate in our window-set (and remove the duplicate)
            while s[R] in window:
                window.remove(s[L]) # remove the duplicate
                L += 1              # shrink the window from the left

            # add the element to the window-set
            window.add(s[R])        
            # update max substring length
            maxLength = max(maxLength, R - L + 1)
    
        return maxLength
        


            
    
