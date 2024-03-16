#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # using prefix sum
        count = 0
        max_length = 0
        count_to_idx = {0: -1}

        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in count_to_idx:
                max_length = max(max_length, i - count_to_idx[count])
            else:
                count_to_idx[count] = i

        return max_length


nums = [1, 1, 0, 0, 1, 1, 0, 1, 1]
# nums = [0, 1]
sol = Solution()
print(sol.findMaxLength(nums))


# @lc code=end
