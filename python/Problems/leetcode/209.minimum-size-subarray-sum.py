#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window
        left, total = 0, 0
        min_len = len(nums) + 1
        for i, num in enumerate(nums):
            total += num
            while total >= target:
                min_len = min(min_len, i - left + 1)
                total -= nums[left]
                left += 1
        return min_len % (len(nums) + 1)


# @lc code=end
