"""
Topological sort is an algorithm for linearly ordering the vertices of a directed acyclic graph such that for every directed edge 
(u,v) vertex, u comes before v in the ordering.

    Given a directed graph, perform a topological sort on its vertices and return the order as a list of vertex labels. 
    There may be multiple valid topological sorts for a given graph, so you may return any valid ordering.

"""

from typing import List


class TopologicalSort:
    def topologicalSort(self, edges: List[List[int]], n: int) -> List[int]:
        # given the edges of the DAG, build adjacency list to represent the DAG

        # contruct empty adjacency list, nodes numbered from 1 to n
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []

        # traverse the edges and populate the adjacency list to build the DAG, directed acylical graph
        for src, dst in edges:
            adj[src].append(dst)

        topSort  = []       # initialize our result
        visited = set()     # use a HashSet to keep track of the visited vertices

        # run post-order DFS on each vertex in the DAG
        for i in range(1, n + 1):
            self.dfs(i, adj, visited, topSort)

        # reverse the order of the DFS result, to have the topological sort
        topSort.reverse()

        # return topological sort list
        return topSort


    def dfs(self, src, adj, visited, topSort) -> None:
        # check if current vertex h as already been visited
        if src in visited:
            return          # technically we could simply return anything
        
        visited.add(src)    # add src vertex to the visited set

        for neighbor in adj[src]:
            self.dfs(neighbor, adj, visited, topSort)

        topSort.append(src)
        
