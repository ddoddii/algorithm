# Merge Sorted Array
from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for i in range(0, n):
        nums1[m + i] = nums2[i]
    nums1.sort()


nums1 = [1, 2, 3, 0, 0, 0, 0]
nums2 = [2, 5, 6, 7]
m = 3
n = 4
