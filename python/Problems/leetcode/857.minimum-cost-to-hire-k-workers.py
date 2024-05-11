#
# @lc app=leetcode id=857 lang=python3
#
# [857] Minimum Cost to Hire K Workers
#

# @lc code=start
from typing import List
import heapq


class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        # ratio = quality / wage (wage 대비 가장 quality 가 높은 순서대로 정렬!)
        ratio = sorted([(w / q, q) for q, w in zip(quality, wage)])
        res = 0.0
        max_heap = []
        max_ratio = 0.0
        quality_sum = 0

        # 초기 baseline 계산
        for i in range(k):
            max_ratio = max(max_ratio, ratio[i][0])
            quality_sum += ratio[i][1]
            heapq.heappush(max_heap, -ratio[i][1])
        res = max_ratio * quality_sum

        # 더 작은 res 있나 확인
        n = len(quality)
        for i in range(k, n):
            max_ratio = max(max_ratio, ratio[i][0])
            quality_sum += ratio[i][1] + heapq.heappop(max_heap)
            heapq.heappush(max_heap, -ratio[i][1])
            res = min(res, max_ratio * quality_sum)
        return res


quality = [3, 1, 10, 10, 1]
wage = [4, 8, 2, 2, 7]
k = 3
print(Solution().mincostToHireWorkers(quality, wage, k))
# @lc code=end
