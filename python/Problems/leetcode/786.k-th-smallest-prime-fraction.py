#
# @lc app=leetcode id=786 lang=python3
#
# [786] K-th Smallest Prime Fraction
#

# @lc code=start
from typing import List
from heapq import heappush, heappop


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # 1. Initialize heap
        heap = []
        for i in range(len(arr) - 1):
            heappush(heap, (arr[i] / arr[-1], i, len(arr) - 1))
        # 2. Find k th smallest fraction
        for _ in range(k - 1):
            frac, i, j = heappop(heap)
            if j - 1 > i:
                heappush(heap, (arr[i] / arr[j - 1], i, j - 1))
        frac, i, j = heappop(heap)
        return (arr[i], arr[j])


arr = [1, 2, 3, 5]
k = 3
print(Solution().kthSmallestPrimeFraction(arr, k))
# @lc code=end
