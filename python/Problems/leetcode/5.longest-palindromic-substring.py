#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        start, maxLength = 0, 1

        # 1-length substring are all palindromes
        for i in range(len(s)):
            dp[i][i] = True

        # check 2-length substring
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start, maxLength = i, 2

        # check for longer than 3 characters
        for length in range(3, len(s) + 1):
            for i in range(len(s) - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > maxLength:
                        start, maxLength = i, length

        return s[start : start + maxLength]

    """
    - i 에서 시작해서 양 옆으로 확장
    - odd length, even length <- edge case 생각 !!
    """

    def longestPalindrome2(self, s: str) -> str:
        res = ""
        resLen = 0
        n = len(s)

        for i in range(n):
            # odd length
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            # even length
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res


s = "babad"
sol = Solution()
print(sol.longestPalindrome2(s))

# @lc code=end
