"""
    Design a Segment Tree class.

    Your SegmentTree class should support the following operations:

    SegmentTree(int[] arr) will initialize a segment tree based on the given array arr. You can assume that the array arr is non-empty.
    int query(int l, int r) will return the sum of all elements in the range [l, r] inclusive. You can assume that 0 <= l <= r < arr.length.
    void update(int idx, int val) will update the element at index idx in the original array to be val. You can assume that 0 <= idx < arr.length.

"""

class SegmentTreeNode:
    def __init__(self, total, L, R):
        self.sum = total 
        self.left = None
        self.right = None
        self.L = L
        self.R = R

class SegmentTree:

    def __init__(self, nums: list[int]):
        self.root = self.build(nums, 0, len(nums) - 1)
   
    def build(self, nums, L, R):
        if L == R:
            return SegmentTreeNode(nums[L], L, R)

        M = (L + R) // 2
        root = SegmentTreeNode(0, L, R)
        root.left = self.build(nums, L, M)
        root.right = self.build(nums, M + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root
    
    def update(self, index: int, val: int) -> None:
        self.updateTree(self.root, index, val)

    def query(self, L: int, R: int) -> int:
        return self.queryRange(self.root, L, R)
    
    def updateTree(self, root, index: int, val: int) -> None:
        if root.L == root.R:
            root.sum = val
            return
        M = (root.L + root.R) // 2
        if index > M:
            self.updateTree(root.right, index, val)
        else:
            self.updateTree(root.left, index, val)
        root.sum = root.left.sum + root.right.sum
    
    def queryRange(self, root, L: int, R: int) -> int:
        if L == root.L and R == root.R:
            return root.sum
        
        M = (root.L + root.R) // 2
        if L > M:
            return self.queryRange(root.right, L, R)
        elif R <= M:
            return self.queryRange(root.left, L, R)
        else:
            return (self.queryRange(root.left, L, M) + self.queryRange(root.right, M + 1, R))
        

