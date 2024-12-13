"""
    Q: Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.
       Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

"""



# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
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
