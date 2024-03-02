#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [["." for _ in range(n)] for _ in range(n)]
        answer = []

        def search(row, cols, negDiags, posDiags, board):
            if row == n:
                answer.append(["".join(row) for row in board])
                return
            for col in range(n):
                if col in cols or (row - col) in negDiags or (row + col) in posDiags:
                    continue
                cols.add(col)
                negDiags.add(row - col)
                posDiags.add(row + col)
                board[row][col] = "Q"
                search(row + 1, cols, negDiags, posDiags, board)
                # backtrack
                board[row][col] = "."
                cols.remove(col)
                negDiags.remove(row - col)
                posDiags.remove(row + col)

        search(0, set(), set(), set(), board)
        return answer


n = 5
sol = Solution()
print(sol.solveNQueens(n))

# @lc code=end
