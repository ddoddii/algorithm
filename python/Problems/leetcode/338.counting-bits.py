#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#


# @lc code=start
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(n + 1):
            count = bin(i).count("1")
            answer.append(count)
        return answer


# @lc code=end
