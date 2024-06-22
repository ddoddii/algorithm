#
# @lc app=leetcode id=1248 lang=python3
#
# [1248] Count Number of Nice Subarrays
#

# @lc code=start
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] %= 2
        prefix_count = [0] * (n + 1)
        prefix_count[0] = 1
        # prefix sum
        s, ans = 0, 0
        for num in nums:
            s += num
            if s >= k:
                ans += prefix_count[s - k]
            prefix_count[s] += 1
        return ans


nums = [1, 1, 2, 1, 1]
k = 3
print(Solution().numberOfSubarrays(nums, k))

# @lc code=end
