# Singly Linked List Node
class ListNode:
    def __init__(self, val=None, next_node=None) -> None:
        self.val = val
        self.next = next_node

# Implementation for Singly Linked List 
class LinkedList:
    def __init__(self) -> None:
        # Init the list with a 'dummy' node which makes 
        # removing a node from the beginning of list easier.

        # a dummy node helps us a lot in different edge cases
        # such as when we have an empty list 
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        # since we have our head pointing to the dummy node
        # let's set our curr pointer to head.next (not the dummy node)
        curr = self.head.next
        i = 0
        # move our pointer until we reached the index
        while curr:
            # if we reached the index, we want to return the value
            if i == index:
                return curr.value
            # move pointer forward
            curr = curr.next
            # increment i pointer
            i += 1
        return -1 # index out of bounds

    def insertHead(self, val: int) -> None:
        # create a new node
        new_node = ListNode(val)
        # set new node at the head of the linked list
        # self.head == dummy node, so we set right after the dummy node
        new_node.next = self.head.next
        self.head.next = new_node

        # edge case. What if our linked list was initially empty before insertion?
        if not new_node.next:
            # we need to set the tail node to the last node we inserted
            self.tail = new_node
        
    def insertTail(self, val: int) -> None:
        # set the tail.next to the new Node
        self.tail.next = ListNode(val)
        # update our tail pointer to node just inserted
        self.tail = self.tail.next
    
    def remove(self, index: int) -> bool:
        # start at the dummy node since we want to have a reference of node before target
        # when we remove a node from a LinkedList we need to a reference to the node before the target
        curr = self.head
        i = 0
        # 
        while i < index and curr:
            # goal here is to move curr to the node before target node
            i += 1
            curr = curr.next
          
        # check if we are at the node before target node
        # check if we also have the target node
        if curr and curr.next:
            # check if we are trying to remove the tail
            if curr.next == self.tail:
                # if we removed the tail
                # we need to update our tail back to the node before the deleted node
                self.tail = curr
            # set curr.next to point to the node after the target
            curr.next = curr.next.next
            return True
       
        return False # out of bounds
    

    def getValues(self) -> list[int]:
        # traversal over the linked list
        values = []
        curr = self.head.next
        if curr:
            values.append(curr.val)
            curr = curr.next
        return values