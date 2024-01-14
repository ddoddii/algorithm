# 216. Combination Sum III
from typing import List
from itertools import combinations


def combinationSum(k: int, n: int) -> List[List[int]]:
    answer = []
    nums = [i for i in range(1, 10)]
    for combi in combinations(nums, k):
        if sum(combi) == n:
            answer.append(list(combi))
    return answer


# backtracking
def combinationSum2(k: int, n: int) -> List[List[int]]:
    res = []

    def backtrack(num, stack, target):
        if len(stack) == k:
            if target == 0:
                res.append(stack)
            return
        for x in range(num + 1, 10):
            if x <= target:
                backtrack(x, stack + [x], target - x)
            else:
                return

    backtrack(0, [], n)
    return res


print(combinationSum2(3, 9))
