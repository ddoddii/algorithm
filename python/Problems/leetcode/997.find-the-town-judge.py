#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustGraph = defaultdict(list)
        judgeCandidate = []
        for a, b in trust:
            trustGraph[b].append(a)
        # judge is trusted by everybody = key judge contains everybody else
        for k in trustGraph.keys():
            if len(set(trustGraph[k])) == n - 1:
                judgeCandidate.append(k)
        # judge cannot trust anyone
        if not judgeCandidate:
            return -1
        for a, b in trust:
            for j in judgeCandidate:
                if j == a:
                    return -1
        else:
            return judgeCandidate[-1]

    def findJudge2(self, n: int, trust: List[List[int]]) -> int:
        in_degree = [0] * (n + 1)
        out_degree = [0] * (n + 1)

        for a, b in trust:
            out_degree[a] += 1
            in_degree[b] += 1

        for i in range(1, n + 1):
            if in_degree[i] == (n - 1) and out_degree[i] == 0:
                return i
        return -1


n = 4
trust = [[1, 4], [2, 4], [3, 4], [1, 2]]
sol = Solution()
print(sol.findJudge2(n, trust))

# @lc code=end
