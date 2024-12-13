"""
    Implement Dijkstra's shortest path algorithm.

    Q: Given a weighted, directed graph, and a starting vertex, return the shortest distance from the starting vertex to every vertex in the graph.

    Input:

        n - the number of vertices in the graph, where (2 <= n <= 100). Each vertex is labeled from 0 to n - 1.
        edges - a list of tuples, each representing a directed edge in the form (u, v, w), where u is the source vertex, v is the destination vertex, and w is the weight of the edge, where (1 <= w <= 10).
        src - the source vertex from which to start the algorithm, where (0 <= src < n).

"""

import heapq
from typing import Dict, List

class Dijkstra:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

       ### Setup ### 

        adj = {}    # given edges, define adjacency list to traverse the graph

        # populate the adjecency list with the given edges
        for i in range(n):
            adj[i] = []

        # u: src, v: dst, w: weight
        for u, v, w, in edges:
            adj[u].append([v, w]) 

        
        ### Dijkstra's Algorithm starts practically here ###

        shortest = {}           # initialize our result as a HashMap
        minHeap = [[0, src]]    # add src node to our MinHeap with a weight of 0, from src to src cost 0

        # repeat until our MinHeap is empty
        while minHeap:
            # pop the vertex with minimum weight
            w1, n1 = heapq.heappop(minHeap)
            # if popped vertex has already been visited, let's skip it
            if n1 in shortest:
                continue
            # if not visited yet, add it to our result
            shortest[n1] = w1

            # visit all neighbors of the popped vertex
            for n2, w2 in adj[n1]:
                # if neighbor has not been visited yet
                if n2 not in shortest:
                    # add it to our MinHeap
                    heapq.heappush(minHeap, [w1 + w2, n2])
        
        return shortest
