class SegmentTree:
    def __init__(self, total, L, R):
        self.sum = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R
    
    @staticmethod
    # O(n)
    # a static method is a method that belongs to a class rather than an instance of the class
    def build(self, nums, L, R):
        # if we hit the base case, range is exhausted
        if L == R:
            # we build the tree
            return SegmentTree(nums[L], L, R)
        M = (L + R) // 2
        root = SegmentTree(0, L, R)
        root.left = SegmentTree.build(nums, L, M)
        root.rigth = SegmentTree.build(nums, M + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root

    # O(log n)
    def update(self, index, value):
        if self.L == self.R:
            self.sum = value
            return
        M = (self.L + self.R) // 2
        if index > M:
            self.right.update(index, value)
        else:
            self.left.update(index, value)
        self.sum = self.left.sum + self.right.sum
    
    # O(log n)
    def queryRange(self, L, R):
        # best case scenario if our query range is exactly at the current node
        if L == self.L and R == self.R:
            # we can simply return the sum of the current node
            return self.sum
    
        # compute middle
        M = (self.L + self.R) // 2

        # if L > M , then our range lies on the right subtree
        if L > M:
            return self.right.rangeQuery(L, R)
        
        # if R <= M , then our range lies on the left subtree
        elif R <= M:
            return self.left.rangeQuery(L, R)
    
        # if range is not in either left or right subtree
        # then it must lie in both subtrees
        else:
            return (self.left.rangeQuery(L, M) + self.right.rangeQuery(M + 1, R))

