#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
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
    """
    - BFS , level_size 이용
    - Time : O(N) - 모든 노드 탐색해야 함
    - Space : O(N)
    """

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = [root]
        level = 0
        while q:
            level_size = len(q)
            for _ in range(level_size):
                curr = q.pop(0)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            level += 1
        return level

    """
    - DFS
    - Time : O(N)
    """

    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root:
                return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

        return dfs(root, 0)


# @lc code=end
