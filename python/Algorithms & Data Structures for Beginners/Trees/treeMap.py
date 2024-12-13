# Binary Search Tree Node
class TreeNode:
    def __init__(self, key = None, val = None ,left = None, right = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

# Implementation for a Binary Search Tree Map
class TreeMap:
    
    def __init__(self):
        # initializing an empty TreeMap
        self.root = None

    # Insert a new node with key, value pair in the TreeMap --> Iterative Implementation
    def iterativeInsert(self, key: int, val: int) -> None:
        # create a new node with given key, value pair 
        newNode = TreeNode(key=key, val=val)

        # if tree is empty, set the root to the new node
        if not self.root:
            self.root = newNode
            return
        
        # keep a pointer to traverse the tree
        curr = self.root

        while True:
            # if current node key is greater than given key, we move to the left subtree
            if curr.key > key:
                # if no left child yet, create it with the new node
                if not curr.left:
                    curr.left = newNode
                    return
                # move pointer to the left subtree
                curr = curr.left
            # if current node key is smaller than given key, we move to the right subtree
            elif curr.key < key:
                # if no right child yet, create it with the new node
                if not curr.right:
                    curr.right = newNode
                    return
                # move pointer to the rigth subtree
                curr = curr.right

            # if we found a node with the same given key, override its value with the given value
            else:
                curr.val = val
                return
        
    # Insert a new node with key, value pair in the TreeMap --> Recursive Implementation
    def insert(self, key: int, val: int) -> None:

        # use a helper function to inser recursively
        def insertHelper(root: TreeNode, key: int, val: int) -> TreeNode:
            # if tree is empty
            if not root:
                # return a new node with given key, value pair
                return TreeNode(key=key, val=val)

            # if given key is smaller than the current node key
            if root.key > key:
                # recursively process the left subtree, and update the left subtree
                root.left = insertHelper(root.left, key, val)
            # if given key is greater than the current node key
            elif root.key < key:
                # recursively process the right subtree, and update the right subtree
                root.right = insertHelper(root.right, key, val)
            # if we found a node with the same given key, override its value with the given value
            else:
                root.val = val
            
            # return the updated root
            return root
        
        # update root or its right/left subtree
        self.root = insertHelper(self.root, key, val)
    
    # Return the value mapped with the key. If the key is not present in the tree, return -1 
    def get(self, key: int) -> int:

        def getNode(root: TreeNode, key: int) -> TreeNode:
            # keep a pointer to traverse the tree
            curr = root
            # traverse until we see a node
            while curr:
                # if given key is greater than current key, move to the right
                if key > curr.key:
                    curr = curr.right
                # if given key is smaller than current key, move to the left
                elif key < curr.key:
                    curr = curr.left
                # we found desired node with given key, return it
                else:
                    return curr
            return curr
        
        # get the node with given key
        node = getNode(self.root, key)

        return node.val if node else -1

    # Return the value mapped to the smallest key in the tree. If the tree is empty, return -1
    def getMin(self) -> int:        
        minNode = self.minValueNode(self.root)
        return minNode.val if minNode else -1

    # Find the node with the smallest key in the tree
    def minValueNode(self, root: TreeNode) -> TreeNode:
        # keep a pointer to traverse the tree to its left subtree
        curr = root
        # until we see a node on the left subtree keep moving to the left
        while curr and curr.left:
            curr = curr.left
        return curr
    
    # Return the value mapped to the greatest key in the tree. If the tree is empty, return -1
    def getMax(self) -> int:

        def maxValueNode(root: TreeNode) -> TreeNode:
            # keep a pointer to traverse the tree to its right subtree
            curr = root
            # until we see a node on the right subtree keep moving to the right
            while curr and curr.right:
                curr = curr.right
            return curr
        
        maxNode = maxValueNode(self.root)

        return maxNode.val if maxNode else -1

    # Remove the key-value pair with the given key from the tree
    def remove(self, key: int) -> None:
        
        # helper function to recursively remove the key-value pair with the given key from the tree 
        def removeHelper(root: TreeNode, key: int) -> TreeNode:
            # if tree is empty, return 
            if not root:
                return None
            # if given key is smaller than current node key, recursively process left subtree
            if root.key > key:
                root.left = removeHelper(root.left, key)
            # if given key is greater than current node key, recursively process right subtree
            elif root.key < key:
                root.right = removeHelper(root.right, key)
            
            # we found target node to be removed from the tree
            else:
                # if target node does not have the left child, replace the target node with the right child
                if not root.left:
                    return root.right
                # if target node does not have the right child, replace the target node with the left child
                elif not root.right:
                    return root.left
                
                # if target node has both the left and right children
                # we want to swap the target node with its in-order successor, i.e. smallest node in target right subtree
                else:
                    # find the smallest node in the right subtree
                    minNode = self.minValueNode(root.right)

                    # update the current node key, value pair with the smallest node key, value pair
                    root.key = minNode.key
                    root.val = minNode.val

                    # make sure the duplicate is removed
                    root.right = removeHelper(root.right, minNode.key)
            
            return root

        self.root = removeHelper(self.root, key)


    # Return an array of the keys in the tree in ascending order, i.e. in-order traversal of the keys
    def getInorderKeys(self) -> list[int]:
        res = []

        # helper function to traverse the tree in-order recursively
        def inorder(root: TreeNode):
            # if tree is empty, return 
            if not root:
                return
            # recursively process left subtree
            inorder(root.left)
            # add current node key to the result
            res.append(root.key)
            # recursively process right subtree
            inorder(root.right)

        inorder(self.root)

        return res

