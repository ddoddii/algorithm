#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#


# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        binary = format(n, "b")
        one_count = binary.count("1")
        if one_count == 1:
            return True
        return False

    def isPowerOfTwo2(self, n: int) -> bool:
        return n > 0 and n.bit_count() == 1

    def isPowerOfTwo3(self, n: int) -> bool:
        return n > 0 and (n & n - 1) == 0


# @lc code=end
