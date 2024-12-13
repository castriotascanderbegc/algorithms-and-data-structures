class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Implementation for Doubly Linked List
class LinkedList:
    def __init__(self):
        # Init the list with 'dummy' head and tail nodes which makes 
        # edge cases for insert & remove easier.
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail # type: ignore
        self.tail.prev = self.head # type: ignore
    
    def insertFront(self, val):
        newNode = ListNode(val)
        newNode.prev = self.head # type: ignore
        newNode.next = self.head.next

        self.head.next.prev = newNode # type: ignore
        self.head.next = newNode # type: ignore

    def insertEnd(self, val):
        newNode = ListNode(val)
        newNode.next = self.tail # type: ignore
        newNode.prev = self.tail.prev

        self.tail.prev.next = newNode # type: ignore
        self.tail.prev = newNode # type: ignore

    # Remove first node after dummy head (assume it exists)
    def removeFront(self):
        self.head.next.next.prev = self.head # type: ignore
        self.head.next = self.head.next.next # type: ignore

    # Remove last node before dummy tail (assume it exists)
    def removeEnd(self):
        self.tail.prev.prev.next = self.tail # type: ignore
        self.tail.prev = self.tail.prev.prev # type: ignore

    def print(self):
        curr = self.head.next
        while curr != self.tail:
            print(curr.val, " -> ") # type: ignore
            curr = curr.next # type: ignore
        print()