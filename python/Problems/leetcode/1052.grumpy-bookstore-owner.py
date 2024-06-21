#
# @lc app=leetcode id=1052 lang=python3
#
# [1052] Grumpy Bookstore Owner
#

# @lc code=start
from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        # sliding window
        n = len(customers)

        # base state
        base_satisfaction = sum(c for c, g in zip(customers, grumpy) if g == 0)

        # first window
        extra_satisfaction = sum(
            c for c, g in zip(customers[:minutes], grumpy[:minutes]) if g == 1
        )

        max_extra_satisfaction = extra_satisfaction

        for i in range(1, n - minutes + 1):
            if grumpy[i - 1] == 1:
                extra_satisfaction -= customers[i - 1]
            if grumpy[i + minutes - 1] == 1:
                extra_satisfaction += customers[i + minutes - 1]

            max_extra_satisfaction = max(max_extra_satisfaction, extra_satisfaction)

        return base_satisfaction + max_extra_satisfaction


customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
minutes = 3
print(Solution().maxSatisfied(customers, grumpy, minutes))
# @lc code=end
