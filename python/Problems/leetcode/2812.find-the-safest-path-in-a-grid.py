#
# @lc app=leetcode id=2812 lang=python3
#
# [2812] Find the Safest Path in a Grid
#

# @lc code=start
from typing import List
from collections import deque


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        d = [[float("inf") for _ in range(n)] for _ in range(n)]
        q = deque()

        def in_range(x, y):
            return 0 <= x and x < n and 0 <= y and y < n

        dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

        # 1. BFS for calculating manhatten distance
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    d[i][j] = 0
                    q.append((i, j))
        while q:
            x, y = q.popleft()
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny):
                    if d[nx][ny] > d[x][y] + 1:
                        q.append((nx, ny))
                        d[nx][ny] = d[x][y] + 1

        # 2. DFS for checking if travel is possible with safety factor (v)
        def can_travel(v):
            visited = set()

            def dfs(x, y):
                if x == n - 1 and y == n - 1:
                    return True
                visited.add((x, y))
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    if (
                        in_range(nx, ny)
                        and ((nx, ny) not in visited)
                        and d[nx][ny] >= v
                    ):
                        if dfs(nx, ny):
                            return True
                return False

            return dfs(0, 0)

        # 3. Binary Search to find maximum safety factor
        left, right = 0, min(d[0][0], d[-1][-1])
        while left <= right:
            mid = (left + right) // 2
            if can_travel(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right


grid = [[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]
print(Solution().maximumSafenessFactor(grid))

# @lc code=end
