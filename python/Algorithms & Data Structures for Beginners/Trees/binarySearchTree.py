from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # search a value in a binary search tree
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # T(n): O(log n)
        # we search by using simple Binary Search
        if not root:
            return None

        if root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return root
    
    # insert a new node and return the root of the BST
    def insert(self, root: TreeNode, val: int) -> TreeNode:
        # T(n): O(log n)
        # we first search the right position to insert the node by traversing the BST
        if not root:
            return TreeNode(val=val)
        
        if root.val > val:
            root.left = self.insert(root.left, val)
        elif root.val < val:
            root.right = self.insert(root.right, val)

        return root
    
    # Return the minimum value node of the BST
    def minValueNode(self, root: TreeNode) -> TreeNode:
        # The min value node of the BST will be the left-most node in the BST
        curr = root
        while curr and curr.left:
            curr = curr.left
        
        return curr
    
    # remove a node and return the root of the BST
    def remove(self, root: TreeNode, val:int) -> TreeNode:
        """
        T(n): O(log n)
        Before revmoing a node from a BST, we need to conider two cases:
            1. The target node has 0 or 1 child
                --> 0 child: We can set the parent left/right child pointer to Null if target is a leaf node
                --> 1 child: We can set the parent left/right child pointer to the target's left/right child 
            2. The target node has 2 children
                --> 2 children: we need to replace the node with its in-order successor
                                The in-order successor is the left-most node in the right subtree of the target node.
                                It is the smallest node along all the nodes that are greater than the target node
        """
        if not root:
            return None
        
        # if target node is on the left
        if root.val > val:        
            root.left = self.remove(root.left, val)
        # else if targer node is on the right
        elif root.val < val:
            root.right = self.remove(root.right, val)
        
        # if we are at the target node
        else:
            # Case 1. The target node has 0 or 1 child
            # if it does not have the left child
            if not root.left:
                return root.right
            # if it does not have the right child
            elif not root.right:
                return root.left
            # Case 2. The target node has 2 children
            else:
                # find the in-order successor
                # find the smallest node within the right subtree
                minValueNode = self.minValueNode(root.right)
                # override the root value to be this minimum node value
                root.val = minValueNode.val
                # remove the depublicate node since we overriden root
                root.right = self.remove(root.right, minValueNode) 
        return root
            
    # Depth-First Search Algorithm
    """
        Time Complexity: T(n): O(n)
        We need to traverse every node in the BST, therefore the time complexity is the size of the BST
        The size of the BST is n = # of nodes in the BST
    """

    # In-order Traversal --> Prioritize left, parent node, right
    def inorder(self, root:TreeNode) -> None:
        if not root:
            return
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)

    # Pre-order Traversal --> Prioritize parent node, left, right
    def preorder(self, root:TreeNode) -> None:
        if not root:
            return
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    # Post-order Traversal --> Prioritize left, right, parent node
    def postorder(self, root:TreeNode) -> None:
        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val)



    # Breadth-First Search Algorithm 
    """
        Time Complexity: T(n) = O(n)
        We are visiting each node in the tree exactly once, and we visit them all. So the time complexity is the size 
        of the tree, which is n = # of nodes in the tree

        The idea behind BFS is:
            Process all nodes in each layer/level before moving to the next. 
            So, we process a node, and then its children from left to right. 
            This is also called, level-order traversal. 

        Implementation: 
            We will use a Queue to implement BFS. 
                we move the root into the queue
                until we have elements in the queue, we loop through these elements in the queue, and
                we pop from the queue, process the node, insert its left and right children (if any) and continue. 
                Once the queue is empty and there are no more nodes to visit, we are done traversing. 
    """

    def bfs(self, root: TreeNode) -> None:
        queue = deque()     # use a queue
        # insert the root in the queue
        if root:
            queue.append(root)
        
        # keep track of the tree level
        level = 0

        # until we have elements in the queue
        while len(queue) > 0:
            print("Tree level: ", level)
            # loop through the eleemnts in the queue, i.e. current level of the tree
            for i in range(len(queue)):
                # pop current node from the queue
                curr = queue.popleft()
                # process the node, ex: we print its value
                print(curr.val)
                # if current node has a left child, insert in the queue
                if curr.left:
                    queue.append(curr.left)
                # if current node has a right child, insert in the qeue
                if curr.right:
                    queue.append(curr.right)
            
            # increment tree level, and continue
            level += 1

