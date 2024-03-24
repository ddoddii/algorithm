#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    # sol1 : use hashmap to store occurence
    def findDuplicate(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1
        ans = list(k for k, v in dic.items() if v > 1)
        return ans[0]

    # sol2 : slow & fast pointer - Floyd's Cycle Detection
    def findDuplicate2(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


nums = [3, 1, 3, 4, 2]
sol = Solution()
print(sol.findDuplicate2(nums))

# @lc code=end
