#
# @lc app=leetcode id=1110 lang=python3
#
# [1110] Delete Nodes And Return Forest
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional, List
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        # bfs
        q = collections.deque([(root, False)])
        to_delete = set(to_delete)
        res = []
        while q:
            node, hasParent = q.popleft()
            if not hasParent and node.val not in to_delete:
                res.append(node)
            hasParent = not node.val in to_delete
            if node.left:
                q.append((node.left, hasParent))
                if node.left.val in to_delete:
                    node.left = None
            if node.right:
                q.append((node.rigt, hasParent))
                if node.right.val in to_delete:
                    node.right = None
        return res

    def delNodes2(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        # dfs
        res = []
        to_delete = set(to_delete)

        def dfs(node, hasParent):
            if not node:
                return None
            to_delete_curr = node.val in to_delete
            if not hasParent and not to_delete_curr:
                res.append(node)
            node.left = dfs(node.left, not to_delete_curr)
            node.right = dfs(node.right, not to_delete_curr)
            return None if to_delete_curr else node

        dfs(root, False)
        return res


# @lc code=end
