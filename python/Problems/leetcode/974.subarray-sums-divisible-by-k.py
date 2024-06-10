#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start
from typing import List
from collections import defaultdict


# 음수값이 있다 !!
# dic{key : prefix_sum, value : num of occurence}
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dic = defaultdict(int)
        dic[0] = 1
        prefix_sum = 0
        ans = 0
        for i in range(n):
            prefix_sum += nums[i]
            if k != 0:
                # modulo normalization
                prefix_sum = (prefix_sum % k + k) % k
            if prefix_sum in dic:
                ans += dic[prefix_sum]
            dic[prefix_sum] += 1
        return ans


nums = [4, 5, 0, -2, -3, 1]
k = 5
print(Solution().subarraysDivByK(nums, k))

# @lc code=end
