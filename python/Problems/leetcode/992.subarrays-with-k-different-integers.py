#
# @lc app=leetcode id=992 lang=python3
#
# [992] Subarrays with K Different Integers
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums, k):
            left, right, cnt = 0, 0, 0
            d = defaultdict(int)
            while right < len(nums):
                d[nums[right]] += 1
                while len(d) > k:
                    d[nums[left]] -= 1
                    if d[nums[left]] == 0:
                        del d[nums[left]]
                    left += 1
                cnt += right - left + 1
                right += 1

            return cnt

        return atMostK(nums, k) - atMostK(nums, k - 1)


nums = [1, 2, 1, 2, 3]
k = 2
sol = Solution()
print(sol.subarraysWithKDistinct(nums, k))


# @lc code=end
