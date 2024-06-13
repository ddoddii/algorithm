#
# @lc app=leetcode id=2037 lang=python3
#
# [2037] Minimum Number of Moves to Seat Everyone
#

# @lc code=start
from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        ans = 0
        for x, y in zip(seats, students):
            ans += abs(x - y)
        return ans


seats = [4, 1, 5, 9]
students = [1, 3, 2, 6]
print(Solution().minMovesToSeat(seats, students))
# @lc code=end
