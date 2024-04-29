#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        for k in counter1.keys():
            if k in counter2.keys():
                for _ in range(min(counter1[k], counter2[k])):
                    ans.append(k)
        return ans

    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect2(nums2, nums1)
        cnt = Counter(nums1)
        ans = []
        for x in nums2:
            if cnt[x] > 0:
                ans.append(x)
                cnt[x] -= 1
        return ans

    # sol3- if sorted, two pointers
    def intersect3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        ans = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1
        return ans


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(Solution().intersect3(nums1, nums2))
# @lc code=end
