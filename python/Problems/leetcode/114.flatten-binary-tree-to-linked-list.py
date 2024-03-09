from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []

        def preorder(node):
            if not node:
                return
            stack.append(node)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        if stack:
            for i in range(len(stack) - 1):
                stack[i].left = None
                stack[i].right = stack[i + 1]
            stack[-1].left = None
            stack[-1].right = None

    def flatten2(self, root: Optional[TreeNode]) -> None:
        # flatten root tree and return list tail
        def dfs(root):
            if not root:
                return None

            leftTail = dfs(root.left)
            rightTail = dfs(root.right)

            if leftTail:
                leftTail.right = root.right
                root.right = root.left
                root.left = None
            last = rightTail or leftTail or root
            return last

        dfs(root)

    def flatten3(self, root: Optional[TreeNode]) -> None:
        curr = root
        while curr:
            if curr.left:
                prev = curr.left
                while prev.right:
                    prev = prev.right  # 왼쪽 subtree 의 가장 오른쪽 노드 찾기
                prev.right = curr.right  # 1. prev 와 현재 curr 의 right 연결
                curr.right = curr.left  #  2. curr과 curr.left 연결
                curr.left = None  # 3. curr.left 없애기
            curr = curr.right
