# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    if version:
        return True
    return False

class Solution:
    """
        We need to find the first bad version in a range of version from 1 <--------> n 
        The importan thing to note here is, any version after a bad version is also bad

        The idea here is to use a simple Binary Search where:
            if our mid is a bad version --> we want to move our right pointer to the left of mid since we know
            all the version in the range mid <----> n are also bad.

            However, we might be already arrived at a solution. So we need to check whether the version prior to
            mid is either bad or not bad, and that is still within our bounds
                if bad --> we can move the right pointer to the left of mid
                if not bad --> we found our solution, mid is the first bad version.


            if our mid is not a vad version --> we move our left pointer to the right of mid since we know all
            the versions in range 1 <----> mid are also not bad 
    """
    def firstBadVersion(self, n: int) -> int:
        # Sets our left and right pointer
        low, high = 1, n
        while low <= high:
            # set the mid point
            mid = low + ((high - low) // 2)
            if isBadVersion(mid):                           # if bad version, move right pointer to the left of mid
                if mid != 1 and not isBadVersion(mid - 1):  # check whether mid is already the solution
                    return mid
                high = mid - 1
            else:
                low = mid + 1                               # if not bad version, move left pointer to the right of mid

        # return our solution
        return mid                                     
