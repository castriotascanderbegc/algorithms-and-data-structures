"""
    You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.

    Every integer appears exactly once, except for one integer which appears two or more times. Return the integer that appears more than once.

    You must solve the problem without modifying the array nums and uses only constant extra space.

"""
class Solution:
    """
        We can solve below in O(n) time and O(1) space without using extra space and without modifying the input array.

        The question is tricky but we can look at each value in the array as being the pointer to the next value in the array. 
        In this way we can treat the input array as a LinkedList with a cycle. 

        Since each number is in the range from 1 to n, we know each value pointing to the next element/node in the list will not be out of bound. 

        Also, since we know we have n + 1 numbers in the array/list and numbers ranging from 1 no n, then there must be at least one number that is a duplicate. 

        We can use Floyd's Algorithm (Fast and Slow pointers) to detect where is the begininning of the cycle, which will be the number we want to return. 

        input array: [1, 3, 4, 2, 2]

        by treating them as pointers, our LL is: 0 -> 3 -> 2 -> 4 -> 2. We can see there's a cycle starting at node 2. 

        We can now use Floyd's algorithm (Fast and Slow pointers) to detect the cycle and also to find where the cycle starts. 

    """
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow