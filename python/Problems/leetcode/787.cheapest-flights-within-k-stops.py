#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
import heapq
from typing import List
from collections import defaultdict


class Solution:
    """
    - Dijkstra's Algorithm
    - Time : O(F*k*log(n*k))
    - heappush, heappop for k stops : O(log(n*k))
    - max num of heap operations : O(F*k) , where F = number of flights
    """

    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        flightMap = defaultdict(list)
        for begin, end, price in flights:
            flightMap[begin].append((end, price))
        # heap : [amount, src, k]
        heap = [(0, src, k + 1)]
        visited = defaultdict(lambda: float("inf"))
        # keep track of least amount to get to loc with how much steps
        visited[(src, k + 1)] = 0

        while heap:
            amount, loc, k_left = heapq.heappop(heap)
            if loc == dst:
                return amount
            if k_left > 0:
                for next_loc, price in flightMap[loc]:
                    new_amount = amount + price
                    if new_amount < visited[(next_loc, k_left - 1)]:
                        visited[((next_loc, k_left - 1))] = new_amount
                        heapq.heappush(heap, (new_amount, next_loc, k_left - 1))
        return -1

    """
    - Bellman-Ford Algorithm
    - Time : O(k * E) (k : at most stops, E : edges)
    """

    def findCheapestPrice2(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()
            for begin, end, price in flights:
                if prices[begin] == float("inf"):
                    continue
                if prices[begin] + price < tmpPrices[end]:
                    tmpPrices[end] = prices[begin] + price
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]


sol = Solution()
n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1

print(sol.findCheapestPrice2(n, flights, src, dst, k))
# @lc code=end
