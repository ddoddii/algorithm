# Find Peak Element
from typing import List

# O(n) - linear scan
def findPeakElement( nums: List[int]) -> int:
    n = len(nums)
    if n <= 3:
        return nums.index(max(nums))
    if nums[0] > nums[1]:
        return 0
    if nums[n - 1] > nums[n - 2]:
        return n - 1
    for i in range(1, n - 1):
        before = nums[i - 1]
        curr = nums[i]
        after = nums[i + 1]
        if curr == max(before, after, curr):
            return i
        if i == n - 2:
            if curr == max(before, curr):
                return i

# O(logn) - Binary Search
def findPeakElement2(nums: List[int]) -> int:



nums = [1, 2, 1, 3, 5, 6, 4]
n = len(nums)
