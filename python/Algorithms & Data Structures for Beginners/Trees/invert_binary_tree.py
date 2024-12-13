"""
    You are given the root of a binary tree root. Invert the binary tree and return its root.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 

        # swap left and right child
        root.left, root.right = root.right, root.left

        # recursively process left and right child
        self.invertTree(root.left)
        self.invertTree(root.right)

        # return root
        return root
        