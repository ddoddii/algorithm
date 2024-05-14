#
# @lc app=leetcode id=1219 lang=python3
#
# [1219] Path with Maximum Gold
#

# @lc code=start
from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        visited = set()
        row, col = len(grid), len(grid[0])
        max_gold = 0
        dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

        def in_range(x, y):
            return 0 <= x and x < row and 0 <= y and y < col

        def backtrack(x, y, visited, gold):
            nonlocal max_gold  # nonlocal to modify value max_gold inside nested function
            if not in_range(x, y) or (x, y) in visited or grid[x][y] == 0:
                return gold
            visited.add((x, y))
            gold += grid[x][y]
            max_gold = max(max_gold, gold)
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                backtrack(
                    nx,
                    ny,
                    visited,
                    gold,
                )
            visited.remove((x, y))  # backtrack - remove from visited
            return max_gold

        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    max_gold = max(max_gold, backtrack(i, j, visited, 0))
        return max_gold


grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
print(Solution().getMaximumGold(grid))
# @lc code=end
