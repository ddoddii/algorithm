#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start
from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # graph shortest path, bfs
        def neighbors(state):
            for i in range(4):
                x = int(state[i])
                for d in range(-1, 2):
                    y = (x + d) % 10
                    yield state[:i] + str(y) + state[i + 1 :]

        dead = set(deadends)
        if "0000" in dead or target in dead:
            return -1
        if target == "0000":
            return 0

        q = deque([("0000", 0)])
        visited = set(["0000"])

        while q:
            state, cnt = q.popleft()
            for neighbor in neighbors(state):
                if neighbor == target:
                    return cnt + 1
                if neighbor not in visited and neighbor not in dead:
                    visited.add(neighbor)
                    q.append([neighbor, cnt + 1])

        return -1


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
print(Solution().openLock(deadends, target))
# @lc code=end
