from typing import List


class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
    
    # Find parent of n, with path compression.
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    # Union by height / rank.
    # Return false if already connected, true otherwise.
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True

"""
    Q: Number of Connected Components in an Undirected Graph
    
    There is an undirected graph with n nodes. 
    There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.
    
    The nodes are numbered from 0 to n - 1.
    
    Return the total number of connected components in that graph.
"""

class Solution:
    """
        We can use Union-Find (Disjoint Set Union) data structure to check whether we can union two components
    """
    # Time Complexity: T(n): O(V + (E * a(V))) where V is the number of vertices and E is the number of edges in the graph. a() is used for amortized complexity
    # Space Complexity: S(n): O(V)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create an object of UF data structure
        union_find = UnionFind(n)
        # initially we have n seperate components
        res = n
        # traverse each given edge
        for n1, n2 in edges:
            # check if we can union the edges in a single component
            if union_find.union(n1, n2):
                # if succesfull, decrement our result
                res -= 1
        # return our result
        return res
        