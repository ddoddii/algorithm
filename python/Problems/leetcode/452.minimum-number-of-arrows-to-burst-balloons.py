#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        end = points[0][1]
        count = 1
        for i in range(1, len(points)):
            if points[i][0] > end:
                count += 1
                end = points[i][1]
        return count


# @lc code=end
