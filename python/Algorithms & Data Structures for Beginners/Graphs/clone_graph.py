"""
    Q:  Given a node in a connected undirected graph, return a deep copy of the graph.
        Each node in the graph contains an integer value and a list of its neighbors.

        For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph. 
        The index of each node within the adjacency list is the same as the node's value (1-indexed).
        The input node will always be the first node in the graph and have 1 as the value.
"""


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque
from typing import Optional
class Solution:
    # To create a deep copy of the graph we will use DFS on each node    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # we create a mapping from the original node to its deep copy
        copies = {}
        def dfs(node: Optional['Node']):
            # if given node already stored in our map, return its deep copy
            if node in copies:
                return copies[node]   # temp[copy] will return the copy of the node
            
            copy = Node(node.val)     # create a copy
            copies[node] = copy       # insert node in the map, mapping to its copy

            # loop through the neighbors of the node
            for neighbor in node.neighbors:
                # recursively run dfs on the neighbor
                copy.neighbors.append(dfs(neighbor))
            
            # return the copy
            return copy
        
        return dfs(node) if node else None

