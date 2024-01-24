#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [0 for _ in range(len(nums))]

        def backtracking(temp, used):
            if len(temp) == len(nums):
                res.append(temp[:])
                # note [:] make a deep copy since otherwise we'd be append the same list over and over

            for i in range(len(nums)):
                if not used[i]:
                    temp.append(nums[i])
                    used[i] = 1
                    backtracking(temp, used)
                    used[i] = 0
                    temp.pop()

        backtracking([], used)
        return res


nums = [1, 2, 3]
s = Solution()
print(s.permute(nums))


# @lc code=end
