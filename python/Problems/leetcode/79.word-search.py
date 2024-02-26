#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        def in_range(x, y):
            return (
                x >= 0
                and x < len(board)
                and y >= 0
                and y < len(board[0])
                and not visited[x][y]
            )

        def find(x, y, idx):
            if idx == len(word):
                return True

            if not in_range(x, y) or board[x][y] != word[idx]:
                return False

            visited[x][y] = True

            dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
            for dx, dy in zip(dxs, dys):
                new_x, new_y = x + dx, y + dy
                if find(new_x, new_y, idx + 1):
                    return True
            visited[x][y] = False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if find(i, j, 0):
                        return True

        return False

    def exist2(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            # good condition
            if i == len(word):
                return True
            # bad condition
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or word[i] != board[r][c]
                or (r, c) in path
            ):
                return False

            path.add((r, c))
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
sol = Solution()
print(sol.exist2(board, word))
# @lc code=end
