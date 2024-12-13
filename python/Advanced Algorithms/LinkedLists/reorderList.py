"""
    Q: You are given the head of a singly linked-list.

    The positions of a linked list of length = 7 for example, can intially be represented as:

    [0, 1, 2, 3, 4, 5, 6]

    Reorder the nodes of the linked list to be in the following order:

    [0, 6, 1, 5, 2, 4, 3]

    Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

    [0, n-1, 1, n-2, 2, n-3, ...]

    You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
        The idea to solve this is to break it down in 3 diff steps:
            1. Using fast and slow pointers we find the middle of the list
            2. We reverse the 2nd half of the list
            3. Using two pointers we merge the two halves of the lists in the required order

        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next    # initialize fast and slow pointers

        # find the middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        

        second = slow.next              # initialize second pointer to next half of the array (node next to middle node)
        prev = slow.next = None         # break the link between middle node and the node next to it

        # reverse 2nd half of the list 
        while second:   
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first, second = head, prev      # initialize the two pointers at the beginning of the two halves of the list
        
        # merge the two halves of the list
        while second:
            tmp1 = first.next           # save first pointer next node
            tmp2 = second.next          # save second pointer next node

            first.next = second         # set first.next to point to second pointer node
            second.next = tmp1          # set second.next to point to first pointer next node

            first = tmp1                # update first pointer
            second = tmp2               # update second pointer

        
        