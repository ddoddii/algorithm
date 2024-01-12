# Koko Eating Bananas
"""
- Binary Search
"""
from typing import List
import math


def minEatingSpeed(piles: List[int], h: int) -> int:
    left = min(piles)
    right = max(piles)
    while left < right:
        mid = (left + right) // 2
        hours = hoursToEat(piles, mid)
        # 걸린 시간이 길면 스피드를 증가시킨다.
        if sum(hours) > h:
            left = mid + 1
        # 걸린 시간이 짧으면 스피드를 감소시킨다.
        else:
            right = mid
    return left


def hoursToEat(piles: List[int], speed: int) -> int:
    hours = list(map(lambda x: math.ceil(x / speed), piles))
    return hours


piles = [3, 6, 7, 11]
h = 8


print(minEatingSpeed(piles, h))
