"""
    Q: Add Two Numbers

    You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

    The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.

    Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Return the sum of the two numbers as a linked list.

"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """ 
        To add two numbers, we start at each number's digit. 
        We add going digit by digit keeping track of the carry (if any) that is added to the next two digits. 

        We iterate through the lists l1 and l2 until both reach null. We add the valus of both nodes as well as the carry.

        If either of the node's val is Null, use 0 in its place and continue the process keeping track of the carry.

        If we are left with any carry, we add an extra node with that carry value and return the head of the result list


    """
    # Time Complexity: T(n) = O(m + n) where m = len(l1) and n = len(l2)
    # Space Complexity: S(n) = O(1)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # keep track of the carry
        carry = 0
        # create a dummy node
        dummy = ListNode()
        # set our result list to the dummy node
        node = dummy

        # keep moving through l1 and l2
        while l1 or l2:
            
            # l1's digit
            firstOp = l1.val if l1 else 0
            # l2's digit
            secondOp = l2.val if l2 else 0

            # calculate the next digit
            val = firstOp + secondOp + carry
            carry = val // 10
            val = val % 10
            # create the new node
            node.next = ListNode(val=val)
            
            # update the pointers
            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # if we have a carry, create a new node
        if carry:
            node.next = ListNode(val=carry)
        
        # return the head of the result list
        return dummy.next
