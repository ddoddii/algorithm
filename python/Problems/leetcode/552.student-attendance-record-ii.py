#
# @lc app=leetcode id=552 lang=python3
#
# [552] Student Attendance Record II
#


# @lc code=start
from collections import Counter
import sys

sys.setrecursionlimit(10**7)


class Solution:
    """
    sol1. Recursion -> TLE
    """

    def checkRecord(self, n: int) -> int:
        # A가 2번 이상, L은 연속 3번이면 안됨
        count = 0
        record = ["A", "L", "P"]
        mod = 10**9 + 7

        def is_eligible(curr_attendance, curr_record):
            counter = Counter(curr_record)
            if counter["A"] >= 1 and curr_attendance == "A":
                return False
            if len(curr_record) > 1:
                if (
                    curr_record[-1] == "L"
                    and curr_record[-2] == "L"
                    and curr_attendance == "L"
                ):
                    return False
            return True

        def recursion(curr_idx, curr_record):
            nonlocal count
            if curr_idx == n:
                count += 1
                return
            for r in record:
                if is_eligible(r, curr_record):
                    recursion(curr_idx + 1, curr_record + r)

        recursion(0, "")
        return count % mod

    """
    sol2. DP
    """

    def checkRecord2(self, n: int) -> int:
        mod = 10**9 + 7
        # dp[i][a][l] : length i, 'a' absences, 'l' consecutive lates
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        dp[0][0][0] = 1

        for i in range(1, n + 1):
            for a in range(2):
                for l in range(3):
                    # Case 1 : Add 'P'
                    dp[i][a][0] = (dp[i][a][0] + dp[i - 1][a][l]) % mod
                    # Case 2 : Add 'A' if no 'A'
                    if a > 0:
                        dp[i][a][0] = (dp[i][a][0] + dp[i - 1][a - 1][l]) % mod
                    # Case 3 : Add 'L' if not already two consecutive 'L's
                    if l > 0:
                        dp[i][a][l] = (dp[i][a][l] + dp[i - 1][a][l - 1]) % mod
        res = 0
        for a in range(2):
            for l in range(3):
                res = (res + dp[n][a][l]) % mod
        return res


n = 3
print(Solution().checkRecord2(n))
# @lc code=end
