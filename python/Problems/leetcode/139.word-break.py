#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # sol1 : DP
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        max_len = max(map(len, wordDict))
        wordSet = set(wordDict)
        # find word that ends at i
        for i in range(1, n + 1):
            for j in range(i - 1, max(i - max_len - 1, -1), -1):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
            # print(dp)
        return dp[n]

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        # sol2 : DFS & Memoization
        memo = defaultdict(int)
        wordSet = set(wordDict)

        def dfs(s, wordSet, memo):
            if s in memo:
                return memo[s]
            if s in wordSet:
                return True
            for i in range(1, len(s)):
                prefix = s[:i]
                if prefix in wordSet and dfs(s[i:], wordSet, memo):
                    memo[s] = True
                    return True
            memo[s] = False
            return False

        return dfs(s, wordSet, memo)


s = "aaaaaaa"
wordDict = ["aaaa", "aaa"]
print(Solution().wordBreak2(s, wordDict))

# @lc code=end
