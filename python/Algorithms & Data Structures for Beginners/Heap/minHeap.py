class Heap:

    """
    A heap is a specialized, tree-based data structure, which is a complete binary tree.
    It implements an abstract data type called the Priority Queue. 

    A Min Heap -> has the smallest value at the root node and when deleting, the smallest value has the highest priority

    Heap Properties
    1. Structure Property
        A binary heap is a binary tree that is a complete binary tree, where every single level of the tree is filled completely, 
        except the lowest level nodes, which are filled contiguosly from left to right

    2. Order Property
        The order property for a min-heap is that all of the descendents should be greater than their ancestors. 
        If we have a tree rooted at y, every node in the right and left subtrees should be greater than or equal to y

    Under the hood, heaps are built using arrays

    A node's left child, right child and parent can be calculated using the following formulas, where i is the index of a given node in the array

        left child = 2 * i 
        right child = 2 * i + 1
        parent = i / 2

    """
    def __init__(self) -> None:
        self.heap = [0]             # use a dummy node
    
    def push(self, val) -> None:
        """
            Insert a value in the heap

            Time Complexity: T(n): O(log n)
            We know the tree will always be balanced, so the height of the tree is log n
        """

        self.heap.append(val)       # insert the node/value at the end of the heap
        i = len(self.heap) - 1      # initialize pointer i @ the last element in the heap

        # The idea here is move up the tree making sure the Order Property is still satisfied 

        # We need to percolate up
        # Until the current node is smaller than its parent, we need to swap it and move up the binary tree
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            # store the current node
            tmp = self.heap[i]
            # move the parent node at child index
            self.heap[i] = self.heap[i // 2]
            # move node at parent index
            self.heap[i // 2] = tmp
            # move up in the tree
            i = i // 2              # round down the division

    def top(self) -> int:
        """
            Get the element with highest priority, i.e. minimum value in the heap
            
            Time Complexity: T(n): O(1)
        """
        # no elements in the heap
        if len(self.heap) == 1:
            return None  # type: ignore

        return self.heap[1]
    
    def pop(self) -> int:
        """
            Pop a value from the heap. We will pop the element with highest priority, i.e. minimum value in the heap

            Time Complexity: T(n): O(log n)
            We know the tree will always be balanced, so the height of the tree is log n

            The idea behind pop is: 
                Take the right-most node of the last level, i.e. last element/node in the heap tree
                and swap it with the root node. This way we know we maintain the Structure Property. 

                In order to maintain the Order Property of the heap, we can:
                    Percolate down and make sure the node moved to the root is at the right position in the heap tree
        """

        # no elements in the heap
        if len(self.heap) == 1:
            return None  # type: ignore
        
        # one element in the heap
        if len(self.heap) == 2:
            return self.heap.pop()
        
        # take the root, i.e. the element with highest priority in the heap, the minimum value
        res = self.heap[1]

        # take the last element in the heap and set it as the new root
        self.heap[1] = self.heap.pop()

        i = 1
        # we need to percolate down
        # until we have a left child, i.e. leftChild = 2 * i 
        while 2 * i < len(self.heap):

            """
                we need to worry about 3 cases
                    1. The node has no children
                    2. The node only has a left child, we are guranteed to have at least the left in this case
                    3. The node has two children
            """

            # if we have 2 children, and right child is smaller than the left child
            if (2 * i + 1 < len(self.heap) and 
                self.heap[2 * i + 1] < self.heap[2 * i] and 
                self.heap[2 * i + 1] < self.heap[i]):
                # perform the swap with the right child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = tmp

                i = 2 * i + 1

            # if we only have the left child
            elif self.heap[2 * 1] < self.heap[i]:
                # perform the swap with the left child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = tmp

                i = 2 * 1
            
            # no children, we can break out of the loop
            else:
                break
            
        return res
        


    def heapify(self, arr: list[int]) -> None:
        """
            The idea behind heapify to build a heap is to satisfy the structure and order property. 
            We need to make sure our binary heap is a complete binary tree and that every node's value is at most its parent's value.


            Because the leaf nodes can't violate the min-heap properties, there is no need to perform heapify on them. 
            We only need to start at heap.length // 2. Then we can percolate down as done in pop()

            Time Complexity: T(n) = O(n)
            There are n nodes in a binary tree, there are roughly n / 2 leaf nodes. We can figure out how many levels each node has to percolate down and the amount of work 
            heapify performs at each level.

            We don't perform heapify at the 3rd/last level. The nodes on the 2nd level need to percolate down one level, and the nodes on the 1st level are percolating down 2 levels, 
            with the root node having to percolate down allt the levels. 
            So while the number of nodes halves each time, the number of levels to be percolated increases. 
            There is a mathemtical summation to resolve this that approximates to O(n)
        """

        # we move the first element in the array at the end
        arr.append(arr[0])

        self.heap = arr


        # now we know the structure property is satisfied
        
        # we can skip the leaf nodes
        curr = (len(self.heap) - 1) // 2

        # move backwards in the array
        while curr > 0:
            # we need to percolate down
            i = curr
            # we need to percolate down
            # until we have a left child, i.e. leftChild = 2 * i 
            while 2 * i < len(self.heap):

                """
                    we need to worry about 3 cases
                        1. The node has no children
                        2. The node only has a left child, we are guranteed to have at least the left in this case
                        3. The node has two children
                """

                # if we have 2 children, and right child is smaller than the left child
                if (2 * i + 1 < len(self.heap) and 
                    self.heap[2 * i + 1] < self.heap[2 * i] and 
                    self.heap[2 * i + 1] < self.heap[i]):
                    # perform the swap with the right child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = tmp

                    i = 2 * i + 1

                # if we only have the left child
                elif self.heap[2 * 1] < self.heap[i]:
                    # perform the swap with the left child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = tmp

                    i = 2 * 1
                
                # no children, we can break out of the loop
                else:
                    break
            
            curr -= 1








