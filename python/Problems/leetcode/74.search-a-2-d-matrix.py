#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr, target):
            l, r = 0, len(arr) - 1
            while l <= r:
                m = (l + r) // 2
                if target == arr[m]:
                    return True
                if target < arr[m]:
                    r = m - 1
                else:
                    l = m + 1
            return False

        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][0]:
                l = mid + 1
            else:
                return True
        return binary_search(matrix[r], target) if r >= 0 else False

    """
    - 한개의 1D sorted array 로 다루기
    """

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, (m * n) - 1
        while left <= right:
            mid = (left + right) // 2
            # divmod(x,y) = (x // y, x % y)
            # 2D array 에서 idx 가지고 row,col 찾을 때 -> row,col = divmod(idx,len(col))
            mid_row, mid_col = divmod(mid, n)
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
sol = Solution()
print(sol.searchMatrix2(matrix, 3))


# @lc code=end
