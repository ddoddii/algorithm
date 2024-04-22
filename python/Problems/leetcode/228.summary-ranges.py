#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
from typing import List


class Solution:
    # sol1
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0
        while i < len(nums):
            start = nums[i]
            # print("start : ", start)
            while i < len(nums) - 1 and nums[i + 1] == nums[i] + 1:
                i += 1
            end = nums[i]
            if start == end:
                ans.append(str(start))
            else:
                ans.append(str(start) + "->" + str(end))
            i += 1
            # print("end i : ", i)

        return ans

    # sol2 : list comperhension
    def summaryRanges2(self, nums: List[int]) -> List[str]:
        ranges = []  # [start,end]
        for n in nums:
            if ranges and ranges[-1][1] == n - 1:
                ranges[-1][1] = n
            else:
                ranges.append([n, n])
        return [f"{x}->{y}" if x != y else f"{x}" for x, y in ranges]


nums = [0, 1, 2, 4, 5, 7]
print(Solution().summaryRanges2(nums))
# @lc code=end
