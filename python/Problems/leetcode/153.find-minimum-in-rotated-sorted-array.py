#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        idx = 0
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                idx += 1
            else:
                break
        if idx == len(nums) - 1:
            return nums[0]
        return nums[idx + 1]

    def findMin2(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


nums = [5, 1, 2, 3, 4]
# nums = [11, 13, 15, 17]
sol = Solution()
print(sol.findMin2(nums))

# @lc code=end
