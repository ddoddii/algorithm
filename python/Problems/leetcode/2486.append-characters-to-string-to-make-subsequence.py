#
# @lc app=leetcode id=2486 lang=python3
#
# [2486] Append Characters to String to Make Subsequence
#


# @lc code=start
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # find the longest prefix of t that is subsequence of s
        n, m = len(s), len(t)
        j = 0
        for i in range(n):
            if j < m and s[i] == t[j]:
                j += 1

        return m - j


s = "coaching"
t = "coding"
print(Solution().appendCharacters(s, t))
# @lc code=end
