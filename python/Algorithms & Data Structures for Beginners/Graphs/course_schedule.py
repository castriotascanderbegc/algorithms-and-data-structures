"""
    Q: You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

    The pair [0, 1], indicates that must take course 1 before taking course 0.

    There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

    Return true if it is possible to finish all courses, otherwise return false.

"""

from typing import List


class Solution:
    # This is a classic example of Topological Sort Algorithm
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}               # given course,prerequesites edges, we can map each course to its prerequiste

        # DFS helper
        def dfs(src):
            if src in visited:
                return True
            if src in path:
                return False            # cycle
            path.add(src)
            for nei in adj[src]:
                if not dfs(nei):
                    return False        # cycle

            path.remove(src)
            visited.add(src)
            return True

        # initialize our course map
        for course in range(numCourses):
            adj[course] = []
        
        # populate each course in the map with its prerequisite
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        visited = set() # initialize visited cell set
        path = set()    # initialize path set to detect a cycle

        # run DFS on each course
        for course in range(numCourses):
            # if DFS is not succesfull, immediately return False
            if not dfs(course):
                return False
        
        # if we haven't returned yet, Topological Sort Algorithm was succesfull, we can return True
        return True