#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        grid = [[1 for _ in range(i + 1)] for i in range(numRows)]
        if numRows <= 2:
            return grid
        for i in range(2, numRows):
            for j in range(1, i):
                grid[i][j] = grid[i - 1][j - 1] + grid[i - 1][j]
        return grid


# @lc code=end
