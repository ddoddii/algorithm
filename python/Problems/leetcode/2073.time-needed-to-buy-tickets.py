#
# @lc app=leetcode id=2073 lang=python3
#
# [2073] Time Needed to Buy Tickets
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        dic = defaultdict(int)
        target = tickets[k]
        while dic[k] < target:
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    dic[i] += 1
                    time += 1
                    if dic[k] == target:
                        break
        return time

    def timeRequiredToBuy2(self, tickets: List[int], k: int) -> int:
        time = 0
        while True:
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    time += 1
                if tickets[i] == 0:
                    return time


tickets = [2, 3, 2]
k = 2
sol = Solution()
print(sol.timeRequiredToBuy(tickets, k))
# @lc code=end
