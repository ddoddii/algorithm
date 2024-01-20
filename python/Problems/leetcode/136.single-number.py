#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
from typing import List

"""
- Bit manipulation 
- XOR (^)
- a^a = 0, a^0 = a
- XOR operation to effectively filter out all the numbers that appear in pairs, 
leaving only the unique number
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor = xor ^ num
        return xor


nums = [4, 1, 2, 1, 2]
s = Solution()
print(s.singleNumber(nums))


# @lc code=end
