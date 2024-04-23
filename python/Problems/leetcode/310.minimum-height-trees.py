#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start
from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 1. Build adj list
        adj = defaultdict(list)
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)
        print(adj)

        # 2. Calculate height for all nodes (dfs) -> O(n^2), TLE
        def dfs(node, visited):
            visited.add(node)
            max_height = 0
            for neighbor in adj[node]:
                if neighbor not in visited:
                    height = dfs(neighbor, visited)
                    max_height = max(max_height, height)
            visited.remove(node)
            return max_height + 1

        heights = defaultdict(int)
        for node in range(n):
            visited = set()
            height = dfs(node, visited)
            heights[node] = height

        return [k for k, v in heights.items() if v == min(heights.values())]

    # bfs - center of a tree
    def findMinHeightTrees2(self, n: int, edges: List[List[int]]) -> List[int]:
        # 1. Build adj list
        adj = defaultdict(list)
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)

        def bfs(start):
            visited = [-1] * n
            q = deque([start])
            visited[start] = 0
            farthest_node = start
            while q:
                node = q.popleft()
                for neighbor in adj[node]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = visited[node] + 1
                        q.append(neighbor)
                        if visited[neighbor] > visited[farthest_node]:
                            farthest_node = neighbor
            return farthest_node, visited

        # use 2 bfs (center of tree)
        farthest, _ = bfs(0)
        farthest_from_first, distances = bfs(farthest)
        _, distances_from_second = bfs(farthest_from_first)
        min_height = (max(distances) + 1) // 2

        return [
            i
            for i in range(n)
            if max(distances[i], distances_from_second[i]) == min_height
        ]

    """
    sol3
    idea : if the height of a tree with root x is h, 
    then the height of the same tree with the leaves removed and with root x is h - 1.
    """

    def findMinHeightTrees3(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [set() for _ in range(n)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = [x for x in range(n) if len(graph[x]) <= 1]
        prev_leaves = leaves
        while leaves:
            new_leaves = []
            for leaf in leaves:
                if not graph[leaf]:
                    return leaves
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            prev_leaves, leaves = leaves, new_leaves
        return prev_leaves


n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
print(Solution().findMinHeightTrees3(n, edges))


# @lc code=end
