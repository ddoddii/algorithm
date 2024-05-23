#
# @lc app=leetcode id=1712 lang=python3
#
# [1712] Ways to Split Array Into Three Subarrays
#

# @lc code=start
from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)

        ans = 0
        n = len(nums)
        for i in range(1, n):
            j = bisect_left(prefix, 2 * prefix[i])
            k = bisect_right(prefix, (prefix[i] + prefix[-1]) // 2)
            ans += max(0, min(n, k) - max(i + 1, j))

        return ans % (pow(10, 9) + 7)


nums = [1, 2, 2, 2, 5, 0]
print(Solution().waysToSplit(nums))

# @lc code=end
