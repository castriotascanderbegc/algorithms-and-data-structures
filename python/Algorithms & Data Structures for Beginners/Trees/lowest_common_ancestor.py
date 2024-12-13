"""
    Q: Given a binary search tree (BST) where all node values are unique, 
    and two nodes from the tree p and q, 
    return the lowest common ancestor (LCA) of the two nodes.

    The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. 
    The ancestor is allowed to be a descendant of itself.

"""

class TreeNode:
    def __init__(self, val:0, left:None, right:None):
        self.val = val
        self.left = left
        self.right = right

class Solution: 
    def recurisveLCA(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if current root is greater than both p and q, then only recurse on the left subtree
        if root.val > p.val and root.val > q.val:
            root = self.recurisveLCA(root.left, p, q)
        # if current root is smaller than both p and q, then only recurse on the right subtree
        elif root.val < p.val and root.val < q.val:
            root = self.recurisveLCA(root.right, p, q)
        else: 
            # if none of above is valid, then we found our lowest common ancestor
            return root
        
        # return empty root if any
        return root


    def iterativeLCA(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:   
        while True:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
            
