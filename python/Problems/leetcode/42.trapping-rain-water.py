#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n
        boundary = [0] * n
        ans = 0
        maxLeft[0], maxRight[-1] = height[0], height[-1]
        for i in range(1, n):
            if height[i] > maxLeft[i - 1]:
                maxLeft[i] = height[i]
            else:
                maxLeft[i] = maxLeft[i - 1]
        for i in range(n - 2, -1, -1):
            if height[i] > maxRight[i + 1]:
                maxRight[i] = height[i]
            else:
                maxRight[i] = maxRight[i + 1]
        for i in range(n):
            boundary[i] = min(maxLeft[i], maxRight[i])
        for i in range(n):
            ans += boundary[i] - height[i]
        return ans

    """
    - Two pointer
    """

    def trap2(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        ans = 0
        i, j = 1, len(height) - 1
        lmax, rmax = height[0], height[-1]
        while i <= j:
            if height[i] > lmax:
                lmax = height[i]
            if height[j] > rmax:
                rmax = height[j]

            if lmax <= rmax:
                ans += lmax - height[i]
                i += 1

            else:
                ans += rmax - height[j]
                j -= 1
        return ans


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# height = [4, 2, 0, 3, 2, 5]
print(Solution().trap2(height))
# @lc code=end
