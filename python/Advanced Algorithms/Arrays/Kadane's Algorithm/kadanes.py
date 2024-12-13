"""
    Kadane's algorithm is a greedy-dynamic programming algorithm that can be used on an array. 
    It is used to calculate the maximum sum in a subarray ending at a particular position and typically runs in O(n) time, linear.

    Q: Find a non-empty subarray (contigous elements) with the largest sum

"""

# brute force solution runs in O(n^2)
# makes a two-pass on the array with a nested for-loop. For each iteration of the outer loop, the inner loop does linear work. 
def bruteForce(nums: list[int]) -> int:
    maxSum = nums[0]                        # initialize maxSum to the first element in the array
    for i in range(len(nums)):
        curSum = 0                          # keep track of the current sum
        for j in range(i, len(nums)):
            curSum += nums[j]               # update current sum by adding the current element
            maxSum = max(maxSum, curSum)    # update maximum sum by taking the max between maximum so far and current sum 

    return maxSum   # return maximum sum found


# kadane's algorithm runs in O(n)
# makes a one-pass on the array. The idea is to reset the current sum if we ever it to be negative, and to move to a new subarray.
def kadanes(nums: list[int]) -> int:
    maxSum = nums[0]                    # initialize maxSum to the first element in the array
    curSum = 0                          # initialize current sum to 0

    for n in nums:                      # move through each element in the array
        curSum = max(curSum, 0)         # check whether the current sum is negative. If yes, reset it to 0 and move to next subarray
        curSum += n                     # update current sum by adding the current element
        maxSum = max(maxSum, curSum)    # update max sum by taking the max between the current sum and the maximum sum so far

    return maxSum                       # return the largest sum


"""
    Sometimes above question will ask us to actually return the subarray with the largest sum rather than the sum itself. 
    In this case, we can use the same algorithm as above using a left pointer and a right pointer to keep track of the boundaries of a sliding window. 
    
    Our window will make sure that the subarray sum will be non-negative, otherwise we will reset it. And slide the window to a new subarray.
"""

def slidingWindow(nums: list[int]) -> list[int]:
    maxSum = nums[0]        # initialize max sum to the first element in the array
    curSum = 0              # initialize current sum to 0
    maxL, maxR = 0, 0       # keep track of the boundaries of the subarray with largest sum
    L = 0                   # initialize a left pointer

    # move through the array with a rigth pointer
    for R in range(len(nums)):

        if curSum < 0:      # check whether current sum is negative. If yes, reset it and slide the window, i.e. move left pointer where right pointer currently is
            curSum = 0
            L = R
        
        curSum += nums[R]       # update the current sum by adding the current element
        if curSum > maxSum:     # check whether the current sum is greater than the maximum sum so far
            maxSum = curSum     # if yes, update max sum to the current sum
            maxL, maxR = L, R   # update the boundaries of the subarray with largest sum to left and right pointers

    return [maxL, maxR]