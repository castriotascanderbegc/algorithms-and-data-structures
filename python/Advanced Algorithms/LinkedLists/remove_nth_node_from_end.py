"""
    Q: You are given the beginning of a linked list head, and an integer n.

    Remove the nth node from the end of the list and return the beginning of the list.
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Linear Time O(n)
    # Two pointers techinique
    # One pass
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)   # create a dummy node from where left should start
        left = dummy                # initialize left pointer at the dummy node
        right = head                # initialize right pointer at the head

        # we want to traverse the list with left and right having right + n

        # move right pointer n steps ahead
        while n > 0:
            right = right.next
            n -= 1
        
        # move left and right pointers
        while right:
            left = left.next
            right = right.next
        
        # at this point left will point at the node right before the node to be deleted
        # delete the node
        left.next = left.next.next

        # return the updated linked list
        return dummy.next

    # Linear Solution O(n)
    # Two Pointers
    # Two pass
    def removeNthFromEndTwoPass(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if we only have one node in the list
        # set the head to None
        if not head.next:
            head = None
        
        # if we have multiple nodes in the list
        else:
            # initialize pointers at the head
            curr, left, right = head, head, head

            # let's count how many nodes we have
            # first pass
            count = 0
            while curr:
                curr = curr.next
                count += 1

            # if number of nodes is equal to the nth node to delete
            # ex: [1, 2], n = 2
            # out: [2]
            if count == n:
                # we can simply return head.next
                return head.next

            # move through the list with left and right pointers count - n times
            for i in range((count - n)):
                left = right
                right = right.next
        
            # now at this point right points to node to be removed and left points to prev node
            next_node = right.next if right else None
            left.next = next_node
        return head
