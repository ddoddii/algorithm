#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        answer = []
        idx = 0

        # 1. Add all intervals before start of newInterval start
        while idx < len(intervals) and intervals[idx][1] < newInterval[0]:
            answer.append(intervals[idx])
            idx += 1

        # 2. Merge with newInterval
        while idx < len(intervals) and intervals[idx][0] <= newInterval[1]:
            newInterval = [
                min(newInterval[0], intervals[idx][0]),
                max(newInterval[1], intervals[idx][1]),
            ]
            idx += 1
        answer.append(newInterval)

        # 3. Add all intervals after merge
        while idx < len(intervals):
            answer.append(intervals[idx])
            idx += 1

        return answer


intervals = [[1, 5], [6, 8], [9, 13], [14, 15]]
newInterval = [7, 9]
# result : [[1,5],[6,13]]
sol = Solution()
print(sol.insert(intervals, newInterval))

# @lc code=end
