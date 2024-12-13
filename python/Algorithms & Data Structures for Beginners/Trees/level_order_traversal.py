"""
    Given a binary tree root, return the level order traversal of it as a nested list, 
    where each sublist contains the values of nodes at a particular level in the tree, 
    from left to right.
"""
# Definition for a binary tree node.
from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderTraversal(self, root: TreeNode) -> List[List[int]]:
        res = []                # initialize our result
        q = deque()             # declare our queue

        # if input root is given, append to our queue
        if root:
            q.append(root)

        # repeat until our queue is empty        
        while q:
            # store node values in the current level
            level = []
            # iterate over length of the queue, a snapshot
            for i in range(len(q)):
                # pop from left of the queue
                node = q.popleft()
                # if a valid node
                if node:
                    # append value to the current level
                    level.append(node.val)

                    # if node has a left child, append to the queue
                    if node.left:
                        q.append(node.left)
                
                    # if node has a right child, append to the qeuee
                    if node.right:
                        q.append(node.right)

            # append currnet level node values to the result
            res.append(level)

        return res
        
