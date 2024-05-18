#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        n = len(nums)
        ans = list(k for k, v in counter.items() if v > n / 2)

        return ans[0]


nums = [3, 2, 3]
print(Solution().majorityElement(nums))

# @lc code=end
