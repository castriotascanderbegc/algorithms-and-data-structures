"""
    Q: Given the root of a binary tree, return its depth.
    
    The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional

class Solution:
    # Recursive Solution using DFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # Iterative Solution using DFS
    def maxDepthIterative(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([root.left, depth + 1])
                stack.append([root.right, depth + 1])
        return res

    # BFS Solution
    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        level = 0
        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            level += 1
        
        return level


    
        
