class TreeNode:
    def __init__(self, val = None, left = None, right = None) -> None:
        self.val = val
        self.left = None
        self.right = None
class Solution:
    """
        Suppose we are given the following question, use backtracking algorithm to find a soltution. 
        Q: Determine if a path exists from the root of the tree to a leaf node. It might not contain any zeroes.
            Return True if it does exist, False otherwise. Populate its path if any.
    """
    def canReachLeaf(self, root: TreeNode) -> bool:
        # base case: empty tree or root value is 0
        if not root or root.val == 0:
            return False
    
        # if we are at a leaf node, and have not returned False yet, we are done
        if not root.left and not root.right:
            return True
        
        # recursively process left subtree
        if self.canReachLeaf(root.left): # type: ignore
            return True

        # recursively process right subtree
        if self.canReachLeaf(root.right): # type: ignore
            return True

        # if we haven't return True yet, we haven't found a solution   
        return False
    
    def leafPath(self, root: TreeNode, path: list[int]) -> bool:
        # base case: empty tree or root value is 0
        if not root or root.val == 0:
            return False
        
        # add root to our solution path
        path.append(root.val) # type: ignore

        # if we are at a leaf node, and have not returned False yet, we are done
        if not root.left and not root.right:
            return True
        
        # recursively process left subtree
        if self.leafPath(root.left, path): # type: ignore
            return True

        # recursively process right subtree
        if self.leafPath(root.right, path): # type: ignore
            return True

        # if we haven't return True yet, pop back from the solution path
        path.pop()

        # if we haven't return True yet, we haven't found a solution   
        return False