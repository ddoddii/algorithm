# Best Time to Buy and sell stock
# buy = 먼저 , sell = 나중
# 이득 = sell - buy (나중 - 먼저)
from typing import List


def maxProfit(prices: List[int]) -> int:
    profit = 0
    minPurchase = prices[0]
    # 먼저 (buy)
    for i in range(1, len(prices)):
        # 나중 (sell)
        profit = max(profit, prices[i] - minPurchase)
        minPurchase = min(minPurchase, prices[i])
    return profit


def maxProfit2(prices: List[int]) -> int:
    profit = 0
    minPurchase = prices[0]
    for price in prices:
        curProfit = price - minPurchase
        if curProfit > profit:
            profit = curProfit
        if price < minPurchase:
            minPurchase = price


prices = [7, 1, 5, 3, 6, 4]
