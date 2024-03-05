#
# @lc app=leetcode id=948 lang=python3
#
# [948] Bag of Tokens
#

# @lc code=start
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if not tokens:
            return 0
        tokens.sort()
        max_score = 0
        score = 0
        left, right = 0, len(tokens) - 1
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)

            elif score > 0 and right > left:
                power += tokens[right]
                score -= 1
                right -= 1

            else:
                break

        return max_score


tokens = [100, 200]
power = 150
sol = Solution()
print(sol.bagOfTokensScore(tokens, power))
# @lc code=end
