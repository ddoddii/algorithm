#
# @lc app=leetcode id=2864 lang=python3
#
# [2864] Maximum Odd Binary Number
#


# @lc code=start
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count("1")
        zeros = s.count("0")
        answer = "1" * (ones - 1) + "0" * zeros + "1"
        return answer


s = "0101"
sol = Solution()
print(sol.maximumOddBinaryNumber(s))
# @lc code=end
