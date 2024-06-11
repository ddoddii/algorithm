#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#

# @lc code=start
from typing import List
from collections import Counter


class Solution:
    """
    Sol1. Use hashmap
    """

    def relativeSortArray1(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = Counter(arr1)
        ans = []
        left = []
        for a in arr2:
            while counter[a]:
                ans.append(a)
                counter[a] -= 1
        for k, v in counter.items():
            if v > 0:
                for _ in range(v):
                    left.append(k)
        left.sort()
        return ans + left

    """
    Sol2. Sort in arr1 - swap the position in order of occurence in arr2
    """

    def relativeSortArray2(self, arr1: List[int], arr2: List[int]) -> List[int]:
        idx = 0
        n, m = len(arr1), len(arr2)
        # relative order
        for i in range(m):
            for j in range(n):
                if arr1[j] == arr2[i]:
                    arr1[idx], arr1[j] = arr1[j], arr1[idx]
                    idx += 1
        # remaining order
        arr1[idx:] = sorted(arr1[idx:])
        return arr1


arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
print(Solution().relativeSortArray(arr1, arr2))

# @lc code=end
