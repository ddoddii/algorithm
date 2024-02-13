#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        n = len(merged)
        if n % 2 == 1:
            answer = merged[n // 2]
        else:
            answer = (merged[n // 2] + merged[n // 2 - 1]) / 2
        return answer

    """
    - Time complexity should be O(log(m+n))
    - 짧은 것에 Binary Search
    """

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # for A
            j = half - i - 2  # for B
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if i + 1 < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if j + 1 < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2 == 1:
                    return min(Aright, Bright)
                # even
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # A is too big
            elif Aleft > Bright:
                r = i - 1
            # A is too small
            else:
                l = i + 1


# @lc code=end
