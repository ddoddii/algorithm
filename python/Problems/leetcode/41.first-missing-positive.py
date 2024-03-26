#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        for n in range(1, length + 1):
            if dic[n] == 0:
                return n
        if dic[0] > 0:
            return length
        else:
            return length + 1

    def firstMissingPositive2(self, nums: List[int]) -> int:
        nums = set(nums)
        i = 1
        while i in nums:
            i += 1
        return i


nums = [2]
sol = Solution()
print(sol.firstMissingPositive(nums))
# @lc code=end
