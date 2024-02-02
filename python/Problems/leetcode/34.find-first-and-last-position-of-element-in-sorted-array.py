#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
from typing import List

"""
- binary search
- 1. 리스트 내에 중복된 값이 있는 경우 idx 를 찾을 때 첫번째 인덱스, 마지막 인덱스 찾는 함수 다르게 짜기
- 
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(left, right, nums, target):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target or (mid > 0 and nums[mid - 1] == target):
                    right = mid - 1
                else:
                    return mid
            return -1

        def findLast(left, right, nums, target):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target or (
                    mid < len(nums) - 1 and nums[mid + 1] == target
                ):
                    left = mid + 1
                else:
                    return mid
            return -1

        if not nums:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        first_idx = findFirst(left, right, nums, target)
        if first_idx == -1:
            return [-1, -1]
        right_idx = findLast(left, right, nums, target)
        return [first_idx, right_idx]

    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, target, leftBias):
            l, r = 0, len(nums) - 1
            i = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
                # 일치해도 포인터 업데이트
                else:
                    i = mid
                    if leftBias:
                        r = mid - 1
                    else:
                        l = mid + 1
            return i

        left = binarySearch(nums, target, True)
        right = binarySearch(nums, target, False)
        return [left, right]


nums = [7, 8, 8]
target = 8
sol = Solution()
print(sol.searchRange2(nums, target))
# @lc code=end
