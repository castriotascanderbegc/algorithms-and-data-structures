"""
    A prefix sum if a super useful technique that can be used on arrays. 
    For example, it is useful when we want to retrieve the sum of a subarray ending at an arbitrary index, say i. 

    The basic idea is to to create an array and fill it up such that each value at its i-th index is the running sum of 
    another subarray that starts at index 0 and goes up to and including the i-th index. 
"""
class Prefix:
    """
        To build our prefix sum, given an array nums add each value to a curren total.
        For each iteration, append the current total to the prefix array. 

        Time Complexity: O(n)
    """
    def __init__(self, nums: list[int]) -> None:
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)
    

    """
        To calculate the sum of a subarray in the range [left, right]. 
        We can return prefix[right] - prefix[left - 1] (if left > 0, otherwise we use 0 for prefix[left - 1]). 
        The -1 is needed to exlude the running sum of all the values before left. 

        Time Complexity: O(1)
    """
    def rangeSum(self, left: int, right: int) -> int:
        rightPrefix = self.prefix[right]
        leftPrefix = self.prefix[left - 1] if left > 0 else 0

        return (rightPrefix - leftPrefix)
    
