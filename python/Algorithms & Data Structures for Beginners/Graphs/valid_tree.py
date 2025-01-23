"""
    Q: Graph Valid Tree
    Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
    write a function to check whether these edges make up a valid tree.
"""
from typing import List


class Solution:
    """
        DFS on an adjacency list to detect any cycle
    """
    # Time Complexity: T(n): O(E + V) where V is the number of vertices and E is the number of edges in the graph
    # Space Complexity: S(n): O(E + V)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # if we aren't given any node, technically an empty tree is a valid tree
        if not n:
            return True
        
        # first create an adjacency list given the edges
        adjList = {i: [] for i in range(n)}
        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)

        # define our DFS algorithm
        def dfs(node, prev):
            # if node has already been visited, we have a cycle
            if node in visit:
                return False        
            
            # add current node to visited set   
            visit.add(node)
            
            # traverse the neighbors of the current node
            for neighbor in adjList[node]:
                # if neighbor is the parent of the current node, then just skip it
                if neighbor == prev:
                    continue
                # if we encounter a cycle now, immediately return false
                if not dfs(neighbor, node):
                    return False
            # we haven't detected any cycle
            return True

        # define our visit set
        visit = set()
        
        # make sure we don't have any cycle and all the nodes have been visited
        return dfs(0, -1) and n == len(visit)

        