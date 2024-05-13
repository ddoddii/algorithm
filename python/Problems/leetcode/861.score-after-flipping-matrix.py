#
# @lc app=leetcode id=861 lang=python3
#
# [861] Score After Flipping Matrix
#

# @lc code=start
from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        res = (1 << (col - 1)) * row
        for j in range(1, col):
            val = 1 << (col - 1 - j)
            set_count = 0
            for i in range(row):
                if grid[i][j] == grid[i][0]:
                    set_count += 1
            res += max(set_count, row - set_count) * val

        return res


grid = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
print(Solution().matrixScore(grid))
# @lc code=end
