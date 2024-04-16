#
# @lc app=leetcode id=623 lang=python3
#
# [623] Add One Row to Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # dfs
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        def dfs(curr,d):
            if not curr:
                return
            if d == depth-2:
                tempLeft = curr.left if curr.left else None
                tempRight = curr.right if curr.right else None
                
                curr.left = TreeNode(val)
                curr.right = TreeNode(val)
                curr.left.left = tempLeft
                curr.right.right = tempRight
                
            dfs(curr.left,d+1)
            dfs(curr.right,d+1)
        dfs(root,0)
        return root
    
    def addOneRow2(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # bfs
        if depth == 1: return TreeNode(val, left=root)
        
        q = deque([root])
        
        for _ in range(depth-2):
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        while q:
            node = q.popleft()
            node.left = TreeNode(val, left = node.left)
            node.right = TreeNode(val, right = node.right)
        return root
        
# @lc code=end

