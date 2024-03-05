#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for idx in len(s):
            if counter[s[idx]] == 1:
                return idx


s = "leetcode"
sol = Solution()
print(sol.firstUniqChar(s))

# @lc code=end
