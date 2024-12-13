"""
    Q: You are given two integer arrays preorder and inorder.

        preorder is the preorder traversal of a binary tree
        inorder is the inorder traversal of the same tree
        Both arrays are of the same size and consist of unique values.
        Rebuild the binary tree from the preorder and inorder traversals and return its root.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # if either of two inputs is empty, we can simply return None
        if not preorder or not inorder:
            return None
        
        # we know the first value of preorder will be the root of our BinaryTree
        # remember preorder is: root left right
        root = TreeNode(preorder[0])
        # find the root index in the inorder
        # remember inorder is: left root right
        mid = inorder.index(preorder[0])

        # create the left subtree
        # from preorder we want to read all the values from the node after the root until all nodes in the left subtree which is given by mid, i.e. 1 -> mid + 1
        # from inorded we want to read all the values to the left of the root, therefore up until mid, i.e. 0 -> mid - 1
        root.left = self.buildTree(preorder[1: mid + 1], inorder[: mid])
                

        # create the right subtree
        # from preorder we want to read all the values after the all the values in the left subtree, given by mid + 1 until the end, i.e. mid + 1 -> len(preorder) - 1
        # from inorder we want to read all the values to the right of the root to the end, i.e. mid + 1 -> len(preorder) - 1
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        # return the root
        return root

        