# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        """ 
            The idea here is to solve the question iteratively using two pointers.
            At each node, we'd like to take the links to the next node and reverse them. 
            So we have the folllwing:
                - 1. pointer to the HEAD node (a.k.a CURR)
                - 2. pointer to the PREV node (initially set to None)

            We move through the linked list until we see a node, and for each node:
                - we first store the next node in a temporary node
                - we take the next node link and reverse it
                - we shift both pointers: 
                        - pointer 2, PREV node to CURR node
                        - pointer 1, CURR node to the next node (temporary node)

            Once we reached the end, and have reversed the entire linked list we can simply return the PREV node, which will be our new HEAD node


            Time Complexity: O(n)
            Space Complexity: O(1)
        """

        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def myBruteForceSolution(self, head: ListNode) -> ListNode:
        """
            The idea here is to use stack to reverse a singly linked list.
            We first traverse the linked list pushing every node in the stack
            We then pop each node form the stack and chain to the new head moving each time to the next node

            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        if not head or not head.next:           # if we have an empty list or only one node in the linked list simply return it
            return head
        stack = []                              # create a stack to push nodes into
        while head:                             # moving through the linked list
            stack.append(head)                  # append entire node in the stack
            head = head.next                    # type: ignore # move forward in the linked list
                                                
        head = stack.pop()                      # point the new head to the laste node of the original linked list
        curr = head                             # set a pointer to this new head
        while len(stack):                       # move through the stack          
            curr.next = stack.pop()             # set the next node to the node popped from the stack
            curr.next.next = None               # next node.next is still pointing to original node in the linked list, need to break chaining
            curr = curr.next                    # move to next node
        return head                             # return the head
        