#
# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#

# @lc code=start
from typing import List
from collections import defaultdict, deque
import heapq


class Solution:
    # sol1) adj list + dfs
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:

        adj = defaultdict(list)
        for edge in edges:
            f, t = edge
            adj[f].append(t)
            adj[t].append(f)

        visited = set()

        def travel(adj, visited, node, destination):
            if node == destination:
                return True
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    if travel(adj, visited, neighbor, destination):
                        return True
            return False

        return travel(adj, visited, source, destination)

    # sol2) adj list + bfs
    def validPath2(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        q = deque([source])
        visited = set([source])

        while q:
            node = q.popleft()
            if node == destination:
                return True
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)

        return False

    # sol3) graph algorithm
    def validPath3(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # dijkstra's algorithm
        distances = {node: float("inf") for node in range(n)}
        distances[source] = 0
        priority_q = [(0, source)]

        while priority_q:
            curr_dist, curr_node = heapq.heappop(priority_q)
            if curr_node == destination:
                return True

            if curr_dist > distances[curr_node]:
                continue
            for neighbor in adj[curr_node]:
                dist = curr_dist + 1
                if dist < distances[neighbor]:
                    distances[neighbor] = dist
                    heapq.heappush(priority_q, (dist, neighbor))

        return False


n = 6
edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
source = 0
destination = 5
print(Solution().validPath3(n, edges, source, destination))

# @lc code=end
