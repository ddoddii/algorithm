#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # to find pivot

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # if mid is bigger, than pivot is at right of mid
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left

        # to find target is in which side of pivot
        left, right = 0, len(nums) - 1
        if target >= nums[pivot] and target <= nums[right]:
            left = pivot
        else:
            right = pivot

        # binary search to find target idx
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

s = Solution()
print(s.search(nums, target))


# @lc code=end
