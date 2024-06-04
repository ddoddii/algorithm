#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#


# @lc code=start
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        counter = Counter(s)
        ans = 0
        odd_found = False
        for count in counter.values():
            if count % 2 == 0:
                ans += count
            else:
                ans += count - 1
                odd_found = True
        if odd_found:
            ans += 1
        return ans


s = "abccccdd"
print(Solution().longestPalindrome(s))


# @lc code=end
