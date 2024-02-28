#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []

        def is_palindrome(string, l, r) -> bool:
            if l >= r:
                return True
            if string[l] != string[r]:
                return False
            return is_palindrome(string, l + 1, r - 1)

        if len(s) == 1:
            return [[s]]

        # find all substrings that is palindrome
        def dfs(start, path):
            if start == len(s):
                answer.append(path[:])
                return
            for end in range(start, len(s)):
                if is_palindrome(s, start, end):
                    dfs(end + 1, path + [s[start : end + 1]])

        dfs(0, [])
        return answer

    """
    sol2. Backtracking
    """

    def partition2(self, s: str) -> List[List[str]]:
        answer = []
        sub = []

        def is_palindrome(string, l, r) -> bool:
            if l >= r:
                return True
            if string[l] != string[r]:
                return False
            return is_palindrome(string, l + 1, r - 1)

        # choice for partition
        def dfs(idx):
            if idx == len(s):
                answer.append(sub[:])
                return
            for end in range(idx, len(s)):
                if is_palindrome(s, idx, end):
                    sub.append(s[idx : end + 1])
                    dfs(end + 1)
                    sub.pop()

        dfs(0)
        return answer


s = "abbab"
sol = Solution()
print(sol.partition2(s))

# @lc code=end
