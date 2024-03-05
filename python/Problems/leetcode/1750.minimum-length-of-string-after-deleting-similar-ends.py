#
# @lc app=leetcode id=1750 lang=python3
#
# [1750] Minimum Length of String After Deleting Similar Ends
#


# @lc code=start
class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            curr = s[left]
            while left <= right and s[left] == curr:
                left += 1
            while left <= right and s[right] == curr:
                right -= 1

        return right - left + 1 if right >= left else 0


sol = Solution()
s = "bbbbbbbbbbbbbbbbbbbbb"
print(sol.minimumLength(s))

# @lc code=end
