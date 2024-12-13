"""
    Q: Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

    A valid binary search tree satisfies the following constraints:

    The left subtree of every node contains only nodes with keys less than the node's key.
    The right subtree of every node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees are also binary search trees.

"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            # technically an empty tree is a valid BST
            if not node:
                return True

            # we need to satify root.val > root.left.val and root.val < root.right.val
            if not (node.val > left and node.val < right):
                return False
            
            # recursively check left subtree and right subtree
            # changing either left or right boundary
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        # -∞ < root < ∞
        return valid(root, float("-inf"), float("+inf"))
        