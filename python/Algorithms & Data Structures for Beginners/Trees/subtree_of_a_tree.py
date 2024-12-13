"""
    Q: Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise
    A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


# Time Complexity: O(s * t) where s = size of tree rooted at root, and t = size of tree rooted at subroot

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if subRoot is not given, return True. A tree is a subset of itself
        if not subRoot:
            return True
        # if root is not give, return False. 
        if not root:
            return False
        
        # check if given trees are the same
        if self.isSameTree(root, subRoot):
            return True
        
        # recursively check if either left or right child are subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both tree are empty, then they are the same 
        if not p and not q:
            return True
        # if either tree is empty, then they are not the same
        if not p or not q:
            return False
        # if we have both trees, check root value of each
        if p.val != q.val:
            return False
        
        # recursively process each left and right subtree
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
