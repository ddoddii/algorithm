#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # hashMap
        sumFreq = defaultdict(int)
        sumFreq[0] = 1
        currSum = 0
        count = 0
        for num in nums:
            currSum += num
            if (currSum - goal) in sumFreq:
                count += sumFreq[currSum - goal]
            sumFreq[currSum] += 1
        return count


nums = [1, 0, 1, 0, 1]
goal = 2
sol = Solution()
print(sol.numSubarraysWithSum(nums, goal))

# @lc code=end
