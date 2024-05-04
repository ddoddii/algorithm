#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats, lo, hi = 0, 0, len(people) - 1
        people.sort()
        while lo <= hi:
            if people[hi] + people[lo] <= limit:
                lo += 1
            boats += 1
            hi -= 1
        return boats


people = [5, 1, 4, 2]
limit = 6
print(Solution().numRescueBoats(people, limit))

# @lc code=end
