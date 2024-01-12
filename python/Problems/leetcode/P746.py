# Min Cost Climbing Stairs
"""
DP
"""

from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    n = len(cost)
    if n == 2:
        return min(cost[0], cost[1])

    prev_one, prev_two = cost[0], cost[1]
    for i in range(2, n):
        current_cost = cost[i] + min(prev_one, prev_two)
        prev_one, prev_two = prev_two, current_cost
    return min(prev_one, prev_two)


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(minCostClimbingStairs(cost))
