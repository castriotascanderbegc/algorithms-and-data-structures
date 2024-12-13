"""
    The concept behind fast and slow pointers is:
        we have a fast and slow pointers that can start at same or different locations.
        However, fast pointer will run (move) twice as fast as the slow pointer. 

"""


### Middle of a Linked List

# Q: Find the middle of a linked list

class Node:
    def __init__(self, value = None, next = None) -> None:
        self.value = value
        self.next = next

# Time Complexity: T(n): O(n)
# note, if the length of the list is even and we want the left-most node of the two middle ones
# we can start with slow at the head and fast starting at slow.next
def middleOfList(head: Node) -> Node:
    slow, fast = head, head     # initialize fast and slow pointer at the head
    # move fast and slow pointers until fast reaches the end of the list
    while fast and fast.next:
        slow = slow.next        # slow pointer move once
        fast = fast.next.next   # fast pointer move twice
    
    # by the time we reached the end, slow pointer will be at the middle
    return slow

### Cycle Dectetion 

# Q: Determine if a linked list has a cycle

# Time Complexity: T(n): O(n)
# Space Complexity: S(n): O(1)
def hasCycle(head: Node) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # if there's a cycle. In a circular path, fast will catch up with slow as it moves twice as fast as slow pointer
        if fast == slow:
            return True
    return False

# brute force using a HashSet
# Time Complexity: T(n) = O(n)
# Space Complexity: S(n) = O(n) we allocate a HashSet
def hasCycleHashSet(head: Node) -> bool:
    visited = set()
    # move until the end of the list
    while head:
        # if node has already been visited, it's a cycle
        if head in visited:
            return True
        # add node to the HashSet
        visited.add(head)
        # move pointer
        head = head.next
    return False


### Get head of a cycle

# Q: Determine if a linked list has a cycle and return the head of the cycle

def getCycleStart(head: Node) -> Node:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # if fast and slow meet, we know we are in a cycle and can break from the loop
        # note that where they meet is not necessarily the beginning of the cycle
        if fast == slow:
            break
    
    # if we are not in a cycle, we can simply return None
    if not fast or not fast.next:
        return None

    # initialize a second slow pointer
    # the distance between slow2 and the head of the cycle must be equal to the distance
    # of slow to the head of the cycle
    slow2 = head
    
    # move both slow pointers until they meet
    while slow != slow2:
        slow = slow.next
        slow2 = slow2.next

    # once they meet, we know it's the head of the cycle
    return slow

