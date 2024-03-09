from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        print(mid)
        root = TreeNode(nums[mid])
        # left tree
        root.left = self.sortedArrayToBST(nums[:mid])
        # right tree
        root.right = self.sortedArrayToBST(nums[mid + 1 :])
        return root


nums = [-10, -3, 0, 5, 9]
sol = Solution()
print(sol.sortedArrayToBST(nums))
