#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()

        def backtrack(remaining, combo, start):
            if remaining == 0:
                res.append(list(combo))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                combo.append(candidates[i])
                backtrack(remaining - candidates[i], combo, i)
                combo.pop()

        backtrack(target, [], 0)
        return res


candidates = [2, 3, 6, 7]
target = 7

s = Solution()
print(s.combinationSum(candidates, target))
# @lc code=end
