"""
    The idea behind fixed size sliding window is two maitain two pointers that are k apart from each other
    and fit a certain constraint. 

    Ex: Question: Given an array, return true if there two elements within a window of size k that are equal (duplicates)

"""

# brute force - time complexity: O(n * k) where k, the size of the window, k <= n
# consider every subarray of size k and check for duplicates

def closeDuplicatesBruteForce(nums: list[int], k: int) -> bool:
    for L in range(len(nums)):
        for R in range(L + 1, min(len(nums), L + R)):   # read comment below *** 
            if nums[L] == nums[R]:
                return True
    return False


# *** here we take the minimum between the size of the array and 
# the k offset from the current position of the left pointer
# so we don't go out of bounds


# fixed sliding window approach - time complexity: O(n) with HashSet
# space complexity: O(k), we can only have at most k distinct elements in the HashSet
def closeDuplicates(nums: list[int], k: int) -> bool: 
    window = set()      # use a HashSet to store elements currently in the window of size <= k
    L = 0               # initialize our left pointer

    # pass through the array with a right pointer
    for R in range(len(nums)):
        # if the size of the current window is greater than k, 
        # move left pointer forward and remove element not in the window anymore 
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:   # check whether current element already exists in our window, i.e. HashSet
            return True
        window.add(nums[R])     # if not, add current element to the current window
    
    return False



"""
    Given an array of integers arr and two integers k and threshold, 
    return the number of sub-arrays of size k and average greater than or equal to threshold.
"""

# Using above fixed size sliding window technique
# Linear time complexity - T(n): O(n)
# we make a single pass on the array
def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
    total = 0   # initialize our current total
    res = 0     # initialize our result
    L = 0       # initialize our left pointer

    # move through the array with both pointers
    for R in range(len(arr)):
        # update current total
        total += arr[R]

        # check whether window exceeded size k
        if R - L + 1 > k:
            # if so, remove current element at L from the total
            total -= arr[L]
            # increment L 
            L += 1

        # check whether our window total is greater or equal to the given threshold
        if R - L + 1 == k and (total // k) >= threshold:
            # if so, increment our result
            res += 1
    # return result
    return res
