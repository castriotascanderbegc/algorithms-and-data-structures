class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None
class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail # type: ignore
        self.tail.prev = self.head # type: ignore

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new_node = ListNode(value)
        last_node = self.tail.prev

        last_node.next = new_node # type: ignore
        new_node.prev = last_node
        new_node.next = self.tail # type: ignore
        self.tail.prev = new_node # type: ignore

    def appendleft(self, value: int) -> None:
        new_node = ListNode(value)
        first_node = self.head.next

        self.head.next = new_node # type: ignore
        new_node.prev = self.head # type: ignore
        new_node.next = first_node
        first_node.prev = new_node # type: ignore
        
        

 
    def pop(self) -> int:

        if self.isEmpty():
            return -1

        last_node = self.tail.prev
        value = last_node.val # type: ignore
        prev_node = last_node.prev # type: ignore

        prev_node.next = self.tail
        self.tail.prev = prev_node

        return value

    def popleft(self) -> int:

        if self.isEmpty():
            return -1
        
        first_node = self.head.next
        value = first_node.val # type: ignore
        next_node = first_node.next # type: ignore

        self.head.next = next_node
        next_node.prev = self.head
        
        return value
        
