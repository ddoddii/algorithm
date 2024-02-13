#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        idx = 0
        intervals.sort(key=lambda x: x[0])
        while idx < len(intervals):
            # not overlapping
            if idx == len(intervals) - 1 or intervals[idx][1] < intervals[idx + 1][0]:
                answer.append(intervals[idx])
                idx += 1
            # overlapping
            else:
                intervals[idx + 1][0] = intervals[idx][0]
                intervals[idx + 1][1] = max(intervals[idx][1], intervals[idx + 1][1])
                idx += 1
        return answer

    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        answer = []

        for interval in intervals:
            # start or not overlapping
            if not answer or answer[-1][1] < interval[0]:
                answer.append(interval)
            # overlapping
            else:
                answer[-1][1] = max(answer[-1][1], interval[1])
        return answer


intervals = [[1, 4], [2, 3]]
sol = Solution()
print(sol.merge(intervals))

# @lc code=end
