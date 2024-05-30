#
# @lc app=leetcode id=1442 lang=python3
#
# [1442] Count Triplets That Can Form Two Arrays of Equal XOR
#

# @lc code=start
from typing import List

"""
a ^ a = 0
if xor == 0 exists in arr[i:k], 
than there exists (k-i) where xor of arr[i:j] equals to arr[j:k]
"""


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        cnt = 0
        n = len(arr)
        for i in range(n - 1):
            val = arr[i]
            for k in range(i + 1, n):
                val ^= arr[k]
                if val == 0:
                    cnt += k - i
        return cnt


arr = [2, 3, 1, 6, 7]
print(Solution().countTriplets(arr))
# @lc code=end
