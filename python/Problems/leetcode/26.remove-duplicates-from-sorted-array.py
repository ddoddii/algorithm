#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j

    def removeDuplicates2(self, nums: List[int]) -> int:
        idx = 0
        while idx < len(nums) - 1:
            if nums[idx] == nums[idx + 1]:
                del nums[idx]
            else:
                idx += 1
        return len(nums)


# @lc code=end
