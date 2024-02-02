#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # n * m grid
        n = len(grid)
        m = len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        islands = []
        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

        def in_range(x, y):
            return 0 <= x and x < n and 0 <= y and y < m

        def can_go(x, y):
            if not in_range(x, y):
                return False
            if grid[x][y] == "0" or visited[x][y]:
                return False
            return True

        def dfs(x, y, cnt):
            for dx, dy in zip(dxs, dys):
                new_x, new_y = x + dx, y + dy
                if can_go(new_x, new_y):
                    visited[new_x][new_y] = 1
                    cnt += 1
                    dfs(new_x, new_y, cnt)

        for i in range(n):
            for j in range(m):
                if can_go(i, j):
                    visited[i][j] = True
                    cnt = 1
                    dfs(i, j, cnt)
                    islands.append(cnt)

        return len(islands)


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
sol = Solution()
print(sol.numIslands(grid))
# @lc code=end
