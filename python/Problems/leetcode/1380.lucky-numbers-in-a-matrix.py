#
# @lc app=leetcode id=1380 lang=python3
#
# [1380] Lucky Numbers in a Matrix
#

# @lc code=start
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_row, max_col = list(), list()
        n, m = len(matrix), len(matrix[0])
        for row in matrix:
            min_row.append(min(row))
        for j in range(m):
            col = []
            for i in range(n):
                col.append(matrix[i][j])
            max_col.append(max(col))
        return set(min_row) & set(max_col)


# @lc code=end
