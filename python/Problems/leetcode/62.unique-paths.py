#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#


# @lc code=start
class Solution:
    # DP - 2D
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)]
        for i in range(0, m - 1):
            for j in range(0, n - 1):
                grid[i + 1][j + 1] = grid[i + 1][j] + grid[i][j + 1]
        return grid[-1][-1]


# @lc code=end
