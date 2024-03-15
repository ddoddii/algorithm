#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        answer = [1] * len(nums)
        for i in range(len(nums) - 1):
            left[i + 1] = left[i] * nums[i]
        for i in range(len(nums) - 1, 0, -1):
            right[i - 1] = right[i] * nums[i]
        for i in range(len(nums)):
            answer[i] = left[i] * right[i]

        return answer

    # using prefix, postfix
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        pre = post = 1
        n = len(nums)
        answer = [1] * n
        # calculate prefix (left)
        for i in range(n - 1):
            answer[i + 1] = pre * nums[i]
            pre *= nums[i]
        # calculate postfix (right)
        for i in range(n - 1, -1, -1):
            answer[i] = post * answer[i]
            post *= nums[i]
        return answer


nums = [-1, 1, 0, -3, 3]
sol = Solution()
print(sol.productExceptSelf2(nums))


# @lc code=end
