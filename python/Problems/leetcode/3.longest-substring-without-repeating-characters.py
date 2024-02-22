#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        freq = defaultdict(int)
        maxCount = 0
        start = 0
        for i in range(len(s)):
            if s[i] in freq:
                start = max(start, freq[s[i]] + 1)
            freq[s[i]] = i
            print(freq)
            maxCount = max(maxCount, i - start + 1)
        return maxCount


sol = Solution()
s = "dvdfaa"
print(sol.lengthOfLongestSubstring(s))


# @lc code=end
