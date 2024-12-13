"""

Prim's algorithm is a greedy algorithm that builds the MST of a graph starting from an arbitrary vertex. 
At each step, the algorithm adds the lightest edge connecting a vertex in the MST to a vertex outside the MST, 
effectively "growing" the MST one edge at a time.

Objective:
Given a weighted, undirected graph, find the minimum spanning tree (MST) using Prim's algorithm and return its total weight. 
If the graph is not connected, the total weight of the minimum spanning tree should be -1.


Q:  Implement Prim's minimum spanning tree algorithm.

    Objective:

        Given a weighted, undirected graph, find the minimum spanning tree (MST) using Prim's algorithm and return its total weight. If the graph is not connected, the total weight of the minimum spanning tree should be -1.

    Input:

        n - the number of vertices in the graph, where (2 <= n <= 100). Each vertex is labeled from 0 to n - 1.
        edges - a list of tuples, each representing an undirected edge in the form (u, v, w), where u and v are vertices connected by the edge, and w is the weight of the edge, where (1 <= w <= 10).
"""

from typing import List
import heapq

class Prim: 
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        ### Setup ###

        # given edges, we first build our adjacency list to traverse the graph
        adj = {}
        
        # vertices are labeled from 0 to n - 1
        for i in range(n):
            adj[i] = []
        
        # populate the adjacency list
        # n1: src node, n2: dst node, w: weight for src to dst path
        for n1, n2, w in edges:
            adj[n1].append([n2, w])
            adj[n2].append([n1, w])

        ### Prim's Algorithm starts practically here ###

        # initialize our MinHeap, <weight, n1, n2>
        minHeap = []
        for neighbor, weight in adj[0]:
            heapq.heappush(minHeap, [weight, 0, neighbor])
        
        
        visit = set()   # define visited HashSet -> this is importat to avoid cycles, and keep track of nodes visited
        mst = []        # define minimum spanning tree

        # add first node to visited set
        visit.add(0)

        while len(visit) < n:
            # pop the edge from n1 to n2 with minimum weight
            weight, n1, n2 = heapq.heappop(minHeap)

            # if n2 already been visited, skip it
            if n2 in visit:
                continue

            # if n2 has not been visited, start to build MST one edge at a time
            mst.append([n1, n2])
            visit.add(n2)   # add dst to visited

            # loop over all neighbord of popped node, i.e. n2
            for neighbor, weight in adj[n2]:
                # if neighbor has not been visited yet, add to our MinHeap
                if neighbor not in visit:
                    heapq.heappush(minHeap, [weight, n2, neighbor])
            
        return mst