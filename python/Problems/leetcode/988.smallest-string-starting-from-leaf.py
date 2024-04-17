#
# @lc app=leetcode id=988 lang=python3
#
# [988] Smallest String Starting From Leaf
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
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # dfs 
        def dfs(node,path,smallest):
            # 트리 벗어나면 재귀 빠져나오기
            if not node:
                return
            # 경로에 추가 (루트부터)
            path.append(chr(node.val + ord('a')))
            
            # 리프 도달하면 path 뒤집기
            if not node.left and not node.right:
                curr_string = ''.join(path[::-1])
                smallest[0] = min(smallest[0],curr_string)
            
            # dfs
            dfs(node.left, path, smallest)
            dfs(node.right, path, smallest)
            
            # backtrack
            path.pop()
        smallest = [chr(ord('z')+1)]
        dfs(root,[],smallest)
        return smallest[0]
        
# @lc code=end

