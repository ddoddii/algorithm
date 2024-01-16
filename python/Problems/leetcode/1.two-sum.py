#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
"""
- Hash Table
"""
from typing import List

# Time O(n^2), Brute Force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in range(len(nums)-1):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    answer.append(i)
                    answer.append(j)
                
        return answer

# Hash Table
def twoSum2(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]

# @lc code=end

