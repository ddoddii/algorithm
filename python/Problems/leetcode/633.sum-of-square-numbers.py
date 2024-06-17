#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#


# @lc code=start
class Solution:
    # two pointers
    def judgeSquareSum(self, c: int) -> bool:
        right = int(c**0.5)
        left = 0
        while left <= right:
            sum = right**2 + left**2
            if sum == c:
                return True
            elif sum > c:
                right -= 1
            else:
                left += 1
        return False


c = 10
print(Solution().judgeSquareSum(c))

# @lc code=end
