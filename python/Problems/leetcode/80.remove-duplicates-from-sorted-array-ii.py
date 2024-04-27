#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        occur = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                occur += 1
            else:
                occur = 1
            if occur <= 2:
                nums[idx] = nums[i]
                idx += 1
        print(nums)
        return idx

    def removeDuplicates2(self, nums: List[int]) -> int:
        k = 0
        for num in nums:
            if k < 2 or nums[k - 2] != num:
                nums[k] = num
                k += 1
        print(nums)
        return k


nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(Solution().removeDuplicates2(nums))

# @lc code=end
