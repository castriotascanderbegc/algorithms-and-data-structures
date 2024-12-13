# Definition of a Binary Tree Node
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


# Iterative postorder DFS
# Time and Space: O(n)
def postorder(root):
    stack = [root]
    visited = [False]
    while stack:
        curr, visited = stack.pop(), visited.pop()
        if curr:
            if visited:
                print(curr.val)
            else:
                stack.append(curr)
                visited.append(True)
                stack.append(curr.right)
                visited.append(False)
                stack.append(curr.left)
                visited.append(False)
