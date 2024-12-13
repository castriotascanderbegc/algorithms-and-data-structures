# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution: 
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        ### Recursive Solution

        # base case
        if not head:                # if we don't have a Node to verse, we simply return Null 
            return None
        
        newHead = head              # Set the new head
        if head.next:               # if we have a sub-problem
            newHead = self.reverseList(head.next) # recursive call on the next node in the list 
            head.next.next = head   # reverse the link between the next node and the head 
        head.next = None
        return newHead