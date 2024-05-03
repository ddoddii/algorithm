#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#


# @lc code=start
from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = list(map(int, version1.split("."))), list(
            map(int, version2.split("."))
        )
        for rev1, rev2 in zip_longest(v1, v2, fillvalue=0):
            if rev1 == rev2:
                continue
            return -1 if rev1 < rev2 else 1
        return 0


version1 = "1.0.1"
version2 = "1"
print(Solution().compareVersion(version1, version2))
# @lc code=end
