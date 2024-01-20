#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
from typing import List
import math


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = -math.inf  # holding stock - 1. keep 2. sell
        cash = 0  # not holding stock - 1. continue 2. buy
        for price in prices:
            hold = max(hold, cash - price)
            cash = max(cash, hold + price - fee)
        return cash

    def maxProfit2(self, prices: List[int], fee: int) -> int:
        w_shares = -prices[0]  # cash in hand with shares if you bought on day1
        wo_shares = 0  # cash if you didn't buy in day1

        for i in range(1, len(prices)):
            # max cash in hand with shares
            w_shares = max(
                w_shares,
            )


prices = [1, 3, 2, 8, 4, 9]
fee = 2


# @lc code=end
