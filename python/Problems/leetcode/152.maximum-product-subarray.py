#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = min_product = answer = nums[0]
        for num in nums[1:]:
            print("max_prod : ", max_product)
            tmp_max = max(num, num * max_product, num * min_product)
            print(f"tmp max : {tmp_max}")
            min_product = min(num, num * max_product, num * min_product)
            max_product = tmp_max
            answer = max(answer, max_product)
            print(
                f"min_prod : {min_product}, max_prod : {max_product}, answer : {answer}"
            )
        return answer


sol = Solution()
nums = [2, 3, -2, 4]
print(sol.maxProduct(nums))


# @lc code=end
