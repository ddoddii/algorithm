#
# @lc app=leetcode id=2962 lang=python3
#
# [2962] Count Subarrays Where Max Element Appears at Least K Times
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        target = max(nums)


nums = [1, 3, 2, 3, 3]
k = 2
sol = Solution()
print(sol.countSubarrays(nums, k))
# @lc code=end
