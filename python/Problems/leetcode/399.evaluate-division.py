#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(list)
        for idx, e in enumerate(equations):
            graph[e[0]].append([e[1], values[idx]])
            graph[e[1]].append([e[0], round(1 / values[idx], 5)])
        print(graph)

        def traverse(graph, visited, curr, dest, mul):
            if curr == dest:
                return mul
            visited.add(curr)
            for neighbor, weight in graph[curr]:
                if neighbor not in visited:
                    result = traverse(graph, visited, neighbor, dest, mul * weight)
                    if result != -1:
                        return result
            visited.remove(curr)
            return -1

        answer = []
        for q in queries:
            src, dest = q[0], q[1]
            if src not in graph.keys() or dest not in graph.keys():
                answer.append(-1)
            else:
                visited = set()
                res = traverse(graph, visited, src, dest, 1)
                answer.append(res)

        return answer


equations = [["a", "aa"]]
values = [9.0]
queries = [["aa", "a"], ["aa", "aa"]]
print(Solution().calcEquation(equations, values, queries))
# @lc code=end
