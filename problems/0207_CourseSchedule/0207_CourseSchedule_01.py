"""
Date        : 6 Febuary 2022
Runtime     : 120 ms, faster than 55.08% of Python3 online submissions for Course Schedule.
Memory Usage: 16.8 MB, less than 48.49% of Python3 online submissions for Course Schedule.
"""

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
        visited = set()
        path = list()
        order = list()
        for course in range(numCourses):
            if course not in visited:
                visited.add(course)
                if not self.dfs(graph, course, path, order, visited):
                    return False   
        return True
    
    def dfs(self, graph, vertex, path, order, visited) -> bool:
        path.append(vertex)
        for neighbour in graph[vertex]:
            if neighbour in path:
                return False
            if neighbour not in visited:
                visited.add(neighbour)
                if not self.dfs(graph, neighbour, path, order, visited):
                    return False
        order.append(path.pop())
        return True

import unittest

class canFinishCase(unittest.TestCase):
    def test_canFinish(self):
        func = Solution().canFinish
        self.assertEqual(func(2, [[1,0]]), True)
        self.assertEqual(func(2, [[1,0],[0,1]]), False)
        self.assertEqual(func(4, [[1,0],[2,0],[3,1],[3,2]]), True)

if __name__ == "__main__":
    unittest.main()