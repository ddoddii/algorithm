#
# @lc app=leetcode id=1992 lang=python3
#
# [1992] Find All Groups of Farmland
#

# @lc code=start
from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        row, col = len(land), len(land[0])
        visited = [[False for _ in range(col)] for _ in range(row)]
        dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

        def in_range(x, y):
            return 0 <= x and x < row and 0 <= y and y < col

        def is_land(x, y):
            return in_range(x, y) and not visited[x][y] and land[x][y] == 1

        def dfs(x, y, farm):
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if is_land(nx, ny):
                    farm[2], farm[3] = max(farm[2], nx), max(farm[3], ny)
                    visited[nx][ny] = True
                    dfs(nx, ny, farm)

        for x in range(row):
            for y in range(col):
                if is_land(x, y):
                    visited[x][y] = True
                    farm = [0] * 4
                    farm[0], farm[1], farm[2], farm[3] = x, y, x, y
                    dfs(x, y, farm)
                    ans.append(farm)

        return ans

    def findFarmland2(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        res = []
        for i in range(m):
            for j in range(n):
                if (
                    land[i][j] == 1
                    and (i == 0 or land[i - 1][j] == 0)
                    and (j == 0 or land[i][j - 1] == 0)
                ):
                    x, y = i, j
                    while y + 1 < n and land[x][y + 1] == 1:
                        y += 1
                    while x + 1 < m and land[x + 1][y] == 1:
                        x += 1
                    res.append([i, j, x, y])
        return res


land = [[0, 1], [1, 0]]
print(Solution().findFarmland2(land))
# @lc code=end
