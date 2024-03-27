#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
from typing import List
from collections import deque


class Solution:
    """
    - two pointers
    """

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # left, right pointer
        if k <= 1:
            return 0
        count = left = 0
        product = 1
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k and left <= right:
                product /= nums[left]
                left += 1
            count += right - left + 1
        return count

    """
    - sliding windows
    """

    def numSubarrayProductLessThanK2(self, nums: List[int], k: int) -> int:
        left = right = count = 0
        product = 1
        while right < len(nums):
            product *= nums[right]
            while product >= k:
                product /= nums[left]
                left += 1
            count += right - left + 1
            right += 1
        return count

    """
    - 연속이지 않는 모든 subarray 찾는 방법 - dfs
    """

    def numSubarrayProductLessThanK3(self, nums: List[int], k: int) -> int:
        def productLessThanK(arr: List[int], k: int) -> int:
            res = 1
            for a in arr:
                res *= a
            return res < k

        q = []
        res = set()

        def dfs(idx):
            if productLessThanK(q, k):
                res.add(tuple(q))
            if idx == len(nums):
                return
            q.append(nums[idx])
            dfs(idx + 1)
            q.pop()
            dfs(idx + 1)

        dfs(0)

        return len(res)


nums = [10, 5, 2, 6]
k = 100
sol = Solution()
print(sol.numSubarrayProductLessThanK(nums, k))


# @lc code=end
