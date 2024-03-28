#
# @lc app=leetcode id=2958 lang=python3
#
# [2958] Length of Longest Subarray With at Most K Frequency
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # sliding window
        left = right = 0
        max_cnt = 0
        occurMap = defaultdict(int)
        while right < len(nums):
            occurMap[nums[right]] += 1
            while occurMap[nums[right]] > k:
                occurMap[nums[left]] -= 1
                left += 1
            max_cnt = max(max_cnt, right - left + 1)
            right += 1
        return max_cnt


nums = [3, 1, 1]
k = 1
sol = Solution()
print(sol.maxSubarrayLength(nums, k))

# @lc code=end
