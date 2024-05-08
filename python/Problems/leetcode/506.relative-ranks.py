#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#

# @lc code=start
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = []
        rankmap = dict()
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for idx, s in enumerate(sorted(score, reverse=True)):
            rankmap[s] = idx
        for s in score:
            if rankmap[s] < 3:
                ans.append(ranks[rankmap[s]])
            else:
                ans.append(str(rankmap[s] + 1))
        return ans

    def findRelativeRanks2(self, score: List[int]) -> List[str]:
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(
            map(str, range(4, len(score) + 1))
        )
        place = sorted(score, reverse=True)
        d = dict(zip(place, rank))
        return [d.get(s) for s in score]


score = [10, 3, 8, 9, 4]
print(Solution().findRelativeRanks2(score))

# @lc code=end
