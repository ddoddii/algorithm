#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
from typing import List
import math


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # m*n grid
        m, n = len(grid), len(grid[0])
        # move down(x+1, y), right(x,y+1)
        dxs, dys = [1, 0], [0, 1]
        answer = [[math.inf for _ in range(n)] for _ in range(m)]

        def in_range(x, y):
            return 0 <= x and x < m and 0 <= y and y < n

        answer[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                x, y = i, j
                for dx, dy in zip(dxs, dys):
                    new_x, new_y = x + dx, y + dy
                    if in_range(new_x, new_y):
                        answer[new_x][new_y] = min(
                            grid[new_x][new_y] + answer[x][y], answer[new_x][new_y]
                        )
        return answer[-1][-1]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
sol = Solution()
print(sol.minPathSum(grid))

# @lc code=end
