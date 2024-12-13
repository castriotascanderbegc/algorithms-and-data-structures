# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""

    In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the
    (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

    For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with 
    twins for n = 4.

    The twin sum is defined as the sum of a node and its twin.

    Given the head of a linked list with even length, return the maximum twin sum of the linked list.

"""


from typing import Optional


class Solution:
    # Below is a brute force using an extra array
    # Time Complexity: O(n)
    # Space Complexity: O(n) - we allocate an extra array
    def pairSumBruteForce(self, head: Optional[ListNode]) -> int:
        # if not empty linked list
        if head:
            nodes = []  # allocate an extra array
            # move through the linked list
            while head:
                # append the node's value to our array
                nodes.append(head.val)
                # move to next node
                head = head.next
            
            L, R = 0, len(nodes) - 1            # initialize two pointers L and R
            # O(n/2 time)
            maxSum = nodes[L] + nodes[R]        # initialize max sum to be edges of the array/linked list
            while L < R:
                # compute the twin sum
                twinSum = nodes[L] + nodes[R]
                # update the maximum twin sum
                maxSum = max(maxSum, twinSum)
                L += 1                          # increment left pointer
                R -= 1                          # decrement right pointer
            
            return maxSum

        return 0

    # Below is the optimal solution using Fast and Slow pointers technique
    # Time Complexity:  O(n)
    # Space Complexity: O(1) - we don't allocate extra space
    def pairSum(self, head: Optional[ListNode]) -> int:

        """
            using fast and slow pointers technique we can solve without using extra space in linear time.

            Ex: 4 -> 3 -> 2 -> 5 -> 1 -> 8

            Twin pairs: 4, 8
                        3, 1
                        2, 5

            Using fast and slow pointers we know by the end of the linked list we will be able to get to the middle point 
            with the slow pointer and point to 5 -> 1 -> 8 portion of the linked list

            We need the first half in the reverse order (2 -> 3 -> 4). We can do that in place using a temp variable

            We can then traverse the two halves of the linked list at the same time and calculate the maximum twin sum
        """


        fast, slow = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        res = 0
        while slow:
            res = max(res, slow.val + prev.val)
            slow = slow.next
            prev = prev.next
        
        return res
