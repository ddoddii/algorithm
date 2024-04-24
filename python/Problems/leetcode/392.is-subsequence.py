#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#


# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # two pointers (s - subsequence, t - original)
        if not s:
            return True
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if i == len(s) - 1 and s[i] == t[j]:
                return True
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        return False

    def isSubsequence2(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


s = "aaaaa"
t = "bbaaa"
print(Solution().isSubsequence2(s, t))

# @lc code=end
