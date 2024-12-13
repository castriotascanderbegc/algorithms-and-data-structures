from collections import deque

# GraphNode for an adjacency list
class GraphNode:
    def __init__(self, val) -> None:
        self.val = val
        self.neighbors = []

# use a HashMap
adjList = {"A": [], "B": []}

# Given directed edges, build an adjacency list
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
adjList = {}

for src, dst in edges:
    if src not in adjList:
        adjList[src] = []
    if dst not in adjList:
        adjList[dst] = []
    adjList[src].append(dst)

# Directed Graph Class using adjacency list
class Graph:
    def __init__(self) -> None:
        self.adjList = {}
    
    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = set()
        if dst not in self.adjList:
            self.adjList[dst] = set()
        self.adjList[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if not src in self.adjList or not dst in self.adjList[src]:
            return False
        self.adjList[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        def hasPathHelper(node, target, adjList, visit) -> bool:
            if node == target:
                return True
            visit.add(node)
            for neighbor in adjList[node]:
                if neighbor not in visit:
                    if hasPathHelper(neighbor, target, adjList, visit):
                        return True
            return False
        return hasPathHelper(src, dst, self.adjList, set())

    # Count the paths from node to target (backtracking)
    def dfs(self, node, target, adjList, visited: set) -> int:
        if node in visited:
            return 0
        if node == target:
            return 1
    
        count = 0
        visited.add(node)

        for neighbor in self.adjList[node]:
            count += self.dfs(neighbor, target, self.adjList, visited)
        
        visited.remove(node)

        return count

    # Shortest path from node to target
    def bfs(self, node, target, adjList, visited):
        length = 0
        visited = set()
        visited.add(node)
        queue = deque()
        queue.append(node)

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr == target:
                    return length

                for neighbor in self.adjList[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            length += 1
        return length