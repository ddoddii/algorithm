#
# @lc app=leetcode id=1482 lang=python3
#
# [1482] Minimum Number of Days to Make m Bouquets
#


# @lc code=start
from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # m : target bouquets, k : min flowers to make a bouquet
        def canMakeBouquet(d, bloomDay, m, k) -> bool:
            n = len(bloomDay)
            length, bouquet = 0, 0
            for i in range(n):
                if bloomDay[i] <= d:
                    length += 1
                    if length == k:
                        bouquet += 1
                        length = 0
                    if bouquet >= m:
                        return True
                else:
                    length = 0
            return bouquet >= m

        if m * k > len(bloomDay):
            return -1
        l, r = min(bloomDay), max(bloomDay)
        while l < r:
            mid = (l + r) // 2
            if canMakeBouquet(mid, bloomDay, m, k):
                r = mid
            else:
                l = mid + 1

        return l


bloomDay = [7, 7, 7, 7, 12, 7, 7]
m = 2
k = 3
print(Solution().minDays(bloomDay, m, k))

# @lc code=end
