#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#


# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k and stack and digit < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(digit)
        stack = stack[:-k] if k else stack
        ans = "".join(stack).lstrip("0")
        return ans if ans else "0"


num = "1432219"
k = 3
print(Solution().removeKdigits(num, k))

# @lc code=end
