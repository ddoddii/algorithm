#
# @lc app=leetcode id=1208 lang=python3
#
# [1208] Get Equal Substrings Within Budget
#


# @lc code=start
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        start, max_length, curr_cost = 0, 0, 0
        for end in range(n):
            curr_cost += abs(ord(s[end]) - ord(t[end]))
            while curr_cost > maxCost:
                curr_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            max_length = max(max_length, end - start + 1)
        return max_length


s = "abcd"
t = "bcdf"
maxCost = 3
print(Solution().equalSubstring(s, t, maxCost))
# @lc code=end
