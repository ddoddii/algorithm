#
# @lc app=leetcode id=945 lang=python3
#
# [945] Minimum Increment to Make Array Unique
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        next_available = 0
        move = 0

        for num in nums:
            next_available = max(next_available, num)
            move += next_available - num
            next_available += 1

        return move


nums = [3, 2, 1, 2, 1, 7]
print(Solution().minIncrementForUnique(nums))
# @lc code=end
