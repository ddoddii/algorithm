#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        q = [root]
        while q:
            curr = q.pop(0)
            # swap left and right
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return root


# @lc code=end
