from typing import List
from ..Trees.UnionFind.union_find import UnionFind
import heapq

"""
    Kruskal's Algorithm is similar to Prim's for finding the minimum spanning tree in an undirected weighted graph. 
    It is also a greedy algo, that works best on sparse graphs. 

    It works by sorting the edges in increasing order of weights. 
    Starting with an initially empty tree, we consider all edges, and we add the edge with the min weight to our MST, 
    if that does not result in a cycle. 

    To detect a cycle, Kruskal uses UnionFind data structure.


    Kruskal's algorithm is a greedy algorithm that finds the MST of graph. It sorts all the edges from least weight to greatest, and iteratively adds edges to the MST, ensuring that each new edge doesn't form a cycle.

"""


class Kruskal:
    """
        Given a list of edges of a connected undirected graph, 
        with nodes numbered from 1 to n,
        return a list of edges making up the minimum spanning tree
    """
    def minimumSpanningTree(edges: List[List[int]], n: int) -> List[List[int]]:
        minHeap = []
        # populate the min heap
        for n1, n2, weight in edges:
            heapq.heappush(minHeap, [weight, n1, n2])
        
        union_find = UnionFind(n)   # initialize unionfind object
        mst = []                    # initialize mst 
        while len(mst) < n - 1:
            # take edge from n1 to n2 with minimum weight 
            weight, n1, n2 = heapq.heappush(minHeap)
            # if we cannot union them, skip it
            if not union_find.union(n1, n2):
                continue
            # if we can union, append to our minimum spanning tree
            mst.append([n1, n2])
        
        return mst

