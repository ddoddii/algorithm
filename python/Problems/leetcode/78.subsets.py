#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
from typing import List
from itertools import combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def addSubsets(nums, i, subset, answer):
            print(subset)
            if i == len(nums):
                answer.append(subset[:])
                return answer
            # choosing nums[i]
            subset.append(nums[i])
            addSubsets(nums, i + 1, subset, answer)
            # not choosing nums[i]
            subset.pop()
            addSubsets(nums, i + 1, subset, answer)

        addSubsets(nums, 0, [], answer)
        return answer


sol = Solution()
nums = [1, 2, 3]
print(sol.subsets(nums))
# @lc code=end
