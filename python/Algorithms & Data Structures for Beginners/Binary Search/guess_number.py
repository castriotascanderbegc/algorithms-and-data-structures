# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

PICK = 4
def guess(num: int) -> int:

    if num > PICK:
        return -1
    elif num < PICK:
        return 1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        # Range goes from 1 <--------> n
        low, high = 1, n
        while low <= high:
            # let's compute the mid point
            mid = low + ((high - low) // 2) # also (low + high) // 2
            if guess(mid) > 0:          # guess < pick 
                low = mid + 1
            elif guess(mid) < 0:        # guess > pick
                high = mid - 1
            else:
                return mid              # guess == pick
        return -1