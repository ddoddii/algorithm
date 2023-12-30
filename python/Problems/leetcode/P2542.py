# Maximum Subsequence Score
from typing import List
import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs = sorted(pairs, key=lambda pair: pair[1], reverse=True)
        minHeap = []
        n1Sum = 0
        res = 0

        for n1, n2 in pairs:
            n1Sum += n1
            heapq.heappush(minHeap, n1)

            if len(minHeap) > k:
                n1Pop = heapq.heappop(minHeap)
                n1Sum -= n1Pop
            if len(minHeap) == k:
                res = max(res, n1Sum * n2)
        return res


nums1 = [1, 3, 3, 2]
nums2 = [2, 1, 3, 4]
k = 3
n = len(nums1)
