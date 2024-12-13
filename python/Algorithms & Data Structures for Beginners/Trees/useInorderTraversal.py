# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        res = []    # behaves as a global variable for nested functions

        # we perform DFS - In-order traversal. Recursive Solution
        def inorder(root: TreeNode):
            # if we don't see a Node, then pop back from the call stack
            if not root:
                return
            # recursively visit left subtree
            inorder(root.left)
            # append current root value
            res.append(root.val)
            # recursively visit right subtree
            inorder(root.right)

        # we perform DFS - In-order traversal. Iterative Solution using a Stack
        def iterativeInorder(root: TreeNode):
            stack = []      # use a stack
            curr = root     # use a pointer

            # keep traverse the tree if our pointer is pointing to a Node or we have elements in the stack
            while curr or stack:
                
                # keep moving to the left subtree until we can
                while curr:
                    # push nodes we see into the stack
                    stack.append(curr)
                    # move pointer to the left subtree
                    curr = curr.left
                
                # once we don't have any nodes to visit on the left, pop current node from the stack
                curr = stack.pop() 
                # add value to our result
                res.append(curr.val)
                # move our pointer to the right subtree
                curr = curr.right 

        inorder(root)
        #iterativeInorder(root)
        return res