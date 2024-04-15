#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        #dfs 
        def dfs(curr,num):
            if curr is None:
                return 0
            num = num * 10 + curr.val 
            if (curr.left is None and curr.right is None):
                return num
            return dfs(curr.left,num) + dfs(curr.right,num)
        
        return dfs(root,0)
                
# @lc code=end

