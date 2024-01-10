# Remove Element
from typing import List
from bisect import bisect_left, bisect, bisect_right


def removeElement(nums: List[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        # val 과 같지 않으면 앞으로 swap
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


nums = [3, 2, 2, 3, 3]
val = 3
print(removeElement(nums, val))
