#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        # rule1,2 : row, col
        for i in range(n):
            rows = set()
            cols = set()
            for j in range(n):
                if board[i][j] != ".":
                    if board[i][j] in rows:
                        return False
                    rows.add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in cols:
                        return False
                    cols.add(board[j][i])
            # print(rows, cols)
        # rule3 : 3*3
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                sub = set()
                for k in range(3):
                    for l in range(3):
                        num = board[i + k][j + l]
                        if num != ".":
                            if num in sub:
                                return False
                            sub.add(num)

        return True


board = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."],
]
sol = Solution()
print(sol.isValidSudoku(board))
# @lc code=end
