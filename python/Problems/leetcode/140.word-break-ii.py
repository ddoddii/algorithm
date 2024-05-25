#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        ans = []

        def recursion(curr_idx, curr_sent):
            if curr_idx == n:
                ans.append(curr_sent)
                return

            for end_idx in range(curr_idx + 1, n + 1):
                if s[curr_idx:end_idx] in wordDict:
                    recursion(
                        end_idx,
                        curr_sent + (" " if curr_sent else "") + s[curr_idx:end_idx],
                    )

        recursion(0, "")

        return ans


s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
print(Solution().wordBreak(s, wordDict))
# @lc code=end
