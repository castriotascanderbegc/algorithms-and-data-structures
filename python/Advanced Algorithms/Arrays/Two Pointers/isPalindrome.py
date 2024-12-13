"""
    Question: Check if the given array is a palindrome. 
"""

# two pointers technique - linear time
# time complexity: T(n) = O(n) - we make a single pass on the array

def isPalindrome(array: list) -> bool:
    # initialize left and right pointers
    L, R = 0, len(array) - 1

    # repeat loop until pointers cross each other
    while L < R:
        # check whether elem at L matches elem at R
        if array[L] != array[R]:
            # if no, array is not a palindrome
            return False

        # if so, increment L and decrement R
        L += 1
        R -= 1

    # all elem have been checked, the array is a palindrome  
    return True