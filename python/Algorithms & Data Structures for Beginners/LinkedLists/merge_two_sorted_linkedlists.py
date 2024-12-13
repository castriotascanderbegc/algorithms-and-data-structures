# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()                  # create a dummy node that takes care of edge cases if we have empty lists 
        node = dummy                        # set our output list pointer to the dummy node

        while list1 and list2:              # move through the linked lists

            if list1.val < list2.val:       # check if list1 value is smaller than list2 value
                node.next = list1           # set the output list next node to point to list1
                list1 = list1.next          # type: ignore # move through list1
            else:
                node.next = list2           # set the output list next node to point to list2
                list2 = list2.next          # type: ignore # move through list2

            node = node.next                # move with our output list pointer to the next node


        # if we still have either lists, i.e list1 or list2 is not None we need to append its remainder
        # we set the output list next node to the remaining list

        node.next = list1 or list2


        # return start of the output list
        return dummy.next # type: ignore