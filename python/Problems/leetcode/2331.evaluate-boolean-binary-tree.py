#
# @lc app=leetcode id=2331 lang=python3
#
# [2331] Evaluate Boolean Binary Tree
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
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node.val == 0 or node.val == 1:
                return node.val == 1
            # or
            elif node.val == 2:
                return dfs(node.left) or dfs(node.right)
            # and
            elif node.val == 3:
                return dfs(node.left) and dfs(node.right)

        return dfs(root)


# @lc code=end
