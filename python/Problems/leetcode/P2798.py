from typing import List


def numberOfEmployeesWhoMetTarget(hours: List[int], target: int) -> int:
    answer = list(filter(lambda x: x >= target, hours))
    return len(answer)


hours = [0, 1, 2, 3, 4]
target = 2

print(numberOfEmployeesWhoMetTarget(hours, target))
