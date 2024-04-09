#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#


# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic1 = {}
        dic2 = {}
        words = s.split()

        if len(pattern) != len(words):
            return False
        for pattern, word in zip(pattern, words):
            if (pattern in dic1 and dic1[pattern] != word) or (
                word in dic2 and dic2[word] != pattern
            ):
                return False
            dic1[pattern] = word
            dic2[word] = pattern
        return True


pattern = "abba"
s = "dog cat cat dog"
sol = Solution()
print(sol.wordPattern(pattern, s))
# @lc code=end
