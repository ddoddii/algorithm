#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = [(root.left, root.right)]
        while q:
            left, right = q.pop(0)
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            q.append((left.left, right.right))
            q.append((left.right, right.left))
        return True


# @lc code=end
