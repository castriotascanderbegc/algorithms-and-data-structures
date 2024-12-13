# Definition of a Binary Tree Node
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


# Iterative preorder DFS
# Time and Space: O(n)

def preorder(root):
    stack = []
    curr = root
    while curr or root:
        if curr:
            print(curr.val)
            if curr.right:
                stack.append(curr.right)
            curr = curr.left
        else:
            curr = stack.pop()