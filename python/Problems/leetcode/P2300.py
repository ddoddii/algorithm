# Successful pairs of Spells and Potions
from typing import List
from bisect import bisect_left


def successfulPairs(
    self, spells: List[int], potions: List[int], success: int
) -> List[int]:
    potions.sort()
    answer = []
    for spell in spells:
        # spell * potion >= success 찾기 ==> potion >= success / spell 찾기
        idx = bisect_left(potions, success / spell)
        successful_combinations = len(potions) - idx
        answer.append(successful_combinations)
    return answer


spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7
