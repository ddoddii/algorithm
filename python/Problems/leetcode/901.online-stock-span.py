#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#


# @lc code=start
class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if not self.stack or (self.stack and self.stack[-1][0]) > price:
            self.stack.append((price, 1))
            return 1
        count = 1
        while self.stack and self.stack[-1][0] <= price:
            count += self.stack.pop()[1]
        self.stack.append((price, count))
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end
