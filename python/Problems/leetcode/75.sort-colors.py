#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
from typing import List
from collections import Counter


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        zero, one, two = counter[0], counter[1], counter[2]
        nums[:zero] = [0] * zero
        nums[zero : zero + one] = [1] * one
        nums[zero + one :] = [2] * two

    """
    Counting sort
    """

    def sortColors2(self, nums: List[int]) -> None:
        count = [0] * 3
        for num in nums:
            count[num] += 1
        i = 0
        for color, freq in enumerate(count):
            for _ in range(freq):
                nums[i] = color
                i += 1
        print(nums)


nums = [2, 0, 2, 1, 1, 0]
print(Solution().sortColors2(nums))

# @lc code=end
