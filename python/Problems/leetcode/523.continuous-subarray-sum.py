#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
from typing import List
from collections import defaultdict


# ! Prefix sum
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        dic = defaultdict(int)
        dic[0] = -1
        prefix_sum = 0
        for i in range(n):
            prefix_sum += nums[i]
            if k != 0:
                prefix_sum %= k
            if prefix_sum in dic:
                if i - dic[prefix_sum] > 1:
                    return True
            else:
                dic[prefix_sum] = i
        return False


nums = [1, 23, 2, 4, 6, 6]
k = 7

print(Solution().checkSubarraySum(nums, k))
# @lc code=end
